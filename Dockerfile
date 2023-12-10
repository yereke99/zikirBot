# Use the official Python image as a base image
FROM python:3.8.0

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container image
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir aiogram==2.16 aioschedule pytz

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "run.py"]
