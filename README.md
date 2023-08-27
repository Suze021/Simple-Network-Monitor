# Network Monitor

Network Monitor is a Python program designed to monitor network traffic on a specified port. The program uses the Tkinter GUI toolkit for creating an interactive interface that allows users to start and stop the monitoring process. It listens for incoming connections on the chosen port and logs any received data. This project serves as a basic foundation for developing more advanced network monitoring applications.

## Table of Contents
- [Author](#author)
- [Features](#features)
- [Dependencies](#dependencies)
- [Usage](#usage)
  - [Installation](#installation)
  - [Running the Program](#running-the-program)
- [How It Works](#how-it-works)
- [License](#license)

## Author
- **Author:** Guilherme De Oliveira Rocha
- **Date:** 2023/08/26

## Features
- Graphical user interface (GUI) for easy interaction.
- Selection of a specific port for monitoring.
- Display of connection information and incoming data in the GUI.

## Dependencies
- Python 3.7 or later
- Tkinter library (for GUI)
- Threading library (for concurrent execution)
- Socket library (for network communication)

## Usage

### Installation
Ensure you have Python 3.7 or later installed. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

### Running the Program
1. Open a command prompt or terminal window.
2. Navigate to the directory containing the `NetworkMonitor.py` file.
3. Run the program by entering the following command:
4. The program's graphical user interface will appear.

### Using the GUI
1. The GUI will display an input field labeled "Enter Port."
2. Enter the desired port number you want to monitor in the input field.
3. Click the "Start Monitoring" button to initiate network monitoring on the specified port.
4. The program will start listening on the entered port and display a log message indicating that monitoring has begun.
5. Any incoming data on the specified port will be logged in the text area.
6. To stop monitoring, click the "Stop Monitoring" button. The program will close the listening socket and display a log message confirming that monitoring has stopped.

## How It Works
- The program initializes a GUI using the Tkinter library.
- Upon clicking the "Start Monitoring" button, the program creates a socket and binds it to the specified IP address and port.
- A separate thread is launched to handle the monitoring loop, ensuring the GUI remains responsive.
- Connection information is logged when a client connects to the listening socket.
- Data received from the client is logged in the GUI.
- Clicking the "Stop Monitoring" button closes the listening socket, ending the monitoring process.

## License
This project is open-source and distributed under the GNU GENERAL PUBLIC LICENSE. See the GNU License file for more information.
