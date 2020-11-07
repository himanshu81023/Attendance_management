from django.db import models

class cls(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    # def __init__(self):
    #     return self.name

class student(models.Model):
    fullname = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=7)
    present = models.IntegerField()
    total_class = models.IntegerField()
    clas = models.ForeignKey(cls,on_delete=models.CASCADE)

    # def __init__(self):
    #     return self.fullname

