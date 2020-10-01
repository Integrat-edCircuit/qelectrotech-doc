#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# qelectrotech documentation build configuration file, created by
# sphinx-quickstart on Sun Aug 11 17:09:51 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys; sys.setrecursionlimit(2000)
import sphinxbootstrap4theme
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'rst2pdf.pdfbuilder',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'QElectroTech'
copyright = '2020, The QElectroTech Team'
author = 'Fernando Mateu'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.8'
# The full version, including alpha/beta/rc tags.
release = '2020'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '.hg*', 'Lib', 'Scripts']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# The filename format for language-specific figures
figure_language_filename = "{path}{language}/{basename}{ext}"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinxbootstrap4theme'
html_theme_path = [sphinxbootstrap4theme.get_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Navbar style.
    # Values: 'fixed-top', 'full' (Default: 'fixed-top')
    'navbar_style' : 'fixed-top',

    # Navbar link color modifier class.
    # Values: 'dark', 'light' (Default: 'dark')
    'navbar_color_class' : 'dark',

    # Navbar background color class.
    # Values: 'inverse', 'primary', 'faded', 'success',
    #         'info', 'warning', 'danger' (Default: 'inverse')
    'navbar_bg_class' : 'primary',

    # Show global TOC in navbar.
    # To display up to 4 tier in the drop-down menu.
    # Values: True, False (Default: True)
    'navbar_show_pages' : True,

    # Link name for global TOC in navbar.
    # (Default: 'Pages')
    'navbar_pages_title' : 'Pages',

    # Specify a list of menu in navbar.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean)
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    'navbar_links' : [
         ("Home", "https://qelectrotech.org/", True),
         ("Forum", "https://qelectrotech.org/forum/", True)
    ],

    # Total width(%) of the document and the sidebar.
    # (Default: 80%)
    'main_width' : '100%',

    # Render sidebar.
    # Values: True, False (Default: True)
    'show_sidebar' : True,

    # Render sidebar in the right of the document.
    # Values：True, False (Default: False)
    'sidebar_right': False,

    # Fix sidebar.
    # Values: True, False (Default: True)
    'sidebar_fixed': True,

    # Html table header class.
    # Values: 'inverse', 'light' (Deafult: 'inverse')
    'table_thead_class' : 'inverse'
}

# html_theme_options = {
#     'show_related' : 'true',
#     'fixed_sidebar' : 'true',
#     'sidebar_includehidden' : 'true',
#     'body_text_align' : 'justify',
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = { 
    '**': [
        'globaltoc.html',
#         'relations.html',
#         'sourcelink.html',
#         'searchbox.html'
    ] 
}

html_context = {
    'css_files': ['_static/custom.css'],
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'QElectroTechdoc'

# -- Options for pdf output ---------------------------------------------

#pdf_documents = [(master_doc, htmlhelp_basename, project, copyright),]
pdf_documents = [('index', u'QElectroTechdoc-0.8', u'QElectroTech User Manual', u'2020, The QElectroTech Team'),]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'QElectroTech.tex', 'QElectroTech Documentation',
     'Fernando Mateu', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'QElectroTech', 'QElectroTech Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'QElectroTech', 'QElectroTech Documentation',
     author, 'QElectroTech', 'One line description of project.',
     'Miscellaneous'),
]
