"""
doit task/build automation
"""

import os
from doit.tools import create_folder

from lattice import Lattice

data_model = Lattice()

def task_validate_example_files():
  '''Validates the example files against the JSON schema (and other validation steps)'''
  return {
    'file_dep': data_model.examples + [schema.path for schema in data_model.schemas],
    'actions': [(data_model.validate_example_files,[])]
  }
