from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'passgen/index.html')

    def post(self, request):
        pass