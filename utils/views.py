import json
from channels.generic.websocket import AsyncWebsocketConsumer
from kafka import KafkaConsumer
from asgiref.sync import sync_to_async
import asyncio

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        # Initialize Kafka consumer directly without sync_to_async
        self.consumer = KafkaConsumer(
            'Location_data',
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
        # Start sending Kafka messages in the background
        self.kafka_task = asyncio.create_task(self.send_kafka_messages())

    async def send_kafka_messages(self):
        try:
            while True:
                # Poll for messages with sync_to_async
                message = await sync_to_async(self.consumer.poll)(timeout_ms=1000)
                
                for topic_partition, messages in message.items():
                    for msg in messages:
                        location_data = msg.value
                        # Send data asynchronously to the WebSocket
                        await self.send(text_data=json.dumps(location_data))
        except Exception as e:
            print(f"Error sending Kafka messages: {e}")
        finally:
            # Close the Kafka consumer on error or disconnection
            await sync_to_async(self.consumer.close)()

    async def disconnect(self, close_code):
        # Cancel the background task and close the Kafka consumer
        self.kafka_task.cancel()
        await sync_to_async(self.consumer.close)()
        await self.close()

    async def receive(self, text_data):
        # Handle incoming messages if needed
        await self.send(text_data=json.dumps({"message": "Message received"}))
