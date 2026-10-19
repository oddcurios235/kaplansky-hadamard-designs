# Hadamard designs and incidence repair for Kaplansky's direct-finiteness problem

**Y. T. Miah — Research draft, 17 October 2026; revised 19 October 2026**

[Paper](../main.pdf) · [Mathematical sources](SOURCES.md) · [Dependencies](DEPENDENCIES.md)

## Contribution

The paper develops finite incidence constructions for odd-characteristic group algebras. Real Hadamard matrices replace an auxiliary-prime restriction. Repair-only union rows have fixed multiplicities, while the signed integer corrections are fixed affine offsets to the complete populations. Lines and Hadamard-decorated lines form the leading distribution, whose reduced-turn kernel admits an explicit contraction and uniform finite-size domination after inflation.

The principal finite results are a conditional plane-order `q=p^3` construction from a real Hadamard matrix of order `4p`, and an unconditional eventual signed-alphabet bound

`|T| ≤ p^6 + p^3 + 2^10 p^(23/20)` for primes `p ≥ 2^23`,

using Du–Jiang's Hadamard-existence theorem. The Ghaderpour parameter choice is also covered, with an alternative proof of its required matrix orders. In characteristic three, complete finite data use 6,654 signed letters, root degree 93, maximum graph degree 325, primitive leading bulk 132,388,347, and a fixed reservoir of 39,858 vertices per class.

Table 2 compares the two displayed characteristic-three direct-finiteness constructions directly. The present input has fewer signed letters and a smaller root degree than Mghirbi–Douglas, but maximum graph degree 325 is larger than their 257; there is no componentwise improvement. Their compact root and exact colour-balance repair are credited as predecessors.

The qualitative conclusion—torsion-free hyperbolic groups with scalar direct-finiteness failure in odd characteristic—is already given by Mghirbi–Douglas. The present group-algebra corollaries use the attributed OpenAI–Ivanov matching and bounded-path framework and Mghirbi–Douglas's deterministic geometric criterion. The contribution is the different finite construction and its quantitative bounds.

Alphabet size is not graph size, relator count, witness support, or computational cost. The characteristic-three threshold `m≥925` certifies sufficient finite-size turn domination only; it does not specify a computed terminal group presentation. No optimality or practical runtime bound is asserted.

## Reproduce the finite certificates

Use Python 3.10 or later, with NumPy and SymPy. From this directory:

```sh
python -m pip install -r requirements.txt
python verify/verify.py --output checks/results.json
```

Do not enable Python's `-O` option: the program requires assertions. It exits unsuccessfully if a check fails. Input certificates are read, not overwritten; the output directory is created as needed. Each output records the exact Python, NumPy and SymPy versions used; the original tested versions appear in `verification_summary.json`. A successful verification record is provided in `checks/finite_verification_2026-10-19.json`.

The program reconstructs all characteristic-three incidence coordinates from the specified finite data, the two-pencil seed, inverse pairing, repairs, reservoirs and pools; checks the separate error constants and the exact spectral margin; constructs the six small Paley Hadamard matrices and checks both design Gram identities; verifies the determinant obstruction for the unchanged Mghirbi–Douglas `q=p^4` model; and checks arithmetic boundary cases for the asymptotic theorems. The universal inequalities are proved in the paper.

The checks do not construct the external large Hadamard matrices, rerun the external complementary-sequence coverage computation, enumerate the final matching, or decide equality in its group. They are exact finite computations, not a formal proof of the full group-algebra theorem.

## Files

- `../main.pdf`: the research paper, including complete proofs and finite specifications.
- `verify/verify.py`, `requirements.txt`: reconstruction and exact checking program.
- `data/characteristic_three.json`, `data/hadamard_matrices.json`: necessary finite certificates compared with reconstructed data.
- `verification_summary.json`: Summary of the recorded finite checks and test environment.
- `checks/finite_verification_2026-10-19.json`: Recorded successful execution of the finite verifier.
- `SOURCES.md`, `DEPENDENCIES.md`: source versions and mathematical attribution.
- `RIGHTS.md`, `THIRD_PARTY_NOTICES.md`: rights and dependency notices.

## Citation and rights

Cite: Y. T. Miah, *Hadamard designs and incidence repair for Kaplansky's direct-finiteness problem*, research draft dated 17 October 2026, revised 19 October 2026.

The manuscript, original finite datasets and explanatory documentation are licensed **CC BY 4.0**, and the original verifier `verify/verify.py` is licensed **BSD 3-Clause**, subject to the author's applicable rights. See [LICENSE.md](../LICENSE.md), [RIGHTS.md](RIGHTS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
