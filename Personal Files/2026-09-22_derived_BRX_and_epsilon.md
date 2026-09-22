# Derived BR_X^th and numeric epsilon

**Session date:** 2026-09-22  
**Status:** HOLD test-module. Not ledger IN.  
**Inputs used:** V_orb Scheme A (gamma_d, gamma_s), 7 active clockwork slots (Phi_8 is reset), neutron valence udd.  
**Inputs not used:** Delta_TEP as a fit knob, Tau cylinder, 4 alpha/3, WilfiCon, phi, Fornal-Grinstein on-shell chi gamma.

This replaces the pipeline's underived target 0.0094 with a formula built from corpus objects.

---

## Variable and function key

| Symbol | Meaning | Value |
|---|---|---|
| gamma_d | Lorentz factor of domain 1 (d, near, neutron valence) | 2.176 |
| gamma_s | Lorentz factor of domain 2 (s, mid, first non-valence domain) | 43.29 |
| gamma_c, gamma_b, gamma_t | Faster hidden domains | 589.4, 1936.6, 7.989e4 |
| gamma_hex | Six-domain conformal / hex factor | 1.405 |
| N_7 | Active clockwork slots. Phi_8 is reset, not a slot. | 7 |
| BR_0 | Isotropic hidden branching (unpolarized, B ~ 0) | derived |
| epsilon | Relative modulation under magnetic polarization | derived |
| s | Polarization parameter | 0 unpolarized; +1 magnetic-bottle lock |
| tau_beta | Inverse of the visible beta width | 888.1 ± 2.0 s |

Functions:

BR_0 = 1 / (gamma_d * gamma_s)

BR_Sigma = (1/gamma_d) * sum_{i in {s,c,b,t}} 1/gamma_i

BR_X(s) = BR_0 * (1 + epsilon * s)

tau_tot(s) = tau_beta * (1 - BR_X(s))

Delta tau_pol = tau_beta * BR_0 * epsilon

---

## 1. Mechanism

A free neutron is a Prime-domain u plus two near-domain d's. Visible beta decay stays on the Prime / near pair and yields a Prime proton.

A hidden branch is a two-clock coincidence on the internal supersphere: the near-domain clock and the first non-valence clock (domain 2, s) must present a simultaneous tick so the Mirron 2-surface can hand the udd cell into an off-Prime sheet. That sheet does not yield a Prime-domain proton.

Time-dilation of domain i relative to Prime is gamma_i. Uncorrelated clocks coincide at rate 1/(gamma_i gamma_j). Prime has gamma_0 = 1 and does not appear in the product.

Final state is domain-internal. No on-shell chi gamma or chi e+ e-.

---

## 2. Leading BR_X^th

BR_0 = 1 / (2.176 * 43.29) = 1 / 94.19904 = 0.010616

The pipeline printed theory_target_BR = 0.0094. That is (gamma_hex - 1)/gamma_s = 0.405/43.29 = 0.009356. Hex surplus is a gravitational average, not a tunneling rate. Replace the pipeline target with 1/(gamma_d gamma_s).

Subleading: BR_Sigma = 0.011639. Quote BR_0 as the prediction and +0.001023 as a one-sided theory band.

Not used: WKB e^{-2} = 0.135; Zeeman mu B / Delta_TEP ~ 10^{-16}; 4 alpha/3.

---

## 3. Numeric epsilon

epsilon_7 = 1/7 = 0.14286

One of seven active slots locks to B when the trap holds low-field-seeking neutrons.

epsilon_{2/7} = 2/7 = 0.28571

Nucleon-structure refinement: two valence d quarks address the same slot.

s = 0: unpolarized or B ~ 0 (proton beam, J-PARC, ideal material bottle).
s = +1: magnetic bottle, lock opens the hidden gate.

Oriented form if the octonion axis is unknown: BR_X(theta) = BR_0 (1 + epsilon cos theta).

Do not use epsilon = mu_n B / Delta_TEP.

---

## 4. Predictions

With tau_beta = 888.1 s:

| Setup | s | epsilon | BR_X | tau_tot |
|---|---|---|---|---|
| Beam / material / unpolarized | 0 | — | 0.01062 | 878.67 s |
| Magnetic bottle | +1 | 1/7 | 0.01213 | 877.33 s |
| Magnetic bottle | +1 | 2/7 | 0.01365 | 875.98 s |

Delta tau_pol = 1.33 s (eps 1/7) or 2.66 s (eps 2/7).
Observed material − magnetic = 2.3 s. eps 2/7 is closer. That is a check, not a fit.

Hard falsifiers:
1. J-PARC appearance must return ~888 s if s=0. Published 877.2 s is a live fail unless +4.0/-3.6 s systematics move it up.
2. Magnetic-bottle polarity / map with |Delta tau| << 1 s kills eps = 1/7.
3. Material and magnetic averages converging to < 0.4 s kills both epsilons.
4. On-shell photons or e+e- at 1% withdraws the module.
5. BBN / |V_ud| must use tau_beta ~ 888 s, not the bottle number.

---

## 5. Ledger

HOLD. Do not move to IN until J-PARC, a polarity run, and the CKM/BBN assignment are faced.

Engine: sb_engine/neutron.py ; CLI: python research_tool.py neutron

---

## Worked numbers

gamma_d gamma_s = 94.19904
BR_0 = 0.01061582
tau_beta BR_0 = 9.428 s
tau_tot(s=0) = 878.67 s
Delta tau(eps 1/7) = 1.332 s
Delta tau(eps 2/7) = 2.664 s
