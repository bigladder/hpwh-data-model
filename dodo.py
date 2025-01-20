"""
doit task/build automation
"""

import os
from doit.tools import create_folder

from lattice import Lattice

data_model = Lattice()


def task_validate_example_files():
    """Validates the example files against the JSON schema (and other validation steps)"""
    return {
        "file_dep": data_model.examples
        + [schema.file_path for schema in data_model.schemas],
        "actions": [(data_model.validate_example_files, [])],
    }


def task_generate_cpp_code():
    """Generate CPP headers and source for example schema."""
    return {
        "file_dep": [schema.file_path for schema in data_model.cpp_schemas]
        + [schema.meta_schema_path for schema in data_model.schemas],
        "targets": [schema.cpp_header_file_path for schema in data_model.cpp_schemas]
        + [schema.cpp_source_file_path for schema in data_model.cpp_schemas],
        "actions": [(data_model.generate_cpp_project, [[]])],
        "clean": True,
    }
