**Question 3:** By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


**Solution:**

Yes, by default, Django signals run within the same database transaction as the caller. In this case, we started a transaction and it failed, so everything was rolled back, including the signal that was triggered. We had also created an entry in a different table for that instance, but when the transaction failed and was rolled back, that entry was rolled back too, since it was part of the same database transaction.You can see that in log.
![image](https://github.com/user-attachments/assets/2f159d17-4899-4bb6-9392-6fb6a8d5dfba)

You can also see the log in ***/api/que3/***.

views.py
```python 
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
```

signals.py
```python 
    print("Signal started...")
    Message.objects.create(mess=f'Created By the User {instance.username}')
    print("Signal Ended...")
```


