Holeysheet
---------
Python package to read holey sheets (spreadsheets with holes in them).

# Install

Start by installing [Poetry](<https://python-poetry.org/>)

1. `poetry install`
2. `poetry run python holeysheet/cli.py` (Need to have the config file and xls(m/x))

# Config file

The config file is expected to be in `config.yaml`. It should be in the following format:

```yaml
regions:
  - literals:
      - name: Type
        value: Budget 2022
      - name: Park
        cell: C10
    sheet: Parkmanagement
    header:
      row: 10
      column: C
    regions:
      - range:
          start: G12
          end: Q35
        literals:
          - name: Region
            cell: C12
      - range:
          start: G37
          end: Q60
        literals:
          - name: Region
            cell: C37
      - range:
          start: G64
          end: Q219
        literals:
          - name: Region
            cell: C63
```

Every region can be seen as a range in the excel file with a given header row and column. Subregions (regions within
regions) overwrite top level region information, or inherit it. The first subregion for instance will have more
literals, the data will be on a different range, but the header info and sheet info is taken over from the top-level
region.

**Note: currently expecting there to be a `test.xlsm` file**