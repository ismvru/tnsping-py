#!/usr/bin/env python2
# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.

from __future__ import print_function
import socket
import argparse
import sys
from time import time


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def tnsping(db_addr, db_port=1521, db_timeout=1):
    """
    tnsping

    db_addr - Database hostname or IP
    db_port - Database port
    db_timeout - Database connection timeout

    Returns database ping time, float, seconds
    Or -1 if can't connect to database
    """
    packet = (
        b"\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff"
        b"\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d"
        b"\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))"
    )
    # Try to send PING
    ts = time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(db_timeout)
        sock.connect((db_addr, db_port))
        sock.send(packet)
        while True:
            data = sock.recv(4096)
            if not data:
                break
            recv = data[12:].decode()
        sock.close()
    # Return false on any errors
    except Exception as e:
        eprint(e.__class__, e)
        return -1
    # Return false if string from DB is not correct
    if recv != "(DESCRIPTION=(TMP=)(VSNNUM=0)(ERR=0)(ALIAS=LISTENER))":
        return -1
    te = time()
    return te - ts


def main():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str, help="Database hostname or IP")
    parser.add_argument(
        "--port", "-p", nargs="?", default=1521, type=int, help="Database port"
    )
    parser.add_argument(
        "--timeout",
        "-t",
        nargs="?",
        default=1.0,
        type=float,
        help="Database connection timeout",
    )
    args = parser.parse_args()

    print(tnsping(args.host, args.port, args.timeout))


if __name__ == "__main__":
    main()
