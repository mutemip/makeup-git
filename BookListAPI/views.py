from django.shortcuts import render

from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def books_view(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"Books": list(books)})
    else:
        if request.method == "POST":
            title = request.POST.get('title')
            author = request.POST.get('author')
            price = request.POST.get('price')
        book = Book(
            title=title, 
            author=author, 
            price=price
            )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        return JsonResponse(model_to_dict(books) and status==201)


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets


@api_view(['GET','POST'])# http methods supported by this endpoint
def books(request):
    return Response('List of books', status=status.HTTP_200_OK)


# class based views extending APIView
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
    
# classes that extend viewsets
class BookView(viewsets.ViewSet):
    def list(self, request):
         return Response({"message":"All books"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a book"}, status.HTTP_200_OK)