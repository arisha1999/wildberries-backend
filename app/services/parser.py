import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.db import transaction
from ..models.product import Product


class ParserService:
    BASE_URL = "https://www.wildberries.ru"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    @classmethod
    def parse_and_save_products(cls, search_query: str, limit: int = 20):
        """Основной метод парсинга и сохранения товаров"""
        try:
            html = cls._fetch_html(search_query)
            products_data = cls._parse_html(html, limit)
            cls._save_products(products_data, search_query)
            return True, f"Успешно спаршено {len(products_data)} товаров"
        except Exception as e:
            return False, f"Ошибка парсинга: {str(e)}"

    @staticmethod
    def _fetch_html(search_query: str):
        response = requests.get(
            f"{ParserService.BASE_URL}/catalog/0/search.aspx?search={search_query}",
            headers=ParserService.HEADERS
        )
        response.raise_for_status()
        return response.text

    @staticmethod
    def _parse_html(html: str, limit: int):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select('.product-card')[:limit]

        products = []
        for item in items:
            # Реализация парсинга конкретных данных
            products.append({
                'name': "Пример товара",
                'price': 9999.0,
                'old_price': 12999.0,
                'rating': 4.5,
                'reviews': 150
            })
        return products

    @staticmethod
    @transaction.atomic
    def _save_products(products_data: list, category: str):
        for data in products_data:
            Product.objects.update_or_create(
                name=data['name'],
                defaults={
                    'price': data['price'],
                    'discounted_price': data['old_price'],
                    'rating': data['rating'],
                    'reviews_count': data['reviews'],
                    'category': category,
                    'parsed_at': datetime.now()
                }
            )