from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.views import generic
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Count
from .models import Rookie, BlackHandTest, Sith
from .forms import RookieForm, BlackHandTestForm, AddBlackHand

# Create your views here.
def index(request):
    return render(request, 'ordenofthesith/index.html')

class CreateRookie(generic.CreateView):
    form_class = RookieForm
    template_name = 'ordenofthesith/create_rookie.html'

def blackHandTest(request, rookie_id, planet_id):
    rookie = get_object_or_404(Rookie, id=rookie_id)
    questions = get_object_or_404(BlackHandTest, planet_id=planet_id).questions.all()

    if request.method != 'POST':
        form = BlackHandTestForm(rookie=rookie,
                                questions=[(question.id, question.content) for question in questions])
    else:
        form = BlackHandTestForm(data=request.POST,
                                rookie=rookie,
                                questions=[(question.id, question.content) for question in questions])
        if form.is_valid():
            form.save()
            name = rookie.name
            messages.success(request, f'Пользователь {name} зарегистрирован!')
            return HttpResponseRedirect(reverse('ordenofthesith:index'))
    
    context = {'rookie': rookie, 'questions': questions, 'form': form}
    return render(request, 'ordenofthesith/blackhand_test.html', context)

class SithListView(generic.ListView):
    model = Sith
    template_name = 'ordenofthesith/show_sith.html'
    context_object_name = 'sith'

def showRookies(request, sith_id):
    sith = Sith.objects.get(id=sith_id)
    # Первый фильтр с привязкой рекрута к планете, но по заданию сказано показывать всех, поэтому используем второй
    #rookie = Rookie.objects.filter(planet=sith.planet).filter(sith=None)
    rookie = Rookie.objects.filter(sith=None)
    context = {'sith': sith, 'rookie': rookie}
    return render(request, 'ordenofthesith/show_rookies.html', context)

def showAnswers(request, sith_id, rookie_id):
    sith = Sith.objects.get(id=sith_id)
    rookie = Rookie.objects.get(id=rookie_id)
    answers = rookie.answers_set.all()

    if request.method != 'POST':
        form = AddBlackHand()
    else:
        form = AddBlackHand(data=request.POST, initial={'sith': sith, 'rookie': rookie})
        if form.is_valid():
            # Устанавливаем ограничение на кол-во черных рук у одного ситха
            countblock = sith.rookie_set.count()
            if countblock < 3:
                form.save()
                subject = rookie.name
                email = rookie.email
                send_mail(subject, f'{sith} принял вас к себе в черные руки!', 'postlows@gmail.com', [email])
                messages.success(request, f'{subject} был добавлен в черные руки!')
                return HttpResponseRedirect(reverse('ordenofthesith:index'))
            else:
                messages.warning(request, 'Ваш лимит на количество черных рук исчерпан!')
                return HttpResponseRedirect(reverse('ordenofthesith:index'))
    
    context = {'sith': sith, 'rookie': rookie, 'answers': answers, 'form': form}
    return render(request, 'ordenofthesith/show_answers.html', context)

def showSithCount(request):
    # Выводим полный список ситхов с кол-вом черных рук
    sith = Sith.objects.all().annotate(Count('rookie'))
    #sith = get_object_or_404(Sith).annotate(Count('rookie'))
    context = {'sith': sith}
    return render(request, 'ordenofthesith/show_sith_count.html', context)

def sithRookieOne(request):
    # Выводит всех ситхов у которых более 1-ой черной руки
    sith = Sith.objects.annotate(num=Count('rookie')).filter(num__gt=1)
    context = {'sith': sith}
    return render(request, 'ordenofthesith/sith_rookie_one.html', context)