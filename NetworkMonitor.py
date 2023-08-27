import tkinter as tk
import socket
import threading

#*Description: This program is a simple network monitor that listens on port 8080 and logs all data received
#*It is intended to be used as a starting point for more complex network monitoring applications
#*And is written in Python 3.7 and uses the Tkinter GUI toolkit.
#*To run it, you must have Python 3.7 installed. You can download it from https://www.python.org/downloads/
#*by opening a command prompt and type "python NetworkMonitor.py".

#-----Copyright (C) 2023  Guilherme De Oliveira Rocha
#-----This program is free software: you can redistribute it and/or modify
#-----it under the terms of the GNU Affero General Public License as published by
#-----the Free Software Foundation, either version 3 of the License, or
#-----(at your option) any later version.
#-----This program is distributed in the hope that it will be useful,
#-----but WITHOUT ANY WARRANTY; without even the implied warranty of
#-----MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#-----GNU Affero General Public License for more details.
#-----You should have received a copy of the GNU Affero General Public License
#-----along with this program.  If not, see <https://www.gnu.org/licenses/>.

class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor")

        self.port_label = tk.Label(self.root, text="Enter Port:")
        self.port_label.pack()

        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()

        self.log_text = tk.Text(self.root)
        self.log_text.pack()

        self.start_button = tk.Button(self.root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Monitoring", command=self.stop_monitoring)
        self.stop_button.pack()

        self.is_monitoring = False
        self.server_socket = None

    def start_monitoring(self):
        port = int(self.port_entry.get())
        self.is_monitoring = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("0.0.0.0", port))
        self.server_socket.listen(5)

        self.log("Monitoring started. Listening on port {0}.".format(port))

        threading.Thread(target=self.monitor).start()

    def stop_monitoring(self):
        self.is_monitoring = False
        if self.server_socket:
            self.server_socket.close()
            self.log("Monitoring stopped.")

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def monitor(self):
        while self.is_monitoring:
            client_socket, client_address = self.server_socket.accept()
            self.log(f"Connection from {client_address[0]}:{client_address[1]}")

            data = client_socket.recv(1024)
            self.log(f"Received: {data.decode('utf-8')}")

            client_socket.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()
