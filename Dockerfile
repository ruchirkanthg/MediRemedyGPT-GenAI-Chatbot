# FROM python:3.13.2-slim

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]


FROM python:3.13.2-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for package builds
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    cmake \
    pkg-config \
    build-essential \
    python3-dev \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && apt-get clean

# Copy requirements.txt first to avoid unnecessary rebuilds
COPY setup.py .  
COPY requirements.txt . 
# Upgrade pip first (recommended)
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the default command
CMD ["python3", "app.py"]