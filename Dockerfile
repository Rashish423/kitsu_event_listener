# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add the app directory to the Python path
ENV PYTHONPATH=/app

# Command to run the event listener
CMD ["python", "src/listener.py"]
