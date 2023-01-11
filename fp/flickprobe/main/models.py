from django.db import models

# Create your models here.

L_CHOICE =( 

    ("hi", "Hindi"), 

    ("en", "English"), 

) 






class movie(models.Model):
         name=models.CharField(max_length=300)
         director=models.CharField(max_length=100)
         cast =models.CharField(max_length=800)
         description=models.TextField(max_length=5000)
         release_date=models.DateField()
         language =models.CharField(choices=L_CHOICE , max_length=20)
 
         rating=models.FloatField()
         poster=models.URLField()
         
    
         def __str__(self):
               return self.name




