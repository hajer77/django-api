from rest_framework import serializers
from courses.models import courses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=courses
        fields=('courseId','courseName','courseSummary','courseImage','courseDate')