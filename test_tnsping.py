# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.

from tnsping import tnsping, main
import sys


def test_logic_localhost():
    res = tnsping("localhost")
    assert res != -1


def test_logic_localhost_invalid_port():
    res = tnsping("localhost", db_port=1522)
    assert res == -1


def test_args_help(capsys):
    sys.argv = ["", "-h"]
    try:
        main()
    except SystemExit:
        pass
    stdout, stderr = capsys.readouterr()
    assert stdout.find("[-h] [--port [PORT]] [--timeout [TIMEOUT]] host") != -1
    assert stderr == ""


def test_args_no_host(capsys):
    sys.argv = [""]
    try:
        main()
    except SystemExit:
        pass
    stdout, stderr = capsys.readouterr()
    assert stderr.find("the following arguments are required: host") != -1
    assert stdout == ""


def test_args_localhost(capsys):
    sys.argv = ["", "localhost"]
    main()
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout.find("0.") == 0


def test_args_localhost_with_timeout(capsys):
    sys.argv = ["", "localhost", "--timeout", "5"]
    main()
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout.find("0.") == 0


def test_args_localhost_with_char_timeout(capsys):
    sys.argv = ["", "localhost", "--timeout", "abc"]
    try:
        main()
    except SystemExit:
        pass
    stdout, stderr = capsys.readouterr()
    assert stderr.find("argument --timeout/-t: invalid float value: 'abc'") != -1
    assert stdout == ""


def test_args_localhost_with_port(capsys):
    sys.argv = ["", "localhost", "--port", "1521"]
    main()
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout.find("0.") == 0


def test_args_localhost_with_port_refused(capsys):
    sys.argv = ["", "localhost", "--port", "1522"]
    main()
    stdout, stderr = capsys.readouterr()
    assert stderr == "<class 'ConnectionRefusedError'> [Errno 111] Connection refused\n"
    assert stdout == "-1\n"


def test_args_localhost_with_char_port(capsys):
    sys.argv = ["", "localhost", "--port", "abc"]
    try:
        main()
    except SystemExit:
        pass
    stdout, stderr = capsys.readouterr()
    assert stderr.find("error: argument --port/-p: invalid int value: 'abc'") != -1
    assert stdout == ""
