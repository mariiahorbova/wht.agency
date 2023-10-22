from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=255)
    members = models.ManyToManyField("employee.Employee", related_name="teams")

    def __str__(self):
        return f"{self.title} [{self.members}]"
