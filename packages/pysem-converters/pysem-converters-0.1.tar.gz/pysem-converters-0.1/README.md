<h1 align="center">PYSEM-CONVERTERS</h1>

<div align="center">

![GitHub status](https://img.shields.io/badge/status-active-brightgreen)
![GitHub issues](https://img.shields.io/github/issues/pysem/converters?color=yellow)
![GitHub pull requests](https://img.shields.io/github/issues-pr/pysem/converters)
![GitHub license](https://img.shields.io/github/license/pysem/converters?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/pysem/converters?color=red)

</div>

---

<p align="center"> 
Pysem-converters is a modular library to simplify unit conversions
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](./TODO.md)
- [Contributing](./CONTRIBUTING.md)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Pysem-converters makes conversions very simple and intuitive. It supports many units.

- OBJECT CONVERTERS
    - isString
    - isInt
    - isFloat
    - isBytes
    - isBool
    - isDictionary
    - isList
    - isSet
    - isTuple
    - isJson
    - json_to_str
    - json_to_bytes
    - json_to_xml
    - str_to_bytes
    - str_to_json
    - bytes_to_str
    - bytes_to_json


- TIME CONVERTERS
    - seconds
    - minutes
    - hours
    - days
    - weeks
    - fortnights
    - years
    - months
    - centuries
    - millenniums


- TEMPERATURE CONVERTERS
    - celsius
    - fahrenheit
    - kelvin


- DISTANCE CONVERTERS
    - centimeter
    - millimeter
    - kilometer
    - inch
    - hand
    - foot
    - yard
    - mile
    - light year
    - astronomical unit
    - parsec
    - nautical mile
    - angstrom
    - micron
    - planck length

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

```
Pint==0.16.1
```

### Installing

```bash
# Using python pip
$ pip install pysem-converters

# Using git
$ git clone https://github.com/pysem/converters.git
$ cd converters
$ pip install -r requirements.txt
$ python setup.py install
```

### Break down into end to end tests

```bash
cd /tests
python3 <test_name>.py
```

## 🎈 Usage <a name="usage"></a>

```python
from pysem_converters import time_converter, SECONDS, MINUTES

print(time_converter(10, SECONDS, MINUTES))
```

## 🚀 Deployment <a name = "deployment"></a>

pysem-converters is a python library, when installed, just import it to your project.

```python
import pysem_converters
from pysem_converters import *
```

## ⛏️ Built Using <a name = "built_using"></a>

- Python
- Pint

## ✍️ Authors <a name = "authors"></a>

- [@tory1103](https://github.com/tory1103) - Idea, Concept & Initial work

See also the list of [contributors](https://github.com/tory1103/LKD/contributors) who participated in this project.

<p align="center">
  <a href="https://github.com/pysem/converters/graphs/contributors">
    <img src="https://contributors-img.web.app/image?repo=pysem/converters"  alt=""/>
  </a>
</p>
