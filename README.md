# PlanetSEmu

Code accompanying the paper **“Emulating Distributions of Planetary System Architectures”** by Ky Potter, Lucas Brefka, Derek Bingham, Eric B. Ford, Kelly R. Moran, and David C. Stenning.

## Overview

Forward models of planetary-system formation can produce scientifically rich distributions of system architectures, but direct use of expensive N-body simulations inside statistical inference can be computationally prohibitive.

**PlanetSEmu** provides a distributional emulator for these simulations. Rather than emulating only a mean response, the framework is designed to generate synthetic draws from the conditional distribution of key planetary-system observables given simulator inputs. The emulator therefore aims to preserve variation, heteroskedasticity, dependence, and rare-event behavior present in the original simulator output.

The emulator targets:

- detected planetary-system multiplicity;
- period-normalized transit-duration ratio, ξ;
- orbital period ratio, P; and
- orbital spacing in mutual Hill radii, Δ.

The resulting surrogate is substantially faster to sample from than rerunning the underlying N-body simulator and is intended to support simulation-based studies of exoplanet populations.

## Method

The emulator uses a modular generative construction rather than fitting a single model to the full mixed discrete-continuous output distribution.

At a high level, the workflow is:

1. Model detected multiplicity conditional on the simulator input.
2. Map detected multiplicity to a coarsened multiplicity group used to stabilize subsequent modeling.
3. Model the conditional marginal distributions of ξ and log(P) using flexible conditional quantile regression.
4. Represent dependence between these quantities in probability-integral-transform (PIT) space using a Student-t copula.
5. Refine upper-tail behavior using extreme-value methods where rare large values are not adequately represented by the baseline quantile models.
6. Model log(Δ) conditionally on the simulator input, multiplicity group, and sampled log(P).
7. Transform modeled quantities back to their scientific scales to obtain a synthetic planetary-system draw.

This structure allows the emulator to reproduce the major distributional features of the simulator while keeping individual components interpretable and diagnostically accessible.

## Paper

The repository accompanies:

> Potter, K., Brefka, L., Bingham, D., Ford, E. B., Moran, K. R., and Stenning, D. C.  
> **Emulating Distributions of Planetary System Architectures.**

The manuscript develops the statistical methodology, motivates the modeling choices, and presents calibration, dependence, and tail diagnostics for the emulator.

A formal citation will be added here when publication information and/or a DOI are available.

## Repository purpose

The code in this repository is intended to support the analyses reported in the paper, including:

- fitting the distributional emulator;
- evaluating out-of-fold calibration;
- examining PIT behavior;
- assessing preservation of dependence;
- evaluating upper-tail and rare-event behavior;
- generating synthetic draws from the fitted emulator; and
- reproducing figures and numerical results reported in the manuscript.

## Reproducibility

Clone the repository with:

```bash
git clone https://github.com/kydpotter/PlanetSEmu.git
cd PlanetSEmu
```

The analysis should be run using the scripts and/or notebooks provided in this repository. Because individual components of the emulator are modular, the fitting, diagnostic, and figure-generation workflows can also be examined separately.

Users interested in reproducing the paper should use the versions of the data, code, and model settings distributed with the release associated with the manuscript whenever possible.

## Model outputs

A fitted emulator generates draws from the conditional distribution of planetary-system architecture summaries rather than returning only point predictions.

A typical emulator draw consists of:

- a detected multiplicity;
- a corresponding multiplicity group;
- a sampled duration-ratio statistic ξ;
- a sampled orbital period ratio P; and
- a sampled mutual Hill spacing Δ.

This makes the emulator suitable for downstream analyses in which uncertainty and the full distribution of simulator outcomes are scientifically relevant.

## Diagnostics

The paper evaluates the emulator using diagnostics designed for distributional rather than purely mean-response prediction. These include assessments of:

- conditional calibration;
- PIT uniformity;
- reproduction of heteroskedasticity;
- dependence preservation;
- tail probabilities and exceedances; and
- behavior across the simulator input space.

These diagnostics are important because a surrogate can reproduce average behavior while still misrepresenting uncertainty, dependence, or rare outcomes.

## Scope

PlanetSEmu was developed for the exoplanet-formation application described in the accompanying paper. The broader statistical framework is modular and may also be useful for other stochastic simulators where the scientific target is the conditional distribution of simulator outcomes rather than only a conditional mean.

The current implementation should therefore be interpreted as both:

1. a reproducible analysis for the planetary-system application; and
2. an example of a more general approach to distributional emulation.

## Authors

- **Ky Potter** — Simon Fraser University; Los Alamos National Laboratory
- **Lucas Brefka** — The Pennsylvania State University; Center for Exoplanets and Habitable Worlds
- **Derek Bingham** — Simon Fraser University
- **Eric B. Ford** — The Pennsylvania State University; Center for Exoplanets and Habitable Worlds; Institute for Computational and Data Sciences; Center for Astrostatistics & Astroinformatics
- **Kelly R. Moran** — Los Alamos National Laboratory
- **David C. Stenning** — Simon Fraser University

## Acknowledgments

The research was supported in part by NSERC Discovery Grants and NASA award **80NSSC24K0150**. Computational research infrastructure was provided by the Penn State Institute for Computational and Data Sciences.

Please see the accompanying paper for the complete acknowledgments and funding statement.

## License

Please refer to the `LICENSE` file in this repository for terms governing use and redistribution of the code.

## Release information

Approved for public release: **LA-UR-26-23261**.
