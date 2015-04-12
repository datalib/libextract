"""
    libextract.html._xpaths
    ~~~~~~~~~~~~~~~~~~~~~~~

    Defines several XPaths used in the article and
    tabular extraction strategies.
"""


SELECT_ALL = '//*'
REL_SELECT_ALL = './/*'

NODES_WITH_TEXT = '//*[not(self::script or self::style)]/\
                     text()[normalize-space()]/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'
