import os

class Greeter:
    def greet(self):
        print("hi")

def hello_world():
    message="hello, world!"
    greeter=Greeter()
    greet_func = getattr(greeter,"greet")
    greet_func()

if __name__=="__main__" :
    hello_world()


''':cvar
Running this code gives :

(base) C:\Users\i340968\Downloads\test\pytest\General>vulture vlture.py
C:\Users\i340968\Downloads\test\pytest\General\vlture.py:1: unused import 'os' (90% confidence)
C:\Users\i340968\Downloads\test\pytest\General\vlture.py:8: unused variable 'message' (60% confidence)



'''