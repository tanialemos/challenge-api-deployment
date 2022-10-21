# OS - Ubuntu
FROM ubuntu

# Update apt repo and install dependencies
RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

# Update pip repo and install python dependencies
#RUN pip install --upgrade pip

# Create a folder "app" at the root of the image
RUN mkdir /app

# Define /app as the working directory
WORKDIR /app

# Copy all the files in the current directory in /app
COPY . /app

# Install dependencies from "requirements.txt"
RUN pip install -r requirements.txt

# Run the app
# Set host to 0.0.0.0 to make it run on the container network
# Set port to the env variable PORT to make it easy to choose the port on the server
CMD uvicorn app:app --host 0.0.0.0 --port $PORT