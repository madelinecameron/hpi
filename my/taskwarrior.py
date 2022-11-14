'''
[[https://inthe.am][TaskWarrior]] data
'''

REQUIRES = [
    'git+https://github.com/hpi/taskwarrior'
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import taskwarrior as user_config

@dataclass
class taskwarrior(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    return get_files(taskwarrior.export_path)


import taskwarrior.dal as dal


def projects():
    _dal = dal.DAL(inputs())
    yield from _dal.projects()

def tasks():
    _dal = dal.DAL(inputs())
    yield from _dal.tasks()

