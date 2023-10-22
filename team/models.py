from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=255)
    members = models.ForeignKey(
        "employee.Employee",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="teams"
    )

    def __str__(self):
        return f"{self.title} [{self.members}]"
