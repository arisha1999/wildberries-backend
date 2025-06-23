from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import product_service


class ProductController(APIView):
    def get(self, request):
        page = request.query_params.get('page', 1)
        products_page = product_service.get_filtered_products(
            filters=request.query_params.dict(),
            page=page
        )

        # Сериализация данных (можно вынести в отдельный модуль)
        data = {
            'items': [{
                'id': product.id,
                'name': product.name,
                'price': float(product.price),
                'discounted_price': float(product.discounted_price),
                'rating': product.rating,
                'reviews_count': product.reviews_count
            } for product in products_page],
            'total_pages': products_page.paginator.num_pages,
            'current_page': products_page.number
        }

        return Response(data, status=status.HTTP_200_OK)