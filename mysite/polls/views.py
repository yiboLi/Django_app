from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list':latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
    
class IndexView(generic.ListView): #display a list of objects
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question':question})
    
class DetailView(generic.DetailView): #display a detail page for a particular type of object
    model = Question #what model it will be acting upon
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request,'polls/results.html', {'question':question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # returns the ID of the selected choice
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question, 'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #the URL to which the user will be redirected 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.