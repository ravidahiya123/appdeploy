from django.db import models

class AppLink(models.Model):
    app_name = models.CharField(max_length=100, db_index=True)
    download_link = models.URLField(unique=True, db_index=True)
    used = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["used", "app_name"]),
        ]

    def __str__(self):
        return f"{self.app_name} – {'USED' if self.used else 'NEW'}"
