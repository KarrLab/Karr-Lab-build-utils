<!--[![PyPI package](https://img.shields.io/pypi/v/Karr-Lab-build-utils.svg)](https://pypi.python.org/pypi/Karr-Lab-build-utils)-->
[![Documentation](https://readthedocs.org/projects/karr-lab-build-utils/badge/?version=latest)](http://karr-lab-build-utils.readthedocs.org)
[![Test results](https://circleci.com/gh/KarrLab/Karr-Lab-build-utils.svg?style=shield)](https://circleci.com/gh/KarrLab/Karr-Lab-build-utils)
[![Test coverage](https://coveralls.io/repos/github/KarrLab/Karr-Lab-build-utils/badge.svg)](https://coveralls.io/github/KarrLab/Karr-Lab-build-utils)
[![Code analysis](https://codeclimate.com/github/KarrLab/Karr-Lab-build-utils/badges/gpa.svg)](https://codeclimate.com/github/KarrLab/Karr-Lab-build-utils)
[![License](https://img.shields.io/github/license/KarrLab/Karr-Lab-build-utils.svg)](LICENSE)
![Analytics](https://ga-beacon.appspot.com/UA-86759801-1/Karr-Lab-build-utils/README.md?pixel)

# Karr Lab build utilities

This package performs several aspects of the Karr Lab's build system:

* Create repositories with our default directory structure and files

  * Files for packaging Python code
  * Sphinx documentation configuration
  * CircleCI build configuration

* Tests code with Python 2 and 3 using pytest
* Uploads test reports to our test history server
* Uploads coverage report to Coveralls
* Generates HTML API documentation using Sphinx

The build system is primarily designed for:

* Code that is implemented with Python 2/3
* Tests that can be run with pytest
* Code that is documented with Sphinx in Napolean/Google style
* Continuous integration with CircleCI

## Installation

1. Install dependencies

  * `git`
  * `libffi-dev`
  * `pygit2`

2. Install package 
  ```
  pip install git+git://github.com/KarrLab/Karr-Lab-build-utils#egg=karr_lab_build_utils
  ```

## Using the utilities to build, test, and document Python packages

### Create a Git repository for the package

Use the `create_repository` subcommand to create a new Git repository
```
karr-lab-build-utils create_repository --dirname /path/to/new_repo --url https://github.com/KarrLab/new_repo.git
```

This will create a repository with the following directory structure and files
```
/path/to/repo/
  LICENSE
  setup.py
  setup.cfg
  MANIFEST.in  
  requirements.txt
  README.md
  <repo_name>
    __init__.py
      __version__ = '<version_number>'
    __main__.py (optional, for command line programs)
  tests/
    requirements.txt
    fixtures/
      secret/ (git-ignored fixtures that contain usernames, passwords, and tokens)
  docs/
    conf.py
    requirements.txt
    index.rst
    _static (optional for any files needed for the documentation)
```

### Write your code

Follow the [Google Python style guide](https://google.github.io/styleguide/pyguide.html)

### Test your code

See our [primer](http://intro-to-wc-modeling.readthedocs.io/en/latest/concepts_skills/software_engineering/testing_python.html)

### Document your code

Follow the following examples

#### Class
```
class MyClass(object):
    ''' Short description

    Long description

    Attributes:
      arg1 (:obj:`type`): description
      arg2 (:obj:`type`): description
      …
    '''

    ...
```

#### Methods
```
def my_method(self, arg1, arg2):
    ''' Short description

    Long description

    Args:
      arg1 (:obj:`type`): description
      arg2 (:obj:`type`, optional): description
      …

    Returns:
      :obj:`type`: description

    Raises:
      :obj:`ErrorType`: description
      …
    '''

    ...
```

### Install the package, run the tests, and generate the documentation
```
karr-lab-build-utils install-requirements
karr-lab-build-utils run-tests
karr-lab-build-utils make-documentation
```

## Documentation
Please see the [API documentation](http://Karr-Lab-build-utils.readthedocs.io).

## License
The build utilities are released under the [MIT license](LICENSE).

## Development team
This package was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.
