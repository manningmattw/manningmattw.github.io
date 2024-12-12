AUTHOR = 'Matthew Manning'
SITENAME = 'Manning the Software Horizon'
SITEURL = "https://manningmattw.github.io"

PATH = "content"
OUTPUT_PATH  = ""
THEME = "/home/manning/pelican-themes/foundation-default-colours"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Python.org", "https://www.python.org/"),
    ("Django", "https://www.djangoproject.com/"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/manningmattw"),
)

DEFAULT_CATEGORY = "main"
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
        },
    },
    'output_format': 'html5',
}


# Foundation Default Colours Theme Settings
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://foundation.zurb.com/">Zurb Foundation</a>. Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'monokai'