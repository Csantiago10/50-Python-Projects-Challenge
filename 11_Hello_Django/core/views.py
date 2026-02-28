from django.shortcuts import render


# Create your views here.
def user_profile(request):
    """Return jsonresponse"""
    # 1. Create a database.
    context = {
        'name': 'Santiago Noreña',
        'role': 'Backend Developer in Training',
        'skills': [
            'Python',
            'Django',
            'Flet',
            'HTML',
            'CSS',
            'Git',
        ]
    }
        
    # 2. Render the template with the context (request, template, context).
    return render(request, 'core/profile.html', context)