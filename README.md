# Warehouse

mahsulotlar va materiallar bilan bog'liq omborlarni boshqarish uchun mahsulotlar ro'yxati va ularning omborlarini ko'rsatadi.

## Models

### Product Model

`Product` modeli mahsulotlar uchun ma'lumotlarni saqlaydi.

| Maydon | Tavsif |
|--------|--------|
| name   | Mahsulot nomi (max_length=100) |
| code   | Mahsulot kodi (unikal) (max_length=50) |
| quantity | Mahsulot miqdori (Integer, default=0) |

### Material Model

`Material` modeli materiallar uchun ma'lumotlarni saqlaydi.

| Maydon | Tavsif |
|--------|--------|
| name   | Material nomi (max_length=100) |

### Warehouse Model

`Warehouse` modeli omborlar uchun ma'lumotlarni saqlaydi.

| Maydon | Tavsif |
|--------|--------|
| material | Materialni ko'rsatish (ForeignKey(Material)) |
| remainder | Ombordagi qolgan miqdor |
| price | Narxi (DecimalField, max_digits=10, decimal_places=2, null=True) |

### ProductMaterial Model

`ProductMaterial` modeli mahsulot va omborlar orasidagi bog'lanishni ifodalaydi.

| Maydon | Tavsif |
|--------|--------|
| product | Mahsulotni ko'rsatish (ForeignKey(Product)) |
| warehouse | Omborni ko'rsatish (ForeignKey(Warehouse)) |
| quantity | Miqdor |


### WarehouseListView

`WarehouseListView` APIView omborlar ro'yxatini chiqarish uchun ishlaydi.

- **GET:** Barcha mahsulotlarni olish va ularning materiallari va omborlarini ko'rsatadi.

## URLs

- `` - Omborlar ro'yxati uchun

- # Mahsulotlar ro'yxati

Bu qismda mahsulotlar va ularning ombor ma'lumotlari ko'rsatilgan.

## Mahsulotlar

### Kompyuter

- Miqdori: 10 ta
- Materiallar:
  - **Protsessor**
    - Ombor IDsi: 1
    - Miqdori: 1
    - Narxi: $500.0
  - **Monitor**
    - Ombor IDsi: 2
    - Miqdori: 1
    - Narxi: $200.0

### Telefon

- Miqdori: 20 ta
- Materiallar:
  - **Ekran**
    - Ombor IDsi: 3
    - Miqdori: 1
    - Narxi: $100.0

