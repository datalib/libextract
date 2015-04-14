from functools import wraps


def debug(fn):
    """
    This decorator will hook into a function's out
    and print out the output value.

    @debug
    @node_processor
    def if_table(node):
        if node.tag == "table":
            table = table_json(node)
            for e, row in enumerate(table['Average female height']):
                s = re.split("^(.*)cm", row)
                table['Average female height'][e] = "".join(s[:2]).strip()
            return table
        else:
            return node

    Sample output:

    decorator running ... output: <generator object filter_tags...>)
    Press <Enter> to continue
    decorator running ... output:
    {
        'Sample population / age range': [
                u'20\u201329',
                u'19\u201349',
                '17 (healthy)',
                ...]
    }
    Press <Enter> to continue
    decorator running ... output: <Element ol at 0x6111778>)
    Press <Enter> to continue
    decorator running ... output: <Element span at 0x61036d8>)
    Press <Enter> to continue
    decorator running ... output: <Element div at 0x38a4bd8>)
    Press <Enter> to continue
    decorator running ... output: <Element ul at 0x3af64a8>)
    Press <Enter> to continue
    """
    prefix = fn.__name__
    @wraps(fn)
    def decorator(*args, **kwargs):
        print("{0} running ... output: {1})".format(prefix, args))

        input("Press <Enter> to continue")

        for d in fn(*args, **kwargs):
            print("{0} running ... output: {1})".format(prefix, d))
            input("Press <Enter> to continue")
            yield d

        #yield data
    return decorator


def stream_debug(fn):
    prefix = fn.__name__
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for item in fn(*args, **kwargs):
            print('%s: %r' % (prefix, item))
            yield item
    return wrapper
