# Potential Lean formalisation targets

No Lean project or mechanically verified proof is included in this repository. The Python verifier checks specified finite identities only; the remaining arguments are presented in the manuscript.

Potential Lean 4 formalisation targets, in roughly increasing order of difficulty:

1. **Finite-design identities (Section 2):** the Hadamard block intersection and replication identities, and the projective-plane line–union identity.
2. **Residue pairing and repair (Section 3):** the modular complement conditions, cyclic two-pencil computation, and exact integer-lifting step.
3. **Characteristic-three arithmetic (Section 6 and Appendix C):** restate selected finite certificates in a proof assistant and verify them by exact arithmetic, independently of the Python implementation.
4. **The three-class contraction argument (Section 4):** formalise the finite matrix identities and spectral inequalities, carefully distinguishing conditional turn weights from joint frequencies.
5. **Probabilistic/geometric arguments (Section 7 and Appendices A–B):** these involve substantially deeper combinatorial and geometric proof obligations; the existing Python checks do not cover them.

The main LaTeX file is `main.tex`, with individual sections in `sections/` and finite certificates in `supplement/data/`. Mathematical antecedents and source versions are listed in [supplement/SOURCES.md](supplement/SOURCES.md); the [mathlib](https://github.com/leanprover-community/mathlib4) library provides Lean 4 infrastructure.

Licensing and attribution information is given in [LICENSE.md](LICENSE.md) and [supplement/RIGHTS.md](supplement/RIGHTS.md).
