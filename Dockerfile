# Use a base image with Python pre-installed
FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages for all challenge levels
RUN apt-get update && apt-get install -y --no-install-recommends lsb-release openssh-server python3 python3-pip sudo curl wget rsync util-linux iproute2 ufw apache2 lvm2 nfs-kernel-server strace apparmor-utils bridge-utils gpg && rm -rf /var/lib/apt/lists/*

# Install Trivy for Senior challenge
RUN wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | tee /usr/share/keyrings/trivy.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/trivy.list
RUN apt-get update && apt-get install -y trivy

# Install Flask
RUN pip3 install Flask

# Create a non-root user for the challenges
RUN useradd -m -s /bin/bash challengeuser
# Set a password for the user
RUN echo "challengeuser:password" | chpasswd
# Add user to sudo group and allow sudo without password for convenience
RUN usermod -aG sudo challengeuser
RUN echo "challengeuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Configure SSH
RUN mkdir /var/run/sshd
# Allow password authentication for SSH
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
# Allow root login for some challenges that might need it
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# Include custom sshd configs
RUN mkdir -p /etc/ssh/sshd_config.d
RUN echo "Include /etc/ssh/sshd_config.d/*.conf" >> /etc/ssh/sshd_config

# Create a broken service for a Senior troubleshooting challenge
RUN echo -e '[Unit]\\nDescription=Broken Service\\n\\n[Service]\\nExecStart=/usr/local/bin/nonexistent-script.sh\\n\\n[Install]\\nWantedBy=multi-user.target' > /etc/systemd/system/servico-quebrado.service

# Copy the application and scripts
COPY app /app
COPY scripts /scripts

# Give execution permissions to the startup script
RUN chmod +x /scripts/start.sh

# Expose ports for SSH and the web app
EXPOSE 22 5000

# Command to run on container start
CMD ["/scripts/start.sh"]
