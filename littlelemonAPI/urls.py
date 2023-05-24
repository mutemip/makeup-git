from django.urls import path
from . import views

urlpatterns = [
    path('menu-item', views.MenuItemsView.as_view()),
    path('menu-item/<int:pk>', views.SingleItemModelSerializer.as_view()),
    # path('category', views.CategoryView.as_view()),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail')
]