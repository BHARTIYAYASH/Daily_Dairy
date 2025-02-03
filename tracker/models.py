from django.db import models
from django.utils.timezone import now

# class DailyConsumption(models.Model):
#     date = models.DateField(auto_now_add=True)  # Auto-fills current date
#     item = models.CharField(max_length=20, choices=[('Milk', 'Milk'), ('Curd', 'Curd'), ('Buttermilk', 'Buttermilk')])
#     quantity = models.FloatField()  # Quantity in liters/KG

class DailyConsumption(models.Model):
    ITEM_CHOICES = [
        ('Milk', 'Milk'),
        ('Curd', 'Curd'),
        ('Buttermilk', 'Buttermilk'),
    ]
    
    date = models.DateField(default=now)  # Default to today's date
    item = models.CharField(max_length=10, choices=ITEM_CHOICES)
    quantity = models.DecimalField(max_digits=4, decimal_places=2)  # Changed to DecimalField

    def __str__(self):
        return f"{self.item} - {self.quantity} ({self.date})"

    # def __str__(self):
    #     return f"{self.date} - {self.item} - {self.quantity}L/KG"

    class Meta:
        ordering = ['-date']
