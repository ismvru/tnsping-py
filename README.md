# Tnsping on pure python

- [Tnsping on pure python](#tnsping-on-pure-python)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Tests](#tests)

Oracle TNSPING application, written on pure python

tnsping.py prints:

- stdout
  - time in seconds of ping
  - -1 if can't connect to database
- stderr
  - none
  - Exception class and exception caption if can't connect to database

## Usage

```text
usage: tnsping.py [-h] [--port [PORT]] host

positional arguments:
  host

options:
  -h, --help            show this help message and exit
  --port [PORT], -p [PORT]
```

## Examples

```bash
./tnsping.py localhost
0.001087312
```

```bash
./tnsping.py localhost -p 1522
<class 'ConnectionRefusedError'> [Errno 111] Connection refused
-1
```

```bash
./tnsping.py some_random_drop_host -p 1522
<class 'TimeoutError'> timed out
-1
```

## Tests

- Run Oracle Database XE (you may use `run_oracle_database.sh` script, but for script usage you need Oracle account with `container-registry.oracle.com` access)
- Run `pytest`
