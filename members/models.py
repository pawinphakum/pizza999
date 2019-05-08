from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('ชื่อ นามสกุล', max_length=200)
    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.CharField('หน้าพิซซ่าที่ชอบ', max_length=200)
    customer = models.ForeignKey(Customer, related_name='favorites', verbose_name='ลูกค้า', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
