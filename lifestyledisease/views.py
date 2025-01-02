from django.shortcuts import render
from .models import Review
# Create your views here.
def index(request):
       Revs=Review.objects.all()
       return render(request,'index.html',{'Revs':Revs})

