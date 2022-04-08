from django.shortcuts import render, redirect
from .models import CustomUser
from order.models import Order
from .forms import UserForm
from django.shortcuts import get_object_or_404


def show_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'user/users.html', {'users': users})


def show_user_by_id(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    orders_by_user = Order.objects.filter(user=user)
    return render(request, 'user/user_by_id.html', {'orders_by_user': orders_by_user, 'user': user})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        return render(request, 'user/create_user.html', {'form': form})

    else:
        form = UserForm()

    return render(request, 'user/create_user.html', {'form': form})


def delete_user(request, user_id):
    CustomUser.delete_by_id(user_id)
    return redirect('all_users')


def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        return render(request, 'user/update_user.html', {'form': form})

    else:
        form = UserForm(instance=user)

    return render(request, 'user/update_user.html', {'form': form})
