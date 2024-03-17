from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductMaterial


class WarehouseListView(APIView):
    # get metodi
    def get(self, request, *args, **kwargs):
        # Barcha mahsulotlarni olish
        products = Product.objects.all()
        # Natijalarni saqlash uchun bo'sh ro'yxat yaratamiz
        result = []

        # Har bir mahsulot uchun
        for product in products:
            # Mahsulot ma'lumotlarini to'plam
            product_data = {
                "product_name": product.name,  # Mahsulot nomi
                "product_qty": product.quantity,  # Mahsulot miqdori
                "product_materials": []  # Mahsulot materiallari ro'yxati
            }

            # Mahsulotning materiallarini olish
            product_materials = ProductMaterial.objects.filter(product=product)

            # Har bir material uchun
            for pm in product_materials:
                # Materialni omborni olish
                warehouse = pm.warehouse

                # Material ma'lumotlari
                product_material = {
                    "warehouse_id": warehouse.id if warehouse else None,  # Ombor idsi
                    "material_name": warehouse.material.name if warehouse else None,  # Material nomi
                    "qty": pm.quantity,  # Miqdori
                    "price": warehouse.price if warehouse else None  # Narxi
                }

                # Mahsulot materiallarini qo'shish
                product_data["product_materials"].append(product_material)

            # Mahsulot ma'lumotlarini ro'yxatga qo'shish
            result.append(product_data)

        # Natijani javob sifatida qaytarish
        return Response({"result": result})
