from django.shortcuts import render, redirect, get_object_or_404
from core.models import Profile
from .forms import ProfileForm


# Create your views here.
def user_profile(request):

    profiles = Profile.objects.all()

    context = {
        "profiles": profiles,
    }

    return render(request, 'core/profile.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()

   
    # render the template with the form included (request, template, context)
    return render(request, 'core/create_profile.html', {'form': form})

def edit_profile(request, profile_id):
    # 1. Search for the profile, if it doesn't exist, return a 404
    profile = get_object_or_404(Profile, id=profile_id)

    # 2. If the request method is POST, update the profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')

    # 3. If the request method is GET, render the form with the profile
    else:
        form = ProfileForm(instance=profile)

    # 4. Render the template with the form included
    return render(request, 'core/create_profile.html', {'form': form})


def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    profile.delete()
    return redirect('profile_list')