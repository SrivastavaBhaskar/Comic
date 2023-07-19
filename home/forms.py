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

    def save(self, comic_id, commit=True, *args, **kwargs):
        chapter = super(AddChapterForm, self).save(commit=False, *args, **kwargs)
        comic = Comic.objects.get(id=comic_id)
        chapter.comic = comic
        chapter.chapter_number = comic.chapters.all().count() + 1
        if commit:
            chapter.save()
        return chapter

class AddPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['image']

    def save(self, chapter_id, commit=True, *args, **kwargs):
        page = super(AddPageForm, self).save(commit=False, *args, **kwargs)
        chapter = Chapter.objects.get(id=chapter_id)
        page.chapter = chapter
        page.page_number = chapter.pages.all().count() + 1
        if commit:
            page.save()
        return page