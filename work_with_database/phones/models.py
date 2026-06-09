from django.db import models
from django.utils.text import slugify

'''создаём модель Phone с полями id, name, price, image, release_date, lte_exists и slug. 
Поле id — должно быть основным ключом модели.
Значение поля slug должно устанавливаться слагифицированным значением поля name.'''

class Phone(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=50)   
    price = models.IntegerField()           
    image = models.URLField()                
    release_date = models.DateField()       
    lte_exists = models.BooleanField()      
    slug = models.SlugField(unique=True, max_length=50)  # slug из названия

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)   # преобразуем name в slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name