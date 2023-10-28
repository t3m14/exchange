from django.shortcuts import render, redirect
from user.models import User
# Create your views here.
def exchanging(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        data = {
                    "usd" : user.balance_usd,
                    "rdw" : user.balance_rdw,
                }
        return render(request, "exchanging.html", data)
    else:
        return redirect('/')