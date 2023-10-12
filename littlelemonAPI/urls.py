from django.urls import path
from . import views



urlpatterns = [
    # CBV urls using generics
    path('menuitem', views.MenuItemsView.as_view()), #CBV
    path('menu-item/<int:pk>', views.SingleItemView.as_view()),

    # CBV urls using ViewSets
    path('menu-items', views.MenuItemViewSet.as_view({'get':'list', 'post': 'create'})),
    path('menu-items/<int:pk>', views.MenuItemViewSet.as_view({'get':'retrieve'})),

    # FBV urls
    path('menu-item1', views.menu_items), #FBV
    path('menu-item1/<int:pk>', views.single_item),
        path('category', views.CategoryView.as_view()),
    path('category/<int:pk>',views.category_detail, name='category-detail'),
    
    #API endpoints authorization layer and user role management
    path('secret', views.secret_view),
    #manager view
    path('groups/manager/users', views.manager_view),

    # delivery view
    # path("groups/delivery/users", views.delivery_view),

    # throttling endpoint
    path("throttle", views.throttle_check),
    path("auth-throttle", views.throttle_user),

    # me endpoint
    path("users/me", views.me, name="me"),

    #ratings API
    path('rating', views.RatingsView.as_view()),
]