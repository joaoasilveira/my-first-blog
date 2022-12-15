from django.shortcuts import render
from .forms import FormServico
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'clientes.html')

        else:
            return render(request, 'novo_servico.html', {'form': form})


