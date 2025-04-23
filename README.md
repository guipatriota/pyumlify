# pyumlify 🧩📦

**Automatically generate PlantUML diagrams from your Python codebase.**

**pyumlify** is a lightweight Python tool that scans your project's source code and automatically generates PlantUML class and package diagrams. It's designed to improve documentation and architecture visibility in any Python-based project — whether it's a microservice, CLI, library, or monolith.

---

## 🔧 Installation
```bash
pip install git+https://github.com/guipatriota/pyumlify.git
```

---

## 🚀 Usage
```bash
pyumlify --root src --output diagrams
```

Options:
- `--root`: Directory where your `.py` files are located (default: `.`)
- `--output`: Directory where `.puml` files will be saved (default: `./plantuml_output`)
- `--requirements`: Path to `requirements.txt` (default: `requirements.txt`)
- `--clear`: (optional) Delete previous `.puml` files in output folder before generating

## 📁 Output
- One `.puml` per package/module
- A `packages.puml` diagram with inter-package dependencies

## 📌 Example
```bash
pyumlify --root my_project --output docs/uml
```

Then render with [PlantUML](https://plantuml.com/):
```bash
plantuml docs/uml/*.puml
```

## 🧪 Run Tests
```bash
pytest tests/
```
---

## 🚀 Features

- 📁 Scans all `.py` files in your project, including modules at the root level.
- 🔍 Detects classes, methods, attributes, and inter-class dependencies.
- 📦 Builds a complete `packages.puml` diagram showing real `import` relationships between packages.
- 📄 Generates one `.puml` file per package/module containing only relevant classes (Class diagrams and Full Package Diagram).
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

## 📜 License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the [LICENSE](./LICENSE) file for details.
