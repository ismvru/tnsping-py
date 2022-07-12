# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.

from tnsping import tnsping


def test_correct():
    res = tnsping("localhost")
    assert res != -1


def test_cant_connect():
    res = tnsping("localhost", db_port=1522)
    assert res == -1
