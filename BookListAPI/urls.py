from django.urls import path
from . import views

urlpatterns = [
    #path('books/', views.books_view, name="books"),
    #path('books-list/', views.books, name="books-list"),

    # Routing class-based views
    


    # Routing classes that extend viewsets
    # path('books', views.BookView.as_view({'get': 'list','post': 'create',})),
    # path('books/<int:pk>', views.BookView.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }))
    path("books", views.BookList.as_view()),
    path('books/<int:pk>',views.BookView.as_view()),
]