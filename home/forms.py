from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class TaskForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'date-picker', 'type': 'date'}), required=True)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'date-picker', 'type': 'time'}), required=True)
    task = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control add-task-name'}),
                           required=True)

    def clean(self):
        date = self.cleaned_data.get('date')
        time = self.cleaned_data.get('time')
        if date and time:
            task_datetime = timezone.make_aware(timezone.datetime.combine(date, time))
            if task_datetime < timezone.now():
                raise ValidationError('Task date and time cannot be in the past.', code="Invalid time")
