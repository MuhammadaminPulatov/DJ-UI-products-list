from django.db.models import Model, CharField, IntegerField, TextField


# Create your models here.
class Product(Model):
    name=CharField(max_length=255)
    desc=TextField()
    price=IntegerField()
    count=IntegerField()
    rating = IntegerField(default=0)


    def __str__(self):
        return self.name