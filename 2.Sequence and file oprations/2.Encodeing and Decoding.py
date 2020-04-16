# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:44:09 2020

@author: I340968
"""
import base64
reference_id=input()
if len(reference_id)==12:
    if reference_id.isalnum():
        reference_id_encrypt = base64.b64encode(reference_id.encode())
        print(reference_id_encrypt)
    else:
        print("Reference_id have special character which is not allowed")
else:
    print("Password should be 12 in length")
    

#Enhancemet code:
#================
    
print("Enhancement of previous code")
reference_id1=input()
if len(reference_id1)==12:
    reference_id_encrypt1 = base64.b64encode(reference_id1.encode())
    print(reference_id_encrypt1)
else:
    print("Password should be 12 in length")

print("Please enter Y- to decode, N- if you don't want to decode")
ch=str(input())
if ch=='Y' or ch=='y':
    reference_id_decode=base64.b64decode(reference_id_encrypt1)
    print(reference_id_decode)
elif ch=='N' or ch=='n':
    print("User opted not to decode")
else:
    print("Only Y and N alone premitted, please select one of them")

    