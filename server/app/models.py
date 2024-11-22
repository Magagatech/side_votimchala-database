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
    FACULTY_CHOICES = [
        ('ict', 'ICT'),
        ('bba', 'BBA'),
        ('dnc', 'DNC'),
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
    profile_pic = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    faculty = models.CharField(
        max_length=20, choices=FACULTY_CHOICES, default='ict')
    email = models.EmailField(max_length=255, blank='true')
    phone = models.CharField(max_length=14, default='+265000000000')

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
    APPLICATION_STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    election = models.ForeignKey(
        Election, on_delete=models.CASCADE, related_name='candidates')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='candidatures')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='candidates')
    # Added back the manifesto field
    manifesto = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=APPLICATION_STATUS, default='pending'
    )

    class Meta:
        unique_together = ('election', 'student', 'position')

    def __str__(self):
        return f"{self.student.firstname} for {self.position.name} ({self.status})"


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
