from .core import extract, pipeline

class EngineError(AttributeError):
    pass

class Engine(object):
    def __init__(self, *args, **kwargs):
        self.mapping = {}
        self.functions = []
        self.payloads = []

        if 'html' in kwargs:
            encoding = kwargs.get('encoding', None)
            self.root_etree = extract(kwargs['html'], encoding)

    def register(self, *funs):
        for fun in funs:
            self.functions.append(fun)
        return self

    def start(self, ):
        pass

    def process(self, *args):
        funcs = self.functions or args

        if not self.root_etree:
            raise (EngineError("No HTML document to extract from."))

        for funs in funcs:
            data = self.root_etree
            self.payloads.append(pipeline(data, funs))
