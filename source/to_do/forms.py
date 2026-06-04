from django import forms

from to_do.models import Task

# class TaskForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=True, label="Заголовок")
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "5"}), max_length=1000, label="Описание")
#     detail_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "5"}), max_length=10000, label="Детальное описание")
#     status = forms.ChoiceField(widget=forms.TextInput(attrs={'class': 'form-control'}), choices=Task.Status.choices, label="Статус задачи")
#     date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Дата')

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Заголовок")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "5"}),label="Описание")
    detail_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "5"}),  label="Детальное описание")

    class Meta:
        model = Task
        fields = ['title', 'description', 'detail_description', 'status', 'date']