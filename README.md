# Tnsping on pure python

- [Tnsping on pure python](#tnsping-on-pure-python)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Tests](#tests)
    - [Using Oracle Database](#using-oracle-database)
    - [Using fake TNSPing responder](#using-fake-tnsping-responder)

[![codecov](https://codecov.io/gh/ismvru/tsnping-py/branch/master/graph/badge.svg?token=5AQSDZ8S7Q)](https://codecov.io/gh/ismvru/tsnping-py)
[![Python tests](https://github.com/ismvru/tsnping-py/actions/workflows/ci.yml/badge.svg)](https://github.com/ismvru/tsnping-py/actions/workflows/ci.yml)

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

### Using Oracle Database

Run Oracle Database XE (you may use `run_oracle_database.sh` script, but for script usage you need Oracle account with `container-registry.oracle.com` access)

After database come up run `pytest -v`

```bash
pytest -v
================================== test session starts ==================================
platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /code/tnsping-py
plugins: betamax-0.8.1, cov-2.12.1
collected 10 items                                                                      

test_tnsping.py::test_logic_localhost PASSED                                      [ 10%]
test_tnsping.py::test_logic_localhost_invalid_port PASSED                         [ 20%]
test_tnsping.py::test_args_help PASSED                                            [ 30%]
test_tnsping.py::test_args_no_host PASSED                                         [ 40%]
test_tnsping.py::test_args_localhost PASSED                                       [ 50%]
test_tnsping.py::test_args_localhost_with_timeout PASSED                          [ 60%]
test_tnsping.py::test_args_localhost_with_char_timeout PASSED                     [ 70%]
test_tnsping.py::test_args_localhost_with_port PASSED                             [ 80%]
test_tnsping.py::test_args_localhost_with_port_refused PASSED                     [ 90%]
test_tnsping.py::test_args_localhost_with_char_port PASSED                        [100%]

================================== 10 passed in 0.02s ===================================
```

### Using fake TNSPing responder

Run `fake_tnsping_responder.py`

After responder start run `pytest -v`

```bash
pytest -v
================================== test session starts ==================================
platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /code/tnsping-py
plugins: betamax-0.8.1, cov-2.12.1
collected 10 items                                                                      

test_tnsping.py::test_logic_localhost PASSED                                      [ 10%]
test_tnsping.py::test_logic_localhost_invalid_port PASSED                         [ 20%]
test_tnsping.py::test_args_help PASSED                                            [ 30%]
test_tnsping.py::test_args_no_host PASSED                                         [ 40%]
test_tnsping.py::test_args_localhost PASSED                                       [ 50%]
test_tnsping.py::test_args_localhost_with_timeout PASSED                          [ 60%]
test_tnsping.py::test_args_localhost_with_char_timeout PASSED                     [ 70%]
test_tnsping.py::test_args_localhost_with_port PASSED                             [ 80%]
test_tnsping.py::test_args_localhost_with_port_refused PASSED                     [ 90%]
test_tnsping.py::test_args_localhost_with_char_port PASSED                        [100%]

================================== 10 passed in 0.02s ===================================
```

In fake_tnsping_responder logs you may see:

```text
Connection from 127.0.0.1, data: b'\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))'
Connection from 127.0.0.1, data: b'\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))'
```
