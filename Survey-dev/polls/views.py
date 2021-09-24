from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse
from .models import Question


def listPolls(request, username):
    username = username
    questions = get_list_or_404(Question)
    return render(request, 'polls/polls.html', { 'username':username, 'questions':questions })


def vote(request, username, question_id):
    question = get_object_or_404(Question, pk=question_id)
    options = question.option_set.filter()
    if request.method == "POST":
        selected_option = request.POST['selected_option']
        option = question.option_set.get(pk = selected_option)
        option.votes += 1
        option.save()
        return redirect(reverse('polls:polls', args=(username, )))
    else:
        return render(request, 'polls/vote.html', { 'username' : username , 'question' : question, 'options' : options })
