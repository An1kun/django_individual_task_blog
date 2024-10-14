from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Follow
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

def user_registration(request):
    # Handle user registration form (Django built-in forms can be used)
    pass

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    print(1)
    print(f"User: {request.user}")  # Check the logged-in user
    profile = request.user.profile
    print(f"Profile: {profile}") 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)  # Redirect to the profile view
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_form.html', {'form': form})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile_view', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(follower=request.user, following=user_to_unfollow).first()
    if follow:
        follow.delete()
    return redirect('profile_view', username=username)