"""
    libextract.xpaths
    ~~~~~~~~~~~~~~~~~

    A handful of useful xpath expressions to help you along
    the way.
"""

PARENT_NODES = '//*/..'

TEXT_NODES = '//*[not(self::script or self::style)]/\
                     text()[normalize-space()]/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'
