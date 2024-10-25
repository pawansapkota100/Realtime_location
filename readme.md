run kakfa using docker:

docker run -p 9092:9092 apache/kafka:3.8.0

run websocket server:
we use daphne to run websocket server
daphne -b 0.0.0.0 -p 8001 realtime.asgi:application
