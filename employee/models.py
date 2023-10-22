from django.db import models

from team.models import Team


class Employee(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(
        Team,
        related_name="employees",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
