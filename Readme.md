## Cloud-Based Data Processing System

 

This project implements a cloud-based data processing system with capabilities for data ingestion, transformation, and retrieval.

 

## Installation

 

1. Clone the repository:

   ```bash

   git clone https://github.com/mukeshsihag/data-processing.git

   cd data-processing

   ```

 

2. Set up a virtual environment:

   ```bash

   python3 -m venv venv

   source venv/bin/activate

   ```

 

3. Install the dependencies:

   ```bash

   pip install -r requirements.txt

   ```

 

## Starting the Application

 

Run the FastAPI application:

```bash

uvicorn main:app --reload

```

The application will be running on `http://127.0.0.1:8000`.

 

## API Endpoints

 

### 1. Data Ingestion

**POST** `/ingestion/upload` 

Upload CSV or JSON file or send raw JSON data.

 

### 2. Data Transformation

**POST** `/transformation/process` 

Process the raw data and perform transformations.

 

### 3. Data Retrieval

**GET** `/retrieval/data` 

Fetch all processed data or filter by criteria such as date or user ID.

 

## Accessing the API Documentation

 

You can access the API documentation at: 

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

 

## Validation Logic

 

Basic validation is performed during data ingestion:

- File type validation (CSV or JSON).

- Data type validation (e.g., numeric values for costs and profit).

 