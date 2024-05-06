from turtle import Turtle

POSITION = (0, 0)
CITIES = {
    "USA": ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
            "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
            "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
            "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
            "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
            "Texas",
            "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
            ],
    "IND": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
            "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
            "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
            "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
            "Chandigarh", "Dadra and Nagar", "Daman and Diu", "Delhi", "Lakshadweep", "Pondicherry"
            ]
    }


# CITIES = {
#     "usa": [],
# "india": [],
# }

class Configurator(Turtle):
    def __init__(self, country):
        super().__init__()
        self.index = 0
        self.cities = CITIES[country]
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.color("black")
        self.write(f"{self.cities[self.index]}")

    def next_question(self):
        self.clear()
        self.index += 1
        if self.index < len(self.cities):
            self.write(f"{self.cities[self.index]}")
