from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import User

import threading

from .models import Message

@receiver(post_save,sender=User)
def signalSyncHandler(sender,instance,**kwaargs):
    print("Signal started...")
    print(f"Signal running in thread: {threading.current_thread().name}")

    Message.objects.create(mess=f'Created By the User {instance.username}')
    print("Signal Ended...")