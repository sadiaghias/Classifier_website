# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
