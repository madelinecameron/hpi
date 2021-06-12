'''
[[https://todoist.com][Todoist]] data
'''

REQUIRES = [
    'git+https://github.com/hpi/todoist'
]

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Iterable

from my.core import Paths, get_files

from my.config import todoist as user_config

@dataclass
class todoist(user_config):
    # paths[s]/glob to the exported JSON data
    export_path: Paths


def inputs() -> Sequence[Path]:
    return get_files(todoist.export_path)


import todoist.dal as dal


def projects():
    _dal = dal.DAL(inputs())
    yield from _dal.projects()

def tasks(args):
    _dal = dal.DAL(inputs())
    yield from _dal.tasks(id=args['id'])

def completed(args):
  _dal = dal.DAL(inputs())

  since = args['since'] if 'since' in args else None
  until = args['until'] if 'until' in args else None
  id = args['id'] if 'id' in args else None

  yield from _dal.completed(since=since, until=until, id=id)

def activity(args):
  _dal = dal.DAL(inputs())
  yield from _dal.activity(_id=args['id'])

def taskComment(args):
  _dal = dal.DAL(inputs())
  yield from _dal.taskComment(_id=args['id'])
