"""
This DAG defines the ETL process for loading cities, weather, and population data into Redshift. 
It includes the extraction, transformation, and loading (ETL) steps as well as table initialization 
and updates for Slowly Changing Dimensions (SCD) in Redshift.
"""

import os  # Standard library import
import sys  # Standard library import
from datetime import datetime  # Standard library import
import logging  # Standard library import

from airflow import DAG  # Third-party import
from airflow.operators.python import PythonOperator  # Third-party import

# Insert your project directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
}