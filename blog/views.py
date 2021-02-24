from django.shortcuts import render, redirect
from .models import BlogPost, BlogGallery, BlogappProfile, BlogMessage, BlogProject
from blog.form import MessageForm
# Create your views here.


def home(request):
    posts = BlogPost.objects.all() 
    gallerys = BlogGallery.objects.all()
    message = BlogMessage.objects.all()
    
    content = {
            'posts': posts [::-1],
            'gallery': gallerys [::-1],
            'profile': BlogappProfile.objects.all(),
            'project': BlogProject.objects.all()
    }

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('home')
        else:
            form = MessageForm()
            content['form'] = form
    else:
        form = MessageForm()
        content['form'] = form        

    return render(request, 'index.html', content)

