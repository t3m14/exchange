from django.shortcuts import render, redirect
from user.models import User
# Create your views here.
def withdraw(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        rdw = user.balance_rdw
        user.save()
        data = {
            "rdw" : rdw,
            "user" : request.user
        }
        return render(request, "withdraw.html", data)
    else:
        return redirect("/login/")
