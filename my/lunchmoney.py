'''
[[https://lunchmoney.app][LunchMoney]] data
'''

REQUIRES = [
    'git+https://github.com/hpi/lunchmoney'
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import lunchmoney as user_config

@dataclass
class lunchmoney(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    return get_files(lunchmoney.export_path)

import lunchmoney.dal as dal

def accounts():
    _dal = dal.DAL(inputs())
    yield from _dal.accounts()

def transactions():
    _dal = dal.DAL(inputs())
    yield from _dal.transactions()
