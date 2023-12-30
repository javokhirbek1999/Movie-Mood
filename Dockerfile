# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/


# RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# # Define the command to run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
