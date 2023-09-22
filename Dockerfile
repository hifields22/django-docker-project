# Use Python 3.9.9 as the base image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install the required Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt gunicorn

# Expose port 8000 for the app
EXPOSE 8080

# Command to run the application using gunicorn
CMD ["/usr/local/bin/gunicorn", "myblog.wsgi:application", "--bind", "0.0.0.0:8080"]
