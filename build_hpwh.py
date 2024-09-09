# Use `pip install lattice` , or copy `lattice` subfolder here.
from lattice import Lattice
from pathlib import Path
import os

root_dir = "data_model"
build_dir = "."
build_out_dir = "../../src/data_model"

lat = Lattice(root_dir, build_dir,  build_out_dir, False)

lat.generate_cpp_headers()

