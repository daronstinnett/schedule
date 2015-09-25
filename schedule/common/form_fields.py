from django import forms
from django.forms.widgets import MultiWidget


class DatePairField(forms.MultiValueField):
    widget = MultiWidget
    
    def __init__(self, input_date_formats=None, input_time_formats=None, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.SplitDateTimeField(),
            forms.SplitDateTimeField(),
        )
        MultiValueField.__init__(self, fields, *args, **kwargs)