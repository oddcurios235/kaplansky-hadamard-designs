# Third-party notices and implementation provenance

The verification program is an original implementation of the formulas and finite constructions described in the accompanying paper. It uses the paper's 82-element cyclic difference set and reconstructs the remaining characteristic-three arrays. The small Hadamard matrices are generated from the displayed Paley formulas, not copied from a matrix database. Neither OpenAI's nor Mghirbi–Douglas's nor Du–Jiang's verification source code is included.

Mathematical ancestry is credited at the points of use in the paper and recorded in [SOURCES.md](SOURCES.md) and [DEPENDENCIES.md](DEPENDENCIES.md). Attribution of a mathematical method is distinct from redistribution of an implementation.

The program imports these separately installed dependencies:

| Dependency | Use | Upstream license information |
|---|---|---|
| NumPy | Bounded integer incidence arrays and small matrix multiplication | [NumPy license](https://github.com/numpy/numpy/blob/main/LICENSE.txt) |
| SymPy | Exact symbolic polynomial expansion and integer arithmetic utilities | [SymPy license](https://github.com/sympy/sympy/blob/master/LICENSE) |

The dependencies and their source trees are not bundled. Their license files are supplied by their distributions. The proof PDF embeds standard TeX fonts for viewing; no font files are redistributed as standalone package assets.
