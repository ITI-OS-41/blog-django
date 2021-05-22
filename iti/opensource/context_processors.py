from django.contrib.auth.models import User
from opensource.models import Category, BadWord
import json 

def extras (request):
    categories = Category.objects.all()
    badWords = BadWord.objects.all().values()
    # Parse the values to get with javascript later
    words = []
    for word in list(badWords):
        words.append(word['word'])
    words = json.dumps(words)



    return {
        'categories': categories,
        'badWords': words,
    }