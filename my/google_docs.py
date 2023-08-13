'''
[[https://google.com][Google]] data
'''

REQUIRES = [
    'git@github.com:hpi/google_docs',
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import google as user_config

@dataclass
class google_docs(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    return get_files(google_docs.export_path)


import google_docs.dal as dal

def rows(args):
  _dal = dal.DAL(inputs())
  yield from _dal.rows(sheet_id=args['sheet_id'])

