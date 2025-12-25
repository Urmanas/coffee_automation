from django.db import models
from django.core.exceptions import ValidationError

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name 


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.TextField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'Жаны буюртма'),
            ('ready', 'Сиздин буюртма даяр'),
            ('done', 'Буюртма жасалып бутту')
        ],
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if self.pk:
            old = Order.objects.get(pk=self.pk)
            if old.status == 'done' and self.status != 'done':
                raise ValidationError('Нельзя изменить завершенный заказ')

    def __str__(self):
        return f'Order #{self.id} — {self.customer_name}'


    
