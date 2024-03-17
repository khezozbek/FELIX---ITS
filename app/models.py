from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.quantity = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.material.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if self.quantity is not None:
            # Agar ombor mavjud bo'lsa
            if self.warehouse:
                # Ombordagi qolgan miqdorni olamiz
                warehouse_remainder = self.warehouse.remainder
                # Agar ombordagi qolgan miqdor mavjud bo'lsa
                if warehouse_remainder is not None:
                    # Yangi qolgan miqdorni hisoblaymiz
                    new_remainder = warehouse_remainder - self.quantity
                    # Agar yangi qolgan miqdor 0 dan kichik yoki teng bo'lsa
                    if new_remainder <= 0:
                        self.quantity = warehouse_remainder
                        new_remainder = 0  # Qolgan miqdorni 0 ga sozlaymiz
                    # Ombordagi qolgan miqdorni yangilaymiz
                    self.warehouse.remainder = new_remainder
                    # Faqat belgilangan maydonlarni yangilaymiz
                    self.warehouse.save(update_fields=['remainder'])
        # saqlash
        super().save(*args, **kwargs)
