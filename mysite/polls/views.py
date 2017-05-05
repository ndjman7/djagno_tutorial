from django.shortcuts import render
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    pass

def results(request, question_id):
    pass

def vote(request, question_id):
    pass
