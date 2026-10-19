# Hadamard designs and incidence repair for Kaplansky’s direct-finiteness problem

**Y. T. Miah** · Research preprint · 19 October 2026

**Archived preprint:** [Zenodo DOI: 10.5281/zenodo.23485436](https://doi.org/10.5281/zenodo.23485436)

[Read the manuscript (PDF)](main.pdf) · [LaTeX source](main.tex) · [Finite verification](supplement/README.md) · [Formalisation notes](FORMALIZATION.md)

## About

This preprint studies quantitative finite-incidence constructions for scalar direct-finiteness counterexamples in torsion-free group algebras of odd characteristic. The finite architecture uses projective-plane incidences, Hadamard auxiliary blocks, two-pencil residue pairing, and exact integer repair. Repair-only union rows have fixed multiplicity, allowing the leading turn distribution to retain the required contraction.

The general construction gives a conditional signed-alphabet formula of `p^6 + p^3 + 4p` when a real Hadamard matrix of order `4p` exists, and an unconditional eventual bound of `p^6 + p^3 + 2^10 p^(23/20)` for primes `p >= 2^23`, using Du–Jiang's Hadamard-existence result. The characteristic-three example has 6,654 signed letters and root degree 93; its maximum graph degree is 325.

The qualitative group-algebra result is due to earlier work, notably Mghirbi–Douglas and its OpenAI–Ivanov antecedents. This paper proposes a different finite design and quantitative improvements for specified finite inputs; it does not claim the first qualitative counterexample. The manuscript contains detailed mathematical attribution and an acknowledgement of substantial GPT-6 Pro contributions.

## Contents

- `main.pdf`, `main.tex`, `references.bib`, `main.bbl`: the manuscript and bibliography.
- `sections/`: eight sections and four appendices, included by `main.tex`.
- `supplement/data/`: finite input certificates.
- `supplement/verify/verify.py`: Python verification and reconstruction program.
- `supplement/checks/`: recorded execution of the verifier.
- `supplement/SOURCES.md`, `supplement/DEPENDENCIES.md`: scholarly sources and mathematical dependency map.
- `LICENSE.md`, `LICENSES/`, `supplement/RIGHTS.md`, `supplement/THIRD_PARTY_NOTICES.md`: the applicable licences and third-party notices.
- `FORMALIZATION.md`: suggested entry points for independent formal verification.

## Run the finite checks

Use Python 3.10 or later with NumPy and SymPy. From the repository root:

```sh
python -m pip install -r supplement/requirements.txt
python supplement/verify/verify.py --output supplement/checks/results.json
```

Do **not** run with `python -O`: the verifier requires assertions. It reconstructs the finite characteristic-three data and checks other exact finite identities. Passing the verifier **does not** formally certify the random-matching, bounded-path, or geometric arguments, and no final matching or group presentation is computed by this script.

## Build the paper

With a TeX installation providing pdfLaTeX and BibTeX:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

If your TeX installation supplies `bibtex.original` instead of `bibtex`, use that command. For Overleaf, upload the repository files and select `main.tex` as the main document.

## Citation, reuse and formalisation

Please cite the manuscript as **Y. T. Miah, _Hadamard designs and incidence repair for Kaplansky’s direct-finiteness problem_ (2026)**. The included `CITATION.cff` has no DOI or arXiv identifier until one is assigned.

Potential targets for independent Lean formalisation are listed in [FORMALIZATION.md](FORMALIZATION.md). There is currently **no Lean formalisation in this repository**.

**Licences:** The manuscript, original documentation and original finite certificate data are available under **CC BY 4.0**; the Python verifier is available under **BSD 3-Clause**, each to the extent of the relevant rights. See [LICENSE.md](LICENSE.md) and [RIGHTS.md](supplement/RIGHTS.md). Third-party rights are unaffected. Please credit and cite the research when you build on it.
