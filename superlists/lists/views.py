from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    new_list= List.objects.create()
    item=Item(text=request.POST['item_text'], list= new_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        error= "You can't have an empty list item"
        return render(render, 'home.html',{'error': error})
    return redirect('/lists/%d/' %(new_list.id,))

def view_list(request, list_id):
    # list all the items from that list
    list_= List.objects.get(id= list_id)

    if request.method== 'POST':
        Item.objects.create(text=request.POST['item_text'], list= list_)
        return redirect('/lists/%d/' %(list_.id))

    return render(request, 'list.html',
                    {  'list': list_, }
        )
