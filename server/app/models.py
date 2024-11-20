from django.db import models
from django.utils.timezone import now


class Roles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ]
    regNumber = models.CharField(
        max_length=15, blank=True, default='BScICT/00/000')
    pwd = models.CharField(max_length=14, default='stu')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default='m')
    cumulativeGPA = models.FloatField(blank=True, default=4.00)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Election(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def is_active(self):
        return self.start_date <= now() <= self.end_date

    def __str__(self):
        return f"Election ({self.start_date} - {self.end_date})"


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    election = models.ForeignKey(
        Election, on_delete=models.CASCADE, related_name='candidates')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='candidatures')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='candidates')

    class Meta:
        unique_together = ('election', 'student', 'position')

    def __str__(self):
        return f"{self.student.firstname} as {self.position.name}"


class Vote(models.Model):
    election = models.ForeignKey(
        Election, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='votes')
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        unique_together = ('election', 'voter', 'candidate')

    def __str__(self):
        return f"Vote by {self.voter.firstname} for {self.candidate.student.firstname} as {self.candidate.position.name}"
