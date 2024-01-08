FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 9000

# Run gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "wsgi:app"]
