from django.shortcuts import render
from firstProject.accounts.models import Profile


def home_view(request, profile=None):
    page_title = 'Apparel Shop'
    if request.user.is_authenticated and not request.user.is_superuser:
        profile = Profile.objects.get(user_id=request.user.id)

    context = {
        'pofile': profile,
        'page_title': page_title
    }
    return render(request, 'front-end/index.html', context)
