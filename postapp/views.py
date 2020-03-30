from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from postapp.models import Post
from postapp.forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from postapp.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "main/signup.html", context={'form': form})



class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "main/index.html"
    context_object_name = "posts"
    ordering =['-post_date']


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "main/postform.html"
    fields = ['title', 'message', 'image']
    
    def form_valid(self, form):
        form.instance.masterpost = self.request.user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "main/post-detail.html"

@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)
    return render(request, "main/profile.html", context={"form":form})

def post_comments(request, postid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(postid)
        if form.is_valid():
            c_form=form.save(commit=False)
            c_form.post = get_object_or_404(Post,id=postid)
            c_form.user=request.user
            print(c_form)
            c_form.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, "main/commentform.html", context={"form":form, })