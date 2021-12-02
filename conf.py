# -- Path setup --------------------------------------------------------------
import os
import sys


sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------
project = "viscloudio"
copyright = "2021, Brighten Tompkins, Bardo Hernandez"
author = "Brighten Tompkins, Bardo Hernandez"


# -- General configuration ---------------------------------------------------
extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary"]

templates_path = ["_templates"]
exclude_patterns = []

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "private-members": True,
    "show-inheritance": True,
}

# -- Options for HTML output -------------------------------------------------
html_theme = "bizstyle"
