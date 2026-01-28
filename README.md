# Python Port Scanner
A multithreaded network reconnaissance tool built in Python.
# Features
Scans a specified target IP for open TCP ports.
Utilizes multi threading for rapid scanning.
Handles timeouts and connection errors gracefully.

# How It Works? The tool uses the socket library to attempt TCP connections (SYN packets). If a connection is accepted (SYN-ACK), the port is logged as open.