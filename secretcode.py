import random
import string 
import secrets
print("==============================================================SECRET CODE==============================================================")
s=3
code=input("Enter the String:")
words = code.split(" ")
new=""
print("\nSender side:")
if(len(code)>=3):
              for i in range(len(code)):
                if i==0:
                  new = new + code[i]
              res = ''.join(secrets.choice(string.ascii_lowercase) for x in range(s)) 
              res1 = ''.join(secrets.choice(string.ascii_lowercase) for x in range(s)) 
              print("Encoded string is ->",str(res) +code[1:] + new + str(res1))  
else:
  print("Encoded string is ->",code [::-1])
print("\nReciever side:")
if(len(code)>=3):
  print("Decoded string is ->",code)
else:
  print("Decoded string is ->",code)
print("\n")


# st = input("Enter message:")
# words = st.split(" ")
# s=3
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = ''.join(secrets.choice(string.ascii_lowercase) for x in range(s))
#       r2 = ''.join(secrets.choice(string.ascii_lowercase) for x in range(s)) 
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))