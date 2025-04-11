# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /Users/shivopamtiwari/Documents/Git_repo/templates

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Run the command to start the app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]