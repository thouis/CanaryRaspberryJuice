import socket
import select
import sys
from struct import pack
from util import flatten_parameters_to_string, flatten

""" @author: Aron Nieminen, Mojang AB"""

class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""

    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def send(self, *data):
        """Sends data."""
        vals = [str(d) for d in flatten(data)]
        print vals
        numargs = len(vals)
        self.socket.sendall(pack("B", numargs))
        for v in vals:
            self.socket.sendall(pack("!i", len(v)))
            self.socket.sendall(v)
        self.drain()
        self.lastSent = ",".join(vals)

    def send_raw(self, *data):
        """Sends data."""
        vals = [d for d in flatten(data)]
        numargs = len(vals)
        self.socket.sendall(pack("B", numargs))
        for v in vals:
            self.socket.sendall(pack("!i", len(v)))
            self.socket.sendall(v)
        self.drain()
        self.lastSent = ",".join(repr(v) for v in vals)

        
    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()

    def __del__(self):
        self.socket.sendall(pack("B", 0))
        self.socket.close()
