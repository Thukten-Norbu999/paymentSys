from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from useraccount.models import Account
from .models import Transactions

def moneyTransfer(fr, to, amount):

        if fr.balance >= amount:
            fr.balance -= amount
            to.balance += amount
            fr.save()
            to.save()
            return True, "Transfser Done"
        else:
             return False, "Insufficient Balance"

@login_required(login_url='/login/')
def payment(request):
    user = request.user
    frm = Account.objects.get(user=user)
    if request.method == "POST":

        account = frm.account_no
        
        amount = float(request.POST['amt'])
        to_acc = request.POST['to'].strip()
        # tpin = request.POST['tpin']
        remark = request.POST['remark']
        print(to_acc)
        if amount and to_acc and remark:
            to = Account.objects.filter(account_no=to_acc)
            
            
            if to:
                done = moneyTransfer(frm, to[0], amount)
                if done[0]:
                    transaction = Transactions.objects.create(
                    frm = account,
                    amount=amount,
                    to=to_acc,
                    remarks=remark
                )
                    transaction.save()
                    messages.success(request, done[1])
                    return redirect('viewHistory')
                    
                else:
                    messages.error(request, done[1])
            else:
                messages.error(request, 'The account does not exist')
        else:
            if not(amount):
                messages.error(request, 'Enter amount')
            elif not(remark):
                messages.error(request, 'Enter remark')
            else:
                messages.error(request, 'Enter recipient account no')


        # if amount and to_acc and tpin:
        #     to = Account.objects.filter(account_no=to_acc)
        #     if to:
        #         pass

        # else:
        #     if not(amount):
        #         messages.error(request, 'Enter amount')
        #     else:
        #         messages.error(request, 'Enter recipient account no') TODO this is for when account model has tpin field

        content = {
            'account':frm,
        }
        return render(request, 'payment.html', content)
    else:

        content = {
            'account':frm,
        }
        return render(request, 'payment.html', content)


@login_required(login_url='/login/')
def viewHistory(request):
    user = request.user
    
    account = Account.objects.get(user=user)
    
    transactions = Transactions.objects.filter(frm=account.account_no)

    content = {
        'transactions':transactions,

    }
    return render(request, 'history.html', content)


