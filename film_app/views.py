from django.shortcuts import render, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from film_app.forms import AddDirectorForm, AddFilmForm
from film_app.models import Film, Director


def index(request):
    return render(request, 'film_app/index.html')


def home(request):
    films = Film.objects.all()
    return render(request, 'film_app/homepage.html', {'films': films})


class AddFilm(CreateView):
    form_class = AddFilmForm
    template_name = 'film_app/add_film.html'
    success_url = "/homepage"


class AddDirector(CreateView):
    form_class = AddDirectorForm
    template_name = 'film_app/add_director.html'
    success_url = "/homepage"


class FilmView(DetailView):

    model = Film
    template_name = 'film_app/film_details.html'


class EditFilm(UpdateView):

    template_name = 'film_app/add_film.html'
    success_url = '/homepage'
    form_class = AddFilmForm


    def get_object(self, queryset=None):
        return Film.objects.get(pk=self.kwargs['pk'])


class EditDirector(UpdateView):

    template_name = 'film_app/add_director.html'
    success_url = '/homepage'
    form_class = AddDirectorForm


    def get_object(self, queryset=None):
        return Director.objects.get(pk=self.kwargs['pk'])