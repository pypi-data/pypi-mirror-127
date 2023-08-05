Hookup is a Python decorator to monitor one or more attributes on a given object, and trigger a callback function to be called when the attribute(s) value changes.

Example:

```python
from hookup import hookup

@hookup(attrs=["version"], callback="update_version")
class Software:
    def __init__(self):
        version = 1

    def update_version(self):
        # This is the callback function that will be called when the attribute's value changes
        with open("version.txt") as _file:
            _file.write(self.version)

software = Software()
software.version=2
```

# Installation

To install Hookup, simply:

```
$ pip install hookup
```

# Usage

Hookup is designed to be used as a decorator on a class:

```python
@hookup(attrs=["version"], callback="update_version")
class Software:
```

You must pass in the two required arguments:
1. `attrs` - a List of attributes that will be watched for changes
2. `callback` - a function belonging to the class used as a callback

Upon the value of any watched attribute (`attrs`) changing from one value to another, the callback function will be executed.

The callback function will be called with no additional parameters. For example, the following would both be valid callbacks:

```python
def callback(self):
```

```python
def callback(self, option="default"):
```


# Contributing

1. Check for open issues or open a new issue to kick off discussion
2. Fork the repository on Github, create a branch and make your code changes
3. Write a test which shows that the bug was fixed, or that the new feature works as expected
4. Send a PR with a clear description of the change


# Changelog

## 0.1.1 (2021-11-10)

* Initial release
