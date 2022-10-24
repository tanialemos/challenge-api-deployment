# OS - Ubuntu
FROM ubuntu

# Update apt repo and install dependencies
RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

# Update pip repo and install python dependencies
#RUN pip install --upgrade pip

# Create a folder "app" at the root of the image
RUN mkdir /app

# Copy all the files in the current directory in /app
COPY . /app

# Define /app/project as the working directory
WORKDIR /app/project

# Install dependencies from "requirements.txt"
RUN pip install -r /app/requirements.txt

# Run the app
# Set host to 0.0.0.0 to make it run on the container network ONLY USE 0.0.0.0 for container purposes
# Set port to the env variable PORT to make it easy to choose the port on the server
# Using port 8000 to test because $PORT was causing an error
CMD uvicorn app:app --host 0.0.0.0 --port 8000

# to build an image from inside the directory $ docker build . -t my_api_name
# -t for tag, give a name to the image
# to run from terminal inside the directory $ docker run -it -p 8000:8000 my_api
# the first port represetns the port on my machine and the second the port on the container
