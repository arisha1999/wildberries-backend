from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена со скидкой"
    )
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    reviews_count = models.IntegerField(default=0, verbose_name="Количество отзывов")
    category = models.CharField(max_length=100, verbose_name="Категория")
    parsed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата парсинга")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-parsed_at']

    def __str__(self):
        return f"{self.name} ({self.price}₽)"