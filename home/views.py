from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request,"index.html")
def hleb(request):
    x={"eat1":"лимонад"}
    return render(request,"home.html",{"eat1":"лимонад","eat2":"кокакола"})    