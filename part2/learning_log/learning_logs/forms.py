from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:  # 根据哪个模型，哪个字段创建表单
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
