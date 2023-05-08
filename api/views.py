from api.serialize import ServisSerializer
from api.models import Servis
from rest_framework.views import APIView
from rest_framework.response import Response

class ServisTable(APIView):
    def get(self, request):
        ServisObj=Servis.objects.all()
        ServisSerializeObj = ServisSerializer(ServisObj,many=True)
        return Response(ServisSerializeObj.data)
    def post(self, request):
        serializeObj = ServisSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)
