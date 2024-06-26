```markdown
# Flask Web Server

This project is a simple Flask web server that listens on port 8000. It includes a REST API endpoint that responds with a specified age.

## Setup and Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/IdoShoshani/flask-webserver.git
   cd flask-webserver
   ```

2. **Install dependencies:**
   ```sh
   pip install Flask
   ```

3. **Run the Flask application:**
   ```sh
   python main.py
   ```

## REST API

### GET /age
Returns the specified age in the query parameter.

**Request:**
```sh
GET /age?age=18
```

**Response:**
```
Your age is: 18
```

## Concepts Explained

### External IP

An external IP address, also known as a public IP address, is the address assigned to your network by your Internet Service Provider (ISP). This address is used to communicate with devices and servers outside your local network. It is accessible from anywhere on the internet.

### Internal IP

An internal IP address, also known as a private IP address, is assigned to devices within a local network by a router. This address is used for communication between devices within the same local network. Internal IP addresses are not accessible from the internet.

### Ports

Ports are numerical identifiers in the range 0-65535 used to route network traffic to specific services running on a device. For example, web servers typically use port 80 for HTTP traffic and port 443 for HTTPS traffic. In this project, the Flask web server listens on port 8000.

### Example

- **External IP:** `203.0.113.1` (can be accessed from anywhere on the internet)
- **Internal IP:** `192.168.1.2` (can only be accessed within the local network)
- **Port 8000:** The Flask server listens on this port for incoming HTTP requests.
