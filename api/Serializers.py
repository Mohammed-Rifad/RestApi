from django.db.models import fields
from rest_framework import serializers
from .models import Course, Trainer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields="__all__"