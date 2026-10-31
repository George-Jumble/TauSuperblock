# Why EM can be domain-confined while gravity mixes

**Session date:** 19 September 2026  
**Claim:** Photons are causally confined to a domain because each domain has its own null cone (staggered orbital velocities). Gravity still influences other domains because it is not the same captured-null-signal that light is.  
**Short answer:** The *causal-confinement* idea is the right Superblock reason. The *black-hole / gravity-beyond-the-horizon* slogan is the wrong reason, and “gravity is not bound by \(c\)” is forbidden *inside our domain* by GW170817. Write an inter-domain kernel, not a superluminal graviton.

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(i,j=1,\ldots,6\) | Superblock domains |
| \(g_{\mu\nu}^{(i)}\) | metric of domain \(i\) |
| \(c_i\) | null-cone speed in domain \(i\), measured with that domain’s metric and clocks |
| \(V_{\rm orb}^{(i)}\) | staggered orbital velocity of domain \(i\) on the supersphere |
| \(F_{\mu\nu}^{(i)}\) | Faraday tensor living in domain \(i\) |
| \(A_\mu^{(i)}\) | electromagnetic potential of domain \(i\) |
| \(\mathcal K_{ij}\) | inter-domain gravitational / impulse kernel |
| \(c_{\rm GW}\) | speed of gravitational waves *in our domain* |
| \(c_{\rm EM}\) | speed of light *in our domain* |
| \(\langle T_{\mu\nu}^{(j)}\rangle_i\) | stress of domain \(j\) as it appears in domain \(i\) after averaging |

---

## 1. Yes: the intended picture

Six co-located 3+1D domains sit on an internal supersphere. They are given staggered \(V_{\rm orb}^{(i)}\) from the E8 / phase construction. Each domain therefore has its own time orientation and its own null cone. A photon is a null excitation of *that* domain’s Maxwell field. It cannot jump cones. What we call dark matter is ordinary stress on another cone, seen only through a channel that is not Maxwell.

That is intelligible. It is a geometric hidden-sector theory: one shared embedding, several domain-intrinsic gauge fields, one mixed gravitational kernel.

The next sentences have to be more careful than the black-hole analogy.

---

## 2. The black-hole slogan does not do this job

“Photons can be captured by a black hole; gravity manifests beyond the event horizon” is popular language. It is not a mixing mechanism.

Nothing causal comes out of a horizon. Light does not leave. Gravitational *signals* (waves) also do not leave. The exterior field of a black hole is the geometry of the outside, fixed by the mass-energy that produced the hole and by the vacuum Einstein equation. It is not a messenger that outran light from the interior.

If a draft uses horizons as the reason gravity mixes and light does not, a referee will read “TSB gravity is superluminal” and stop. Delete the horizon analogy from the mixing paragraph. Keep horizons for collapse / bounce / PK-engine discussions if they belong there. They do not explain inter-domain dark matter.

---

## 3. Gravity is bound by \(c\) *inside our domain*

GW170817: a neutron-star merger produced gravitational waves and light that arrived within a few seconds after \(\sim 130\) million years. In our domain,

\[
\left|\frac{c_{\rm GW}-c_{\rm EM}}{c_{\rm EM}}\right|\lesssim 10^{-15}.
\]

So TSB cannot say “electromagnetism is bound by the speed of light and gravity is not.” Not here. Not in the solar system. Not in the LIGO band.

The only version that survives is:

- *Inside domain \(i\)*, Maxwell and the local impulse / wave channel share that domain’s null cone. \(c_{\rm GW}^{(i)}=c_{\rm EM}^{(i)}\).
- *Between domains*, there is no shared Maxwell field. There is an averaged kernel \(\mathcal K_{ij}\) defined on the embedding (supersphere / twistor space / time average), not a photon and not a gravitational wave running along our light cones from domain \(j\) to domain \(i\).

Different sentence. Different object. The inter-domain channel is not “gravity faster than light.” It is “gravity is an embedding average; light is domain-intrinsic.”

---

## 4. What “different speeds of light” is allowed to mean

It cannot mean six different numerical values of \(c\) in one shared 4D coordinate chart. That is a Lorentz-violating multi-metric soup, already constrained by cosmic rays, gravitational Čerenkov, and GW170817.

It can mean this:

