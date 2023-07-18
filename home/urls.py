from django.urls import path
from django.conf.urls.static import static
from Comics import settings


from home.views import (
    home_view,
    add_comic_view,
    comic_details_view,
    add_comic_chapter_view,
    read_comic_chapter_view,
    add_pages_to_chapter_view
)


urlpatterns = [
    path('', home_view, name='home'),
    path('addComic/', add_comic_view, name='add-comic'),
    path('comicDetails/<int:id>', comic_details_view, name='view-comic'),
    path('comicDetails/<int:id>/addChapter', add_comic_chapter_view, name='add-comic-chapter'),
    path('comicDetails/<int:comicid>/chapter/<int:chapterid>/addPages', add_pages_to_chapter_view, name='add-pages'),
    path('comicDetails/<int:comicid>/readChapter/<int:chapterid>', read_comic_chapter_view, name='read-chapter'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
