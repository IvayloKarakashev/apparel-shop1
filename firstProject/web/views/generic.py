from django.http import HttpResponseRedirect
from django.shortcuts import render

from firstProject.accounts.forms import SubscribeToNewsletterForm
from firstProject.accounts.models import Profile, Subscribers
from firstProject.web.models import Category


def home_view(request, profile=None):
    page_title = 'Apparel Shop'
    form = None
    user_is_subscribed = Subscribers.objects.filter(subscribed_user_id=request.user.id)
    new_categories = Category.objects.order_by('-id')[:3]

    if request.user.is_authenticated and not request.user.is_superuser:
        profile = Profile.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = SubscribeToNewsletterForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.subscribed_user_id = request.user.id
            obj.save()
            return HttpResponseRedirect(request.path_info)

    if request.method == 'GET':
        form = SubscribeToNewsletterForm()

    context = {
        'pofile': profile,
        'page_title': page_title,
        'subscription_form': form,
        'user_is_subscribed': user_is_subscribed,
        'new_categories': new_categories
    }
    return render(request, 'front-end/index.html', context)
