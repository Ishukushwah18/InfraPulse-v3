# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Install Linux Packages
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# Copy Requirements
COPY app/requirements.txt .

# Install Python Packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY app/ .

# Expose Flask Port
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# Run Application
CMD ["python", "app.py"]