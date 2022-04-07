from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import F
from django.http import HttpResponseBadRequest

from .models import Order
from .forms import OrderForm


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('created_at', 'plated_end_at').all()
        return render(request, 'order/order_list.html', context={'orders': orders})


class FilteredOrderList(View):
    def get(self, request):
        orders = Order.objects \
            .filter(plated_end_at__gte=F('end_at')) \
            .order_by('created_at', 'plated_end_at') \
            .all()
        return render(request, 'order/order_list.html', context={'orders': orders})


class OrderFormView(View):
    def get(self, request, order_id=None):
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            form = OrderForm(instance=order)
        else:
            form = OrderForm()

        return render(request, 'order/order_form.html', context={'form': form})

    def post(self, request, order_id=None):
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            form = OrderForm(request.POST, instance=order)
        else:
            form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('order_list')

        return HttpResponseBadRequest('Bad Request')


class DeleteOrderView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return redirect('order_list')
