run kakfa using docker:

docker run -p 9092:9092 apache/kafka:3.8.0

run websocket server:
we use daphne to run websocket server
daphne -b 0.0.0.0 -p 8001 realtime.asgi:application

# Interactive Documentation

## Running Kafka Using Docker

To run Kafka using Docker, execute the following command:

```bash
docker run -p 9092:9092 apache/kafka:3.8.0
```

To run asgi server, execute the following command:

```bash
daphne -b 0.0.0.0 -p 8001 realtime.asgi:application
```

To run webserver, execute the following command:

```bash
python manage.py runserver
```
