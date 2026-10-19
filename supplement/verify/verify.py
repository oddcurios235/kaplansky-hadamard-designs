#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2026 Y. T. Miah
"""Reproduce the finite certificates for the Hadamard--Kaplansky construction.

Run from the supplement/ directory:
    python verify/verify.py --output checks/results.json

Python 3.10+, NumPy and SymPy are required. All certificate comparisons are exact.
Stored data are compared against independently reconstructed arrays; they are not
used as a substitute for the reconstruction. Keep Python assertions enabled.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

import numpy as np
import sympy as sp

D = [0,1,3,9,27,32,81,96,151,199,243,288,453,457,509,584,597,614,
729,803,864,904,932,1003,1133,1359,1371,1493,1527,1745,1752,1791,
1842,1856,2044,2187,2225,2384,2409,2419,2482,2525,2592,2712,2796,
2833,2956,3009,3056,3233,3292,3399,3418,3478,3554,3611,3791,3802,
4019,4077,4113,4190,4429,4479,4495,4581,4730,4763,5110,5235,5256,
5373,5414,5526,5568,5588,5696,5905,5927,6132,6397,6561]

def quotient(q: int, e: int, gamma: F = F(1,2)) -> list[list[F]]:
    v=q*q+q+1; a=F(1,(q+1)**2); b=F((q+1)**2,v*v)
    return [[e*b,(e-1)*gamma**2,(v-e)*b],
            [(e-1)*a,e*b,(v-e)*a],
            [e*a,e*b,(v-e-1)*a]]

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def spectral_certificate(q: int,e: int,large_vector: bool=False):
    Q=quotient(q,e)
    vec=[F(e+1) if large_vector else F(e+4,4),F(1),F(1)]
    ratios=[sum(Q[i][j]*vec[j] for j in range(3))/vec[i] for i in range(3)]
    R=max(ratios)
    assert 0<R<1
    tau=(1-R)/8; lam=(1+R)/2
    assert (1+tau)**2*R < lam < 1
    assert (1+tau)*F(1,2)<1
    out={'q':q,'e':e,'letters':q*q+q+1+e,'alphabet_generators':(q*q+q+1+e)//2,
         'test_vector':[str(x) for x in vec],'raw_row_ratios':[str(x) for x in ratios],
         'tau':str(tau),'lambda':str(lam),
         'inflated_max':str((1+tau)**2*R)}
    return out,tau,lam

class Field:
    """Prime fields and F_25 = F_5[u]/(u^2-2), used only for small Paley checks."""
    def __init__(self,q):
        if q==25:self.q,self.p,self.ext=25,5,True
        elif sp.isprime(q):self.q,self.p,self.ext=q,q,False
        else:raise ValueError('Only prime fields and F_25 are implemented.')
    def add(self,x,y):
        if not self.ext:return (x+y)%self.p
        return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
    def neg(self,x):
        if not self.ext:return -x%self.p
        return ((-(x%5))%5)+5*((-(x//5))%5)
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        if not self.ext:return x*y%self.p
        a,b=x%5,x//5;c,d=y%5,y//5
        return (a*c+2*b*d)%5+5*((a*d+b*c)%5)
    def power(self,x,n):
        y=1
        while n:
            if n&1:y=self.mul(y,x)
            x=self.mul(x,x);n//=2
        return y
    def chi(self,x):
        if x==0:return 0
        a=self.power(x,(self.q-1)//2)
        assert a in (1,self.neg(1))
        return 1 if a==1 else -1

def paley(order: int, field_order: int, kind: int):
    ff=Field(field_order); q=field_order
    C=np.array([[ff.chi(ff.sub(i,j)) for j in range(q)] for i in range(q)],dtype=np.int64)
    assert np.array_equal(C@C.T,q*np.eye(q,dtype=np.int64)-np.ones((q,q),dtype=np.int64))
    if kind==1:
        assert q%4==3 and order==q+1
        H=np.block([[np.ones((1,1),dtype=np.int64),np.ones((1,q),dtype=np.int64)],
                    [-np.ones((q,1),dtype=np.int64),C+np.eye(q,dtype=np.int64)]])
    else:
        assert kind==2 and q%4==1 and order==2*(q+1)
        A=np.block([[np.zeros((1,1),dtype=np.int64),np.ones((1,q),dtype=np.int64)],
                    [np.ones((q,1),dtype=np.int64),C]])
        I=np.eye(q+1,dtype=np.int64)
        assert np.array_equal(A@A,q*I)
        H=np.block([[A+I,A-I],[A-I,-A-I]])
    assert set(H.flat)=={-1,1}
    assert np.array_equal(H@H.T,order*np.eye(order,dtype=np.int64))
    H=H*H[0,:][None,:]
    H=H*H[:,0][:,None]
    assert np.all(H[0,:]==1) and np.all(H[:,0]==1)
    B=(1-H[1:,1:])//2; e=order-1; h=order//2
    assert np.all(B.sum(0)==h) and np.all(B.sum(1)==h)
    target=(order//4)*(np.eye(e,dtype=np.int64)+np.ones((e,e),dtype=np.int64))
    assert np.array_equal(B@B.T,target) and np.array_equal(B.T@B,target)
    return H,B

def histogram(p:int,e:int,q:int):
    assert p>=5 and sp.isprime(p) and (e+1)%(4*p)==0 and q%p==0
    k=pow(4,-1,p);hh=pow(2,-1,p);c=(1-k)%p
    alpha=[0]*p;alpha[0]=1;alpha[k]=-1
    C=[0]*p
    for i,x in [(1,e),(k,2),(c,4),(hh,-e-6)]:C[i]+=x
    assert sum(C)==0
    beta=[0]*p
    for i in range(1,p):
        t=i*k%p;beta[t]=beta[(t-k)%p]+C[t]
    assert beta[0]-beta[(-k)%p]==C[0]
    assert sum(beta)%p==0
    mean=sum(beta)//p;beta=[x-mean for x in beta]
    assert sum(beta)==0 and max(abs(x) for x in beta)<=e+6
    assert sum(t*beta[t] for t in range(p))%p==(-k)%p
    assert all(sum(alpha[i]*beta[(t-i)%p] for i in range(p))==C[t] for t in range(p))
    A=[q//p+x for x in alpha];B=[q//p+x for x in beta]
    assert min(A+B)>=0
    n=[sum(A[i]*B[(t-i)%p] for i in range(p))+2*(t==k)+(q-1)*(t==hh) for t in range(p)]
    assert sum(n)==q*q+q+1 and n[1]-n[0]==e
    nn=n[:];nn[0]+=e
    assert all(nn[t]==nn[(1-t)%p] for t in range(p)) and nn[hh]%2==0
    Cbase=sum(t*(A[t]+B[t]) for t in range(p))+hh
    Z=(2*(q+1)*Cbase-(q*q+q+1+e))//p
    assert p*Z==2*(q+1)*Cbase-(q*q+q+1+e)
    return {'alpha':alpha,'beta':beta,'residue_counts':n,'Cbase':Cbase,'repair_norm_bound':1+2*Cbase+(p+2)*Z}

def cyclic_expand(coeff,support):
    out=np.zeros(len(coeff),dtype=np.int64)
    for t in support:out+=np.roll(coeff,int(t))
    return out

def characteristic_three():
    q,v,e,p,h=81,6643,11,3,6
    differences=Counter((x-y)%v for x in D for y in D if x!=y)
    assert len(D)==q+1 and len(differences)==v-1 and set(differences.values())=={1}
    # Construct the new two-pencil seed directly from the projective incidence list.
    p0=sorted((-x)%v for x in D);p1=sorted((1-x)%v for x in D)
    common=sorted(set(p0)&set(p1));assert len(common)==1
    conn=common[0];countsA=[28,26,27];countsB=[24,28,29]
    coeff=np.zeros(v,dtype=np.int64)
    for pencil,hist in [(p0,countsA),(p1,countsB)]:
        lines=[x for x in pencil if x!=conn]
        vals=[i for i,n in enumerate(hist) for _ in range(n)]
        assert len(lines)==len(vals)==q
        for ell,z in zip(lines,vals):coeff[ell]+=z
    coeff[conn]+=2
    assert int(coeff.sum())==168 and int(np.count_nonzero(coeff))==111
    w=np.r_[cyclic_expand(coeff,D),np.zeros(e,dtype=np.int64)]
    classes=[np.flatnonzero(w[:v]%p==i).tolist() for i in range(p)]
    assert list(map(len,classes))==[2182,2193,2268]
    inv=np.full(v+e,-1,dtype=np.int64)
    for a,b in list(zip(range(v,v+e),classes[1][:e]))+list(zip(classes[0],classes[1][e:]))+list(zip(classes[2][::2],classes[2][1::2])):
        assert a!=b and inv[a]==inv[b]==-1
        inv[a]=b;inv[b]=a
    assert np.all(inv>=0) and np.array_equal(inv[inv],np.arange(v+e))
    assert np.all((1-w-w[inv])%3==0)
    z=(1-w-w[inv])//3
    shifts=np.array([(-x)%v for x in D[:4]],dtype=np.int64)
    RU=sorted({(a+ell)%v for a in D for ell in shifts})
    assert len(RU)==325
    pencil=np.zeros(v,dtype=np.int64)
    for ell in shifts:pencil[(np.array(D)+ell)%v]+=1
    pencil[RU]-=1
    assert pencil[0]==3 and np.count_nonzero(pencil)==1
    xL=coeff.copy();yL=coeff.copy();xR=np.zeros(v,dtype=np.int64);yR=xR.copy()
    for i in range(v):
        xL[(i+shifts)%v]+=z[i];xR[i]-=z[i]
    for j in range(v,v+e):
        i=inv[j];yL[(i+shifts)%v]+=z[j];yR[i]-=z[j]
    def incidence(a,b):return np.r_[cyclic_expand(a,D)+cyclic_expand(b,RU),np.zeros(e,dtype=np.int64)]
    assert np.all(incidence(xL,xR)+incidence(yL,yR)[inv]==1)
    full_norm=1+sum(int(abs(a).sum()) for a in (xL,xR,yL,yR))
    assert full_norm==34807
    # Compact root S_r=L_0 union E. Integer all-ordinary vector:
    # -107 sum L_x + 27 sum R_x = 1_P.
    assert np.all(cyclic_expand(np.full(v,-107,dtype=np.int64),D)+cyclic_expand(np.full(v,27,dtype=np.int64),RU)==1)
    xL+=107;xL[0]+=1;xR-=27
    Sr=np.zeros(v+e,dtype=np.int64);Sr[D]=1;Sr[v:]=1
    assert Sr.sum()==93 and Sr.sum()%3==0
    X=incidence(xL,xR);Y=incidence(yL,yR)
    assert np.array_equal(X+Y[inv],Sr)
    # Auxiliary blocks remain the explicit 11-point Paley design.
    H=[sorted(set(range(e))-{(s+j)%e for s in [1,3,4,5,9]}) for j in range(e)]
    HB=np.array([[int(t in block) for t in range(e)] for block in H],dtype=np.int64)
    assert np.array_equal(HB@HB.T,3*(np.eye(e,dtype=np.int64)+np.ones((e,e),dtype=np.int64)))
    # Primitive pure-line core.
    g=math.gcd(h,q+1);b0=(h*v-e*(q+1))//g;b1=(q+1)//g
    N=(h//g)*v*v;F0=(h//g)*v*(q+1)
    assert (b0,b1,N,F0)==(19478,41,132388347,1634178)
    assert math.gcd(b0,b1)==1
    assert v*(b0+e*b1)==N and (q+1)*(b0+e*b1)==v*h*b1==F0
    # Reservoir: 2 line copies, 4 undecorated union copies at every translate.
    # Decorate 244 line copies with each H_j; use distinct line indices 244*j+k.
    line_offset=np.full(v,2,dtype=np.int64)
    decor=np.zeros((v,e),dtype=np.int64)
    for j in range(e):
        for k in range(244):
            ell=244*j+k
            line_offset[ell]-=1;decor[ell,j]+=1
    assert int(line_offset.min())==1
    Rslots=(q+1)*2+325*4
    assert Rslots==1464 and 244*h==Rslots
    # Enumerate slots of the reservoir independently, including all auxiliary coordinates.
    rs=np.r_[cyclic_expand(line_offset+decor.sum(1),D)+cyclic_expand(np.full(v,4,dtype=np.int64),RU),decor.sum(0)@HB]
    assert np.all(rs==Rslots)
    # Positivity at m=1, hence at all larger m; union counts have zero leading term.
    assert np.all(b0+line_offset-xL>0) and np.all(b0+line_offset+yL>0)
    assert np.all(4-xR>0) and np.all(4+yR>0)
    assert np.all(b1+decor>0)
    # Exact inverse-letter pool equality at m=1. The same identity is affine in m.
    core=np.full(v+e,F0,dtype=np.int64)
    plus=core+rs-X+Sr;minus=core+rs+Y;Bpool=core+rs
    assert np.array_equal(plus,minus[inv]) and np.array_equal(Bpool,Bpool[inv])
    boundX=incidence(abs(xL),abs(xR));boundY=incidence(abs(yL),abs(yR))
    Bcoord=int(max(boundX.max(),boundY.max()))
    E=Rslots+Bcoord+1
    cert,tau,lam=spectral_certificate(q,e)
    # A simpler chosen certificate for this one fully expanded example.
    tau,lam=F(1,1000),F(249,250)
    raw=max(F(t) for t in cert['raw_row_ratios'])
    assert (1+tau)**2*raw<lam
    cert.update(tau=str(tau),lambda_chosen=str(lam),
                inflated_max=str((1+tau)**2*raw))
    cert['lambda']=str(lam)
    mturn=math.ceil(F(E*(q+1),F0)/tau)
    assert mturn*F0*tau*F(1,q+1)>=E
    raw_norm=1+sum(int(abs(a).sum()) for a in (xL,xR,yL,yR))
    result={'p':3,'q':q,'e':e,'letters':v+e,'alphabet_generators':(v+e)//2,
            'two_pencil_histograms':[countsA,countsB],'connecting_line_shift':conn,
            'base_coefficient_sum':int(coeff.sum()),'nonzero_line_coefficients':int(np.count_nonzero(coeff)),
            'ordinary_residue_counts':list(map(len,classes)),
            'full_root_repair_norm':full_norm,'compact_root_repair_norm':raw_norm,
            'compact_root_degree':93,'minimum_degree':82,'maximum_degree':325,
            'core_N':N,'core_F':F0,'core_plain_line_multiplicity':b0,'core_each_decorated_line_multiplicity':b1,
            'reservoir_N':6*v,'reservoir_F':Rslots,
            'sum_x':int(xL.sum()+xR.sum()),'sum_y':int(yL.sum()+yR.sum()),
            'correction_coefficient_ranges':[(int(a.min()),int(a.max())) for a in (xL,xR,yL,yR)],
            'coordinate_absolute_correction_bound':Bcoord,'candidate_additive_bound':E,
            'turn_domination_m_threshold':mturn,
            'normalized_bulk_reduction_factor':2*10**14,
            'all_coordinate_repair_and_pool_checks':True,'spectral_certificate':cert}
    arrays={'D':D,'pencil_shifts':shifts.tolist(),'seed_nonzero_coefficients':[[i,int(a)] for i,a in enumerate(coeff) if a],
            'involution':inv.tolist(),'x_line':xL.tolist(),'x_union':xR.tolist(),
            'y_line':yL.tolist(),'y_union':yR.tolist(),'auxiliary_blocks':H}
    return result,arrays

def obstruction_polynomial():
    p=sp.symbols('p');q=p**4;v=q*q+q+1;e=p*p+p+1
    a=1/(q+1)**2;b=(q+1)**2/v**2;gam=(p-1)/p
    Q=sp.Matrix([[e*b,(e-1)*gam**2,(v-e)*b],[(e-1)*a,e*b,(v-e)*a],[e*a,e*b,(v-e-1)*a]])
    det=sp.factor((sp.eye(3)-Q).det());num,den=sp.fraction(det)
    u=sp.symbols('u');shift=sp.Poly(sp.expand((-num).subs(p,u+3)),u)
    assert all(c>0 for c in shift.all_coeffs())
    return {'det_I_minus_Q':str(det),'positive_numerator_coefficients_in_p_minus_3':list(map(int,shift.all_coeffs())),
            'interpretation':'All coefficients are positive; det(I-Q)<0 for every real p>=3. Thus rho(Q)>1.'}

def supports_sanity():
    # Product coefficients can attain min(s,t) even in a torsion-free group.
    # These are tests of the coefficient estimate, not zero-divisor searches.
    for p in [3,5,7,11]:
        # Over the torsion-free cyclic group Z, (1+x+...+x^(p-1))^2 has coefficient p.
        a={i:1 for i in range(p)}
        out=Counter()
        for i,ai in a.items():
            for j,aj in a.items():out[i+j]+=ai*aj
        assert max(out.values())==p
        assert all(n<=min(len(a),len(a)) for n in out.values())
    return {'product_fibre_bound_tests':True,'examples':'Products in the integral group algebra of the infinite cyclic group.'}


def affine_and_scale_checks(c3: dict) -> dict:
    """Separate affine and pair-incidence errors and check the degree-based scale."""
    Caff=c3['reservoir_N']+c3['compact_root_repair_norm']
    E=c3['candidate_additive_bound']
    assert Caff==896128 and E==18417
    NR,N,F0=c3['reservoir_N'],c3['core_N'],c3['core_F']
    offsets=[NR-c3['sum_x']+1,NR+c3['sum_y'],NR]
    assert offsets==[-471038,39840,39858]
    assert max(map(abs,offsets))<=Caff and N>3*Caff
    f=F(82,6643);Dmax=325
    b=0
    while 2**b<8*Dmax/f:b+=1
    A=256*b
    assert (b,A)==(18,4608)
    assert 4*Dmax/f<2**b and Dmax<2**b
    rho=(f/(1000*Dmax))**2
    d0=math.ceil(1000*A/rho)
    assert 41*rho<f/4
    C3=36*(F(24*Dmax,41)/f)**41
    assert C3*rho**39<F(1,2)
    n925=925*N
    L925=(n925.bit_length()-1)//A
    assert L925==0
    gap925=F(925*F0,82000)-E
    gap924=F(924*F0,82000)-E
    assert gap925==F(693,40) and gap924==-F(651,250)
    eps=F(1,5312000)
    area=F(16,13)/eps
    assert area==F(84992000,13)
    assert F(16,13)/F(1,6464000)==F(103424000,13)
    return {'affine_error_bound':Caff,'turn_error_bound':E,
            'class_offsets':offsets,'b_scale':b,'A':A,'rho':str(rho),
            'diameter_coefficient':d0,'L_at_m_925':L925,
            'minimum_log2_n_for_L_at_least_3':3*A,
            'turn_domination_slack_at_925':str(gap925),
            'epsilon':str(eps),'area_coefficient':str(area)}

def asymptotic_checks() -> dict:
    """Check exact parameter formulas, not the external Hadamard existence proofs."""
    P=int(sp.nextprime(2**60));a=14
    while 2**(5*(a-14))<P-1:a+=1
    t_dj=6*((P.bit_length()-1)//40)+10
    assert a>=t_dj  # Sylvester doubling gives the exact Ghaderpour-parameter order.
    H=P*2**a;e=H-1;q=P**3
    assert H%(4*P)==0 and q>=8*e*(e+1) and P*P>=e+6
    assert H**5<=2**75*P**6
    gh,_,_=spectral_certificate(q,e,large_vector=True)
    # Points near the first threshold and near discontinuities of the floor.
    samples=sorted({int(sp.nextprime(2**23)),int(sp.nextprime(2**24)),
                    *[int(sp.prevprime(2**k)) for k in [40,80,120]],
                    *[int(sp.nextprime(2**k)) for k in [40,80,120]]})
    rows=[]
    for p in samples:
        b=(p.bit_length()-1)//40
        a_gh=14
        while 2**(5*(a_gh-14))<p-1:a_gh+=1
        assert a_gh>=6*b+10
        H=p*2**(6*b+10);e=H-1;q=p**3
        assert p>=2**23 and H%(4*p)==0
        assert p>=2**(12*b+23) and p>=2**(6*b+11)
        assert q>=8*e*(e+1) and p*p>=e+6
        assert H**20<=2**200*p**23
        sc,_,_=spectral_certificate(q,e,large_vector=True)
        rows.append({'p':p,'b':b,'Hadamard_order':H,'letters':q*q+q+H,
                     'spectral_certificate':sc})
    return {'Ghaderpour_parameter':{'p':P,'a':a,'Du_Jiang_exponent':t_dj,
                         'Sylvester_doublings':a-t_dj,'Hadamard_order':P*2**a,
                         'spectral_certificate':gh},
            'Du_Jiang_boundary_samples':rows,
            'scope':'Arithmetic consequences of cited existence theorems; large matrices not generated.'}

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('checks/results.json'))
    parser.add_argument('--data',type=Path,default=Path(__file__).resolve().parents[1]/'data')
    args=parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are part of the verifier.')
    c3,arrays=characteristic_three()
    expected=json.loads((args.data/'characteristic_three.json').read_text())
    assert arrays==expected,'Reconstructed characteristic-three arrays differ from the certificate.'
    mats={};rows=[]
    for p,order,fieldq,kind in [(5,20,19,1),(7,28,13,2),(11,44,43,1),
                               (13,52,25,2),(17,68,67,1),(19,76,37,2)]:
        H,B=paley(order,fieldq,kind);q=p**3;e=order-1
        hc=histogram(p,e,q);sc,tau,lam=spectral_certificate(q,e)
        h=order//2;g=math.gcd(h,q+1);v=q*q+q+1
        assert g==2 and (h*v-e*(q+1))//g>0
        rows.append({'p':p,'Hadamard_order':order,'Paley_field_order':fieldq,
                     'Paley_type':kind,'q':q,'e':e,'letters':v+e,
                     'alphabet_generators':(v+e)//2,'core_N':(h//g)*v*v,
                     'minimum_degree':q+1,'maximum_degree':max((p+1)*q+1,q+1+e),
                     'histogram':hc,'spectral_certificate':sc})
        mats[str(order)]=H.tolist()
    expected_mats=json.loads((args.data/'hadamard_matrices.json').read_text())
    assert mats==expected_mats,'Regenerated Paley matrices differ from the certificate.'
    obstruction=obstruction_polynomial()
    p=sp.symbols('p')
    numerator=-sp.fraction(sp.factor(sp.sympify(obstruction['det_I_minus_Q'])))[0]
    assert list(map(int,sp.Poly(numerator,p).all_coeffs()))==[
        1,1,0,-1,1,12,-4,-14,11,31,-21,-31,26,43,-37,-46,
        40,38,-45,-36,37,18,-31,-17,22,4,-15,-1,7,-2,-2,1]
    assert obstruction['positive_numerator_coefficients_in_p_minus_3'][-1]==833193976801090
    results={'all_checks_passed':True,
             'test_environment':{'python':platform.python_version(),
                                 'numpy':np.__version__,'sympy':sp.__version__},
             'characteristic_three':c3,
             'affine_and_scale_checks':affine_and_scale_checks(c3),
             'order_4p_examples':rows,'asymptotic_parameter_checks':asymptotic_checks(),
             'MD_unchanged_p4_obstruction':obstruction,'support_bound_checks':supports_sanity()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'output':str(args.output),
                      'signed_letters':c3['letters'],'maximum_degree':c3['maximum_degree'],
                      'affine_error_bound':896128,'turn_error_bound':18417,
                      'turn_domination_threshold':925,'small_Hadamard_examples':len(rows)},indent=2))

if __name__=='__main__':
    main()
