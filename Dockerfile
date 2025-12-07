FROM python:3.10-slim-buster

# Create working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining project files
COPY . .

# Expose Flask port
EXPOSE 8080

# Run your Flask app
CMD ["python", "app.py"]
