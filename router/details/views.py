from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import View
from details.models import Detail


class DetailCreateView(CreateView):
    model = Detail
    fields = 'sapid', 'hostname', 'loopback', 'mac_address'
    success_url = '/'

class DetailUpdateView(UpdateView):
    model = Detail
    fields = 'sapid', 'hostname', 'loopback', 'mac_address'
    success_url = '/'

class DetailListView(ListView):
    model = Detail

    def get_queryset(self):
        return self.model.objects.filter(is_deleted=False)

class DetailDeleteView(View):
    model = Detail

    def get(self, request, pk):
        obj = self.model.objects.get(id=pk)
        obj.deactivate()
        return redirect('/')

