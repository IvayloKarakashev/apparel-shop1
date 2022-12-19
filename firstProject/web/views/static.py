from django.views import generic as generic_views

from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import FAQ


class FAQView(PageTitleMixin, generic_views.ListView):
    page_title = 'FAQ'
    model = FAQ
    template_name = 'front-end/faq.html'


class TermsAndConditionsView(PageTitleMixin, generic_views.TemplateView):
    page_title = 'Terms and Conditions'
    template_name = 'front-end/terms.html'


class AboutView(PageTitleMixin, generic_views.TemplateView):
    template_name = 'front-end/about-us.html'
    page_title = 'About us'
