# python-immutable-fs-trees

[![github action status](https://github.com/hexlet-components/python-immutable-fs-trees/workflows/Python%20CI/badge.svg)](https://github.com/hexlet-components/python-immutable-fs-trees/actions)

## Install

```shell
pip install hexlet-immutable-fs-trees
```

## Usage example

```python

>>> import hexlet.fs as fs
>>> fs.is_file(fs.mkfile('config'))
True
>>> fs.is_directory(fs.mkdir('etc'))
True

>>> tree = fs.mkdir('etc', [fs.mkfile('config'), fs.mkfile('hosts')])
>>> children = fs.get_children(tree)
>>> fs.get_name(children[0])
'config'
>>> list(map(lambda item: fs.get_name(item), children))
['config', 'hosts']

```

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/hexletguides.github.io/master/images/hexlet_logo128.png)](https://ru.hexlet.io/pages/about)

This repository is created and maintained by the team and the community of Hexlet, an educational project. [Read more about Hexlet (in Russian)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-immutable-fs-trees).
