from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from courses.models import courses
from courses.serializers import CourseSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def courseApi(request,id=0):
    if request.method=='GET':
        coursesapi = courses.objects.all()
        courses_serializer=CourseSerializer(coursesapi,many=True)
        return JsonResponse(courses_serializer.data,safe=False)
    elif request.method=='POST':
        course_data=JSONParser().parse(request)
        courses_serializer=CourseSerializer(data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False) 
    elif request.method=='PUT':
        course_data=JSONParser().parse(request)
        course=courses.objects.get(courseId=course_data['courseId']) 
        courses_serializer=CourseSerializer(course,data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save() 
            return JsonResponse("Update Successfully", safe=False) 
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        course=courses.objects.get(courseId=id)    
        course.delete()
        return JsonResponse("Deleted Successfully", safe=False) 

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

 