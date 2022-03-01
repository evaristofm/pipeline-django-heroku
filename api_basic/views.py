from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User





class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer







# # views baseadas em classes genericas
# class GenericApiView(generics.GenericAPIView,
#      mixins.ListModelMixin, mixins.CreateModelMixin,
#      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#      mixins.DestroyModelMixin):
#
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, id):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)


# #Views baseadas em Class A PIVIEW
# class ArticleApiView(APIView):
#
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetail(APIView):
#
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         article = Article.objects.get(id=id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         article = Article.objects.get(id=id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, id):
#         article = Article.objects.get(id=id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# # Views Baseadas em Funções
#
# @api_view(['GET', 'POST'])
# def article_list(request, format=None):
#
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk, format=None):
#
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

