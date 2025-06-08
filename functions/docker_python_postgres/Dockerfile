# -----------------------------------------------------------------------------
# Use an official lightweight Python runtime as a base image
# -----------------------------------------------------------------------------
    FROM python:3.9-slim

    # -----------------------------------------------------------------------------
    # Set the working directory in the container to /app
    # -----------------------------------------------------------------------------
    WORKDIR /app
    
    # -----------------------------------------------------------------------------
    # Copy the requirements.txt file into the container at /app
    # -----------------------------------------------------------------------------
    COPY requirements.txt .
    
    # -----------------------------------------------------------------------------
    # Install the required Python packages from requirements.txt
    # -----------------------------------------------------------------------------
    RUN pip install --no-cache-dir -r requirements.txt
    
    # -----------------------------------------------------------------------------
    # Copy the rest of the application code into the container
    # -----------------------------------------------------------------------------
    COPY main.py .
    COPY data/data.csv data/
    
    # -----------------------------------------------------------------------------
    # Define the container entry point.
    # This allows command-line arguments to be passed when running the container.
    # -----------------------------------------------------------------------------
    ENTRYPOINT ["python", "main.py"]
