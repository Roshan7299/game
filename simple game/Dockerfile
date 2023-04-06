# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the game files into the container
COPY game.py .

# Install any necessary dependencies
RUN pip install random

# Set the default command to run the game.py file
CMD ["python", "game.py"]
