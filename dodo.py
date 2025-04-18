"""
doit task/build automation
"""

from lattice import Lattice

data_model = Lattice(build_validation=False)


def task_generate_meta_schemas():
    """Generate JSON meta schemas"""
    return {
        "file_dep": [schema.file_path for schema in data_model.schemas],
        "targets": [schema.meta_schema_path for schema in data_model.schemas],
        "actions": [(data_model.generate_meta_schemas, [])],
        "clean": True,
    }


def task_validate_schemas():
    """Validate the example schemas against the JSON meta schema"""
    return {
        "task_dep": [f"generate_meta_schemas"],
        "file_dep": [schema.file_path for schema in data_model.schemas]
        + [schema.meta_schema_path for schema in data_model.schemas],
        "actions": [(data_model.validate_schemas, [])],
    }


def task_generate_json_schemas():
    """Generate JSON schemas"""
    return {
        "task_dep": [f"validate_schemas"],
        "file_dep": [schema.file_path for schema in data_model.schemas]
        + [schema.meta_schema_path for schema in data_model.schemas],
        "targets": [schema.json_schema_path for schema in data_model.schemas],
        "actions": [(data_model.generate_json_schemas, [])],
        "clean": True,
    }


def task_validate_example_files():
    """Validates the example files against the JSON schema (and other validation steps)"""
    return {
        "task_dep": [f"validate_schemas"],
        "file_dep": data_model.examples
        + [schema.file_path for schema in data_model.schemas],
        "actions": [(data_model.validate_example_files, [])],
    }


def task_generate_cpp_code():
    """Generate CPP headers and source for example schema."""
    return {
        "task_dep": [f"validate_schemas"],
        "file_dep": [schema.file_path for schema in data_model.cpp_schemas]
        + [schema.meta_schema_path for schema in data_model.schemas],
        "targets": [schema.cpp_header_file_path for schema in data_model.cpp_schemas]
        + [schema.cpp_source_file_path for schema in data_model.cpp_schemas],
        "actions": [(data_model.generate_cpp_project, [])],
        "clean": True,
    }
