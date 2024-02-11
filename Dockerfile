# Use a minimal base image for efficiency
FROM python:3.12-slim-buster



WORKDIR /app
COPY app.yaml ./app.yaml
COPY example.py ./example.py
COPY context.py ./context.py
COPY requirements.txt ./


# Mount venv directory (adjust the path as needed)
VOLUME ["/.venv:/app/venv"]

# Expose the Flask API port (default: 5000)
EXPOSE 5000

# Set the entrypoint to run your Flask app
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
