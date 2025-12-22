from django.db import models

class Orders(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.TextField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'New'),
            ('ready', 'Ready'),
            ('done', 'Done')
        ],
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)