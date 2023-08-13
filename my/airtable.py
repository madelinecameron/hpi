'''
[[https://airtable.com][Airtable]] data
'''

REQUIRES = [
    'git+https://github.com/hpi/airtable',
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import airtable as user_config

@dataclass
class airtable(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    return get_files(airtable.export_path)


import airtable.dal as dal

def sessions():
    _dal = dal.DAL(inputs())
    yield from _dal.sessions()


from my.core.pandas import check_dataframe, DataFrameT

def records(args = dict()):
    _dal = dal.DAL(inputs())
    yield from _dal.records(base_name=args.get('baseName'), table_name=args.get('tableName'))
