#!/usr/bin/env python3
import socketserver


class TNSPingHandler(socketserver.BaseRequestHandler):
    def handle(self):
        packet = (
            b"\x00W\x00\x00\x01\x00\x00\x00\x018\x01,\x00\x00\x08\x00\x7f\xff"
            b"\x7f\x08\x00\x00\x01\x00\x00\x1d\x00:\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x190\x00\x00\x00\x8d"
            b"\x00\x00\x00\x00\x00\x00\x00\x00(CONNECT_DATA=(COMMAND=ping))"
        )
        self.data = self.request.recv(4096).strip()
        print(f"Connection from {self.client_address[0]}, data: {self.data}")
        if self.data == packet:
            self.request.sendall(
                b'\x00A\x00\x00\x04\x00\x00\x00"\x00\x005'
                b"(DESCRIPTION=(TMP=)(VSNNUM=0)(ERR=0)(ALIAS=LISTENER))"
            )


if __name__ == "__main__":
    host = "localhost"
    port = 1521
    with socketserver.TCPServer((host, port), TNSPingHandler) as server:
        server.serve_forever()
