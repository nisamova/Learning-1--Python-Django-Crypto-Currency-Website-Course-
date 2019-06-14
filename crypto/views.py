from django.shortcuts import render

# Added this to give instruction to urls.py-crypto file to request/render hoempage
def home(request):
     return render(request, 'home.html', {})
