# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code to the container
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Define the command to run your app with the dev server
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]