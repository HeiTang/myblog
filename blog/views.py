from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import Post

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .forms import UserCreationForm
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        new_post = Post(title=new_title, text=new_text)
        new_post.save()
        new_post.publish()
        return redirect('post_list')
    return render(request, 'blog/post_create.html', {})

class UserCreate(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        messages.success(self.request, '帳戶已創立')
        return reverse('login') 