**Question 1:** By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Solution:**

By default django signals are executed synchronously.
![image](https://github.com/user-attachments/assets/10a002cc-b28f-4920-af06-fb3ef76ca9a7)

Here,you can see in the logs that the that first the process is started and then entry of user is done,and after that signal is triggered and after that only process is returned and ended, therefore it clearly shows that the process is Synchronous.
You can see the log in ***/api/que1/***.

views.py
```python 
    print("process initiated")  
    old_user=User.objects.all()
    old_user.delete()
    print("User object is to be created...")
    user=User.objects.create_user(username="user1",password="anypass")
    print("Process Ended")  
```

signals.py
```python 
    print("process initiated")  
    old_user=User.objects.all()
    old_user.delete()
    print("User object is to be created...")
    user=User.objects.create_user(username="user1",password="anypass")
    print("Process Ended")  
```


