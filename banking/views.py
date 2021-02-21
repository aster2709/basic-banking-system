from django.shortcuts import render, redirect
from .models import Customer, Transaction
from .forms import FromForm,ToForm,AmountForm
from django.contrib import messages

# Create your views here.




def index(request):
    return render(request, 'banking/index.html')


def customer(request):
    a = [x for x in Customer.objects.all()]
    return render(request, 'banking/customer.html', {'customers': a})


def transfer(request):
    if request.method == 'POST':
        form1, form2, form3 = FromForm(request.POST), AmountForm(request.POST), ToForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            name1 = form1.cleaned_data['name1']
            name2 = form3.cleaned_data['name2']
            amount = form2.cleaned_data['amount']
            print(name1,amount,name2)
            b = Customer.objects.get(pk=int(name1)+1)
            c = Customer.objects.get(pk=int(name2)+1)
            if b.balance-amount<0:
                messages.warning(request, f'balance not sufficient on {b}')
            else:
                b.balance -= amount
                c.balance += amount
                messages.success(request, f'Transaction completed successfully')
                b.save()
                c.save()
                Transaction.objects.create(from_cust=b,to_cust=c,amount=amount)
            return redirect('transfer')
    else:
        form1, form2, form3 = FromForm(), AmountForm(), ToForm()
    return render(request, 'banking/transfer.html', {'form1': form1, 'form2': form2, 'form3': form3})

def log(request):
    log = [x for x in Transaction.objects.all()]
    return render(request, 'banking/log.html', {'logs':log})


def detail(request, customer_id):
    cust = Customer.objects.get(pk=int(customer_id))
    return render(request,  'banking/detail.html', {'customer':cust})
