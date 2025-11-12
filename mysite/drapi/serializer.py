from rest_framework import serializers
from .models import Aiquest


# if follow step 2/3/4(normaly api view/Class Based View APIView/ListModelMixin in Rest er shahajje CURD kora) then need under line of code 

# modelSerializer use korle nicer ei 4 line code lagbe shudu
class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields= ['id','teachers_name','course_name','course_duration','sit']

 

# or



# nomal serializer diye korle nicer code gulolagbe. r modelserializer diye korle uporer just koyek line code lagbe shudu
# if follow step 1(normaly CURD kora) then need under line of code  

'''class AiquestSerializer(serializers.Serializer):
    teachers_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=25)
    course_duration = serializers.IntegerField()
    sit = serializers.IntegerField()

    def create(self, validated_data):
        return Aiquest.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.teachers_name = validated_data.get('teachers_name', instance.teachers_name)
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_duration = validated_data.get('course_duration', instance.course_duration)
        instance.sit = validated_data.get('sit', instance.sit)
        instance.save()
        return instance '''
