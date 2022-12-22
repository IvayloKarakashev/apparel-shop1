def is_seller(user):
    return user.groups.filter(name='Sellers').exists()