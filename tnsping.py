#!/usr/bin/env python3
# Copyright (C) 2022 Mikhail Isaev <admin@ismv.ru>


import socket
import argparse
import sys
from time import time, sleep


def tnsping(db_addr: str, db_port: int = 1521, db_timeout: float = 1) -> float:
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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(db_timeout)
            sock.connect((db_addr, db_port))
            sock.send(packet)
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                recv = data[12:].decode()
    # Return false on any errors
    except Exception as e:
        print(e.__class__, e, file=sys.stderr)
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
    parser.add_argument(
        "--count",
        "-c",
        nargs="?",
        default=1,
        type=int,
        help="Count of tnsping trys",
    )
    parser.add_argument(
        "--interval",
        "-i",
        nargs="?",
        default=1,
        type=float,
        help="Interval between requests",
    )
    args = parser.parse_args()

    for _ in range(args.count):
        print(tnsping(args.host, args.port, args.timeout))
        if args.count > 1:
            sleep(args.interval)


if __name__ == "__main__":
    main()
