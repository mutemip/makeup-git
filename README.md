# Heading one
___
## Heading two
___
### Heading Three
___
**Bold**
___
__Bold__

`` Practicing Tags ``

``BookView``

### Code Block (3 ```)
___
```
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

```