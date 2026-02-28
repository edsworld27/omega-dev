# OMEGA JARVIS DOCKER VAULT
# Bulletproof Isolation Layer

FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir streamlit pandas watchdog

# Copy the dashboard and system scripts
COPY omega-dashboard.py .
COPY omega-backup.py .
COPY omega-publish.py .
COPY jarvis/ ./jarvis/
COPY Projects/ ./Projects/

# Expose Streamlit port
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the dashboard
ENTRYPOINT ["streamlit", "run", "omega-dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
