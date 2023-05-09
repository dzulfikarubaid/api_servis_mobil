from api.serialize import ServisSerializer
from api.models import Servis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ServisCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializeObj = ServisSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class ServisTable(APIView):
    def get(self, request):
        ServisObj=Servis.objects.all()
        ServisSerializeObj = ServisSerializer(ServisObj,many=True)
        return Response(ServisSerializeObj.data)
class ServisUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,pk):
        try:
            ServisObj=Servis.objects.get(pk=pk)
        except:
            return Response("Data not found")
        serializeObj = ServisSerializer(ServisObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class ServisDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,pk):
        try:
            ServisObj=Servis.objects.get(pk=pk)
        except:
            return Response("Data not found")
        ServisObj.delete()
        return Response(200)