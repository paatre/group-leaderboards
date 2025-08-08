from django import forms
from .models import RunningActivity


class RunningActivityForm(forms.ModelForm):
    class Meta:
        model = RunningActivity
        fields = [
            "activity_date",
            "distance",
            "duration",
            "pace",
            "heart_rate_avg",
            "heart_rate_max",
            "ascent",
            "descent",
        ]
        widgets = {
            "activity_date": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date"}
            ),
            "distance": forms.NumberInput(
                attrs={"placeholder": "42.20 (km)", "step": "0.01", "min": "0"}
            ),
            "duration": forms.TextInput(attrs={"placeholder": "HH:MM:SS"}),
            "pace": forms.TextInput(attrs={"placeholder": "MM:SS"}),
        }
