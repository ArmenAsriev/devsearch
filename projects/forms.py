from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Projects, Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']

        labels = {
            'body': 'Add a comment to your vote',
            'value': 'Place your vote'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'image', 'description',
                  'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
