# To retrieve open ports on a Windows machine using Python

# pip install psutil

import psutil

def get_open_ports():
    open_ports = set()

    # Browse all running processes
    for process in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            # Retrieve login information for each processs
            connections = process.info['connections']

            for conn in connections:
                # Check if the connection is a TCP connection and if it is in "LISTEN" state
                if conn.status == psutil.CONN_LISTEN and conn.type == psutil.SOCK_STREAM:
                    # Add the port to the list of open ports
                    open_ports.add(conn.laddr.port)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return open_ports

if __name__ == "__main__":
    open_ports = get_open_ports()

    if open_ports:
        print("Open ports on Linux machine:")
        for port in sorted(open_ports):
            print(port)
    else:
        print("No open ports found.")
