from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ContactForms
from .models import Aboutus, Menu, Team, Testimonial, Menu2, Menu3


# from .forms import ContactForms

def about(request):
    about = Aboutus.objects.all()
    context = {
        "about": about
    }
    return render(request, "about.html", context=context)


def contact(request):
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    context = {
        "form": form,
    }
    return render(request, 'contact.html', context=context)


def index(request):
    about = Aboutus.objects.all()
    menu = Menu.objects.all()
    menu2 = Menu2.objects.all()
    menu3 = Menu3.objects.all()
    team = Team.objects.all()
    testi = Testimonial.objects.all()
    context = {
        "about": about,
        "menu": menu,
        "menu2": menu2,
        "menu3": menu3,
        "team": team,
        "testi": testi
    }
    return render(request, "index.html", context=context)


def menu(request):
    menu = Menu.objects.all()
    menu2 = Menu2.objects.all()
    menu3 = Menu3.objects.all()
    context = {
        "menu": menu,
        "menu2": menu2,
        "menu3": menu3,

    }
    return render(request, "menu.html", context=context)


def service(request):
    context = {

    }
    return render(request, "service.html", context=context)


def team(request):
    team = Team.objects.all()
    context = {
        "team": team

    }
    return render(request, "team.html", context=context)


def testimonial(request):
    testi = Testimonial.objects.all()
    context = {
        "testi": testi
    }
    return render(request, "testimonial.html", context=context)

def menuDetail(request, menu):
    men = get_object_or_404(Menu, slug=menu)
    context = {
        "men": men
    }
    return render(request, "menuDetail.html", context=context)

def menu2Detail(request, menu2):
    men2 = get_object_or_404(Menu2, slug=menu2)
    context = {
        "men2": men2
    }
    return render(request, "menu2Detail.html", context=context)

def menu3Detail(request, menu3):
    men3 = get_object_or_404(Menu3, slug=menu3)
    context = {
        "men3": men3
    }
    return render(request, "menu3Detail.html", context=context)

def teamDetail(request, team):
    tea = get_object_or_404(Team, slug=team)
    context = {
        "tea": tea
    }
    return render(request, "teamDetail.html", context=context)

def testiDetail(request, testi):
    testi = get_object_or_404(Testimonial, slug=testi)
    context = {
        "testi": testi
    }
    return render(request, "testiDetail.html", context=context)

class MenuCreateView(CreateView):
    name = Menu
    template_name = "menuCreate.html"
    fields = ('name', 'price', 'bio', 'img', 'slug')
class MenuUpdateView(UpdateView):
    name = Menu
    fields = ("name", "price", "bio", "img", "slug")
    template_name = 'menuEdit.html'


class MenuDeleteView(DeleteView):
    name = Menu
    template_name = "menuDelete.html"
    success_url = reverse_lazy('index')
