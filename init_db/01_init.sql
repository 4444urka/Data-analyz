CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    wind_speed FLOAT
);

