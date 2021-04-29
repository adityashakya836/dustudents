from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class News(models.Model):
    id=models.AutoField(primary_key=True)
    news_title=models.CharField(max_length=250)
    news_description=models.TextField()
    news_image=models.ImageField(upload_to='newspics/images',default="")
    news_category=models.CharField(max_length=50)
    news_date=models.DateTimeField()
    news_by=models.CharField(max_length=50)
    def __str__(self):
        return self.news_title

class Contacts(models.Model):
    c_name=models.CharField(max_length=30)
    c_email=models.EmailField(max_length=50)
    c_phone=models.CharField(max_length=20)
    c_message=models.TextField(max_length=200)

    def __str__(self):
        return self.c_name


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=255)

    def __str__(self):
        return self.program_name


class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=CASCADE)
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    program = models.ForeignKey(Program, on_delete=CASCADE)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    subject_id = models.AutoField(primary_key=True)

    subject_name = models.CharField(max_length=255,default="")
    subjet_syllabus=models.FileField(upload_to='syllabus/',default="")

    subject_notes = models.FileField(upload_to='notes/',default="")

    subject_practicals_list=models.FileField(upload_to='practicals/',default="",blank=True)
    subject_practicals=models.FileField(upload_to='practicals/',default="",blank=True)

    subject_previous_year_paper=models.FileField(upload_to="pyq/",blank=True,default="")

    reference_books=models.FileField(upload_to="referencebooks/",default="",blank=True)
    sub_name=models.CharField(max_length=255,default="")
    subject_description=models.TextField(blank=True)
    sem = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', "Third"),
        ('Fourth', 'Fourth'),
        ('Fifth', 'Fifth'),
        ('Sixth', 'Sixth'),
    )
    sub_sem = models.CharField(max_length=255, choices=sem)

    def __str__(self):
        return self.subject_name

