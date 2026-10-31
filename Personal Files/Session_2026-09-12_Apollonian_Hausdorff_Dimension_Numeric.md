# Session 2026-09-12 — Numerical Hausdorff dimension of the Apollonian residual set

**Method:** Generate a finite 2D Apollonian packing with centers; count circles of curvature \(\le K\); fit \(N(K)\sim c\,K^\delta\).

**3D:** literature value recorded; not recomputed in this run.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(r_i\) | Radius of circle \(i\) |
| \(k_i=1/r_i\) | Curvature |
| \(z_i\) | Complex centre |
| \(N(K)\) | Number of generated circles with \(0<k\le K\) |
| \(\delta\) | Fitted residual-set dimension (Boyd: \(N(K)\propto K^\delta\)) |
| \(\delta_2^{\mathrm{lit}}\) | Published 2D gasket dimension \(\approx 1.305686728\) |
| \(\delta_3^{\mathrm{lit}}\) | Published 3D residual dimension \(\approx 2.4739465\) |
| \(K_{\max}\) | Curvature cutoff of the generation |
| \(c\) | Prefactor in \(N=c K^\delta\) |
| \(f_{\mathrm{oct}}\) | Octant fill (not used in the fit) |

---

## 2. Recursion used

\[
k_4=k_1+k_2+k_3\pm 2\sqrt{k_1k_2+k_1k_3+k_2k_3},
\]

\[
z_4=\frac{k_1z_1+k_2z_2+k_3z_3\pm 2\sqrt{k_1k_2z_1z_2+k_1k_3z_1z_3+k_2k_3z_2z_3}}{k_4}.
\]

**Key:** \(k_i,z_i\) as above; both sign combinations kept if the circle is new and interior.

Seed: bounding circle \(k=-1\) at \(z=0\); two \(k=2\) at \(z=\pm 1/2\); inner \(k=3\) at \(z=\pm i/3\).

---

## 3. Run

| Quantity | Value |
|----------|--------|
| Positive circles stored | \(80\,001\) |
| \(K_{\max}\) | \(1999.86\) |
| Fit window | \(K\in[78.6,\,2000]\) |
| \(\delta_{\mathrm{fit}}\) | \(1.30239\) |
| \(c_{\mathrm{fit}}\) | \(4.70\) |
| \(\log\) RMS of fit | \(0.110\) |
| \(\delta_2^{\mathrm{lit}}\) | \(1.305686728\) |
| Relative error | \(0.25\%\) |

Sample counts:

| \(K\) | \(N(K)\) | \(N/K^{1.3057}\) |
|------:|--------:|-----------------:|
| 8.0 | 31 | 2.05 |
| 78.6 | 1163 | 3.90 |
| 246.3 | 6840 | 5.16 |
| 436.0 | 14474 | 5.18 |
| 771.9 | 29189 | 4.95 |
| 1366.6 | 51821 | 4.17 |
| 1999.9 | 80001 | — |

The ratio \(N/K^{1.3057}\) is not perfectly flat because the run is truncated at \(K_{\max}\) (missing descendants of large-\(k\) parents) and the seed had duplicate listings. The slope in the mid window is still within a quarter percent of the published \(\delta_2\).

---

## 4. What this number is

\(\delta\) is the dimension of the **residual set** (the foam), not of the disks and not of a Tau fiber. In 2D it lies between \(1\) and \(2\). In 3D the published analogue is \(\delta_3\approx 2.4739\) (between \(2\) and \(3\)).

If option B of the previous note is used (Soddy hierarchy in the octant interstitial), the hierarchical Mirron count below a cutoff scales as

\[
N_{\mathrm{M}}^{\mathrm{(hier)}}(K_{\mathrm{cut}})
\sim
c\,K_{\mathrm{cut}}^{\delta},
\qquad
\delta=\delta_3\text{ in Prime 3-space}.
\]

**Key:** \(K_{\mathrm{cut}}\) must still be named before this is a finite physical count. This fit does not name it and does not derive \(\tau\).

---

## 5. Status

| Item | Status |
|------|--------|
| 2D numerical \(\delta_{\mathrm{fit}}=1.302\) | this run |
| 2D literature \(\delta_2=1.305686728\) | accepted |
| 3D literature \(\delta_3\approx 2.4739\) | accepted, not recomputed |
| Use as survey \(N_\tau\) | rejected (keep octant \(8^g\)) |

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
