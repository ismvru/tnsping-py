# Tnsping on pure python

- [Tnsping on pure python](#tnsping-on-pure-python)
  - [Usage](#usage)
    - [Python3 version](#python3-version)
    - [Python2 version](#python2-version)
    - [Docker version](#docker-version)
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

### Python3 version

```text
usage: tnsping.py [-h] [--port [PORT]] [--timeout [TIMEOUT]] [--count [COUNT]] [--interval [INTERVAL]] host

positional arguments:
  host                  Database hostname or IP

options:
  -h, --help            show this help message and exit
  --port [PORT], -p [PORT]
                        Database port
  --timeout [TIMEOUT], -t [TIMEOUT]
                        Database connection timeout
  --count [COUNT], -c [COUNT]
                        Count of tnsping trys
  --interval [INTERVAL], -i [INTERVAL]
                        Interval between requests
```

### Python2 version

```text
usage: tnsping_py2.py [-h] [--port [PORT]] [--timeout [TIMEOUT]]
                      [--count [COUNT]] [--interval [INTERVAL]]
                      host

positional arguments:
  host                  Database hostname or IP

optional arguments:
  -h, --help            show this help message and exit
  --port [PORT], -p [PORT]
                        Database port
  --timeout [TIMEOUT], -t [TIMEOUT]
                        Database connection timeout
  --count [COUNT], -c [COUNT]
                        Count of tnsping trys
  --interval [INTERVAL], -i [INTERVAL]
                        Interval between requests
```

### Docker version

```bash
docker build . --tag registry/image:tag
```

```text
docker run -it --rm registry/image:tag -h
usage: tnsping.py [-h] [--port [PORT]] [--timeout [TIMEOUT]] [--count [COUNT]] [--interval [INTERVAL]] host

positional arguments:
  host                  Database hostname or IP

options:
  -h, --help            show this help message and exit
  --port [PORT], -p [PORT]
                        Database port
  --timeout [TIMEOUT], -t [TIMEOUT]
                        Database connection timeout
  --count [COUNT], -c [COUNT]
                        Count of tnsping trys
  --interval [INTERVAL], -i [INTERVAL]
                        Interval between requests
```

## Examples

One request to DB

```bash
./tnsping.py localhost
0.0007433891296386719
```

5 requests to DB with 0.1s interval

```bash
./tnsping.py localhost -i 0.1 -c 5
0.0006456375122070312
0.0007336139678955078
0.0007565021514892578
0.0007164478302001953
0.0007593631744384766
```

One request to DB, but nothing listens on port

```bash
./tnsping.py localhost -p 1522
<class 'ConnectionRefusedError'> [Errno 111] Connection refused
-1
```

One request to DB, but firewall drops all requests on port

```bash
./tnsping.py some_random_drop_host -p 1522
<class 'TimeoutError'> timed out
-1
```

## Tests

All tests written for Python 3 version.

A python 2 version has been written, but will not be further developed, since Python 2 [is already outdated](https://www.python.org/doc/sunset-python-2/) at the moment of development

### Using Oracle Database

Run Oracle Database XE (you may use `run_oracle_database.sh` script, but for script usage you need Oracle account with `container-registry.oracle.com` access)

After database come up run `pytest -v`

```bash
pytest -v
================================== test session starts ==================================
platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /code/own/tnsping-py
plugins: anyio-3.6.1, betamax-0.8.1, cov-2.12.1
collected 16 items                                                                      

test_tnsping.py::test_logic_localhost PASSED                                      [  6%]
test_tnsping.py::test_logic_localhost_invalid_port PASSED                         [ 12%]
test_tnsping.py::test_args_help PASSED                                            [ 18%]
test_tnsping.py::test_args_no_host PASSED                                         [ 25%]
test_tnsping.py::test_args_localhost PASSED                                       [ 31%]
test_tnsping.py::test_args_localhost_with_timeout PASSED                          [ 37%]
test_tnsping.py::test_args_localhost_with_char_timeout PASSED                     [ 43%]
test_tnsping.py::test_args_localhost_with_port PASSED                             [ 50%]
test_tnsping.py::test_args_localhost_with_port_refused PASSED                     [ 56%]
test_tnsping.py::test_args_localhost_with_char_port PASSED                        [ 62%]
test_tnsping.py::test_args_localhost_with_count PASSED                            [ 68%]
test_tnsping.py::test_args_localhost_with_count_0 PASSED                          [ 75%]
test_tnsping.py::test_args_localhost_with_count_char PASSED                       [ 81%]
test_tnsping.py::test_args_localhost_with_count_interval PASSED                   [ 87%]
test_tnsping.py::test_args_localhost_with_count_interval_01 PASSED                [ 93%]
test_tnsping.py::test_args_localhost_with_count_interval_char PASSED              [100%]

================================== 16 passed in 10.57s ==================================
```

### Using fake TNSPing responder

Run `fake_tnsping_responder.py`

After responder start run `pytest -v`

```bash
pytest -v
================================== test session starts ==================================
platform linux -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /code/own/tnsping-py
plugins: anyio-3.6.1, betamax-0.8.1, cov-2.12.1
collected 16 items                                                                      

test_tnsping.py::test_logic_localhost PASSED                                      [  6%]
test_tnsping.py::test_logic_localhost_invalid_port PASSED                         [ 12%]
test_tnsping.py::test_args_help PASSED                                            [ 18%]
test_tnsping.py::test_args_no_host PASSED                                         [ 25%]
test_tnsping.py::test_args_localhost PASSED                                       [ 31%]
test_tnsping.py::test_args_localhost_with_timeout PASSED                          [ 37%]
test_tnsping.py::test_args_localhost_with_char_timeout PASSED                     [ 43%]
test_tnsping.py::test_args_localhost_with_port PASSED                             [ 50%]
test_tnsping.py::test_args_localhost_with_port_refused PASSED                     [ 56%]
test_tnsping.py::test_args_localhost_with_char_port PASSED                        [ 62%]
test_tnsping.py::test_args_localhost_with_count PASSED                            [ 68%]
test_tnsping.py::test_args_localhost_with_count_0 PASSED                          [ 75%]
test_tnsping.py::test_args_localhost_with_count_char PASSED                       [ 81%]
test_tnsping.py::test_args_localhost_with_count_interval PASSED                   [ 87%]
test_tnsping.py::test_args_localhost_with_count_interval_01 PASSED                [ 93%]
test_tnsping.py::test_args_localhost_with_count_interval_char PASSED              [100%]

================================== 16 passed in 10.57s ==================================
```

In fake_tnsping_responder logs you may see:

```text
Connection from 127.0.0.1, data: b'\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))'
Connection from 127.0.0.1, data: b'\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))'
```
