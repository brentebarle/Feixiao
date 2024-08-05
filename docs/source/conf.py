# Configuration file for the Sphinx documentation builder.

import tibas.tt
import alabaster

# -- Project information -----------------------------------------------------
project = 'Feixiao'
author = 'Brent Ebarle'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',    # Include documentation from docstrings
    'sphinx.ext.napoleon',   # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',   # Add links to highlighted source code
    'sphinx.ext.githubpages'
]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'tt'  # You can change this to other themes like 'sphinx_rtd_theme'
html_theme_path = [tibas.tt.get_path(), alabaster.get_path()]
html_static_path = ['_static']

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Modify to point to your source code directory

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = []  # List any modules to mock if they are not installed in the build environment
