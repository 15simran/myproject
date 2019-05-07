from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import datetime


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

gap_choices=(
    (1,0),(2,1),(3,2),
    )
'''
class StudentBranch(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
'''



class c_notice(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notices')
    per_10th=models.FloatField()
    per_12th=models.FloatField()
    no_backlog=models.IntegerField(default="0")
    aggregate=models.FloatField()
    company_name=models.CharField(max_length=20)
    company_package=models.FloatField()
    add_notice=models.FileField(upload_to='classroom\\fileData')
    date = models.DateField(("Date"), default=datetime.date.today)
    year_gap=models.IntegerField(choices=gap_choices, default="0")
    branches = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name



class g_notice(models.Model):
    name=models.CharField(max_length=20)
    add_notice=models.FileField(upload_to='classroom\\fileData')
'''
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year
'''
gap_choices=(
    (1,0),(2,1),(3,2)
)


class NewStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    dob=models.DateField(default=datetime.date.today )
    gender=models.CharField(max_length=10)
    contactnum=models.CharField(max_length=10)

    tenper=models.FloatField()
    tweper=models.FloatField()
    tenyop=models.IntegerField()
    tweyop=models.IntegerField()
    egap=models.IntegerField(choices=gap_choices)
    
    gper=models.FloatField()
    back=models.IntegerField()
    is_placed=models.BooleanField(default=False)
    regid=models.IntegerField()
    rollno=models.CharField(max_length=10)
    branch=models.CharField(max_length=20)
    notice = models.ManyToManyField(c_notice,  related_name='eligible_students')

    def _str_(self):
        return self.fname
    
