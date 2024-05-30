from rest_framework import serializers
from .models import TableType, TableInfo, Student

class TableInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInfo
        fields = ['id', 'table_type', 'question', 'is_true']

class TableTypeSerializer(serializers.ModelSerializer):
    tables = TableInfoSerializer(many=True, read_only=True)

    class Meta:
        model = TableType
        fields = ['id', 'name', 'tables']

class TableInfoAnswerSerializer(serializers.ModelSerializer):
    table_name = serializers.CharField(source='table_type.name')

    class Meta:
        model = TableInfo
        fields = ['id', 'question', 'is_true', 'table_name']

class StudentSerializer(serializers.ModelSerializer):
    tables = TableInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_number', 'name', 'tables']
