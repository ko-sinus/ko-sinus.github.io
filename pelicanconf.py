#from datetime import datetime
#COPYRIGHT_YEAR = datetime.now().year

SITE_AUTHOR = "kosinus"
DEFAULT_PAGINATION = 5
DEFAULT_LANG = "en"
SUMMARY_MAX_LENGTH = 42
# DISQUS_SITENAME = "dhilipsiva"
# MAIN_MENU = True
PATH = "content"

ROBOTS = "index, follow"

SITEDESCRIPTION = "Koji Andria"
SITELOGO = "/images/kosinus.jpg"
SITENAME = "Koji Andria"
BIO_TEXT = "Health Devices Engineer."
FOOTER_TEXT = '@2022 by Koji Andriamahery. Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'
SITETITLE = "kosinus"
SITEURL = "https://ko-sinus.github.io"

FAVICON = "/images/favicon.ico"

THEME = "pneumatic"
SIDEBAR_LINKS = [
    '<a href="/about-me/">About me</a>',
    '<a href="/resume/">Resume</a>',
    '<a href="/projects/">\nProjects</a>'
]
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = 'projects/' + ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

INDEX_SAVE_AS = 'projects/index.html'
ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DELETE_OUTPUT_DIRECTORY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'linenums': None}
    }
}

TIMEZONE = 'Europe/Paris'

ICONS_PATH = 'images'
LINKS = (("home", "/"),)

# Social widget
SOCIAL_ICONS = [
    ('https://www.linkedin.com/in/koji-andria/lang?=ENG', 'LinkedIn', 'fa-linkedin'),
    ('https://github.com/ko-sinus', 'GitHub', 'fa-github'),
]

PLUGIN_PATHS = ['myplugins']
PLUGINS = ['assets', 'neighbors']

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

#templates = ['404.html']
#TEMPLATE_PAGES = {page: page for page in templates}

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None