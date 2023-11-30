from django.shortcuts import render, redirect, get_object_or_404

from . models import Food, Consume
# Create your views here.


def index(request):
    saved_food = None  # Initialize saved_food
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        Consume.objects.create(user=user, food_consumed=consume)
        food = Food.objects.all()

    else:
        food = Food.objects.all()
    saved_food = Consume.objects.filter(user=request.user)
    context = {'food': food, 'title': 'Calory Tracker',
               'saved_food': saved_food}
    return render(request, 'calory/app.html', context)


# def delete_consume(request, pk):
#     consume = get_object_or_404(Consume, pk=pk, user=request.user)
#     consume.delete()
#     return redirect('index')

def delete_consume(request, pk):
    consume = get_object_or_404(Consume, pk=pk)

    consume.delete()
    return redirect('tracker')
