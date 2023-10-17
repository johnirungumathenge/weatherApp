from django.shortcuts import render, HttpResponse
import requests
from django.contrib import messages
import datetime

# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Meru'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c865f10a4b625f89729d078d5768ed49'

    PARAMS = {'units':'metric'}

    

    try:
        data = requests.get(url, PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request, 'index.html', {'description': description, 'icon':icon, 'temp':temp, 'day':day, 'city':city,'exception_occurred':False})
    
    except:
        exception_occurred = True
        messages.error(request, "The specified place not found in API")
        day = datetime.date.today()

    
        return render(request, 'index.html', {'description': 'clear sky', 'icon':'01d', 'temp':25, 'day':day, 'city':'Meru', 'exception_occurred':True})