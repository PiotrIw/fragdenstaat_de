# Use a base image with Python and Node.js
FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gnupg \
    build-essential python3-dev \
    software-properties-common \
    git \
    wget \
    apt-transport-https \
    cmake \
    pkg-config \
    gdal-bin libgdal-dev \
    libfreetype6 libfreetype6-dev \
    imagemagick libmagickwand-dev \
    libpq-dev postgresql-client \
    poppler-utils libpoppler-dev libpoppler-cpp-dev \
    qpdf \
    libpango1.0-0 libpango1.0-dev \
    libgeoip-dev \
    libmagic1 libmagic-dev

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pnpm && \
    pip install --upgrade pip && \
    pip install uv
# RUN apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# Set the global bin directory for pnpm
RUN mkdir -p /usr/local/share/.config/pnpm && \
    # echo "export PNPM_HOME=/usr/local/share/.config/pnpm" >> /etc/profile.d/pnpm.sh && \
    # echo "export PATH=\$PNPM_HOME/bin:\$PATH" >> /etc/profile.d/pnpm.sh
ENV PNPM_HOME=/usr/local/share/.config/pnpm
ENV PATH=$PNPM_HOME/bin:$PATH

# Set working directory
WORKDIR /app

RUN git config --global --add safe.directory /app

# Copy the local scripts and configuration
COPY . /app

# Install Python and frontend dependencies
RUN pip install -r requirements-dev.txt && \
    pnpm install

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Use the entrypoint script
# ENTRYPOINT ["/app/entrypoint.sh"]

# Command to start the development server
CMD ["bash"]

