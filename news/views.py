from django.shortcuts import render


def home(request):
    import requests
    import json

    news_api_request= requests.get("http://newsapi.org/v2/top-headlines?country=eg&apiKey=930dd01371994db694cfc31a75620641")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html' , {'api':api})