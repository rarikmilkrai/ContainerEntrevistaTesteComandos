# Use a base image with Python pre-installed
FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-server \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Flask
RUN pip3 install Flask

# Create a non-root user for the challenges
RUN useradd -m -s /bin/bash challengeuser
# Set a password for the user (replace 'password' with a more secure one if needed)
RUN echo "challengeuser:password" | chpasswd
# Add user to sudo group
RUN usermod -aG sudo challengeuser

# Configure SSH
RUN mkdir /var/run/sshd
# Allow password authentication for SSH
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Copy the application and scripts
COPY app /app
COPY scripts /scripts

# Give execution permissions to the startup script
RUN chmod +x /scripts/start.sh

# Expose ports for SSH and the web app
EXPOSE 22 5000

# Command to run on container start
CMD ["/scripts/start.sh"]
