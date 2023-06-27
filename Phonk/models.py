from django.db import models

# Create your models here.
class phonk_singer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    big_award = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(null=True)
    def __str__(self) -> str:
        return f'{self.name} - {self.surname}'
    
    def get_absolute_url(self):
        return f"/{self.pk}"