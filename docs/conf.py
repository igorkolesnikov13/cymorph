import sphinx_rtd_theme
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import cymorph

# -- Project information -----------------------------------------------------

project = 'cymorph'
copyright = '2022, Igor Kolesnikov'
author = 'Igor Kolesnikov'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'numpydoc',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting'
]

numpydoc_show_class_members = False
autosummary_generate = ["reference.rst"]
autoclass_content = "class"
autodoc_default_flags = ["members", "no-special-members"]
source_suffix = '.rst'
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_theme = 'sphinx_rtd_theme'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

epub_show_urls = 'footnote'

# additional
exclude_patterns = ['_build', '**.ipynb_checkpoints']
default_role = 'obj'
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = []
htmlhelp_basename = 'cymorphdoc'
latex_elements = {}
latex_documents = [
  ('index', 'cymorph.tex', u'cymorph Documentation',
   u'Igor Kolesnikov', 'manual'),
]

man_pages = [
    ('index', 'cymorph', u'cymorph Documentation',
     [u'Igor Kolesnikov'], 1)
]

texinfo_documents = [
  ('index', 'cymorph', u'cymorph Documentation',
   u'Igor Kolesnikov', 'cymorph', 'One line description of project.',
   'Miscellaneous'),
]
