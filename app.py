from flask import Flask, request
from menu import get_menu
from whatsapp import send_buttons, send_message
from config import VERIFY_TOKEN, PORT


app = Flask(__name__)


# Temporary memory for active users
# No database required
user_state = {}



# WhatsApp webhook verification
@app.route("/webhook", methods=["GET"])
def verify():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")


    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge

    return "Verification failed", 403





# Receive WhatsApp messages
@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()


    try:

        message = data["entry"][0]["changes"][0]["value"]["messages"][0]


        phone = message["from"]


        # If user sends normal text
        if message["type"] == "text":

            text = message["text"]["body"].lower()


            if phone not in user_state:

                user_state[phone] = "main"

                menu = get_menu("main")

                send_buttons(phone, menu)


            elif text in ["hi","hello","hey","start"]:

                user_state[phone] = "main"

                menu = get_menu("main")

                send_buttons(phone, menu)


            else:

                send_message(
                    phone,
                    "Please use the buttons below 👇"
                )

                send_buttons(
                    phone,
                    get_menu(user_state[phone])
                )





        # If user clicks button
        elif message["type"] == "interactive":


            button_id = message["interactive"]["button_reply"]["id"]


            user_state[phone] = button_id


            menu = get_menu(button_id)



            send_buttons(
                phone,
                menu
            )



    except Exception as e:

        print("Error:",e)



    return "OK",200





if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=int(PORT)
    )
