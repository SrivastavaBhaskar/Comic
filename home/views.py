from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from home.models import Comic
from home.forms import AddComicForm, RatingForm, AddChapterForm, AddPageForm
# Create your views here.

def home_view(request):
    context = {}
    comics = Comic.objects.all()
    p = Paginator(comics, 10)
    comics = p.get_page(1)
    context['comics'] = comics
    return render(request, 'home/home.html', context=context)

@login_required
def add_comic_view(request):
    context = {}
    form = AddComicForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(home_view)
    context['form'] = form
    return render(request, 'home/addComic.html', context=context)


def comic_details_view(request, id=None):
    context = {}
    form = RatingForm(request.POST or None)
    if not id:
        return redirect(home_view)
    else:
        comic = Comic.objects.get(id=id)
        chapters = comic.chapters.all()
        context['comic'] = comic
        context['chapters'] = chapters
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            comic.total_reviews = comic.total_reviews + 1
            comic.rating = ((comic.rating * (comic.total_reviews-1)) + int(rating)) / comic.total_reviews
            comic.save()
            form = RatingForm()
        context['form'] = form
    return render(request, 'home/comicDetails.html', context=context)

@login_required
def add_comic_chapter_view(request, id=None):
    context = {}
    if not id:
        return redirect(home_view)
    chapterform = AddChapterForm(request.POST or None)
    pageform = AddPageForm(request.POST or None, request.FILES or None)
    if chapterform.is_valid() and pageform.is_valid():
        chapter = chapterform.save(comic_id=id)
        pageform.save(chapter_id=chapter.id)
        return redirect(home_view)
    context['chapterform'] = chapterform
    context['pageform'] = pageform
    return render(request, 'home/addComicChapter.html', context=context)

@login_required
def add_pages_to_chapter_view(request, comicid=None, chapterid=None):
    context = {}
    number_of_pages = int(request.GET.get("number_of_pages")) or None
    AddPageFormset = formset_factory(AddPageForm, extra=number_of_pages)
    formset = AddPageFormset(request.POST or None, request.FILES or None)
    if formset.is_valid():
        for form in formset:
            form.save(chapterid)
    context['formset'] = formset
    return render(request, 'home/addChapterPages.html', context=context)

def read_comic_chapter_view(request, comicid=None, chapterid=None):
    context = {}
    if not comicid or not chapterid:
        return redirect(home_view)
    else:
        comic = Comic.objects.get(id=comicid)
        chapter = comic.chapters.get(id=chapterid)
        pages = chapter.pages.all()
        if chapter == comic.chapters.last():
            context['last_chapter'] = True
        else:
            context['next_chapter'] = comic.chapters.get(chapter_number=chapter.chapter_number+1).id
        if chapter == comic.chapters.first():
            context['first_chapter'] = True
        else:
            context['previous_chapter'] = comic.chapters.get(chapter_number=chapter.chapter_number-1).id
        context['comic'] = comic
        context['chapter'] = chapter
        context['pages'] = pages
    return render(request, 'home/comicChapter.html', context=context)

