from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name
    

class Student(models.Model):
    fname = models.CharField(max_length=50,null=True,default='first name')
    lname = models.CharField(max_length=50,null=True,default='last name')
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.fname + ' ' + self.lname

    def is_graduated(self):
        return self.age > 18
    is_graduated.boolean = True
