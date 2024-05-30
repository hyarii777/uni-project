from django.contrib import admin
from .models import TableType, TableInfo, Student

class TableTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class TableInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_type', 'question', 'is_true')
    list_filter = ('table_type', 'is_true')
    search_fields = ('question',)

class TableInfoInline(admin.TabularInline):
    model = Student.tables.through
    extra = 1
    verbose_name = "Table Info"
    verbose_name_plural = "Tables Info"
    can_delete = False
    readonly_fields = ('tableinfo_question', 'tableinfo_is_true')

    def tableinfo_question(self, instance):
        return instance.tableinfo.question
    tableinfo_question.short_description = "Question"

    def tableinfo_is_true(self, instance):
        return instance.tableinfo.is_true
    tableinfo_is_true.short_description = "Is True"

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_number', 'name', 'email', 'gender', 'college')
    search_fields = ('student_number', 'name', 'email', 'college')
    inlines = [TableInfoInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tables')

admin.site.register(TableType, TableTypeAdmin)
admin.site.register(TableInfo, TableInfoAdmin)
admin.site.register(Student, StudentAdmin)
