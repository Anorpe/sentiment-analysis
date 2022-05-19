FROM python:3.8.5

# Maintainer info
LABEL maintainer="aorregop@unal.edu.co"

# Make working directories
RUN  mkdir -p  /sentiment-analysis
WORKDIR  /sentiment-analysis

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  . .

# Run the python application
CMD ["python", "main.py"]