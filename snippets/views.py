from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


class SnippetList(mixins.ListModelMixin,  # list (get)
				  mixins.CreateModelMixin,  # create (post)
				  generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,  # detail (get)
					mixins.UpdateModelMixin,  # update (put)
					mixins.DestroyModelMixin,  # destroy (delete)
					generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

# class SnippetList(APIView):
# 	"""
# 	List all snippets, or create a new snippet.
# 	"""
# 	def get(self, request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	# create Snippet
# 	def post(self, request, format=None):
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
# 	"""
# 	Retrieve, update or delete a snippet instance.
# 	"""
# 	def get(self, request, pk, format=None):
# 		snippet = get_object_or_404(Snippet, pk=pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	# update Snippet
# 	def put(self, request, pk, format=None):
# 		snippet = get_object_or_404(Snippet, pk=pk)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	# delete Snippet
# 	def delete(self, request, pk, format=None):
# 		snippet = get_object_or_404(Snippet, pk=pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
