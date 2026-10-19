# Mathematical dependencies

This document records the mathematical dependencies of the manuscript's principal results. Source keys and versions are given in SOURCES.md. The finite assertions, probabilistic realization, and geometric/algebraic conclusions are separate theorem layers.

## Theorem map

| Statement in this paper | Imported ingredients | Role in the present argument |
|---|---|---|
| Definition 2.1; Lemmas 2.2–2.3 | Classical normalized Hadamard core; Singer projective planes | Both auxiliary Gram identities, ordinary integer pencil identity, exceptional-root congruences, and the precise finite interface. |
| Lemmas 3.1–3.2; Proposition 3.3 | Projective-line incidences; MD26 §7.2 for the preceding colour-balance and compact-root formulation | Two-pencil histograms; complementary residue pairing; exact integer lift; replacement of the full root by `L_0 ∪ E`. The two-pencil and coordinate-repair arguments are proved in full in §3. |
| Theorem 4.1 | The preceding incidence and repair lemmas | Primitive line/decorated-line bulk, balanced fixed reservoir, positivity, separate affine/turn errors, the full-alphabet squared-turn quotient, and uniform finite-size domination. No graph existence theorem is used in this finite theorem. |
| Theorem 5.2 | A real Hadamard matrix of order `4p`, as an explicit hypothesis | Histogram feasibility and two exact spectral inequalities at `q=p^3`. No assertion that all orders `4p` exist. |
| Theorem 5.3 | DJ24 Theorem 3; Sylvester doubling. Gh15 Theorem 10 supplies the parameter choice, not an indispensable unverified sequence estimate. | Exact order `p*2^a_p`; explicit threshold `p≥2^60`; the alphabet and maximum-degree bounds. |
| Theorem 5.4 | DJ24 Theorem 3, including its external finite-coverage input | Direct use of that Hadamard order; threshold `p≥2^23`; histogram and contraction hypotheses; `p^6+p^3+2^10 p^(23/20)` alphabet bound. |
| Proposition 6.2 | The printed 82-element difference set and eleven explicit auxiliary blocks | Rule-generated 111-entry seed, all repairs and matching pools, compact root, fixed reservoir, primitive bulk and exact rational contraction. |
| Lemmas 7.1, 7.3; Proposition 7.2 | OAI197a §3.3 and Lemma 3.3; Iva26 two-colour model; McKay switching ancestry | Switch stays in the actual sign/inverse-letter subpool; injective reverse count under girth conditioning; degree-based cycle count and nonempty girth event. |
| Proposition 7.4; Lemmas 7.5–7.6 | OAI197a Proposition 3.4 and equation (4.11); Iva26 §6.1; MD26 Proposition 7.9(c) | Expansion and diameter using actual degree `D`; finite candidate domination and the stage expectation for this affine reservoir model. |
| Theorem 7.7 and Appendix A | OAI197a Theorem 4.1 and Lemmas 4.2–4.4; Iva26 §6.1 | Complete multiplicity proof with the new image estimate. Common grid, complete-assignment projections and minimum of stage first moments are inherited, not claimed as new methods. |
| Theorem 8.1 and Appendix B | MD26 Theorem B, Definitions 3.2–3.3, Proposition 4.4; OAI196/OAI197a cone and planar framework; OAI257 free-boundary antecedent; LT79, LS77 Chapter V, CH82, BP93, Hat02, Bro82, BH99 | The criterion and its proof are reproduced with attribution; Proposition 8.2 verifies the full parameter comparison for the selected finite input. No new criterion is claimed. |
| Lemma 8.4; Theorem 8.5 | Iva26 Lemma 2.2; exceptional-root assembly of OAI197a; MD26 Lemma 6.1, Proposition 7.11 and Theorem B | Signed self-pairing with defect `J−E_rr`, so `b` has the positive unsigned formula; separate proof that `c≠0` by protection of its root. |
| Corollary 8.6 | Classical ring identities, also recorded in BFF24 §1 and MD26 §2; ES04 Corollary 4.7 | Scalar/matrix failures, coefficient extension, idempotent, square-zero element, unit of order `p`, and nonsoficity. These overlap the qualitative consequences in MD26. |
| Proposition C.1 | The precise MD26 §7 auxiliary types and leading frequencies | Exact determinant obstruction at `q=p^4`, for the unchanged model only. |
| Appendix D | Mon69; finite-pattern methods of DHJ15 and Sch13; Gar24 §§1, 3; BFF24 §1; Iva26 §8.3 and MD26 Proposition 8.3; weak Nullstellensatz | Support-height lifting and an effective finite exceptional-characteristic argument. Not a characteristic-zero counterexample or the paper's main novelty claim. |

