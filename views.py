#-*- coding: utf-8 -*-

from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    output=', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse('Vous regardez la question %s.' %question_id)

def results(request, question_id):
    response='Vous regardez les resultats de la question %s'
    return HttpResponse(response %question_id)
    
def vote(request, question_id):
    return HttpResponse('Vous votez pour la question %s.' %question_id)



