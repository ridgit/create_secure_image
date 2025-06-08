# ACME Labs Data Processing and Loading Pipeline

This project processes an input CSV file containing oil well data, cleans and validates it, and then loads the processed data into a PostgreSQL database. The solution is containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

- **Docker:** Ensure Docker is installed on your system.  
  [Get Docker](https://docs.docker.com/get-docker/)

- **Docker Compose:**  
  - Docker Compose is integrated with Docker Desktop on many systems.  
  - If you're using an older version, install Docker Compose separately.  
  - On some systems, you might need to use the command `docker compose` instead of `docker-compose`.

- **CSV Input File:**  
  - Place your input CSV file (e.g., `data.csv`) in a folder named `data` in the project root.

## Project Structure

- **main.py:**  
  Python script that:
  - Processes and cleans the CSV file.
  - Replaces missing or invalid values.
  - Sorts data by `API10`.
  - Loads the processed data into PostgreSQL and runs sample queries (if a DB URL is provided).

- **requirements.txt:**  
  Lists the Python dependencies needed for the project.

- **Dockerfile:**  
  Containerizes the Python application.

- **docker-compose.yml:**  
  Defines the services:
  - `db`: Runs a PostgreSQL instance.
  - `app`: Runs the Python script, passing environment variables and command-line arguments.

## How to Run

   ```bash
   docker compose up --build
