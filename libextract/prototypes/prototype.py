from functools import wraps
from statscounter import stats

from ..formatters import table_json, get_table_rows, chunks



def processes(*tags):
    tags = set(tags)
    def decorator(fn):
        @wraps(fn)
        def reducer(nodes):
            for n in nodes:
                #yield fn(n) if n.tag in tags else n
                if n.tag in tags:
                    yield fn(n)
                    continue
                yield n
        return reducer
    return decorator


def reduces(*tags):
    tags = set(tags)
    def decorator(fn):
        @wraps(fn)
        def reducer(nodes):
            return [fn(n) for n in nodes if n.tag in tags]
        return reducer
    return decorator


def maps(tag):
    def decorator(fn):
        @wraps(fn)
        def mapper(node):
            for row in node.iter(tag):
                yield fn(row)
        return mapper
    return decorator


@reduces('td')
def count_td(node):
    return 1


@maps('tr')
def td_counts(node):
    return sum(count_id(node))


@maps('tr')
def td_list_per_tr(node):
    return get_td(node)


@processes('table')
def convert_table(node):
    table = table_json(node)
    if not table:
        mode = stats.mode(td_counts(node))
        rows = [tds for tds in td_list_per_tr(node) if len(tds) == mode]

        table = {str(col): [' '.join(row[col].text_content().split()) for row in rows]
                 for col in range(mode)}
    return table
