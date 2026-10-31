# Session Log: Radiation Pressure in the Early Universe vs. Present

**Date:** Tuesday, August 11, 2026  
**Query:** was the radiation pressure greater in the earlier universe than it is now?  
**User:** William Brown (aka Grody Turdmongerson / @t98817)  
**Context:** Cosmology / Tau-Superblock related inquiry (general relativistic cosmology foundation)

---

## Direct Answer

**Yes.** The radiation pressure was vastly greater in the earlier universe than it is today.

---

## Detailed Explanation

### 1. What is radiation pressure in cosmology?

In the standard cosmological model (and any FRW-based framework, including extensions such as Tau-Superblock / multi-domain models), the cosmic radiation field consists primarily of:

- Photons (cosmic microwave background + any residual high-energy backgrounds)
- Neutrinos (and other relativistic species in the early universe)
- Any other ultrarelativistic particles or fields

For an ultrarelativistic (radiation-like) fluid, the equation of state is:

\[
P_r = \frac{1}{3} \rho_r c^{2}
\]

**Key to variables and functions:**

- \( P_r \): radiation pressure (force per unit area, SI units: Pa = N m⁻²)
- \( \rho_r \): radiation energy density (energy per unit volume)
- \( c \): speed of light in vacuum (\( \approx 2.998 \times 10^{8} \) m s⁻¹)
- The factor \( 1/3 \) arises because the momentum flux of isotropic ultrarelativistic particles is one-third of their energy density (from the stress-energy tensor of a perfect fluid with \( w = 1/3 \)).

Thus radiation pressure is **directly proportional** to the radiation energy density.

### 2. How radiation energy density evolves with cosmic expansion

The scale factor of the universe is denoted \( a(t) \), normalized so that \( a_0 = 1 \) today.

- Number density of photons (or other relativistic particles) scales as \( n \propto a^{-3} \) (volume dilution).
- Each photon’s energy redshifts as \( E \propto a^{-1} \) (wavelength stretches with expansion).
- Therefore total radiation energy density scales as:

\[
\rho_r(a) \propto a^{-4}
\]

or, equivalently, in terms of redshift \( z \) (where \( 1 + z = 1/a \)):

\[
\rho_r(z) = \rho_{r,0} (1 + z)^{4}
\]

**Key to variables:**

- \( a \): dimensionless scale factor of the FLRW metric (\( a = 1 \) today)
- \( z \): cosmological redshift
- \( \rho_{r,0} \): present-day radiation energy density
- \( \rho_r(z) \): radiation energy density at redshift \( z \)

Because \( P_r \propto \rho_r \), we also have:

\[
P_r(z) = P_{r,0} (1 + z)^{4}
\]

### 3. Quantitative comparison

Present-day radiation energy density (photons + neutrinos, standard model) is extremely small:

\[
\rho_{r,0} c^{2} \approx 4.2 \times 10^{-14}\ \mathrm{J\, m^{-3}}
\]

(or in more common cosmological units, \( \Omega_r h^{2} \approx 4.15 \times 10^{-5} \)).

At earlier times:

| Epoch                        | Approximate redshift \( z \) | Scale factor \( a \) | Factor \( (1+z)^{4} \) | Relative radiation pressure |
|-----------------------------|------------------------------|----------------------|-------------------------|-----------------------------|
| Today                       | 0                            | 1                    | 1                       | 1×                          |
| Recombination / CMB last scattering | ~1090                       | ~9.2 × 10⁻⁴          | ~1.4 × 10¹²             | ~1.4 trillion times greater |
| Matter-radiation equality   | ~3400                        | ~2.9 × 10⁻⁴          | ~1.3 × 10¹⁴             | ~130 trillion times greater |
| Big Bang nucleosynthesis    | ~10⁹                         | ~10⁻⁹                | ~10³⁶                   | 10³⁶ times greater          |
| Electroweak epoch (example) | ~10¹⁵                        | ~10⁻¹⁵               | ~10⁶⁰                   | 10⁶⁰ times greater          |

Even at the relatively “recent” epoch of recombination (≈380 000 years after the Big Bang), radiation pressure was already more than a **trillion times** higher than today. At earlier epochs the disparity becomes astronomically larger.

### 4. Physical consequences of the higher early radiation pressure

- **Radiation-dominated era**: Until matter-radiation equality (\( z \approx 3400 \)), radiation energy density (and therefore pressure) dominated the total energy budget of the universe. The expansion rate was controlled by radiation: \( H \propto a^{-2} \).
- **Acoustic oscillations**: In the photon-baryon fluid before recombination, radiation pressure provided the restoring force that drove the baryon acoustic oscillations (BAO) we observe today in the CMB and large-scale structure.
- **Jeans length / gravitational collapse**: High radiation pressure raised the Jeans mass, suppressing the growth of density perturbations on small scales until after recombination (the “Silk damping” and free-streaming effects).
- **Acceleration equation**: The second Friedmann equation (Raychaudhuri) contains the term \( \rho + 3P \). For radiation, \( \rho + 3P = 2\rho > 0 \), so radiation decelerates the expansion more strongly than non-relativistic matter (\( P \approx 0 \)).

### 5. Nuances and edge cases

- **Local vs. cosmic mean**: The question refers to the *cosmic* radiation field (CMB + neutrino background). Local radiation pressure inside stars, near black holes, or in terrestrial laboratories is of course unrelated to cosmic expansion history.
- **Other relativistic components**: In the very early universe, additional degrees of freedom (e.g., more neutrino species, sterile neutrinos, or hypothetical light particles) would have increased \( \rho_r \) still further. Standard cosmology already includes three neutrino species that were relativistic at early times.
- **Dark energy / vacuum pressure**: Today the dominant “pressure” in the universe is the negative pressure of dark energy (\( P_{\Lambda} \approx -\rho_{\Lambda} c^{2} \)). Radiation pressure is negligible by comparison.
- **Tau-Superblock / multi-domain context**: In frameworks with multiple co-located domains or conformal factors, the effective radiation content and its pressure contribution can be modulated by domain-specific scale factors or conformal weights. However, within each individual 3+1 domain that experiences standard expansion, the \( a^{-4} \) scaling of radiation still holds, so the qualitative conclusion remains: radiation pressure was far higher at early times.

### 6. Summary

Radiation pressure scales as \( (1+z)^{4} \). Because the universe has expanded by many orders of magnitude since the earliest epochs, the radiation pressure was enormously greater in the past than it is now. This fact is one of the cornerstones of the standard thermal history of the universe and of any geometric unification framework that recovers standard FLRW evolution in the late-time limit.

---

**Session saved:** 2026-08-11_Radiation_Pressure_Early_Universe.md  
**Location:** Tau-Superblock_Universe / Personal_Files  
