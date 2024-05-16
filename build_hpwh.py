# Use `pip install lattice` , or copy `lattice` subfolder here.
from lattice import Lattice
from pathlib import Path
import os

root_dir = "data_model"
build_dir = "."
build_out_dir = "out"

lat = Lattice(root_dir, build_dir,  build_out_dir, True)

lat.generate_cpp_headers()
#lat.generate_json_schemas#(build_out_dir, build_out_dir)
#lat.generate_json_examples()f

#in_file = "Rheem2020Prem50.yaml"
#out_file = "out.json"
#lat.do_translate(in_file, out_file)