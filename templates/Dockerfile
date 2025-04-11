# Use a full Python image (not slim) to avoid numpy/pandas build errors
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (for Docker caching)
COPY templates/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY templates/ .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
