# from django.db import models
# from projects_app.models import Project

# class Bug(models.Model):

#     PRIORITY_CHOICES = [
#         ('LO','Low'),
#         ('MD','Medium'),
#         ('HI','High')
#     ]
#     STATE_CHOICES = [
#         ('RE','Resolved'),
#         ('UN', 'Unresolved')
#     ]

#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default='0')
#     name = models.CharField(max_length=50)
#     desc = models.TextField()
#     priority = models.CharField(max_length=2, choices = PRIORITY_CHOICES)
#     state = models.CharField(max_length=2, choices = STATE_CHOICES)

#     def __str__(self):
#         return self.name
from django.db import models
from projects_app.models import Project
from django.utils.timezone import now


class Bug(models.Model):

    PRIORITY_CHOICES = [
        ('LO','Low'),
        ('MD','Medium'),
        ('HI','High')
    ]
    STATE_CHOICES = [
        ('RE','Resolved'),
        ('UN', 'Unresolved')
    ]

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default='0')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    priority = models.CharField(max_length=2, choices = PRIORITY_CHOICES)
    state = models.CharField(max_length=2, choices = STATE_CHOICES)
    created_date = models.DateTimeField(default=now)
    developer = models.CharField(max_length=10)
    developer_email = models.EmailField(max_length=254,blank=True)


    def __str__(self):
        return self.name
        