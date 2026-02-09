# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Dreem User's Manual"
copyright = "2025 by Unicontsoft"
author = "Unicontsoft"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = "index"
language = 'bg'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
# html_logo = "_static/logo-wide.svg"
html_title = "Unicontsoft Dreem"
# html_copy_source = True
# html_favicon = "_static/logo-square.svg"
html_last_updated_fmt = ""

html_static_path = ['_static']
html_css_files = ["tweaks.css"]

html_theme_options = {
    "path_to_docs": ".",
    "repository_url": "https://github.com/Unicontsoft/unicontsoft.github.io",
    "repository_branch": "master",
    "use_repository_button": True,
    "navigation_with_keys" : True,
    # "home_page_in_toc": True,
    # "use_edit_page_button": True,
    "use_source_button": True,
    # "use_issues_button": True,
    # "use_repository_button": True,
    "use_download_button": False,
    "use_sidenotes": True,
    "toc_title": "На страницата",
    "show_toc_level": 2,
    "collapse_navigation": False,
    "show_navbar_depth": 1,
    # "announcement": '<div class="bd-header-announcement__content">Test</div>',
    "icon_links": [
        {
            "name": "manual-pdf",
            "url": "https://raw.githubusercontent.com/Unicontsoft/unicontsoft.github.io/pdfs/manual.pdf",
            "icon": "fa-solid fa-file-pdf",
            "type": "fontawesome",
        }
    ],
    "external_links": [
      {"name": "link-one-name", "url": "https://<link-one>"},
      {"name": "link-two-name", "url": "https://<link-two>"}
    ]
}

# -- Options for rinohtype PDF output -------------------------------------
# , logo='_static/rinohtype_logo.pdf'
rinoh_documents = [
    dict(doc='guide/erp/000-index', target='manual', title='Ръководство на потребителя', subtitle='версия 2.0',
         author='Униконт Софт ООД', toctree_only=False,
         template='manual.rtt'),
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 3
