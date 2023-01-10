
from django.shortcuts import render
from django.http import HttpResponse
# from.models import place
# from.models import people
# Create your views here.
def demo(request):
#     obj=place.objects.all()
#     ob=people.objects.all()
      return render(request,"index.html")#{'result':obj,'res':ob})

# Create your views here.
