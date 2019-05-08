from django.db import models

# Create your models here.

#----- ตัวอย่าง one-to-many
class Customer(models.Model):
    name = models.CharField('ชื่อ นามสกุล', max_length=200)
    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.CharField('หน้าพิซซ่าที่ชอบ', max_length=200)
    customer = models.ForeignKey(Customer, related_name='favorites', verbose_name='ลูกค้า', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#----- ตัวอย่าง many-to-many
class Topping(models.Model):
    name = models.CharField('ท็อปปิ้ง', max_length=200)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField('ชื่อเมนูพิซซ่า', max_length=200)
    toppings = models.ManyToManyField(Topping)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
