from django.db import models

# Create your models here.
class Turno(models.Model):
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    pacient = models.ForeignKey('auth.User', related_name='appointments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {}".format(self.title, self.date)