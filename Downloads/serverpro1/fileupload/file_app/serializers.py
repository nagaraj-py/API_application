from rest_framework import serializers
from .models import Employee, GENDER_CHOICES


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=20)
    number = serializers.IntegerField()
    gender = serializers.CharField(max_length=10)
    company = serializers.CharField(max_length=50)
    emp_id = serializers.IntegerField()
    manager = serializers.CharField(max_length=50)
    class Meta:
        model = Employee
        fields = '__all__'

    def update(self, inst, valid_data):
        inst.name = valid_data["name"]
        inst.email = valid_data["email"]
        inst.number = valid_data["number"]
        inst.gender = valid_data["gender"]
        inst.company = valid_data["company"]
        inst.emp_id = valid_data["emp_id"]
        inst.manager = valid_data["manager"]


        inst.save()

        return inst
