from pyumlify.generate import (
    scan_project,
    generate_plantuml_files,
    get_known_external_modules
)

def main():
    """
    Entry point for the pyumlify CLI.
    """
    print("📐 pyumlify is generating your UML diagrams...")
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Generate PlantUML diagrams for a Python project.")
    parser.add_argument("--root", type=str, default=".", help="Root directory of the Python project.")
    parser.add_argument("--output", type=str, default="./plantuml_output", help="Directory to store .puml files.")
    parser.add_argument("--requirements", type=str, default="requirements.txt", help="Path to requirements.txt file.")
    parser.add_argument("--include", type=str, nargs="*", default=[], help="Additional libraries to ignore (e.g. PyPDF2)")
    parser.add_argument("--clear", action="store_true", help="Clear the output directory before generating")

    args = parser.parse_args()

    # Optional: clear output directory
    if args.clear and os.path.exists(args.output):
        import shutil
        shutil.rmtree(args.output)

    os.makedirs(args.output, exist_ok=True)

    # Load external libraries (std lib + requirements + extras)
    external_libs = get_known_external_modules(args.requirements)
    for lib in args.include:
        external_libs.add(lib.lower())

    # Run generation
    project_data = scan_project(args.root)
    generate_plantuml_files(project_data, root_dir=args.root, output_dir=args.output, external_libs=external_libs)
    print("✅ Done! Check the 'plantuml_output/' directory for the generated .puml files.")
