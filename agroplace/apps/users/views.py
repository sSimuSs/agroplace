from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login as system_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .models import Users


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Name")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    # phone = forms.IntegerField()
    email = forms.EmailField(required=False)

    class Meta:
        model = Users
        fields = ["first_name", "phone", "email", "password1", "password2"]


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    page_title = _("Registration")
    return render(request, 'pages/register.html', {'form': form, 'page_title': page_title})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            system_login(request, user=form.get_user())
            nxt = request.GET.get("next", None)
            if not nxt:
                return redirect('/')
            else:
                return redirect(nxt)
    else:
        form = AuthenticationForm()
    page_title = _("Authorization")
    return render(request, 'pages/login.html', {'form': form, 'page_title': page_title})
