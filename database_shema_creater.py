import psycopg2
# Database connection configuration
DB_CONFIG = {
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': '123123',
    'host': 'localhost',
    'port': '5432'
}

# Function to connect to PostgreSQL and create schema
def create_schema():
    schema_query = """
    CREATE TABLE ecommerce_data (
        order_id VARCHAR(255) PRIMARY KEY,
        user_id VARCHAR(255),
        category VARCHAR(255),
        amount NUMERIC,
        payment_method VARCHAR(50),
        status VARCHAR(50),
        timestamp TIMESTAMP
    );
    """
    try:
        # Establish connection
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(schema_query)
        conn.commit()
        print("Schema successfully created.")
    except Exception as e:
        print("Error creating schema:", e)
    finally:
        cursor.close()
        conn.close()

create_schema()
