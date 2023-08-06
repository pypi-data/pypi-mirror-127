# license-header-check

license-header-check is a tool to test if all modules in a python package have a certain license header.

## Install

```bash
pip install license-header-check
```

## Usage

You have to provide two arguments:

* license_file: A file with the license header as its only content.
* package_name: The name of the package that should be checked.

Optional:

* --ignore: A path in the package that should be ignored.

## Example

```bash
license-header-check LICENSE my_package
license-header-check LICENSE my_package --ignore my_package.my_subpackage
```
