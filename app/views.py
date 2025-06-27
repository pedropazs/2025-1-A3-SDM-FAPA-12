from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def listar_itens(request):
    if request.method == 'GET':
        itens = Item.objects.filter(disponivel=True)
        data = [
            {
                'id': item.id,
                'tipo': item.tipo,
                'descricao': item.descricao,
                'quantidade': item.quantidade,
                'estado_conservacao': item.estado_conservacao,
                'local_retirada': item.local_retirada,
                'contato_doador': item.contato_doador,
            }
            for item in itens
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            tipo = body.get('tipo')
            descricao = body.get('descricao')
            quantidade = body.get('quantidade')
            estado_conservacao = body.get('estado_conservacao')
            local_retirada = body.get('local_retirada')
            contato_doador = body.get('contato_doador')
            # Para simplificação, associando ao primeiro usuário
            doador = User.objects.first()
            item = Item.objects.create(
                tipo=tipo,
                descricao=descricao,
                quantidade=quantidade,
                estado_conservacao=estado_conservacao,
                local_retirada=local_retirada,
                contato_doador=contato_doador,
                doador=doador,
            )
            return JsonResponse({'id': item.id}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item não encontrado'}, status=404)

    if request.method == 'PUT':
        try:
            body = json.loads(request.body.decode('utf-8'))
            item.tipo = body.get('tipo', item.tipo)
            item.descricao = body.get('descricao', item.descricao)
            item.quantidade = body.get('quantidade', item.quantidade)
            item.estado_conservacao = body.get('estado_conservacao', item.estado_conservacao)
            item.local_retirada = body.get('local_retirada', item.local_retirada)
            item.contato_doador = body.get('contato_doador', item.contato_doador)
            item.save()
            return JsonResponse({'id': item.id})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        item.delete()
        return JsonResponse({'success': True})
    elif request.method == 'GET':
        return JsonResponse({
            'id': item.id,
            'tipo': item.tipo,
            'descricao': item.descricao,
            'quantidade': item.quantidade,
            'estado_conservacao': item.estado_conservacao,
            'local_retirada': item.local_retirada,
            'contato_doador': item.contato_doador,
        })
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

def home(request):
    return JsonResponse({"message": "Welcome to the Django backend!"})

def about(request):
    return JsonResponse({"message": "This is the about page."})