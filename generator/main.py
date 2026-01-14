import time
import random
import os
import psycopg2
from datetime import datetime

# Configuration from environment variables
DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "analytics_db")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "postgres")

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            print("Connected to database successfully.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database not ready yet, retrying in 5 seconds... Error: {e}")
            time.sleep(5)

def generate_weather_data():
    return {
        "temperature": round(random.uniform(-30, 40), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "pressure": round(random.uniform(730, 780), 2),
        "wind_speed": round(random.uniform(0, 30), 2)
    }

def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    print("Starting data generation...")
    try:
        while True:
            data = generate_weather_data()
            timestamp = datetime.now()
            
            cursor.execute("""
                INSERT INTO weather_data (timestamp, temperature, humidity, pressure, wind_speed)
                VALUES (%s, %s, %s, %s, %s)
            """, (timestamp, data['temperature'], data['humidity'], data['pressure'], data['wind_speed']))
            
            conn.commit()
            print(f"Inserted data at {timestamp}: {data}")
            
            time.sleep(2) # Generate data every 2 seconds
    except KeyboardInterrupt:
        print("Stopping generator...")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
