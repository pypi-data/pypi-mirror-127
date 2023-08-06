[![Pytest](https://github.com/PyEllips/pyElli/actions/workflows/pytest.yml/badge.svg)](https://github.com/PyEllips/pyElli/actions/workflows/pytest.yml) [![Documentation Status](https://readthedocs.org/projects/pyelli/badge/?version=latest)](https://pyelli.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/v/pyElli)](https://pypi.org/project/pyElli/)


# pyElli
PyElli is a numerical solver for spectral ellipsometry employing well-known 2x2 and 4x4 algorithms.
It is intended for a broad case of problems including simple fitting of layered structures, anisotropic layers and any other light interaction with layered 1D structures.
It serves as a system for the day to day ellipsometry task at hand and makes fitting a breeze.

## Features
- A multitude of models to approximate the dielectric function of your material.
- Build up your structure easily from materials and layers.
- Simulate reflectiona and transmission spectra, ellipsometric parameters and Mueller matrices.
- Utilities to quickly convert, plot and fit your measurement data.
- Powerfull when necessary, editable and expandeble.

## How to get it
The installers for all releases are available at the [Python Package Index (PyPI)](https://pypi.org/project/pyElli/).

To install run:
```sh
pip install pyElli
```

A complete environment for pyElli is also available as a [Docker Container](https://hub.docker.com/r/domna/pyelli).
From a running Docker installation simply run:
```sh
docker pull domna/pyelli
```

The source code is hosted on [GitHub](https://github.com/PyEllips/pyElli), to install from source run:
```sh
python setup.py install
```

## Acknowledgements
- Based on Olivier Castany's [Berreman4x4](https://github.com/Berreman4x4/Berreman4x4)
- Solver2x2 based on Steve Byrnes's [tmm](https://github.com/sbyrnes321/tmm)