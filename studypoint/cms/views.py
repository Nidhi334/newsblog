from django.shortcuts import render,redirect
from .models import Content, Topic,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    data = {}
    data['title'] = "Recent Topics"
    data['categories'] = Topic.objects.all()
    data['posts'] = Content.objects.all()
    return render(request, 'home.html', data)


def filter(request, topic_id):
    data= {}
    topic = Topic.objects.get(pk=topic_id)
    data['title'] = f"{topic.name} Posts"
    data['categories'] = Topic.objects.all()
    data['posts'] = Content.objects.filter(topic__id=topic_id)
    return render(request, 'home.html', data)

def search(request):
    query = request.GET.get('q')
    data = {}
    data['title'] = f"search Result for '{query}'"
    data['categories'] = Topic.objects.all()
    data['posts'] = Content.objects.filter(title__icontains=query)
    return render(request, 'home.html', data)

def showPost(request,content_id):
    post = Content.objects.get(pk=content_id)
    data= {}
    data['title'] = post.title
    data['categories'] = Topic.objects.all()
    data['post'] = post
    data['relatedPost'] = Content.objects.exclude(pk=content_id)
    data['comments'] = Comment.objects.filter(content_id=content_id)
    return render(request, 'show-post.html', data)

def saveComment(request,content_id):
    comment_text = request.POST.get('comment')
    content = Content.objects.get(pk=content_id)
    comment = Comment(content_id=content,user_id=request.user,comment=comment_text)
    comment.save()
    return redirect(showPost, content_id=content_id)



def loginview(request):
    form = AuthenticationForm(request.POST or None)
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('homepage')
    data['form'] = form
    return render(request, 'login.html',data )

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
           userForm= form.save(commit=False)
           userForm.is_staff = True
           userForm.is_superuser = True
           userForm.save()
           return redirect('login')
    data = {}
    data['form'] = form
    return render(request, 'register.html',data )

def logoutview(request):
    logout(request)
    return redirect('homepage')
