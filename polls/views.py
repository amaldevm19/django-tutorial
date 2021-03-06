from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import urlparse, parse_qs
from .models import Question, Choice
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views.generic import ListView, DetailView

# def index(request):
#     #Question(question_text ="Added", pub_date=timezone.now()).save()
    
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #output = ', '.join([q.question_text for q in latest_question_list])

#     #template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     #return HttpResponse (template.render(context, request))

#     return render(request,'polls/index.html',context)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(DetailView):
    #try:
        #question = Question.objects.get(pk = question_id)
        #print(question)
        
    #except Question.DoesNoteExit:
        #raise Http404('Question does not exist')
    template_name = 'polls/detail.html'
    model = Question
    #question = get_object_or_404(Question, pk = question_id)
    #return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(DetailView):
    template_name = 'polls/results.html'
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message' : ' You did not select a choice'
        })
    else:
        selected_choice.votes = F('votes')+1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
