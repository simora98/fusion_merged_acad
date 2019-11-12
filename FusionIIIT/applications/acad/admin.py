from django.contrib import admin
from .models import BtechCurriculum,Course,BatchSemester,CurriculumCourse,CurriculumInstructor,MtechCurriculum,MtechSemester,student_acad
# Register your models here.

admin.site.register(BtechCurriculum)
admin.site.register(BatchSemester)
admin.site.register(Course)
admin.site.register(CurriculumCourse)
admin.site.register(CurriculumInstructor)
admin.site.register(MtechSemester)
admin.site.register(MtechCurriculum)
admin.site.register(student_acad)
