from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, EmployeeSerializer
from .models import Employee, GENDER_CHOICES
import openpyxl
from .utils import bulk_emp_creation
from django.shortcuts import get_object_or_404

class FileUploadView(APIView):

	def post(self, request):

		serializer_class = FileSerializer(data=request.data)
		if 'file' not in request.FILES or not serializer_class.is_valid():
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			excel_file = request.FILES['file']
			wb = openpyxl.load_workbook(excel_file)
			worksheet = wb["Sheet1"]
			emp_list = list()

			for index, row in enumerate(worksheet.iter_rows()):
				row_data = list()
				if index == 0:
					continue
				else:
					emp_list.append(Employee(name=row[0].value, email=row[1].value, number=int(row[2].value), gender=row[3].value,
								   company=row[4].value, emp_id=row[5].value, manager=row[6].value))
			bulk_emp_creation(emp_list)
			return Response(status=status.HTTP_201_CREATED)

	def get(self, request):
		#import pdb;pdb.set_trace()
		if request.query_params.get("id"):
			emp = Employee.objects.get(id=int(request.query_params.get("id")))
			serializer = EmployeeSerializer(emp)
			return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
		emp = Employee.objects.all()
		serializer = EmployeeSerializer(emp, many=True)
		return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

	def put(self, request):
		#import pdb;pdb.set_trace()')))
		emp = Employee.objects.get(id=int(request.query_params.get("id")))
		serializer = EmployeeSerializer(emp, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({"status": "success", "data": serializer.data})
		else:
			return Response({"status": "error", "data": serializer.errors})

	def delete(self, request):
		emp = get_object_or_404(Employee, id=int(request.query_params.get("id")))
		emp.delete()
		return Response({"status": "success", "data": "Item Deleted"})

