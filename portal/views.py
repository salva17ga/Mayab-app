from django.shortcuts import render

### views

def index(request): 
    var = "example"
    return render(request, "base.html", {'variable': var})