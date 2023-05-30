### Setup

Install cassandra driver for python

```bash
pip install cassandra-driver
```

### Run

```bash
python3 script.py
```


### Explanation

The script will create a keyspace called `weather_keyspace` with replication factor 1 (because we have only one instance) and a table called `weather_data` with the following schema:

```sql

CREATE TABLE weather_data (
  station_id UUID,
  longitude DECIMAL,
  latitude DECIMAL,
  timestamp TIMESTAMP,
  temperature DOUBLE,
  humidity DOUBLE,
  PRIMARY KEY (station_id, timestamp)
);
```

The script will generate 1 random station with fake data and insert it into the table with the following query:

```sql
INSERT INTO weather_data(station_id, longitude, latitude, timestamp, temperature, humidity) VALUES (?, ?, ?, ?, ?, ?)
```
? are replaced by the values of the station.


The script will then query the table to get the data back and print it.

```sql
SELECT * FROM weather_data WHERE station_id = ?
```

? is replaced by the station id of the station we just inserted.

