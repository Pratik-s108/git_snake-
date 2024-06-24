# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pygame \
 && rm -rf /var/lib/apt/lists/*

# Install pygame
RUN pip install pygame

# Expose port 1020 (example port number) from the container
EXPOSE 1020

# Run the application
CMD ["python", "./snake_game.py"]
