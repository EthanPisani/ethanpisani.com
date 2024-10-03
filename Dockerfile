FROM python:3.9.18-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies

RUN apt-get update && apt-get install -y gcc

RUN pip install --upgrade pip

RUN pip install  --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory

COPY . .

# clean unneeded files
RUN rm -rf /root/.cache/pip
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/cache/apt/*


# Command to run on container start

CMD [ "python", "./main.py" ]

# set port 
EXPOSE 80