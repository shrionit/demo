from django.shortcuts import redirect, render
nav = [
    "Option0",
    "Profile",
    "Option2",
    "Option3",
    "Option4",
]

def marketview(request):            
    if not request.user.is_authenticated:
        return redirect('Login')
    ctx = {
        "navmenu": nav,
        "currentPage": "Profile"
    }
    return render(request,"market/home.html", ctx)