def is_seller(user):
    print(user)
    print(user.groups.filter(name='Sellers').exists())
    return user.groups.filter(name='Sellers').exists()
