from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    # 데이터베이스를 뒤져서 설문목록을 가져와요!
    # ( 테이블명 : polls_question, 클래스명 : Question )
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 데이터 전달용 dictionary를 만들어요.
    context = {'q_list': question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 숫자하나가 question_id로 들어와요! 이숫자는 question id => 설문에대한 PK
    question = get_object_or_404(Question, pk=question_id)
    context = {'selected_question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
    except(KeyError, Choice.DoesNotExist):
        # PK가 없어서 오류가 발생할 경우
        return render(request, 'polls/detail.html', {
            'selected_question': question,
            'error_message': '아무것도 선택하지 않았어요!'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # reverse() => urls.py(URLConf)에 있는 name을 이용해서 url형식으로 변환
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))
        # context = {'selected_question': question}
        # return render(request, 'polls/detail.html', context)
        # return HttpResponse()


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })
