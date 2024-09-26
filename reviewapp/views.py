from django.shortcuts import render
from datetime import datetime
import requests
from .forms import ReviewForm
from .models import Reviews

def home(request):

    city = request.GET.get('search')
    dateandtime = datetime.now()
    response1 = requests.get('https://zenquotes.io/api/quotes/')
    response2 = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e2ea517cea3cba3a6523167871199358&units=metric')

    if response1.status_code == 200:
        data = response1.json()
        quote = data[0]
    else: 
        quote = None 

    if response2.status_code == 200:
        data = response2.json()
        weather = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        weather = None     

    return render(request, 'reviewapp/index.html', {
        'date': dateandtime.date,
        'time': dateandtime.time,
        'quote': quote,
        'weather': weather
    })

def add(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_age = form.cleaned_data['age']
            new_gender = form.cleaned_data['gender']
            new_phone_no = form.cleaned_data['phone_number']
            new_review = form.cleaned_data['review']

            new_reviews = Reviews(
                name = new_name,
                email = new_email,
                age = new_age,
                gender = new_gender,
                phone_number = new_phone_no,
                review = new_review
            )
            new_reviews.save()

            return render(request, 'reviewapp/add.html', {
                'form': ReviewForm(),
                'success': True
            }) 
    else:
        form = ReviewForm()

    return render(request, 'reviewapp/add.html', {
                'form': ReviewForm()
    })

def view_reviews(request):
    show_all = Reviews.objects.all()
    return render(request, 'reviewapp/showreviews.html', {
        'reviews': show_all
    })