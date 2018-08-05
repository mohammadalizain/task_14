# Your imports should be here
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import LV
from rest_framework import routers, serializers, viewsets
# Complete me! I should be your APIListView

	class LV(serializers.HyperlinkedModelSerializer):
        model = LV
        fields = ('name', 'opening_time', 'closing_time')