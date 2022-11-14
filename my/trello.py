'''
[[https://trello.com][trello]] data
'''

REQUIRES = [
    'git+https://github.com/hpi/trello'
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import trello as user_config

@dataclass
class trello(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    print("INSTANT")
    return get_files(trello.export_path)


import trello.dal as dal


def boardsWithCards():
    _dal = dal.DAL(inputs())
    yield from _dal.boardsWithCards()

