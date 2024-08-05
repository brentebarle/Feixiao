# Configuration file for the Sphinx documentation builder.

import os
import sys
from typing import Any, Dict

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../'))  # Modify to point to your source code directory

# -- Project information -----------------------------------------------------
project = 'Feixiao'
author = 'Brent Ebarle'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',    # Include documentation from docstrings
    'sphinx.ext.napoleon',   # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',   # Add links to highlighted source code
    'sphinx.ext.githubpages',  # Publish to GitHub Pages
    'myst_parser',           # Support for Markdown files
    'sphinx_copybutton',     # Adds a "Copy" button to code blocks
    'sphinx_design',         # Adds design elements to documentation
    'sphinx_inline_tabs',    # Support for inline tabs
]

source_suffix = ['.rst', '.md']  # Include both .rst and .md files

master_doc = 'index'

exclude_patterns = []

# -- Autodoc configuration ---------------------------------------------------
autodoc_mock_imports = []  # List any modules to mock if they are not installed in the build environment
autodoc_member_order = 'bysource'
autodoc_preserve_defaults = True
autodoc_typehints = 'description'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_title = 'Feixiao Documentation'
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

html_theme_options: Dict[str, Any] = {
    'source_repository': 'https://gitlab.com/brentebarle/feixiao/',
    'source_branch': 'main',
    'source_directory': 'docs/',
    'footer_icons': [
        {
            'name': 'GitLab',
            'url': 'https://gitlab.com/brentebarle/feixiao',
            'html': """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0l-8 16h16L8 0z"></path>
                </svg>
            """,
            'class': '',
        },
    ],
}

# -- Options for MyST Parser -------------------------------------------------
myst_enable_extensions = [
    'colon_fence',  # Allows using the `:::` syntax for code blocks
    'deflist',      # Allows definition lists
]
myst_heading_anchors = 3  # Number of heading levels to include in the table of contents

# -- Options for Read the Docs and testing -----------------------------------
RTD_TESTING = False
if RTD_TESTING or 'READTHEDOCS' in os.environ:
    html_theme_options['announcement'] = (
        "This documentation is hosted on Read the Docs only for testing. Please use "
        "<a href='https://gitlab.com/brentebarle/feixiao/'>the main documentation</a> instead."
    )

# -- Options for theme development -------------------------------------------
html_js_files = []
html_context: Dict[str, Any] = {}

FONT_AWESOME_TESTING = False
if FONT_AWESOME_TESTING:
    html_css_files += [
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css',
    ]

    html_theme_options['footer_icons'] = [
        {
            'name': 'GitLab',
            'url': 'https://gitlab.com/brentebarle/feixiao',
            'html': '',
            'class': 'fa-brands fa-solid fa-gitlab fa-2x',
        },
    ]
