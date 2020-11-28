from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404 
from django.contrib import messages

from products.models import Product


def view_shoppingbag(request):
    """ Returning the index page """
    return render(request, "shoppingbag/shoppingbag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {shoppingbag[item_id]}')
    else:
        shoppingbag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if quantity > 0:
        shoppingbag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {shoppingbag[item_id]}')
    else:
        shoppingbag.pop(item_id)
        messages.success(request, f'Removed {product.nema} from your bag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_bag'))
    

def remove_from_bag(request, item_id):
    """ Remove the item from the shoppind bag """

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})
    try:
        product = get_object_or_404(Product, pk=item_id)
        if quantity == 0:
            shoppingbag.pop(item_id)
            messages.success(request, f'Removed {product.nema} from your bag')
            
        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(f'Error removing item: {e}')
        return HttpResponse(status=500)
