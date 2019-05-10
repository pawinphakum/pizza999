from django.db import models

# Create your models here.

#----- ตัวอย่าง one-to-many
class Customer(models.Model):
    name = models.CharField('ชื่อ นามสกุล', max_length=200)
    # customer.favorites.all อ้างถึง related_name เพื่อแสดง fovorite ทั้งหมดของ customer นี้
    # หรือถ้าไม่ได้กำหนด related_name ก็ใช้ _set ได้เช่น customer.favorite_set.all
    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.CharField('หน้าพิซซ่าที่ชอบ', max_length=200)
    #customer = models.ForeignKey(Customer, related_name='favorites', verbose_name='ลูกค้า', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name='ลูกค้า', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#----- ตัวอย่าง many-to-many
class Topping(models.Model):
    name = models.CharField('ท็อปปิ้ง', max_length=200)
    # topping.pizza_set.all ใช้ _set เพื่อแสดง pizza ทั้งหมดที่ใช้ topping นี้
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField('ชื่อเมนูพิซซ่า', max_length=200)

    # ตรง ManyToManyField นี้จะไม่ใช่ column จริงๆ ในตารางใดๆ มันจะเป็นแค่ชื่อเพื่อใช้งาน
    toppings = models.ManyToManyField(Topping)
    # pizza.toppings.all แสดง toppings ทั้งหมดของ pizza หน้านี้
    # ไม่สามารถใช้ pizza.topping_set.all แบบ one-to-many ได้
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# ตารางที่สร้างจากตัวอย่าง many-to-many ด้านบน จะมี 3 ตาราง
# pizza
# topping
# pizza_toppings (สังเกตุว่าจะเป็นชื่อ _<ชื่อที่ตั้งไว้>)
