from firstProject.web.models import Category


def categories_context(request):
    categories = Category.objects.all()
    return {'categories': categories}
