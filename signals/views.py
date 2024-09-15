from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import threading
from django.db import transaction,IntegrityError
from .models import Message
# Create your views here.

def que1(request):
    print("process initiated")
    old_user=User.objects.all()
    old_user.delete()
    print("User object is to be created...")
    user=User.objects.create_user(username="user1",password="anypass")
    print("Process Ended")
    return HttpResponse("Here,you can see in the logs that the that first the process is started and then entry of user is done,and after that signal is triggered and after that only process is returned and ended, therefore it clearly shows that the process is <b>Synchronous</b>.")


def que2(request):
    print("Process initiated")
    old_user=User.objects.all()
    old_user.delete()
    print(f"Process running in thread: {threading.current_thread().name}")
    user=User.objects.create_user(username="user1",password="anypass")
    print("Process Ended")
    return HttpResponse("Yes,Django Signal run in the same thread as the caller as you can see in the log(console) that the thread of process and signal is same. But if you want to change you can manually change the thread of signal to run in the different thread from the process.")


def que3(request):
    print(f"Entries of message before process: {Message.objects.count()}")
    print("Process Initiated...")
    old_user=User.objects.all()
    old_user.delete()
    try:
        with transaction.atomic():
            user=User.objects.create_user(username="user1",password="anypass")
            print(f"Entries of message table during transaction: {Message.objects.count()}")

            raise IntegrityError("Forcing rollback")
    except:
        print("Transaction Rolled Back")
    
    print(f"Entries of message after transaction failed:{Message.objects.count()}")
    print("Process Ended...")
    return HttpResponse("Yes, by default, Django signals run within the same database transaction as the caller. In this case, we started a transaction and it failed, so everything was rolled back, including the signal that was triggered. We had also created an entry in a different table for that instance, but when the transaction failed and was rolled back, that entry was rolled back too, since it was part of the same database transaction.")

