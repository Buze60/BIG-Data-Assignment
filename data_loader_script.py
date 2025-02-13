
import pandas as pd
import psycopg2
from data_loader import DB_CONFIG


file_path = "cleaned_reduce_data.csv"
# Load the cleaned CSV data
cleaned_csv = pd.read_csv(file_path)

# Ensure proper datetime conversion and clean up invalid rows
cleaned_csv['timestamp'] = pd.to_datetime(cleaned_csv['timestamp'], errors='coerce')
cleaned_csv = cleaned_csv.dropna(subset=['timestamp'])  # Drop rows where timestamp is NaT

# Function to connect to PostgreSQL and insert data
def load_data_to_db(cleaned_csv):
    try:
        # Establish connection
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Insert each row into the database
        insert_query = """
        INSERT INTO ecommerce_data (order_id, user_id, category, amount, payment_method, status, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in cleaned_csv.iterrows():
            cursor.execute(insert_query, (
                row['order_id'], row['user_id'], row['category'], row['amount'],
                row['payment_method'], row['status'], row['timestamp']
            ))

        # Commit the transaction
        conn.commit()
        print("Data successfully loaded into the database.")

    except Exception as e:
        print("Error loading data into the database:", e)

    finally:
        cursor.close()
        conn.close()

# Load the data to the database
load_data_to_db(cleaned_csv)
