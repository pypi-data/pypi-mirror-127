# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyspectools',
 'pyspectools.astro',
 'pyspectools.mmw',
 'pyspectools.models',
 'pyspectools.qchem',
 'pyspectools.spectra']

package_data = \
{'': ['*'], 'pyspectools': ['mpl_stylesheets/*', 'templates/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'PeakUtils>=1.3.2',
 'astropy==4.3.1',
 'astroquery==0.4.3',
 'bokeh>=2.4.0,<3.0.0',
 'colorlover>=0.3.0,<0.4.0',
 'ipython>=7.28.0,<8.0.0',
 'ipywidgets>=7.6.5,<8.0.0',
 'joblib>=1.0.1,<2.0.0',
 'lmfit>=1.0.2,<2.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'monsterurl>=0.2,<0.3',
 'networkx>=2.6.3,<3.0.0',
 'numba>=0.54.0,<0.55.0',
 'numpy>=1.16',
 'pandas>=1.3.3,<2.0.0',
 'paramiko>=2.7.2,<3.0.0',
 'periodictable>=1.6.0,<2.0.0',
 'plotly>=3.0.0',
 'ruamel.yaml>=0.17.16,<0.18.0',
 'scipy>=1.7.1,<2.0.0',
 'sklearn>=0.0,<0.1',
 'tinydb>=4.5.2,<5.0.0',
 'torch>=1.9.1,<2.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'uncertainties>=3.1.6,<4.0.0']

setup_kwargs = {
    'name': 'pyspectools',
    'version': '4.6.1',
    'description': 'A set of Python tools/routines for spectroscopy',
    'long_description': '# PySpecTools\n\n## A Python library for analysis of rotational spectroscopy and beyond\n\n---\n\n## Introduction\n\n[![DOI](https://zenodo.org/badge/90773952.svg)](https://zenodo.org/badge/latestdoi/90773952)\n[![Build Status](https://travis-ci.com/laserkelvin/PySpecTools.svg?branch=master)](https://travis-ci.com/laserkelvin/PySpecTools)\n\n![pst-logo](docs/source/_images/pst_logo_landscape.png)\n\n`PySpecTools` is a library written to help with analyzing rotational\nspectroscopy data. The main functions of this library are:\n\n1. Wrapper for SPFIT and SPCAT programs of Herb Pickett, with YAML/JSON\n   interpretation\n2. Generating specific figure types using `matplotlib`, such as polyads and\n   potential energy diagrams\n3. Parsing and filtering of Fourier-transform centimeter-wave and\n   millimeter-wave absorption data. This includes:\n   - Fitting of lineshapes (e.g. Lorentizan second-derivative profiles)\n   - Fourier-filtering\n   - Double resonance fitting\n4. Analysis of broad band spectra with the `AssignmentSession` and `Transition` classes.\n   These classes, combined with Jupyter notebooks, provide a way to assign spectra\n   reproducibly; astronomical and laboratory broadband spectra are supported.\n5. Autofit routines are available for a set of special cases, like linear/prolate\n   molecules. Eventually, SPFIT will be a backend option.\n6. Molecule identity inference (NEW!)—this uses a pre-trained probabilistic deep\n   learning model that allows users to perform inference on experimental constants\n   and expected composition to predict the most likely molecular formula and possible\n   functional groups present. See [our paper on the development of the first generation of this model](https://pubs.acs.org/doi/10.1021/acs.jpca.0c01376). An example of how to run this analysis\n   can be found [here.](https://laserkelvin.github.io/PySpecTools/examples/identifying_molecules.html)\n\nThe documentation for PySpecTools can be found [here](https://laserkelvin.github.io/PySpecTools).\n\nIf you use PySpecTools for research, please cite use the DOI badge below to cite the version\nof the package; this is not to track adoption, but rather for the sake of reproducibility!\n\n## Installation\n\n`conda` is the preferred way of maintaining software environments, and `poetry` is used to manage Python package dependencies.\n\nAs of PySpecTools 4.6.1, the installation is intended to be significantly more straightforward\nwith PyPI releases; in a given Python environment, just run:\n\n`pip install PySpecTools`\n\nAlternatively, if you\'re having issues, we recommend creating a new Python environment\nwithin `conda`; with Python 3.7+:\n\n1. `conda create -n pst python=3.7`\n2. `conda activate pst`\n3. `pip install poetry`\n4. `poetry install`\n\nInstallation on Windows is less straightforward. The following instructions avoid\nissues originating from virtual environments created by poetry and include a workaround\nfor a known issue with poetry in Windows.\n\n1. `conda create -n pst python=3.7`\n2. `conda activate pst`\n3. `pip install poetry`\n4. `poetry config virtualenvs.in-project false`\n5. `poetry config virtualenvs.create false`\n6. Navigate to the folder `C:\\Users\\user\\AppData\\Local\\pypoetry\\Cache` and delete all contents of this folder.\n7. Navigate to the folder containing PySpecTools\n8. `poetry install`\n\n## PyPickett\n\n`PySpecTools` includes a set of routines for wrapping SPFIT/SPCAT. The design\nphilosophy behind these functions is that the formatting and running of\nSPFIT/SPCAT can be a little tricky, in terms of reproducibility, parameter\ncoding, and visualization. These problems are solved by wrapping and managing\ninput files in an object-oriented fashion:\n\n1. Able to serialize SPFIT/SPCAT files from more human-friendly formats like\n   YAML and JSON.\n2. Automatic file/folder management, allowing the user to go back to an earlier\n   fit/parameters. Ability to "finalize" the fit so the final parameter set is\n   known.\n3. Display the predicted spectrum using `matplotlib` in a Jupyter notebook,\n   which could be useful for analysis and publication.\n4. A parameter scan mode, allowing the RMS to be explored as a function of\n   whatever parameter.\n\nThere is still much to do for this module, including a way of managing experimental lines.\n\n## Notes on release\n\n`PySpecTools` is currently being released on a irregular schedule, using a sequence-based version numbering system.\nThe numbering works as X.Y.Z, where X denotes huge changes that are backwards incompatible, Y are significant changes\n(typically new features) and Z are minor bug fixes. A freeze and release will typically occur when\na new version with potentially backwards breaking changes are about to be made. The large changes typically occur once a year (based on the trend so far).\n\nCurrently, `PySpecTools` is under the MIT license, which allows anyone to freely use and modify as you wish!\n\n## Planned features\n\n1. Integration of deep learning tools for molecule identifiction and spectral assignment\n2. Probability-based assignment routines - rather than single assignments.\n3. Revamp of codebase - needs a substantial re-organization that will likely result in backwards compatibility breaking.\n4. Additional Cython routines - many functions within `PySpecTools` are fast enough, but we can always go faster 😀\n5. Better abstraction in the `spectra.assignment` modules - need to move a lot of the complicated routines into subclasses (especially for transitions and line lists), although there is a case to be made for a simpler user interface (only have to deal with `LineList`, instead of three subclasses of `LineList`)\n\n## Contributing\n\nIf you have features you think would benefit other spectroscopists, you can raise an issue in the repo. Alternatively (and even better) would be to fork the repo, and submit a pull request!\n\nThe only comments on coding style are: \n\n1. Documentation is written in NumPy style\n2. Object-oriented Python\n3. Formatted with [`black`](https://black.readthedocs.io/en/stable/)\n\nThere are a set of unit tests that can be run to ensure the most complicated routines in the\nlibrary are working as intended. Right now coverage is poor, and so the tests I\'ve written\nfocus on the `assignment` module. There is a script contained in the `tests` folder that will\ngenerate a synthetic spectrum to test functionality on. To run these tests:\n\n``` python\ncd tests\npython generate_test_spectrum.py\npytest\n```\n\nYou will need to have `pytest` installed. These tests are designed to raise errors when there\nare huge errors; some tolerance is included for imperfect peak detection, for example. These\nare defined as constants within the `test_assignment.py` testing script.\n\n---\n\n## Questions? Comments?\n\nIf you have features you would like to have added, please raise an issue on the repo, or\nfeel free to send me an email at kinlee_at_cfa.harvard.edu.\n\nAlso, please feel free to fork and contribute! The code is being formatted with `black`,\nand uses NumPy-style docstrings. If you have any questions about contributing, drop me an\nemail!\n',
    'author': 'Kelvin Lee',
    'author_email': 'kin.long.kelvin.lee@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/laserkelvin/PySpecTools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.10.0',
}


setup(**setup_kwargs)
