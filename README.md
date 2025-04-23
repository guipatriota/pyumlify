# pyumlify

**pyumlify** is a lightweight Python tool that scans your project's source code and automatically generates PlantUML class and package diagrams. It's designed to improve documentation and architecture visibility in any Python-based project — whether it's a microservice, CLI, library, or monolith.

---

## 🚀 Features

- 📁 Scans all `.py` files in your project, including modules at the root level.
- 🔍 Detects classes, methods, attributes, and inter-class dependencies.
- 📦 Builds a complete `packages.puml` diagram showing real `import` relationships between packages.
- 📄 Generates one `.puml` file per package/module containing only relevant classes.
- ✨ Ignores external libraries (via `requirements.txt` + `stdlib_list` + `importlib.metadata`) unless they contain project-specific classes.
- ❌ Skips `__init__` methods for cleaner class diagrams.
- 🎨 Uses a customizable PlantUML theme (Dracula by default).
- 🧠 Works out of the box, no need to modify your codebase.

---

## 📦 Use Cases

- Quickly visualize the structure of legacy code
- Generate architecture documentation for team onboarding
- Validate modularity and coupling in large codebases
- Create visuals for technical reports and system design docs

---

## 🛠 Requirements

- Python 3.8+
- `stdlib_list` (`pip install stdlib_list`)
- (Optional) PlantUML viewer/editor like [PlantUML Online](https://plantuml.com/), VSCode plugin, or IntelliJ plugin.

---

## 🧪 Usage

```bash
python generate_uml.py
```
The output .puml files will be generated in the plantuml_output/ folder.

## 📜 License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the [LICENSE](./LICENSE) file for details.
