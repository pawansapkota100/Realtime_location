from django.shortcuts import render
from .serializer import LocationSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from kafka import KafkaProducer,KafkaConsumer
import json
from django.views.generic import TemplateView
user=get_user_model()


class LocationView(ModelViewSet):
    serializer_class = LocationSerializer
  

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user']=user.objects.first().id
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            producer= KafkaProducer(bootstrap_servers="localhost:9092")
            data= json.dumps(serializer.data).encode('utf-8')
            producer.send("Location_data", data)
            producer.flush()

            # serializer.save()


            return Response({"status": "location updated"}, status=status.HTTP_200_OK)

        # If the data is invalid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowloacationUpdate(ModelViewSet):
    def list(self, request, *args, **kwargs):
        consumer = KafkaConsumer('Location_data',bootstrap_servers=['localhost:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        for message in consumer:
            location_data = message.value
            print(f"Received location: {location_data}")


    

class MapView(TemplateView):
    template_name = 'test.html' 