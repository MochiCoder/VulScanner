import socket
import threading
import concurrent.futures
from datetime import datetime
import sys
import queue

class VulnerabilityScanner:
    def __init__(self, target, port_range=(1, 1024)):
        self.target = target
        self.port_range = port_range
        self.open_ports = queue.Queue()

    def port_scan(self, port):
        """Attempt to connect to a specific port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout

            result = sock.connect_ex((self.target, port))
            if result == 0:  # Port is open
                self.open_ports.put(port)
                banner = self.grab_banner(sock)
                if banner:
                    print(f"Port {port}: Open - Service: {banner}")
                else:
                    print(f"Port {port}: Open")
            sock.close()

        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def grab_banner(self, sock):
        """Attempt to grab service banner"""
        try:
            sock.send(b"GET / HTTP/1.1\r\n\r\n")
            return sock.recv(1024).decode().strip()
        except:
            return None

    def scan(self):
        print(f"\nStarting scan on {self.target}")
        print(f"Time started: {datetime.now()}\n")

        # Using ThreadPoolExecutor for concurrent scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.port_scan, range(self.port_range[0], self.port_range[1]))

        print(f"\nScan completed at {datetime.now()}")
        return list(self.open_ports.queue)

# Test example, test run
if __name__ == "__main__":
    target = input("Enter target IP address: ")
    scanner = VulnerabilityScanner(target)
    open_ports = scanner.scan()
