from django.http import JsonResponse
from .models import Livro, Leitor
from django.views.decorators.csrf import csrf_exempt
import json
import bleach

@csrf_exempt
## CREATE
def criar_livro(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            titulo = bleach.clean(dados.get('titulo', ''), tags=[], attributes={})
            autor = bleach.clean(dados.get('autor', ''), tags=[], attributes={})
            if not titulo or not autor:
                return JsonResponse({'error': 'Título e autor são obrigatórios'}, status=400)
            livro = Livro.objects.create(titulo=titulo, autor=autor)
            return JsonResponse({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor}, status=201)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
        except Exception:
            return JsonResponse({'error': 'Erro interno'}, status=500)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

## READ
from django.http import JsonResponse
from .models import Livro

def listar_livros(request):
    if request.method == 'GET':
        livros = list(Livro.objects.values('id', 'titulo', 'autor'))
        return JsonResponse(livros, safe=False)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def buscar_livro(request, id):
    if request.method == 'GET':
        try:
            livro = Livro.objects.get(pk=id)
            return JsonResponse({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor})
        except Livro.DoesNotExist:
            return JsonResponse({'error': 'Livro não encontrado.'}, status=404)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

## UPDATE

def atualizar_livro(request, id):
    if request.method == 'PUT':
        try:
            dados = json.loads(request.body)
            titulo = dados.get('titulo')
            autor = dados.get('autor')
            if not titulo or not autor:
                return JsonResponse({'error': 'Título e autor são obrigatórios.'}, status=400)
            # Sanitização
            sanitized_titulo = bleach.clean(titulo, tags=[], attributes={})
            sanitized_autor = bleach.clean(autor, tags=[], attributes={})
            livro_atualizado = Livro.objects.filter(pk=id).update(titulo=sanitized_titulo, autor=sanitized_autor)
            if livro_atualizado == 0:
                return JsonResponse({'error': 'Livro não encontrado.'}, status=404)
            return JsonResponse({'message': 'Livro atualizado com sucesso.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

## DELETE
def deletar_livro(request, id):
    if request.method == 'DELETE':
        try:
            livro = Livro.objects.get(pk=id)
            livro.delete()
            return JsonResponse({'message': 'Livro deletado com sucesso.'})
        except Livro.DoesNotExist:
            return JsonResponse({'error': 'Livro não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método não permitido'}, status=405)