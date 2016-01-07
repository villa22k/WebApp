from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

    return render(request, 'home.html')

def new_list(request):
    new_list= List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list= new_list)
    return redirect('/lists/%d/' %(new_list.id,))

def view_list(request, list_id):
    # list all the items from that list
    list_= List.objects.get(id= list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', { 'items': items, })

#list_id will be passed as a capture group -- it will be passed as list_id
