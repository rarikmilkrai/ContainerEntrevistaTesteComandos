#!/bin/bash

# Start the SSH server
/usr/sbin/sshd

# Start the Flask web application in the background
python3 /app/app.py &

# Get the container's IP address and print it
IP_ADDR=$(hostname -I | awk '{print $1}')
echo "############################################################"
echo "Para os desafios, use o seguinte endereço de IP: $IP_ADDR"
echo "Acesse a interface web em http://localhost:5000"
echo "############################################################"


# Keep the container running
tail -f /dev/null
