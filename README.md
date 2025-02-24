# Python Utility Template

Template for a custom Python-based utility that hooks into OVITO and can easily be shared with other users.

This repository contains a template for creating your own [Python script utility](https://ovito.org/docs/python/introduction/custom_utilities.html), 
which can be installed into *OVITO Pro* or the [`ovito`](https://pypi.org/project/ovito/) Python module using *pip*.

## Getting Started

1. Click the "Use this template" button to create your own repository based on this template.
2. Rename `src/PackageName` to reflect the name of your utility.
3. Implement your [utility](https://ovito.org/docs/python/introduction/custom_utilities.html) in [`src/PackageName/__init__.py`](src/PackageName/__init__.py).
4. Fill in the [`pyproject.toml`](pyproject.toml) file. Fields that need to be replaced with your information are enclosed in descriptive `[[field]]` tags. Please make sure to include ovito>=3.12.0 as a dependency. Depending on your needs, you can add additional fields to the `pyproject.toml` file. Information can be found [here](https://setuptools.pypa.io/en/latest/userguide/index.html).
5. Fill in the [`README_Template.md`](README_Template.md) file. Again, the `[[fields]]` placeholders should guide you. Feel free to add other sections like "Images", "Citation", or "References" as needed.
6. Add meaningful examples and data sample files to the `examples` directory to help others understand the use of your modifier.
7. Pick a license for your project and replace the current (MIT) [`LICENSE`](LICENSE) file with your license. If you keep the MIT license, please update the name and year in the current file.
8. Once you're done, rename `README_Template.md` to `README.md`, replacing this file.

## Testing

Python utilities do no support automated testing, yet.
