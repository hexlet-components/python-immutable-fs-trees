# coding: utf-8

__all__ = (
    'mkfile', 'mkdir',
    'is_file', 'is_directory',
)


def mkfile(name, meta={}):
    """Return file node."""
    return {
        'name': name,
        'meta': meta,
        'type': 'file',
    }


def mkdir(name, children=[], meta={}):
    """Return directory node."""
    return {
        'name': name,
        'children': children,
        'meta': meta,
        'type': 'directory',
    }


def is_directory(node):
    """Check is node a directory."""
    return node['type'] == 'directory'


def is_file(node):
    """Check is node a file."""
    return node['type'] == 'file'


def get_children(directory):
    """Return children of node."""
    return directory.get('children', [])


def get_meta(node):
    """Return meta of node."""
    return node['meta']


def get_name(node):
    """Return name of node."""
    return node['name']


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:

            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)

    return result
