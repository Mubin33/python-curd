from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.




 # if follow step 6(Model View Set er shahajje CURD kora) then need under line of code or path use

#  (get all data) (create or post data) (get indivitual data) (update or put data) (delete data)
class AiquwstModelViewSet(viewsets.ModelViewSet):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer  
   





 # if follow step 5(Concrete View class er shahajje CURD kora) then need under line of code or path use
'''
#  (get all data) (create or post data)
class Aiquwst_list_create(ListCreateAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer  

# (get indivitual data) (update or put data) (delete data)
class Aiquest_up_del(RetrieveUpdateDestroyAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer 
        
'''










 # if follow step 4(ListModelMixin in Rest er shahajje CURD kora) then need under line of code or path use
'''
#  (get all data) (create or post data)
class Aiquwst_list_create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs): # ListModelMixin in Rest(get all data)
        return self.list( request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs): # CreateModelMixin in Rest(create or post data)
        return self.create( request, *args, **kwargs)
    
    


# (get indivitual data) (update or put data) (delete data)
class Aiquest_up_del(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs): # RetrieveModelMixin in Rest(get indivitual data)
        return self.retrieve( request, *args, **kwargs)
 

    def put(self, request, *args, **kwargs): # UpdateModelMixin in Rest(update or put data)
        return self.update( request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs): # DestroyModelMixin in Rest(delete data)
        return self.destroy( request, *args, **kwargs)
        
        '''


# or



# if follow step 3(Class Based View APIView er shahajje CURD kora) then need under line of code  

# Class Based View APIView
'''class AiquestCrearte(APIView):
    # get data
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            # complex data
            ai = Aiquest.objects.get(id=id)
            # python dic
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)

        # complex data
        ai = Aiquest.objects.all()
        # python dict
        serializer = AiquestSerializer(ai, many=True)
        return Response(serializer.data)
    

     # post data 
    def post(self, request, format=None): 
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully save data'})
        return Response(serializer.errors)
    



    # put data (fulll data change)
    def put(self, request,pk, format=None): 
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully update full data'})
        return Response(serializer.errors)
    

    # Patch data ( data change)
    def patch(self, request,pk, format=None): 
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully update partial data'})
        return Response(serializer.errors)
    


    # delete data 
    def delete(self, request,pk, format=None): 
        id = pk
        ai = Aiquest.objects.get(pk = id)
        ai.delete() 
        return  Response({'msg': 'Successfully delete data'})'''



# or




# if follow step 2(normaly api view er shahajje CURD kora) then need under line of code  

# API View
'''@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def aiquest_create(request, pk=None):
    # get data all or id 
    if request.method == 'GET':
        id=pk
        if id is not None:
            # complex data
            ai = Aiquest.objects.get(id=id)
            # python dic
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)

        # complex data
        ai = Aiquest.objects.all()
        # python dict
        serializer = AiquestSerializer(ai, many=True)
        return Response(serializer.data)
    

    post data 
    if request.method == 'POST':
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully save data'})
        return Response(serializer.errors)
    

    put data (fulll data change)
    if request.method == 'PUT':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully update full data'})
        return Response(serializer.errors)
    

    Patch data ( data change)
    if request.method == 'PATCH':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg': 'Successfully update partial data'})
        return Response(serializer.errors)
    


    delete data 
    if request.method == 'DELETE':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        ai.delete() 
        return  Response({'msg': 'Successfully delete data'})'''






# or




# if follow step 1(normaly CURD kora) then need under line of code  


# get all data
'''def aiquest_info(request):
    # complex data
    ai = Aiquest.objects.all()
    # python dict
    serializer = AiquestSerializer(ai, many=True)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')


# get data indivisual
def aiquest_info_per_data(request, pk):
    # complex data
    ai = Aiquest.objects.get(id=pk)
    # python dict
    serializer = AiquestSerializer(ai)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def aiquest_create(request):
    # post or create
    if request.method == 'POST':
        json_data = request.body
        # json to string data
        stream =io.BytesIO(json_data)
        # str to py 
        pythonData = JSONParser().parse(stream)
        # python to complex
        serializer = AiquestSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'sussfully send data'}
            jsonData = JSONRenderer().render(res)
            return HttpResponse(jsonData, content_type='application.json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application.json' )
    


    # update or put
    if request.method == 'PUT':
        json_data = request.body
        # json to string data
        stream =io.BytesIO(json_data)
         # str to py 
        pythonData = JSONParser().parse(stream)
        id= pythonData.get('id')
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'sussfully Update data'}
            jsonData = JSONRenderer().render(res)
            return HttpResponse(jsonData, content_type='application.json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application.json' )
    

 
    
    # delete or remove
    if request.method == 'DELETE':
        json_data = request.body
        # json to string data
        stream =io.BytesIO(json_data)
         # str to py 
        pythonData = JSONParser().parse(stream)
        id= pythonData.get('id')
        aiq = Aiquest.objects.get(id=id)
        aiq.delete()
        res = {'msg': 'sussfully Delete data'}
        jsonData = JSONRenderer().render(res)
        return HttpResponse(jsonData, content_type='application.json')'''