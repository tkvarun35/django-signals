**Question 2:** Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


**Solution:**

Yes,Django Signal run in the same thread as the caller.
![image](https://github.com/user-attachments/assets/86304ae2-547a-4bc1-828c-2e3fb3b0393b)

As you can see in the log(console) that the thread of process and signal is same. But if you want to change you can manually change the thread of signal to run in the different thread from the process.
You can see the log in ***/api/que2/***.

views.py
```python 
    print("Process initiated")
    old_user=User.objects.all()
    old_user.delete()
    print(f"Process running in thread: {threading.current_thread().name}")
    user=User.objects.create_user(username="user1",password="anypass")
    print("Process Ended") 
```

signals.py
```python 
    print("Signal started...")
    print(f"Signal running in thread: {threading.current_thread().name}")
    print("Signal Ended...") 
```


