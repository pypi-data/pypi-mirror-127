<div align="center">
    <h1>exex</h1>
    <p>
        <b>CLI for extracting data from Excel documents</b>
    </p>

[![PyPI version](https://badge.fury.io/py/exex-cli.svg)](https://pypi.org/project/exex-cli/)
![test](https://github.com/vikpe/exex-cli/workflows/test/badge.svg?branch=master) [![codecov](https://codecov.io/gh/vikpe/exex-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/vikpe/exex-cli)

<br>

</div>


## Installation
```sh
pip install exex-cli
```

## Usage
### Synopsis
```bash
exex FILENAME --sheet SHEET --range RANGE --format FORMAT 
```

Parameter | Type | Default | Description
--- | --- | --- | ---
`FILENAME` | (required) string | | Path to .xlsx file. 
`[SHEET]` | (optional) string or int | `0` (first sheet) | Name or index of sheet
`[RANGE]` | (optional) range | `all` (all values) | Range to get values from
`[FORMAT]` | (optional) string | `text` | `text`, `table`, `json`, `csv`

**Type of ranges**

Type | Syntax | Example
--- | --- | ---
All values | `all` | `all`
Cell by name | `[COLUMN_NAME][ROW_NUMBER]` | `A1`
Cell by index | `[COLUMN_INDEX],[ROW_INDEX]` | `1,1`
Cell range | `[FROM]:[TO]` |  `A1:A3`
Column | `[COLUMN_NAME]` | `A`
Column range | `[FROM]:[TO]` | `A:C`
Row | `[ROW_NUMBER]` | `1`
Row range | `[FROM]:[TO]` | `1:3`

### Examples

**Get all values as JSON**
```bash
python -m exex_cli sample.xlsx --format json
```

**Get cell range as CSV**
```bash
python -m exex_cli sample.xlsx --range A1:A3 --format csv
```

## Development

**Setup**
```sh
poetry install
```

**Tests** (local Python version)
```sh
poetry run pytest
```

**Code formatting** (black)
```sh
poetry run black .
```
