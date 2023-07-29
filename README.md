 # Simple TCP Client for Banner Grabbing

This is a simple TCP client written in Python 3 that can be used to grab and store the banner from a specified TCP server.

## Prerequisites

Before running the TCP client, make sure you have Python 3 installed on your system.

## Usage

1. Open the terminal or command prompt.

2. Clone or download the `tcp_client.py` file to your local machine.

3. Modify the `TCP_Address` and `PORT` variables in the `tcp_client.py` file with the appropriate IP address and port number of the target server.

4. Open a terminal or command prompt and navigate to the directory where the `tcp_client.py` file is located.

5. Run the TCP client script by executing the following command:

   ```bash
   python3 tcp_client.py
   ```

6. The client will connect to the specified TCP server and retrieve the banner. The banner will be printed on the terminal.

7. The TCP connection will be closed, and the script will terminate.

## Important Note

- This script is intended for educational and legal purposes only. Make sure you have proper authorization before using it on any remote server.

- The script might need modification if the target service responds with a larger banner than the buffer size (currently set to 1024 bytes). In that case, adjust the buffer size accordingly.

## Troubleshooting

- If you encounter any issues, double-check the IP address and port number of the target server.

- Ensure that the target service (in this case, SSH server on port 22) is running and reachable from your network.

- If you're running this script in a restricted environment, make sure that outbound connections to the target server on the specified port are allowed.

- For more information on the `socket` library and its functions, refer to the official Python documentation: https://docs.python.org/3/library/socket.html
 
