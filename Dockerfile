# Use the official Python base image  
FROM python:3.9  
  
# Set the working directory inside the container  
WORKDIR /app  
  
# Copy the requirements file to the container  
COPY requirements.txt .  
  
# Disable SSL certificate verification (optional)  
ENV PYTHONHTTPSVERIFY=0  
  
# Install the Python dependencies  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the application code to the container  
COPY . .  
  
# Set the default command to run when the container starts  
CMD [ "python", "app.py" ]  
