from django.db import models



class Quotes(models.Model):
    quote = models.CharField(max_length=256)
    cite = models.CharField(max_length=32)
    
    def __str__(self):
        return self.quote + '  from   '+self.cite
