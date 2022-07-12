from tnsping import tnsping


def test_correct():
    res = tnsping("localhost")
    assert res != -1


def test_cant_connect():
    res = tnsping("localhost", db_port=1522)
    assert res == -1
