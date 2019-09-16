from django.forms import ModelForm
from django import forms
from .models import Rookie, Answers

class RookieForm(ModelForm):
    class Meta:
        model = Rookie
        exclude = ['sith']

class BlackHandTestForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        rookie = kwargs.pop('rookie')
        questions = kwargs.pop('questions')
        super(BlackHandTestForm, self).__init__(*args, **kwargs)
        self.rookie = rookie
        for question in questions:
            self.fields[str(question[0])] = forms.NullBooleanField(label=question[1], required=False)

    def save(self):
        for question_id, content in self.cleaned_data.items():
            Answers.objects.create(questions_id=question_id, rookie=self.rookie, content=content)
    
class AddBlackHand(forms.Form):
    addBlackHand = forms.BooleanField(label='Добавить к себе рекрута?', required=False)

    def save(self):
        if self.cleaned_data['addBlackHand']:
            sith = self.initial['sith']
            rookie = self.initial['rookie']
            rookie.sith = sith
            rookie.save()