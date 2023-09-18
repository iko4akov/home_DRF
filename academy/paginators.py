from rest_framework.pagination import PageNumberPagination

class AcademyPaginator(PageNumberPagination):
    page_size = 5
