from pyumlify.generate import generate_plantuml_files

def main():
    """
    Entry point for the pyumlify CLI.
    """
    print("📐 pyumlify is generating your UML diagrams...")
    generate_plantuml_files()
    print("✅ Done! Check the 'plantuml_output/' directory for the generated .puml files.")
