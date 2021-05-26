from django.contrib.auth.models import User
from opensource.models import Category, BadWord, Subscribtion, Post
import json 

def extras (request):
    common_tags = Post.tags.most_common()[:4]

    subscribtions = Subscribtion.objects.filter(user=request.user.id)
    categories = Category.objects.all()
    badWords = BadWord.objects.all().values()
    
    # Parse the values to get with javascript later
    words = []
    for word in list(badWords):
        words.append(word['word'])
    words = json.dumps(words)

    for category in categories:
        for sub in subscribtions:
            if sub.category.id == category.id:
                category.is_subscribed = True


    return {
        'categories': categories,
        'badWords': words,
        'common_tags': common_tags
    }