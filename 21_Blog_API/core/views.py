from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    # CASE A: read data from database
    if request.method == 'GET': 
        articles = Article.objects.all() # select * from article table in database
        serializer = ArticleSerializer(articles, many=True) # select * from article table in database and convert to json
        return Response(serializer.data) # return json data
    
    # CASE B: create data in database
    elif request.method == 'POST':
        # 1. Send the JSON data to serializer and save it to database
        serializer = ArticleSerializer(data = request.data)

        # 2. Check if the data is valid review if the data it has no error
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail(request, pk):

    #1. The search: get the data from database by primary key
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #2. Update the data in database
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    #3. Update the data in database
    elif request.method == 'PUT':
        # 1. Send the JSON data to serializer and save it to database
        serializer = ArticleSerializer(article, data = request.data)
        # 2. Check if the data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #4. Delete the data in database
    elif request.method == 'DELETE':
        article.delete()
        return Response({'message': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)