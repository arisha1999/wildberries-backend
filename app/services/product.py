from ..models.product import Product
from django.core.paginator import Paginator


class ProductService:
    @staticmethod
    def get_filtered_products(filters: dict, page: int = 1, per_page: int = 20):
        """Фильтрация и пагинация товаров"""
        queryset = Product.objects.all()

        if min_price := filters.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)
        if max_price := filters.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)
        if min_rating := filters.get('min_rating'):
            queryset = queryset.filter(rating__gte=min_rating)

        paginator = Paginator(queryset.order_by('-id'), per_page)
        return paginator.get_page(page)