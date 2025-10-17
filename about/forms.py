from django import forms
from .models import AboutSection
from gallery.models import Media


class AboutSectionForm(forms.ModelForm):
    media = forms.ModelMultipleChoiceField(
        queryset=Media.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = AboutSection
        fields = ['section_name', 'section_information', 'media']
        widgets = {
            'section_information': forms.Textarea(attrs={'rows': 6}),
        }
