from django.contrib import admin
from classroom.models import User, Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer, c_notice, g_notice, NewStudent

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
admin.site.register(c_notice)
admin.site.register(g_notice)
admin.site.register(NewStudent)

