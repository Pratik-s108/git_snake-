# Use the official Python image
FROM python:3.9

# Create a working directory for the application
WORKDIR /app

# Copy requirements.txt (if you have one)
COPY requirements.txt ./

# Install dependencies if a requirements.txt file exists
RUN pip install -r requirements.txt

# Copy the Python script and any other application files
COPY . .

# Expose the port the application will run on (optional)
EXPOSE 8000

# Run the Python script
CMD ["python", "main.py"]
