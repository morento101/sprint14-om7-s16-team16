from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from order.models import Order

# Create your views here.


def show_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users.html', {'users': users})


def show_user_by_id(request, id):
    user = CustomUser.objects.get(id=id)
    orders_by_user = Order.objects.filter(user=user)
    return render(request, 'user_by_id.html', {'orders_by_user': orders_by_user, 'user': user})


def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        CustomUser.create(email, password, fname, mname, lname)
        return redirect('all_users')
    return render(request, 'create_user.html', {})


def delete_user(request, id):
    CustomUser.delete_by_id(id)
    return redirect('all_users')


def update_user(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        # email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        role = request.POST.get('role')
        user.update(fname, lname, mname, password, role)
        return redirect('all_users')
    return render(request, 'update_user.html', {'user': user})