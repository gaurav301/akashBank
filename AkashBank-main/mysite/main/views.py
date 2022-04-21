from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponsePermanentRedirect
from .models import Customers,Transfers
from django.views.decorators.cache import cache_control
import datetime

# Create your views here.

sender_id=1000
receiver_id=1000
transfer_amount=0

def index(response):
    return render(response,"main/homepage.html",{})

def sendlist(response):
    cust_list=Customers.objects.all()
    return render(response,"main/senderpage.html",{"cust_list":cust_list})

def transfer(response,id):
    global sender_id
    global transfer_amount
    sender_id=id
    sender=Customers.objects.get(cust_id=sender_id)
    if (response.method == "POST"):
        print(response.POST)
        if (response.POST.get('transfer')):
            transfer_amount=(int)(response.POST.get('amount'))
            print(transfer_amount)
            return HttpResponseRedirect("/receivelist")
    return render(response,"main/transferpage.html",{"sender": sender})

def receivelist(response):
    global sender_id
    sender=Customers.objects.get(cust_id=sender_id)
    cust_list=Customers.objects.all()
    return render(response,"main/receiverpage.html",{"sender": sender,"cust_list": cust_list})

def confirm(response,id_receive):
    global receiver_id
    global sender_id
    global transfer_amount
    receiver_id=id_receive
    receiver=Customers.objects.get(cust_id=receiver_id)
    sender=Customers.objects.get(cust_id=sender_id)
    if (response.method == "POST"):
        print(response.POST)
        if (response.POST.get('confirm')):
            print(sender.curr_balance)
            print(transfer_amount)
            sender.curr_balance = sender.curr_balance-transfer_amount
            print(sender.curr_balance)
            receiver.curr_balance = receiver.curr_balance+transfer_amount
            sender.save()
            receiver.save()
            creditor=Transfers(sender_id=Customers.objects.get(cust_id=sender.cust_id), receiver_id=Customers.objects.get(cust_id=receiver.cust_id), sender_name=sender.cust_name, receiver_name=receiver.cust_name, date_of_transfer=datetime.datetime.now(), amount=transfer_amount, credit=True)
            creditor.save()
            debitor=Transfers(sender_id=Customers.objects.get(cust_id=sender.cust_id), receiver_id=Customers.objects.get(cust_id=receiver.cust_id), sender_name=sender.cust_name, receiver_name=receiver.cust_name, date_of_transfer=datetime.datetime.now(), amount=transfer_amount, credit=False)
            debitor.save()
            return HttpResponsePermanentRedirect("/success")
    return render(response,"main/confirmpage.html",{"sender": sender,"receiver": receiver})

def success(response):
    cust_list=Customers.objects.all()
    return render(response,"main/successpage.html",{"cust_list": cust_list})

def history(response,id_history):
    cust=Customers.objects.get(cust_id=id_history)
    credits=cust.sender_set.all()
    credits=credits[::2]
    debits=cust.receiver_set.all()
    debits=debits[::2]
    for item in credits:
        print(item.receiver_name)
    return render(response,"main/historypage.html",{"cust_name":cust.cust_name, "credits":credits, "debits":debits})