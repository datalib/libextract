try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
