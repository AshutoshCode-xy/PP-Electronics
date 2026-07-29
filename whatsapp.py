import requests
from config import ACCESS_TOKEN, PHONE_NUMBER_ID



def send_message(number,text):

    url=f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"


    headers={
        "Authorization":f"Bearer {ACCESS_TOKEN}",
        "Content-Type":"application/json"
    }


    data={

    "messaging_product":"whatsapp",

    "to":number,

    "type":"text",

    "text":{
        "body":text
    }

    }


    response=requests.post(
        url,
        headers=headers,
        json=data
    )


    return response.json()





def send_buttons(number,menu):

    url=f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"


    headers={
        "Authorization":f"Bearer {ACCESS_TOKEN}",
        "Content-Type":"application/json"
    }


    buttons=[]


    for title,id in menu["buttons"]:

        buttons.append({

            "type":"reply",

            "reply":{
                "id":id,
                "title":title
            }

        })



    data={

    "messaging_product":"whatsapp",

    "to":number,

    "type":"interactive",

    "interactive":{

        "type":"button",

        "body":{
            "text":menu["text"]
        },

        "action":{
            "buttons":buttons
        }

    }

    }


    return requests.post(
        url,
        headers=headers,
        json=data
    ).json()
