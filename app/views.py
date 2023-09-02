from django.shortcuts import render, redirect
from .models import Food, Consume

def index(request):

    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
        return redirect('/')
    else:
        foods = Food.objects.all()
    
    consumed_food = Consume.objects.filter(user=request.user)
    context = {'foods': foods, 'consumed_food': consumed_food}
    return render(request, 'index.html', context)

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return  redirect('index')
    return render(request, 'delete.html')
