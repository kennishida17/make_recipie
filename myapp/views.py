from django.shortcuts import render
from .models import Dish
from django.http import HttpResponseRedirect
import openai
openai.api_key = "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"

def index(request):
    posts = Dish.objects.all().order_by('-created_at')[:1]
    if request.method == 'POST':
        post = Dish()
        post.title = request.POST['title']
        question = post.title + "のレシピを教えてください"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",#モデル選択
            messages=[{
            "role":"user",
            "content":question,
            }]
        )
        response = completion.choices[0].message.content
        post.recipie = response
        post.save()
        return HttpResponseRedirect('/top',{'posts':posts})
    else:
        return render(request, 'myapp/index.html',{'posts':posts})
