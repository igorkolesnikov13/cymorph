import sys
import os
import sphinx_rtd_theme
from cymorph.asymmetry import Asymmetry

# generate api directory if it doesn't already exist
if not os.path.exists('api'):
    os.mkdir('api')


# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CyMorph'
copyright = '2022, Igor Kolesnikov and contributors'
author = 'Igor Kolesnikov'

release = '2.0'
version = '2.0.9'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'numpydoc',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting'
]



autosummary_generate = True
templates_path = ['_templates']

# numpydoc_show_class_members = False
# autoclass_content = "class"
# autodoc_default_flags = ["members", "no-special-members"]

source_suffix = '.rst'
master_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
}
intersphinx_disabled_domains = ['std']


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
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
