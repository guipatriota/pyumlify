from setuptools import setup, find_packages

setup(
    name="pyumlify",
    version="0.1.0",
    description="Generate PlantUML class and package diagrams from Python code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Guilherme Ditzel Patriota",
    license="GPLv3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "stdlib_list",
    ],
    entry_points={
        "console_scripts": [
            "pyumlify=pyumlify.generate:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
