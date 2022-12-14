import json

from django.http import JsonResponse

from firstProject.web.models import Product, WishList


def update_wishlist(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=product_id)
    item, created = WishList.objects.get_or_create(user=user, product=product)
    if action == 'remove':
        item.delete()

    return JsonResponse('Wishlist was updated.', safe=False)
