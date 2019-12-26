from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from film_app import views

film_patterns = ([
    path('', views.index, name='index'),
    path('homepage/', views.home, name='homepage'),
    path('add-film/', views.AddFilm.as_view(), name='add-film'),
    path('add-director/', views.AddDirector.as_view(), name='add-director'),
    path('film/<int:pk>', views.FilmView.as_view(), name='film-details'),
    path('update-film/<int:pk>', views.EditFilm.as_view(), name='update-film'),
    path('update-director/<int:pk>', views.EditDirector.as_view(), name='update-director'),

], 'film')

urlpatterns = [
    path('', include(film_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
