# Configuration file for the Sphinx documentation builder.

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
html_theme = 'furo'
html_title = "Feixiao"
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Modify to point to your source code directory

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = []  # List any modules to mock if they are not installed in the build environment
