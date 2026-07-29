MENUS = {

"main": {
"text": "👋 Welcome to ABC Electronics\n\nChoose an option:",
"buttons":[
("🛒 Products","products"),
("🔧 Repair","repair"),
("📞 Contact","contact")
]
},


"products":{
"text":"Select product category:",
"buttons":[
("📱 Mobiles","mobiles"),
("💻 Laptops","laptops"),
("⬅ Back","main")
]
},


"mobiles":{
"text":"Choose mobile brand:",
"buttons":[
("Samsung","samsung"),
("Apple","apple"),
("⬅ Back","products")
]
},


"repair":{
"text":"Choose repair service:",
"buttons":[
("Mobile Repair","mobile_repair"),
("Laptop Repair","laptop_repair"),
("⬅ Back","main")
]
},


"contact":{
"text":"Contact us:\n📞 9876543210",
"buttons":[
("⬅ Back","main")
]
}

}



def get_menu(menu_id):

    return MENUS.get(menu_id, MENUS["main"])
