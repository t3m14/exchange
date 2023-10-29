from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.models import User
from withdraw.models import Transaction 
def index(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("exampleInputUsername1")
        email = login_data.get("exampleInputEmail1")
        phone = request.POST.get("exampleInputPhone1")
        password = request.POST.get("inputPassword", False)
        user_type = login_data.get("exampleCheck1")
        wallet = request.POST.get('wallet')
        usd = request.POST.get('usd')
        rdw = request.POST.get('rdw1')
        fee = request.POST.get('fee')
        data = {
            "username" : username,
            "password" : password,
            "user_type" : user_type,
            "email" : email,
            "phone" : phone,
        }
        print(wallet, rdw)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user = User.objects.get(username=username)
                data = {
                    "usd" : user.balance_usd,
                    "rdw" : user.balance_rdw,
                    "user" : username
                }
                return render(request, 'index.html', data)
            else:
                print("no")
                return redirect("/login/")
        
        elif wallet and rdw:
            if request.user.is_authenticated:
                transaction = Transaction.objects.create(
                    wallet = wallet,
                    rdw = rdw
                )
                transaction.save()
                user = User.objects.get(username=request.user)

                data = {
                    "usd" : user.balance_usd,
                    "rdw" : user.balance_rdw,
                    "user" : request.user
                }
                return render(request, 'index.html', data)
            else:
                return redirect("/login/")
        elif usd and rdw and rdw != "NaN" and fee:
            if request.user.is_authenticated:
                admin = User.objects.get(username="admin")
                admin.balance_rdw += float(fee)
                admin.save()
                user = User.objects.get(username=request.user)
                user.balance_usd = float(user.balance_usd) - float(usd)
                user.balance_rdw = float(user.balance_rdw) + float(rdw)
                user.save()
                data = {
                    "usd" : user.balance_usd,
                    "rdw" : user.balance_rdw,
                    "user" : request.user
                }
                return render(request, 'index.html', data)
            else:
                return redirect("/login/")
        
        else:
            return redirect("/")
    else:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            data = {
                "usd" : user.balance_usd,
                "rdw" : user.balance_rdw,
                "user" : request.user
            }
            return render(request, 'index.html', data)
        else:
            return redirect("/login/")
# Create your views here.