Each domain \(i\) has its own metric \(g_{\mu\nu}^{(i)}\) and its own Maxwell field \(F_{\mu\nu}^{(i)}\). The null cones

\[
g_{\mu\nu}^{(i)}\,dx^\mu dx^\nu=0
\]

need not coincide after the domains are compared through the supersphere embedding. A curve that is null in \(g^{(j)}\) need not be null in \(g^{(i)}\). Photons of \(j\) are not on-shell excitations of \(A_\mu^{(i)}\).

The orbital velocities \(V_{\rm orb}^{(i)}\) then do real work: they are the relative embedding motions that tilt the cones with respect to one another. Causal disconnection of Maxwell is “the cones do not share rays after embedding,” not “one \(c\) is larger than another in SI units.”

Write the comparison map. Call it \(e_i\): domain \(i\) into the supersphere. Then “no EM mixing” is

\[
e_i^*A^{(j)}=0\quad(j\neq i),
\]

or a stronger statement that the pull-back of \(F^{(j)}\) is not a source for \(A^{(i)}\). That is the confinement law. It is a constitutive / bundle statement, not a horizon statement.

---

## 5. The gravitational mixing law, in the same language

If gravity mixes, there must be a kernel that *does* pull stress across the embedding:

\[
G_{\mu\nu}^{(i)}
=8\pi G\left(
T_{\mu\nu}^{(i)}
+\sum_{j\neq i}\mathcal K_{ij}\bigl[\langle T^{(j)}\rangle\bigr]
\right).
\]

**Key:** \(\mathcal K_{ij}\) is not a photon propagator and not a 4D graviton propagator at speed \(c_i\). It is whatever the twistor average / stochastic impulse map produces when domain \(j\)’s stress is read from domain \(i\).

That is why stochastic TSB and “no graviton” matter here. If gravity in TSB is an average of Mirron impulses on the common embedding, \(\mathcal K_{ij}\) is allowed to exist even though \(A_\mu^{(j)}\) does not couple to \(A_\mu^{(i)}\). Light is a connection on a domain bundle. Gravity is a statement about the embedding.

If instead gravity is a metric wave on \(g_{\mu\nu}^{(i)}\) obeying the same cone as \(F_{\mu\nu}^{(i)}\), then tilting the cones confines gravity too, and other-domain matter is dark in every sense, including gravitationally. That would kill the dark-matter story. So TSB *must* keep gravity off the domain Maxwell cone. That is a design requirement, not a slogan.

---

## 6. A clean paragraph for the next draft

Use something this tight:

> Each Superblock domain carries its own metric and its own Maxwell field. Staggered embedding velocities tilt the six null cones so that a ray of domain \(j\) is not a ray of domain \(i\). Photons therefore remain in their domain: there is no shared \(U(1)\) connection. The gravitational channel is not that connection. It is the twistor-averaged impulse kernel on the common supersphere, which maps \(\langle T_{\mu\nu}^{(j)}\rangle\) into the curvature seen in domain \(i\). Inside a single domain, gravitational waves and light share that domain’s cone, in agreement with GW170817. Between domains there are no photons and no superluminal waves — only the average of embedding stress.

Then stop. Do not add event horizons to that paragraph.

---

## 7. What still has to be shown

Understanding the picture is not the same as having the map.

- Define \(e_i\) and the relative \(V_{\rm orb}^{(i)}\) so that the six cones are actually disjoint for Maxwell rays.
- Prove \(e_i^*F^{(j)}=0\) (or the weaker “does not source \(A^{(i)}\)”).
- Construct \(\mathcal K_{ij}\) from the same embedding, without giving it a pole at the speed of light in domain \(i\).
- Check that \(\mathcal K_{ii}\) still gives \(c_{\rm GW}=c_{\rm EM}\) inside our domain.
- Check that \(\mathcal K_{ij}\) for \(j\neq i\) does not produce a fifth force or gravitational Čerenkov radiation in our detectors.
- Produce \(\rho_{\rm DM}^{\rm (eff)}=\sum_{j\neq i}(\mathcal K_{ij}T^{(j)})_{00}\) of the right size and clustering.

Until those exist, “photons are causally confined, gravity still influences space” is the correct *ontology*. It is not yet the proof.

---

## File location

`Tau-Superblock-Universe/Personal-Files/2026-09-19_why-EM-confined-gravity-mixes.md`
