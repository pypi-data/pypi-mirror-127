# Lazy License

[![PyPI package](https://img.shields.io/badge/pip%20install-lazylicense-brightgreen)](https://pypi.org/project/lazylicense/)
[![version number](https://img.shields.io/pypi/v/lazylicense?color=green&label=version)](https://pypi.org/project/lazylicense/)
[![Actions Status](https://github.com/oddaspa/lazylicense/workflows/Build%20status/badge.svg)](https://github.com/oddaspa/lazylicense/actions)
[![PyPI downloads](https://img.shields.io/pypi/dm/lazylicense.svg)](https://pypistats.org/packages/lazylicense)
[![License](https://img.shields.io/github/license/oddaspa/lazylicense)](https://github.com/oddaspa/lazylicense/blob/main/LICENSE.txt)

Python package for adding license for source files.

## Installation

```sh
$ pip install lazylicense
```

## Usage:

Inserts Apache v2.0 snippet at the beginning of files.

Apache v2.0:

```
Copyright [year] [author]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### Arguments

| Argument         | Description                           | Default                        |
| :--------------- | :------------------------------------ | :----------------------------- |
| -e / --extension | Extension type to enter license into. | py                             |
| -f / --folder    | Folder to recursively scan.           | None (entire folder structure) |
| -a / --author    | Author to be injected into license.   | "Author"                       |
| -y / --year      | Year of license.                      | 2021                           |

### Example

```sh
python -m lazylicense --extension py --folder src --author "Odd Gunnar Aspaas" --year 2021
```

## Caveats

Currently only support Apache v2.0 license.
