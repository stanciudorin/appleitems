from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_shoppingbag(request):
    """ Returning the index page """
    return render(request, "shoppingbag/shoppingbag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if quantity > 0:
        shoppingbag[item_id] = quantity
    else:
        shoppingbag.pop(item_id)

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_bag'))
    

def remove_from_bag(request, item_id):
    """ Remove the item from the shoppind bag """

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})
    try:
        if quantity == 0:
            shoppingbag.pop(item_id)
            
        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
