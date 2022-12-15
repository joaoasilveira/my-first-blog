from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Computador
from django.contrib.auth.decorators import login_required
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404


@login_required
def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        computador = request.POST.getlist('computador')
        tipo = request.POST.getlist('tipo')
        modelo = request.POST.getlist('modelo')
        descricao = request.POST.getlist('descricao')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email,
                                                     'computador': zip(computador, tipo, modelo, descricao)})

        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()

        for computador, tipo, modelo, descricao in zip(computador, tipo, modelo, descricao):
            compu = Computador(computador=computador, tipo=tipo, modelo=modelo, descricao=descricao, cliente=cliente)
            compu.save()

        return redirect('/clientes')


@login_required
def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')

    cliente = Cliente.objects.filter(id=id_cliente)
    computador = Computador.objects.filter(cliente=cliente[0])

    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']

    computador_json = json.loads(serializers.serialize('json', computador))
    computador_json = [{'fields': computador['fields'], 'id': computador['pk']} for computador in computador_json]
    data = {'cliente': cliente_json, 'computador': computador_json, 'cliente_id': cliente_id}

    return JsonResponse(data)


@login_required
def excluir_computador(request, id):
    try:
        computador = Computador.objects.get(id=id)
        computador.delete()
        return redirect(reverse('clientes') + f'?aba=att_cliente&id_cliente={id}')
    except:
        return redirect(reverse('clientes') + f'?aba=att_cliente&id_cliente={id}')



@login_required
@csrf_exempt
def update_computador(request, id):
    nome_computador = request.POST.get('computador')
    tipo = request.POST.get('tipo')
    modelo = request.POST.get('modelo')
    descricao = request.POST.get('descricao')

    computador = Computador.objects.get(id=id)

    computador.computador = nome_computador
    computador.tipo = tipo
    computador.modelo = modelo
    computador.descricao = descricao
    computador.save()

    return redirect('/clientes')


@login_required
def update_cliente(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    cliente = get_object_or_404(Cliente, id=id)  # ERRO 404
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})

