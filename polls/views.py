from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

#from django.template import loader

from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
 #   output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))"""

"""def detail(request, question_id):
    return  HttpResponse("You are looking at question %s." % question_id)""""

def details(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' = question})

def results(request, question_id):
    response = "you are looking at questions of result %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
