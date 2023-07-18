from django import forms
from home.models import Chapter, Comic, Page

class AddComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['name', 'image']

class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        choices=[
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5)
        ],
        widget=forms.RadioSelect()
    )
    
class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name']

class AddPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['image']