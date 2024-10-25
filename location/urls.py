from django.urls import path
from .views import LocationView,ShowloacationUpdate


urlpatterns = [
    path('',LocationView.as_view({'post':"create"})),
    path('showlocation/',ShowloacationUpdate.as_view({'get':'list'}))
]
