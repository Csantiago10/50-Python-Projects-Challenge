from django.shortcuts import render
from core.models import Profile


# Create your views here.
def user_profile(request):

    profiles = Profile.objects.all()

    context = {
        "profiles": profiles,
    }

    return render(request, 'core/profile.html', context)