## Why the realization hypotheses hold

The compact exceptional root and exact colour-balance problem already appear in MD26. The present finite architecture changes the auxiliary design, residue modulus, coordinate repair, and treatment of union rows; it does not originate the qualitative counterexample theorem or the geometric criterion. The characteristic-three comparison in §6 uses Mghirbi–Douglas as its scholarly baseline.

The order of choices is: Hadamard matrix and plane; types and residue seed; involution and integer repair; primitive bulk and reservoir; errors and spectral inflation; positivity/turn thresholds; girth scale; decay and unmatched proportion; diameter constant; then the fixed BP triple. Only replication varies after these choices.

1. **Exact counts.** For `n=mN_0`, all three classes have size `n+O(C_aff)`. Every subpool has size `nf+O(C_aff)`, with exact equality between its two slot sets. The root and reservoir are fixed before the matching. Union multiplicities are fixed; signed repairs are fixed affine offsets to the complete populations, including the replicated line populations. All listed multiplicities are positive above the stated threshold.
2. **Turn control.** Every reduced leading turn is positive; the only zero is backtracking. The word weight obeys the combined inversion-and-reversal identity `P_Θ(t_1...t_s)=P_Θ(ι(t_s)...ι(t_1))`. An internal chain vertex has at most `nf Θ(t,u)` candidates in its prescribed class. Every retained image edge requires one distinct matching prescription. The denominator is a letter pool, never a type frequency, so repair-only types with zero leading frequency introduce no division by zero.
3. **Maximum degree.** For already chosen vertices, each outgoing step has at most `D` possible slots. This supplies `D^k` in the short-cycle description count and `4Dk^2` in the local prescription count. Radius bounds also use `D`. The entropy of freely chosen words still uses the full alphabet `|T|`; it is not replaced by `D`.
4. **Girth and conditioning.** `A=256 ceil(log2(8D/f))` and `L=floor(log2(n)/A)` give short-cycle expectation `o(n)` and forbidden switch neighborhoods `O(D^(2L+2))=o(n)`. The conditioned prescription estimate applies when `P_L(S)>0`; a zero-probability prefix gives zero joint probability. It is an upper bound proved by a switching injection, not post-conditioning independence.
5. **BP quantifiers.** A single positive `ε` is fixed before the number of paths, length multiplier and number of comparison pairs. Compared positions use distinct undirected edges. At most one interval is open, and it starts at a fixed root. Repeated traversals are handled by multiplicity levels.
6. **Selection and geometry.** Before testing tuples, enforce positivity, turn domination, `n>3C_aff` and `L≥3`. Also require the diameter and fixed BP tests. With `d=d_0`, `λ_geo=2A`, the selected vertex count gives `log2|VΓ|≤λ_geo L`; the paper's BP triple dominates MD26's triple coordinatewise. The selection includes BP itself, not just absence of reduced spheres.

In the characteristic-three instance, `E_*=18417` controls turn candidates, while `C_aff=896128` bounds class/pool offsets. The sufficient turn threshold is `m≥925`. At `m=925`, the conservative girth scale has `L=0`; this is not a terminal matching threshold. The primitive bulk, reservoir, graph size, relator count and algebraic supports are distinct quantities.

## Computational scope

[verify/verify.py](verify/verify.py) reconstructs the characteristic-three certificate and the six small Hadamard matrices, checks exact rational inequalities and the symbolic obstruction, and tests boundary cases of the proved asymptotic inequalities. The external large Hadamard matrices and DJ24's complementary-sequence coverage computation are not reconstructed. Neither a terminal matching search nor a proof-assistant build is part of this package. The written proofs, not finite tests of the random model, supply the realization and hyperbolicity conclusions.
