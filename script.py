from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

import uuid
import datetime

# Connexion au cluster Cassandra
cluster = Cluster(['localhost'])  # Localhost car pas dans un container (env de dev)
session = cluster.connect()

keyspace_name = 'weather_keyspace'
session.execute("CREATE KEYSPACE IF NOT EXISTS "+keyspace_name+" WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")

session.execute(f"USE {keyspace_name}")

# Création de la table pour les données météo
table_name = 'weather_data'
session.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ("
                "station_id UUID,"
                "longitude DECIMAL,"
                "latitude DECIMAL,"
                "timestamp TIMESTAMP,"
                "temperature DOUBLE,"
                "humidity DOUBLE,"
                "PRIMARY KEY (station_id, timestamp))")


station_id = uuid.uuid4()
longitude = 12.34
latitude = 56.78
timestamp = datetime.datetime.now()
temperature = 25.6
humidity = 60.2

insert_query = session.prepare(f"INSERT INTO {table_name} "
                               "(station_id, longitude, latitude, timestamp, temperature, humidity) "
                               "VALUES (?, ?, ?, ?, ?, ?)")

session.execute(insert_query, (station_id, longitude, latitude, timestamp, temperature, humidity))

select_station_query = session.prepare(f"SELECT * FROM {table_name} WHERE station_id = ?")
result_set = session.execute(select_station_query, [station_id])

for row in result_set:
    print(f"Station ID: {row.station_id}, Timestamp: {row.timestamp}, "
          f"Temperature: {row.temperature}, Humidity: {row.humidity}")



session.shutdown()
cluster.shutdown()
