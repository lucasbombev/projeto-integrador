from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

def list_livros(request):
    livros = [
        {'id': 1, 'titulo': 'Engenharia de Software', 'autor': 'Sommerville'},
        {'id': 2, 'titulo': 'Fundamentos de S.O', 'autor': 'Tannenbaum'},
        {'id': 3, 'titulo': 'Os 3 Porquinhos', 'autor': 'Joseph Jacobs'},
    ]
    return JsonResponse(livros, safe=False)
