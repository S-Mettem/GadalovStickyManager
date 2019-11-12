from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Sticky
from . import forms


# Create your views here.
class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def index(request):
    stickys = Sticky.objects.order_by('-date_added')
    context = {'stickys': stickys}
    return render(request, 'index.html', context)


def my_sticky(request, user_name):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:
        y_sticky = Sticky.objects.filter(user=user).order_by('-favorite')
        context = {'stickys': y_sticky, 'user': user}
        return render(request, 'my_sticky.html', context)
    else:
        return redirect('mainApp:404')


def view_sticky(request, user_name, sticky_id):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:
        y_sticky = Sticky.objects.get(uuidu=sticky_id)
        context = {'sticky': y_sticky, 'user': user}
        return render(request, 'sticky.html', context)
    else:
        return redirect('mainApp:404')


def all_view_sticky(request, sticky_id):
    y_sticky = Sticky.objects.get(uuidu=sticky_id)
    context = {'sticky': y_sticky}
    return render(request, 'sticky_for_all.html', context)


def create_sticky(request, user_name):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:
        if request.method != 'POST':
            form = forms.StickyCreationForm
        else:
            form = forms.StickyCreationForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('mainApp:my_sticky', user_name=user.username)
            context = {'form': form, 'user': user}
            return render(request, 'create_sticky.html', context)

    else:
        return redirect('mainApp:404')


def edit_sticky(request, user_name, sticky_id):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:
        sticky = Sticky.objects.get(uuidu=sticky_id)

        if request.method == 'POST':
            form = forms.StickyCreationForm(request.POST, instance=sticky)

            if form.is_valid():
                form.save()
                return redirect('mainApp:sticky', user_name=user.username,
                                sticky_id=sticky.uuidu)

            else:
                context = {'user': user, 'sticky': sticky, 'form': form}
                return render(request, 'edit_sticky.html', context)

        else:
            form = forms.StickyCreationForm(instance=sticky)
            context = {'user': user, 'sticky': sticky, 'form': form}
            return render(request, 'edit_sticky.html', context)
    else:
        return redirect('mainApp:404')


def delete_sticky(request, user_name, sticky_id):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:

        sticky = Sticky.objects.get(uuidu=sticky_id)

        if request.method != 'POST':
            sticky.delete()
            return redirect('mainApp:my_sticky', user_name=user.username)
        else:
            return redirect('mainApp:sticky', user_name=user.username,
                            sticky_id=sticky.uuidu)

    else:
        return redirect('mainApp:404')


def favorite_sticky(request, user_name, sticky_id):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:
        sticky = Sticky.objects.get(uuidu=sticky_id)

        if request.method != 'POST':
            if sticky.favorite is True:
                sticky.favorite = False
            else:
                sticky.favorite = True
                sticky.save()
                return redirect('mainApp:my_sticky', user_name=user.username)
        else:
            return redirect('mainApp:sticky', user_name=user.username,
                            sticky_id=sticky.uuidu)
    else:
        return redirect('mainApp:404')


def public_sticky(request, user_name, sticky_id):
    user = User.objects.get(username=user_name)
    if request.user.is_authenticated and request.user.username == user.username:

        sticky = Sticky.objects.get(uuidu=sticky_id)

        if request.method != 'POST':
            if sticky.is_public is True:
                sticky.is_public = False
            else:
                sticky.is_public = True
                sticky.save()
                return redirect('mainApp:my_sticky', user_name=user.username)
        else:
            return redirect('mainApp:sticky', user_name=user.username,
                            sticky_id=sticky.uuidu)
    else:
        return redirect('mainApp:404')


def page404(request):
    return render(request, '404.html')


def filter(request, pk):
    stickys = Sticky.objects.all()

    if pk == 1:
        stickys = stickys.order_by('-date_added')
    elif pk == 2:
        stickys = stickys.order_by('title')
    elif pk == 3:
        stickys = stickys.order_by('category')
    elif pk == 4:
        stickys = stickys.order_by('faverite')
    else:
        return redirect('mainApp:index')

    context = {'styckys': stickys}
    return render(request, 'index.html', context)
