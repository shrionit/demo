from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from account.forms import LoginForm, RegisterForm

def register_view(request):
    ctx = {
        "errors": None,
        "error_class": "text-red-600 text-xs pl-1",
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            ctx['errors'] = {}
            for k, v in form.errors.items():
                print(k, v.as_text().split('\n'))
                ctx['errors'][k] = v.as_text().split('\n')
    else:
        form = RegisterForm()
    ctx['form'] = form
    return render(request, 'auth/register.html', ctx)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Incorrect username or password'
    ctx = {
        "form": form,
        "msg": msg,
        "error_class": "font-light text-red-600 text-sm pl-1",
    }
    return render(request, "auth/login.html", ctx)

def logout_view(request):
    logout(request)
    return redirect("Login")