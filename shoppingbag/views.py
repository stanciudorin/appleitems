from django.shortcuts import render


def view_shoppingbag(request):
    """ Returning the index page """
    return render(request, "shoppingbag/shoppingbag.html")