from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import TableType, TableInfo, Student
from .serializers import TableTypeSerializer, TableInfoSerializer, TableInfoAnswerSerializer, StudentSerializer


class TableTypeListAPIView(APIView):
    def get(self, request):
        table_types = TableType.objects.all()
        serializer = TableTypeSerializer(table_types, many=True)
        return Response(serializer.data)


class TableTypeDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return TableType.objects.get(pk=pk)
        except TableType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        table_type = self.get_object(pk)
        serializer = TableTypeSerializer(table_type)
        return Response(serializer.data)


class TableInfoAnswerAPIView(APIView):
    def get(self, request, student_number):
        try:
            student = Student.objects.get(student_number=student_number)
        except Student.DoesNotExist:
            return Response({'error': 'No student found with this student number'}, status=status.HTTP_404_NOT_FOUND)

        table_infos = student.tables.all()
        serializer = TableInfoAnswerSerializer(table_infos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_data = request.data

        student_number = student_data.get('studentNumber', '')
        name = student_data.get('name', '')
        specialization = student_data.get('specialization', '')
        college = student_data.get('college', '')
        phone_number = student_data.get('phoneNumber', '')
        email = student_data.get('email', '')
        gender = student_data.get('gender', 'M')
        which_year = student_data.get('whichYear', 1)
        date_of_birth = student_data.get('dateOfBirth', None)
        address = student_data.get('address', '')

        # Check if the student with this student_number exists
        if Student.objects.filter(student_number=student_number).exists():
            return Response({'error': 'Student number already used'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new student if it doesn't exist
        student = Student.objects.create(
            student_number=student_number,
            name=name,
            specialization=specialization,
            college=college,
            phone_number=phone_number,
            email=email,
            gender=gender,
            which_year=which_year,
            date_of_birth=date_of_birth,
            address=address
        )

        # Extract the answers from the request
        answers = student_data.get('answers', [])

        for answer_data in answers:
            try:
                table_info = TableInfo.objects.get(pk=answer_data['question_id'])
            except TableInfo.DoesNotExist:
                return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)

            answer = answer_data.get('answer', '').lower()
            if answer == 'yes':
                table_info.is_true = True
            elif answer == 'no':
                table_info.is_true = False
            else:
                return Response({'error': 'Invalid answer'}, status=status.HTTP_400_BAD_REQUEST)

            table_info.save()
            student.tables.add(table_info)

        return Response({'status': 'success'}, status=status.HTTP_200_OK)


class StudentListAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
