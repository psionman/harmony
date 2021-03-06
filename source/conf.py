# -- Imports -----------------------------------------------------------------

from recommonmark.parser import CommonMarkParser
import sphinx_bootstrap_theme
import os, re

# -- Get version -------------------------------------------------------------

version_string = ''
VERSION_FILE="versions.py"
with open(VERSION_FILE, 'r') as f_version:
    version_string = f_version.read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_string, re.M)
if mo:
    version_string = mo.group(1)


# -- Project information -----------------------------------------------------

project = 'Harmony User'
copyright = '2021, Jeff Watkins'
author = 'Jeff Watkins'
release = version_string


# -- General configuration ---------------------------------------------------

html_path = os.sep.join(['build', 'html', 'index.html'])
local_index_page = os.getcwd().replace('source', html_path)
print('-'*len(local_index_page))
print(local_index_page)
print('-'*len(local_index_page))
html_favicon = 'favicon.ico'

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
]

source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser',}
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

numfig = True
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]