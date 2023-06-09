from django.urls import path
from . import views

urlpatterns = [
    path('menu-item', views.MenuItemsView.as_view()), #CBV
    path('menu-item1', views.menu_items), #FBV
    path('menu-item1/<int:pk>', views.sengle_item),
    path('menu-item/<int:pk>', views.SingleItemView.as_view()),
    # path('category', views.CategoryView.as_view()),
    path('category/<int:pk>',views.category_detail, name='category-detail')
]