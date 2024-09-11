from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from digestapi.views import BookViewSet, UserViewSet, CategoryViewSet, ReviewViewSet

router = DefaultRouter(trailing_slash=False)

# Register your viewsets here
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'books', BookViewSet, 'book')
router.register(r'reviews', ReviewViewSet, 'review')

urlpatterns = [
    path(
        '', include(router.urls)
    ),  # This includes the registered routes, including /categories
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),
    path(
        'register', UserViewSet.as_view({'post': 'register_account'}), name='register'
    ),
]
