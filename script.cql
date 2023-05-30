CREATE KEYSPACE IF NOT EXISTS weather_keyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}


CREATE TABLE weather_data (
  station_id UUID,
  longitude DECIMAL,
  latitude DECIMAL,
  timestamp TIMESTAMP,
  temperature DOUBLE,
  humidity DOUBLE,
  PRIMARY KEY (station_id, timestamp)
);

INSERT INTO weather_data (station_id, longitude, latitude, timestamp, temperature, humidity)
VALUES (?, ?, ?, ?, ?, ?);


SELECT * FROM weather_data WHERE station_id = ?;


SELECT * FROM weather_data
WHERE station_id = ? AND timestamp >= ? AND timestamp <= ?;


//Les "?" dans les requêtes représentent les paramètres à fournir avec les valeurs correspondantes.