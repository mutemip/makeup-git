# Heading one
___
## Heading two
___
### Heading Three
___
**Bold**
___
__Bold__

*Italic*
> blockquote

### ordered List
1. Mimi
2. WEWE
3. Yeye
4. Wao

### Unordered List
- Wao
- Mimi
* mum
* Dad



---
### LINK
[Using Environment Variables In Django](https://djangocentral.com/environment-variables-in-django/)

### Image
![ProductList](LHG5.jpg)

### Table
| First Name | Last Name |
| ----------- | ----------- |
| Mkuu | Mnyonge |
| Mifupa | Kavu |

### Footnote {#1}
[^1]: This is the footnote.



### Tags
`Code`
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