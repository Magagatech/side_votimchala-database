from django.db import models

# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    regNumber = models.CharField(
        max_length=15, blank=True, default='BScICT/00/000')
    pwd = models.CharField(max_length=14, default='stu')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, blank=True, default='m')
    cumulativeGPA = models.FloatField(blank=True, default=4.00)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.firstname


class Election(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        self.end_date


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.student + "as " + self.position


class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    voter = models.ForeignKey(Student, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter
