import argparse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# =============================================================================
# Function: process_file
# Description: Reads the input CSV, validates and cleans the data based on rules,
#              sorts by api10, and writes the output to a CSV file.
# =============================================================================
def process_file(input_path, output_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_path)
    
    # -----------------------------------------------------------------------------
    # Eliminate Invalid Rows:
    # Drop rows where the api10 column is missing or null.
    # -----------------------------------------------------------------------------
    df = df.dropna(subset=['api10'])
    
    # -----------------------------------------------------------------------------
    # Define a dictionary for column types.

    # -----------------------------------------------------------------------------
    column_types = {
        'api10': 'string',
        'direction': 'string',
        'wellname': 'string',
        'welltype': 'string',
        'operator': 'string',
        'basin': 'categorical',
        'subbasin': 'categorical',
        'state': 'categorical',
        'county': 'categorical',
        'spuddate': 'date',
        'cum12moil': 'number',
        'cum12mgas': 'number',
        'cum12mwater': 'number'
    }
    
    # -----------------------------------------------------------------------------
    # Process each column based on its defined type.
    # For each type:
    #   - If conversion fails, invalid values are replaced with null (NaN).
    #   - Then missing values are filled as follows:
    #       * number/date: fill with the mean
    #       * categorical: fill with the mode (most common value)
    #       * string: leave blank
    # -----------------------------------------------------------------------------
    for col, col_type in column_types.items():
        if col not in df.columns:
            # Skip processing if the column is not present in the data.
            continue
        
        if col_type == 'number':
            # Convert to numeric; errors become NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # Compute the mean (ignoring NaN) and replace missing values
            mean_value = df[col].mean()
            df[col] = df[col].fillna(mean_value)
            
        elif col_type == 'date':
            # Convert to datetime; errors become NaT (not-a-time)
            df[col] = pd.to_datetime(df[col], errors='coerce')
            # For date columns, compute the mean by converting dates to numeric timestamps.
            non_null_dates = df[col].dropna().astype(np.int64)
            if not non_null_dates.empty:
                mean_timestamp = non_null_dates.mean()
                mean_date = pd.to_datetime(mean_timestamp)
                df[col] = df[col].fillna(mean_date)
            
        elif col_type == 'categorical':
            # Convert to a pandas 'category' type
            df[col] = df[col].astype('category')
            # Compute the mode (most frequent value) for the column
            mode_series = df[col].mode()
            if not mode_series.empty:
                mode_value = mode_series[0]
                df[col] = df[col].fillna(mode_value)
            
        elif col_type == 'string':
            # Ensure the column is treated as a string and replace missing values with blank
            df[col] = df[col].astype(str)
            df[col] = df[col].fillna('')
    
    # -----------------------------------------------------------------------------
    # Sort the DataFrame by the api10 column
    # -----------------------------------------------------------------------------
    df = df.sort_values(by='api10')
    
    # -----------------------------------------------------------------------------
    # Write the processed data to the output CSV file
    # -----------------------------------------------------------------------------
    df.to_csv(output_path, index=False)
    
    # Return the output file path for confirmation
    return output_path

# =============================================================================
# Function: load_data_to_db
# Description: Loads the processed CSV file into a PostgreSQL database table
#              and executes two SQL queries to display results.
# =============================================================================
def load_data_to_db(csv_path, db_url):
    # Create a SQLAlchemy engine using the provided database URL
    engine = create_engine(db_url)
    
    # Read the processed CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # -----------------------------------------------------------------------------
    # Load data into a database table named 'oil_wells'.
    # If the table exists, replace it.
    # -----------------------------------------------------------------------------
    df.to_sql('oil_wells', engine, if_exists='replace', index=False)
    
    # -----------------------------------------------------------------------------
    # Query 1: Retrieve the top 5 oil wells based on 'cum12moil' in descending order.
    # -----------------------------------------------------------------------------
    query1 = "SELECT * FROM oil_wells ORDER BY cum12moil DESC LIMIT 5"
    top_5 = pd.read_sql(query1, engine)
    print("Top 5 oil wells by cum12moil:")
    print(top_5)
    
    # -----------------------------------------------------------------------------
    # Query 2: Compute the sum of 'cum12moil', 'cum12mgas', and 'cum12mwater'
    #          for each basin.
    # -----------------------------------------------------------------------------
    query2 = """
    SELECT basin, 
           SUM(cum12moil) as total_cum12moil, 
           SUM(cum12mgas) as total_cum12mgas, 
           SUM(cum12mwater) as total_cum12mwater
    FROM oil_wells
    GROUP BY basin
    """
    sums_by_basin = pd.read_sql(query2, engine)
    print("\nSum of cum12moil, cum12mgas, and cum12mwater by basin:")
    print(sums_by_basin)

# =============================================================================
# Main function: Parses command-line arguments, processes the file, and
# optionally loads data into a database if a DB URL is provided.
# =============================================================================
def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Process and load oil well data.')
    parser.add_argument('--input', required=True, help='Path to input CSV file')
    parser.add_argument('--output', required=True, help='Path to output processed CSV file')
    parser.add_argument('--db_url', required=False, help='Database URL (e.g., postgres://user:pass@host:port/dbname)')
    args = parser.parse_args()
    
    # -----------------------------------------------------------------------------
    # Part 1: Process the input file and save the processed output.
    # -----------------------------------------------------------------------------
    processed_file = process_file(args.input, args.output)
    print(f"Processed file saved to: {processed_file}")
    
    # -----------------------------------------------------------------------------
    # Part 2: If a database URL is provided, load the processed data into the DB
    # and execute the queries.
    # -----------------------------------------------------------------------------
    if args.db_url:
        load_data_to_db(processed_file, args.db_url)

# Entry point of the application
if __name__ == "__main__":
    main()
