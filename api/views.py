from re import I
from django.utils import translation
from rest_framework import serializers
import rest_framework
from rest_framework.views import APIView
from .models import Course, Trainer
from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializers import CourseSerializer,TrainerSerializer
from django.http import Http404
from rest_framework import status

@api_view(['GET',])
def home(request):
     courses=Course.objects.all()
     serializer=CourseSerializer(courses,many=True)
     return Response(serializer.data)

@api_view(['GET',])
def courseDetail(request,c_id):
    course=Course.objects.get(id=c_id)
    serializer=CourseSerializer(course,many=False)
    return Response(serializer.data)

@api_view(['POST',])
def addCourse(request):
    serializer=CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT',])
def courseUpdate(request,pk):
    course=Course.objects.get(id=pk)
    serializer=CourseSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE',])
def deleteCourse(request,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    return Response('Deleted')


class TrainerDetails(APIView):
    def get_object(self,pk):
        try:
            return Trainer.objects.get(id=pk)

        except Trainer.DoesNotExist:
            raise Http404

    def get(self,request):
        trainer=self.get_object()

        serializer=TrainerSerializer(trainer)
        return Response(serializer.data)
    def post(self,request):
        serializer=TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

    def put (self,request,id):
        trainer=self.get_object(id)
        serializer=TrainerSerializer(instance=trainer,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data)
    def delete(self,id):
        trainer=self.get_object(id)
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)