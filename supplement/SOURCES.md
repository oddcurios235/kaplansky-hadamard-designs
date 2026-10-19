# Mathematical sources

**Y. T. Miah, _Hadamard designs and incidence repair for Kaplansky's direct-finiteness problem_. Research preprint, 17 October 2026; revised 19 October 2026.**

This file fixes the external sources behind the paper. Keys agree with the bibliography. [DEPENDENCIES.md](DEPENDENCIES.md) describes the logical uses of these sources. Dates inside manuscripts are not assertions of first public availability.

## Direct construction and realization sources

| Key | Version and stable source | Exact use |
|---|---|---|
| MD26 | N. Mghirbi and S. Douglas, _Kaplansky's conjectures fail for torsion-free hyperbolic groups in positive characteristic_; manuscript dated 14 October 2026; v1.0.1, [DOI 10.5281/zenodo.23374592](https://doi.org/10.5281/zenodo.23374592); [author repository](https://github.com/Apsiape/kaplansky-conjectures-hyperbolic-groups) | Definitions 3.2–3.3, pp. 9–10; Theorem B and its proof, pp. 12–16; Theorem C, pp. 6, 30; Definition 7.1, Lemma 7.2 and §7.4 for the degree/alphabet comparison; §7.2 for colour balance; Proposition 7.11 for signed self-pairing; Proposition 8.3, p. 33, for finite-pattern transfer. The authors' version record identifies v1.0.1 as an author-order correction with no mathematical change. |
| Iva26 | S. V. Ivanov, _Zero divisors in group algebras of torsion-free groups in odd characteristic_, [arXiv:2610.17662v1](https://arxiv.org/abs/2610.17662v1), submitted 13 October 2026, manuscript dated 7 October 2026 | Lemma 2.2; Construction 4.1; Lemmas 4.2 and 4.4; Propositions 5.3 and 6.1; §6.1 on colours in the pattern count; §8.3 on the fixed-group, fixed-support transfer to characteristic zero. |
| OAI197a | OpenAI, _A torsion-free group algebra that is not directly finite_, dated 4 October 2026; [pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/direct-finiteness.pdf) | Proposition 2.1, §3.3, Lemma 3.3, Proposition 3.4, Theorem 4.1, Lemmas 4.2–4.4 and equation (4.11); the planar and cone arguments in §§5–6. The present model-dependent counts and its transfer are proved in §§7–8 and Appendices A–B. |
| OAI196 | OpenAI, _A torsion-free group algebra with zero divisors_, dated 23 September 2026; [pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf) | Predecessor of the matching, planar-extraction and cone-picture method; §4 and the proof of Lemma 5.2. |
| OAI257 | OpenAI, _A hyperbolic group with no geometric CAT(0) action_, dated 25 September 2026; [pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) | Theorem 3.1 and Lemma 3.8: antecedent of free-boundary accounting for a different complex, as attributed by MD26. No CAT(0) assertion is imported into this paper. |

The three OpenAI sources are fixed at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` of `openai/math`. For OAI197a the corresponding editable arguments are in `build/sections/random.tex`, `patterns.tex`, `planar.tex`, `topology.tex`, `algebra.tex` and `assembly.tex`, below the same pinned manuscript directory. PDF numbers, rather than an assumed agreement with source labels, are the principal locators above. These source manuscripts are not redistributed in this package.

## Hadamard existence inputs and their scope

**DJ24.** C. Du and Y. Jiang, _Golay complementary sequences of arbitrary length and asymptotic existence of Hadamard matrices_, [arXiv:2401.15381v1](https://arxiv.org/abs/2401.15381v1), 27 January 2024. Theorem 3, p. 18, supplies real Hadamard matrices of order

`u * 2^(6 floor(log2(u)/40) + 10)`

for every positive odd integer `u`. Its proof is in §IV and uses finite complementary-sequence coverage tabulated in Table II, p. 26. The associated verification sources are fixed at commit [`131f481f11f495a60174afd3220e1bbbdbb833c7`](https://github.com/csrlab-fudan/gcs_hadamard/tree/131f481f11f495a60174afd3220e1bbbdbb833c7) (7 February 2025) of `csrlab-fudan/gcs_hadamard`, in [`hadamard_verifcations/`](https://github.com/csrlab-fudan/gcs_hadamard/tree/131f481f11f495a60174afd3220e1bbbdbb833c7/hadamard_verifcations): `gen_S4.cpp`, `gen_S4.h` and `gcs_hadamard.cpp`. This later code snapshot is a provenance locator, not a claim to identify the exact 2024 execution. The present paper uses the exact v1 theorem; it does not rerun the external coverage computations or use the authors' matrix-generation code. This is the direct external input to Theorem 5.4 and, after Sylvester doubling, to Theorem 5.3.

**Gh15.** E. Ghaderpour, _Signed group orthogonal designs and their applications_, in C. J. Colbourn (ed.), _Algebraic Design Theory and Hadamard Matrices_, Springer Proceedings in Mathematics & Statistics **133** (2015), 107–123; [DOI 10.1007/978-3-319-17729-8_9](https://doi.org/10.1007/978-3-319-17729-8_9), [arXiv:1502.07668v1](https://arxiv.org/abs/1502.07668v1). Theorem 10, pp. 14–15 of the preprint, gives the stated one-variable parameter bound `14 + (1/5) log2(u-1)`. Setting the sole variable to one yields a real Hadamard matrix. Its proof uses the complementary-sequence estimate (15) and Livinskyi's Chapter 5, following Craigen's signed-group approach.

**Source qualification.** DJ24, p. 2, footnote 1, identifies a problem with a stronger estimate in Livinskyi that uses Koukouvinos–Seberry's 1991 Theorem 4. The present paper does not rely on resolving the ancestry of the corresponding older sequence bound. It retains Ghaderpour's parameter choice

`a_p = 14 + ceil(log2(p-1)/5)`

and proves existence at the exact order `p*2^a_p` directly from DJ24 and Sylvester doubling. Thus the numerical conclusion of Theorem 5.3 has an alternative proof, and is not offered as a separate verification of the older complementary-sequence estimate. The direct use of DJ24 in Theorem 5.4 is stronger in range and in its lower-order alphabet term.

**Liv12.** I. Livinskyi, _Asymptotic existence of Hadamard matrices_, M.Sc. thesis, University of Manitoba, Winnipeg, 2012, Chapter 5, especially §5.3. The [institutional thesis](https://mspace.lib.umanitoba.ca/bitstreams/46d98169-d70f-4d13-b3c7-a657d0ce68e2/download) supplies the source and metadata. Cited for the antecedent just described, not as a separately certified computational input.

**Cra95.** R. Craigen, _Signed groups, sequences, and the asymptotic existence of Hadamard matrices_, J. Combin. Theory Ser. A **71** (1995), 241–254, [DOI 10.1016/0097-3165(95)90002-0](https://doi.org/10.1016/0097-3165(95)90002-0). This is methodological ancestry, not a replacement for checking that the final auxiliary matrix is real.

## Classical and contextual references

| Key | Stable identifier or bibliographic locator | Role in this paper |
|---|---|---|
| AOP02 | Ara–O'Meara–Perera, Adv. Math. 170 (2002), 224–238; [DOI](https://doi.org/10.1006/aima.2002.2075) | Context: positive stable-finiteness results. |
| BP93 | Bogley–Pride, _Calculating generators of Π₂_, LMS Lecture Notes 197 (1993), 157–188; [DOI](https://doi.org/10.1017/CBO9780511629358.007) | Classical picture/second-homotopy framework, Appendix B. |
| BH99 | Bridson–Haefliger, _Metric Spaces of Non-Positive Curvature_ (1999); [DOI](https://doi.org/10.1007/978-3-662-12494-9) | Theorem III.H.2.9: linear isoperimetry implies hyperbolicity. |
| Bro82 | Brown, _Cohomology of Groups_, GTM 87 (1982); [DOI](https://doi.org/10.1007/978-1-4684-9327-6) | Chapter VIII: finite-dimensional classifying spaces exclude torsion; the cyclic-group argument is included. |
| Dir37 | Dirichlet, 1837; R. Stephan's translation, [arXiv:0808.1408v2](https://arxiv.org/abs/0808.1408v2), revised 24 November 2014 | Optional auxiliary-prime route. |
| DHJ15 | Dykema–Heister–Juschenko, Exp. Math. 24 (2015), 326–338; [DOI](https://doi.org/10.1080/10586458.2014.993051), [arXiv:1112.1790v4](https://arxiv.org/abs/1112.1790v4) | Cancellation patterns and universal left-invertible-element groups; Appendix D. |
| ES04 | Elek–Szabó, J. Algebra 280 (2004), 426–434; [DOI](https://doi.org/10.1016/j.jalgebra.2004.06.023), [arXiv:math/0305440v2](https://arxiv.org/abs/math/0305440v2) | Corollary 4.7 in the preprint: sofic group algebras are stably finite. |
| Hat02 | Hatcher, _Algebraic Topology_ (2002), [author edition](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) | Theorems 4.5, 4.32: Whitehead and Hurewicz, Appendix B. |
| Kap72 | Kaplansky, _Fields and Rings_, 2nd ed., University of Chicago Press, 1972 | Formulations of the problems. |
| LT79 | Lipton–Tarjan, SIAM J. Appl. Math. 36 (1979), 177–189; [DOI](https://doi.org/10.1137/0136016) | Recursive planar separation, Appendix B. |
| McK81 | McKay, _Subgraphs of random graphs with specified degrees_, Congr. Numer. 33 (1981), 213–223 | Switching antecedent; not the later same-title survey. |
| MW91 | McKay–Wormald, Combinatorica 11 (1991), 369–382; [DOI](https://doi.org/10.1007/BF01275671) | Switching antecedent; no degree-sequence enumeration theorem is used as a black box. |
| Min24 | Mineyev, _The topology and geometry of units and zero-divisors: origami_, 1 April 2024, revised 12 August 2026; [author PDF](https://mineyev.web.illinois.edu/art/top-geom-uzd-origami.pdf) | §2.2 signature condition; distinguish product-term pairing from dart-multiplicity pairing. |
| Mon69 | Montgomery, Bull. Amer. Math. Soc. 75 (1969), 539–540; [DOI](https://doi.org/10.1090/S0002-9904-1969-12234-2) | Characteristic-zero direct finiteness; Appendix D. |
| Oll05 | Ollivier, _A January 2005 Invitation to Random Groups_, Ensaios Matemáticos 10, SBM, 2005 | Earlier multiplicity organization, as used by OAI197a. |
| Pal33 | Paley, _On orthogonal matrices_, J. Math. Phys. 12 (1933), 311–320; [DOI](https://doi.org/10.1002/sapm1933121311) | Small real Hadamard matrices; explicit formulas in Appendix C. |
| Sch13 | Schweitzer, J. Group Theory 16 (2013), 667–693; [DOI](https://doi.org/10.1515/jgt-2013-0017), [arXiv:1202.6645](https://arxiv.org/abs/1202.6645) | Small-support matched rectangles and cancellation-pattern context. |
| Sin38 | Singer, Trans. Amer. Math. Soc. 43 (1938), 377–385; [DOI](https://doi.org/10.1090/S0002-9947-1938-1501951-4) | Cyclic projective-plane action; the characteristic-three difference set is also checked directly. |


## Additional bibliographic locators

| Key | Bibliographic locator | Mathematical use |
|---|---|---|
| BFF24 | H. Bradford and F. Fournier-Facio, _Hopfian wreath products and the stable finiteness conjecture_, Math. Z. **308** (2024), Paper No. 58, 28 pp.; [publisher / DOI](https://doi.org/10.1007/s00209-024-03589-3) | Section 1 records the classical implications from direct-finiteness failure and the Nullstellensatz reduction to finite fields. Cited in §8.3 and Appendix D; no wreath-product or Hopficity theorem is imported. |
| CH82 | D. J. Collins and J. Huebschmann, _Spherical diagrams and identities among relations_, Math. Ann. **261** (1982), no. 2, 155–183; [publisher / DOI](https://doi.org/10.1007/BF01456216) | Classical spherical-diagram and identities-among-relations ancestry for Appendix B. The immediate cone-picture source remains OAI196/OAI197a and MD26. |
| LS77 | R. C. Lyndon and P. E. Schupp, _Combinatorial Group Theory_, Ergebnisse der Mathematik und ihrer Grenzgebiete **89**, Springer-Verlag, Berlin, 1977, Chapter V; [2001 reprint / DOI](https://doi.org/10.1007/978-3-642-61896-3) | Classical van Kampen diagrams, finite presentations and the area convention in Appendix B. The bibliography explicitly distinguishes the original edition from the linked reprint. |
| Gar24 | G. Gardam, _Non-trivial units of complex group rings_, [arXiv:2312.05240v2](https://arxiv.org/abs/2312.05240v2), 29 October 2024 | Sections 1 and 3: finite coefficient equations and characteristic transfer, in Appendix D. |
