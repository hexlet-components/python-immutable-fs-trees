'''Tests for hexlet.fs_tree.'''

from hexlet import fs


def test_is_directory():
    node = fs.mkdir('/')
    assert fs.is_directory(node)
    assert not fs.is_file(node)

def test_build():
    tree = fs.mkdir('/', [
        fs.mkdir('etc'),
        fs.mkdir('usr'),
        fs.mkfile('robots.txt')
    ])

    expected = {
        'children': [
          {
            'children': [],
            'meta': {},
            'name': 'etc',
            'type': 'directory',
          },
          {
            'children': [],
            'meta': {},
            'name': 'usr',
            'type': 'directory',
          },
          {
            'meta': {},
            'name': 'robots.txt',
            'type': 'file',
          },
        ],
        'meta': {},
        'name': '/',
        'type': 'directory',
    }
    assert tree == expected


def test_get_name():
    file = fs.mkfile('robots.txt')
    dir = fs.mkdir('etc')
    assert fs.get_name(file) == 'robots.txt'
    assert fs.get_name(dir) == 'etc'


def test_get_meta():
    file = fs.mkfile('robots.txt', {'owner': 'root'})
    dir = fs.mkdir('etc')
    assert fs.get_meta(dir) == {}
    assert fs.get_meta(file).get('owner') == 'root'


def test_get_meta():
    file = fs.mkfile('robots.txt')
    dir = fs.mkdir('/')
    tree = fs.mkdir('/', [
        fs.mkdir('etc'),
        fs.mkdir('usr'),
        fs.mkfile('robots.txt')
    ])
    expected = [
          {
            'children': [],
            'meta': {},
            'name': 'etc',
            'type': 'directory',
          },
          {
            'children': [],
            'meta': {},
            'name': 'usr',
            'type': 'directory',
          },
          {
            'meta': {},
            'name': 'robots.txt',
            'type': 'file',
          },
        ]
    assert not fs.get_children(file)
    assert fs.get_children(dir) == []
    assert fs.get_children(tree) == expected


