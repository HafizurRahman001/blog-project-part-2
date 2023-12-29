from django.shortcuts import render,redirect
from posts_app.forms import AddPostForm
from posts_app.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        add_post_form = AddPostForm(request.POST)
        if add_post_form.is_valid():
            add_post_form.instance.author = request.user
            add_post_form.save()
            return redirect('home')
    else:
        add_post_form = AddPostForm()
    return render(request,'add_post.html', {'form':add_post_form})


@login_required
def edit_post(request,id):
    post = Post.objects.get(pk=id)
    edit_post_form = AddPostForm(instance=post)
    if request.method == 'POST':
        edit_post_form = AddPostForm(request.POST, instance=post)
        if edit_post_form.is_valid():
            edit_post_form.instance.author = request.user
            edit_post_form.save()
            return redirect('profile')
    return render(request,'add_post.html', {'form':edit_post_form})


@login_required
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('profile')

