# Use an official Python runtime as a base image
FROM python:3.5-slim

#Set labels
LABEL "Author"="Arvin.Cudanin" "Email"="arvin.cudanin@gmail.com"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --proxy=10.158.17.67:8080 -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Cuds

# Run app.py when the container launches
CMD ["python", "app.py"]