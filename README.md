# VulScanner
personal vulnerability scanner

Day 1:
Worked on importing and in particular:
Socket: for network connections
concurrent.futures: for managing thread pools
datetime: timing
queue: For thread-safe port storage

created the Vulerability Scanner Class
works with a target ip and port range
Uses a thread-safe queue for storing the open ports 

Day 2:
Worked on creating a port_scan and grab_banner method
port_scan in particular creates a socket connection to test the ports and uses timeouts to prevent hanging
grab_banner method sends a GET request and then returns the decoded banner information
Currently working on the scan method.


Day 3:
Scan method is the main scannning function and uses Threadpool Executor for concurrency in scanning. 
Returns list of open ports after running.
Looking on things I can improve as the scanner is fully operational, going to make error cases and work on overall security hardening.

Day 4-5:
Looking at implementing something for error handling:
something that would look like this:
def validate_ip(self, ip):
  try:
  socket.inet_aton(ip)
  return true
except socket.error:
  return false
Also looking for something that will print the reports out and be able to time stamp it with datetime.
Performance optimization is also something to look into and working on timeout configurations as well.
