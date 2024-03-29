# Use the official Python base image with version 3.9.13  
FROM python:3.9.13  
  
# Set the working directory in the container  
WORKDIR /app  
  
# Copy the requirements.txt file to the container  
COPY requirements.txt .  
  
# Install the Python dependencies  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the application code to the container  
COPY . .  
  
# Expose the port on which your Flask application will run (replace 5000 with your desired port number)  
EXPOSE 5000  
  
# Set the entrypoint command to run your Flask application  
CMD ["python", "app.py"]  
