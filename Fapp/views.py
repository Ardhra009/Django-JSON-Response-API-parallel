from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse 
# Create your views here.
class homeView(View):
    def get(self,request):
        data=[
            {
                'name':'john',
                'age':20
            },
            {
                'name':'jane',
                'age':25
            }

        ]
        return JsonResponse(data,safe=False)