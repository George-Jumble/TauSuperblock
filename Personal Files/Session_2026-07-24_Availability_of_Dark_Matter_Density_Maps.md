# Session Log: Availability of Dark Matter Density Maps of the Universe

**Date**: 2026-07-24  
**Query**: Are there density maps of the dark matter in the universe available?  
**Context**: General astronomical/cosmological data availability (within ongoing TSB framework discussions).

---

## 1. Short Answer

Yes. Multiple classes of dark-matter density (or mass) maps are publicly available:

- High-resolution projected mass maps from weak gravitational lensing (observational).
- Full-sky or wide-area projected maps from CMB lensing.
- Reconstructed 3-D density and velocity fields of the local Universe.
- Large-scale structure density fields from galaxy redshift surveys (as tracers).
- Full 3-D volume density cubes from cosmological N-body and hydrodynamical simulations.

True volumetric 3-D density maps of the real Universe remain reconstructions or simulations; pure observational maps are usually 2-D projections (surface mass density \(\Sigma\)) or tomographic slices.

---

## 2. Major Public Observational Maps (as of mid-2026)

### 2.1 Highest-resolution weak-lensing mass map — JWST COSMOS-Web (January 2026)

- **Paper**: Scognamiglio et al., *Nature Astronomy* (published online 26 Jan 2026); arXiv:2601.17239.  
- **Coverage**: contiguous ~0.54–0.77 deg² field.  
- **Resolution**: angular resolution \(\approx 1.00 \pm 0.01\) arcmin — more than twice that of previous Hubble maps.  
- **Method**: shapes of ~129–250 000 background galaxies (many measured independently in F115W and F150W).  
- **Content**: reveals filaments, clusters, under-densities and structures out to \(z\sim 2\).  
- **Public data**:  
  - Weak-lensing mass maps released as Supplementary Data with the paper.  
  - JWST imaging: https://exchg.calet.org/cosmosweb-public/DR0.5/  
  - Supporting HST/XMM/Chandra data via IRSA/IPAC COSMOS archive.

This is currently the highest-resolution contiguous dark-matter map in existence.

### 2.2 Wide-area Stage-III weak-lensing surveys

| Survey | Approx. area | Public status | Notes |
|--------|--------------|---------------|-------|
| DES Y3 | ~5 000 deg² | Public mass maps & catalogues | Dark Energy Survey Year-3 cosmic-shear maps; extensively used for cosmology. |
| KiDS-1000 / KiDS-DR5 (Legacy) | ~1 350 deg² | Public | Kilo-Degree Survey; mass maps and cosmology chains released. |
| HSC-SSP | ~1 000 deg² (Wide) | Public DR1–DR3 | Hyper Suprime-Cam; shear catalogues and mass maps available. |

Combined DES + KiDS analyses also exist and release joint data products.

### 2.3 CMB lensing (full-sky projected dark matter)

- **Planck** lensing convergence maps (PR4 and earlier): full-sky projected mass maps publicly available from the Planck Legacy Archive.  
- These provide the largest-area (though lower-resolution) dark-matter maps.

### 2.4 Local-Universe reconstructions

- **Cosmicflows / 2M++ density and peculiar-velocity fields** (within ~200 \(h^{-1}\) Mpc).  
  - Public download of density and velocity grids (ASCII / numpy).  
  - Website: https://cosmicflows.iap.fr/ (or successor portals).  
- Useful for the nearby cosmic web, Local Group, and bulk flows.

### 2.5 Galaxy-density tracers (large-scale structure)

- DESI Year-1 to Year-5 galaxy catalogues and density fields (proxy for dark-matter on large scales).  
- SDSS / BOSS / eBOSS density reconstructions.  
- These are not pure dark-matter maps but are widely used as tracers under the assumption that galaxies follow the total mass distribution on large scales.

### 2.6 Euclid early data

- Euclid Quick Data Releases (Q1/Q2, 2026) beginning to provide high-quality imaging and shear catalogues over limited fields; full dark-matter maps expected in later releases. Public archive at ESAC.

---

## 3. Simulation Density Maps (public volume cubes)

- IllustrisTNG, EAGLE, Millennium, Bolshoi, MultiDark, etc.  
- Full 3-D dark-matter density fields at multiple redshifts are downloadable from the respective project portals.  
- Useful for comparing observed maps with theoretical predictions and for mock-catalogue generation.

---

## 4. Practical Access Notes

- Most survey mass maps are released as FITS files (Healpix or Cartesian) together with shear catalogues, redshift distributions and covariance matrices.  
- Supplementary material of the JWST COSMOS-Web paper contains the high-resolution maps directly.  
- IRSA, ESA archives, CDS/Vizier and the individual survey websites (DES, KiDS, HSC, Euclid) are the primary entry points.  
- For local reconstructions, the Cosmicflows portals provide ready-to-use density grids.

---

## 5. Relevance to TSB Framework (brief)

In the Tav-Superblock picture dark matter is interpreted as the gravitational shadow of the five co-located hidden domains. Observational mass maps therefore constrain the residual multi-domain density after projection onto our 4-D domain and after hierarchical conformal suppression. High-resolution maps (especially the new JWST map and forthcoming Euclid/LSST maps) provide quantitative targets for the predicted residual \(\Omega_{\rm DM}/\Omega_b \approx 5.2\) and for the spatial homogeneity of the domain shadows on scales \(\gtrsim 7\,h^{-1}\) Mpc.

---

## 6. Summary

Yes — high-quality dark-matter density / mass maps are publicly available today, ranging from the ultra-high-resolution JWST COSMOS-Web map (2026) through the wide-area Stage-III lensing surveys (DES, KiDS, HSC), full-sky Planck CMB lensing, local Cosmicflows reconstructions, and large simulation volumes. True volumetric maps of the real Universe remain reconstructions or simulations; the purest observational products are projected (or tomographic) mass maps derived from weak lensing.

**File location**  
`/home/workdir/artifacts/Personal_Files/Session_2026-07-24_Availability_of_Dark_Matter_Density_Maps.md`

---

*End of session — 2026-07-24*
