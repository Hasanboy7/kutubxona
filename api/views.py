from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,ListAPIView
from .serilazers import PlaceSerilazers,CommentSerializer,UserSerializer
from place.models import Place,Comment,User


# ------------------ Place views-------------------------------------------------
class ListTodos(ListAPIView):
    queryset=Place.objects.all()
    serializer_class=PlaceSerilazers

class ListTodo(RetrieveUpdateDestroyAPIView):
    queryset=Place.objects.all()
    serializer_class=PlaceSerilazers

class ListCreate(ListCreateAPIView):
    serializer_class = PlaceSerilazers

    def get_queryset(self):
        return Place.objects.all()
    
# -------------------Comment -----------------------------------------------------

class CommentView(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

# --------------------User--------------------------------------------------------
class UserView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


# --------------------Darsdagi ko'dlar----------------------------------------------
# class PlaceSerilazerView(APIView):
#     def get(self, request):
#         places = Place.objects.all()
#         serializer = PlaceSerilazers(places, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PlaceSerilazers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












