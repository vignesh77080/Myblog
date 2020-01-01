from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfileUser, Post
from django.core.mail import send_mail
from django.conf import settings
from user_login.form import UserLogin, RegistrationForm, ProfileForm, ProfileUpdate, PostCreation 

# Create your views here.
@login_required(login_url= 'login')
def home(request):

    post = Post.objects.all()
    context = {
        'post': post
    }

    return render(request, 'user_login/home.html', context)

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user_creation = User.objects.create_user(username, email, password2)
                if user_creation is not None:
                    user_creation.save()
                    messages.success(request, f'your profile has been created, {username }')
                    send_mail('new account has been created','welcome to our blog',settings.EMAIL_HOST_USER, [form.cleaned_data.get('email')] , fail_silently=False)
                    return render(request, 'user_login/register_success.html' )
            else:
                messages.error(request, 'something went wrong , try again')
                return render(request, 'user_login/register_success.html' )
    else:
        form = RegistrationForm()

    return render(request, 'user_login/register.html',context= {
        'form' : form
    } )

@login_required(login_url= 'login')
def profile(request):

    if request.method == 'GET':
        user_form = ProfileUpdate( instance = request.user )
        profile_form = ProfileForm(instance = request.user.profileuser)
    else:
        user_form = ProfileUpdate(request.POST, instance = request.user )
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profileuser)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, f'your profile has beeen update { request.user}')
            return redirect('/')
        else:
            messages.error(request, 'pleasse enter the corrext values')
 
    context = {
        'u_form': user_form,
        'p_form' : profile_form
    }
    return render(request, 'user_login/profile.html',context)

@login_required(login_url= 'login')
def createpost(request):

    if request.method == 'POST':
        post = PostCreation(request.POST)
        if post.is_valid():
            post.instance.created_by = request.user
            post.save()
            messages.success(request, 'post have been created')
            return redirect('/')            
        else:
            messages.error(request, 'post not created')

    post = PostCreation()
    context = {
        'post': post
    }

    return render(request, 'user_login/create_blog.html', context)

@login_required(login_url= 'login')
def editpost(request, post_id):

    b = User.objects.get(pk = request.user.id).post_set.get(id = post_id)
    if request.method == 'POST':
        post = PostCreation(request.POST, instance= b)
        if post.is_valid():
            post.save()
            messages.success(request, 'post have been updated')
            return redirect('/')
        else:
            messages.error(request, 'post not updated')

    post = PostCreation( instance = b  )
    context = {
        'post': post
    }

    return render(request, 'user_login/edit_blog.html', context)

@login_required(login_url= 'login')
def viewpost(request, post_id):
    c = Post.objects.get(id = post_id)
    post = PostCreation( instance = c )
    print(post)
    context = {
        'post': post
    }
    return render(request, 'user_login/view_blog.html', context)

@login_required(login_url= 'login')
def deletepost(request, post_id):
    d = User.objects.get(pk = request.user.id).post_set.get(id = post_id)
    val = d.title
    if request.method == 'POST':
        if 'first_button' in request.POST:
            d.delete()
            messages.success(request, f'your {val} is deleted')
            return redirect('/')
        else:
            return redirect('/')

    context = {
        'title' : val, 
        'post_id' : post_id
    }

    return render(request, 'user_login/delete_blog.html', context)