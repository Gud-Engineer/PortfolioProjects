"""
Map Trivia : Name States by identifying map of country, generates list of states needed to learn.
ver 0 : USA
ver 0.1 : India
ver 0.2 : Admin Functionality, Adds ease to map regions on map with keyword "Admin CODE"
ver 0.3 : TODO Add

"""
import turtle

import pandas
import pandas as pd

from configurator import Configurator


# TODO Admin Function : Coordinate fetching
def mapit(country):
    """
    Admin Function that is used for co-ordinate setting
    :param country: Country Code further passed to configurator file that loads appropriate region's list.
    :return: saves a csv file with Region and Co-ordinates(x,y)
    """
    configurator = Configurator(country)
    region = []
    x_cors = []
    y_cors = []

    def get_mouse_click_coor(x, y):
        if configurator.index < len(configurator.cities):
            region.append((configurator.cities[configurator.index]))
            x_cors.append(x)
            y_cors.append(y)
            configurator.next_question()
            screen.update()
        else:
            data = {
                "Region": region,
                "x": x_cors,
                "y": y_cors
            }
            df = pandas.DataFrame(data)
            df.to_csv(f'Auto_Cities_{country}.csv')

    screen.onscreenclick(get_mouse_click_coor)


# TODO : Load Map
screen = turtle.Screen()
screen.title("Map Trivia 🌍")
maps = {"USA": "US_States_Img.gif", "IND": "Indian_States_Img1.gif", "Admin USA": "US_States_Img.gif","Admin IND":"Indian_States_Img1.gif"}
country = screen.textinput(title="Map Selection v0.1", prompt="Select your map (Usa/India)")
screen.addshape(maps[country])
turtle.shape(maps[country])

guessed_regions = []
data = pd.DataFrame()
if country in ["Admin USA","Admin IND"]:
    country_code = country.split()[-1]
    mapit(country_code.upper())
    screen.mainloop()
else:
    data = pd.read_csv(f'Auto_Cities_{country}.csv')
    # print(data.head(5))
    all_regions = data.Region.to_list()
    print(all_regions)

    # print(all_us_states)
    while len(guessed_regions) < len(data):
        answer_state = screen.textinput(title=f'{len(guessed_regions)}/{len(data)} Guessed 🔍',
                                        prompt='Whats another state name?').title()
        # print(answer_state)

        if answer_state == 'Exit':
            missing_states = []
            for state in all_regions:
                if state not in guessed_regions:
                    missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv('Regions_to_Learn.csv')
            break

        if answer_state in all_regions:
            guessed_regions.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            region_data = data[data.Region == answer_state]
            # region_data.x returns pandas series, calling int on single series ele is deprecated
            # sol: access single element using iloc
            t.goto(int(region_data.x.iloc[0]), int(region_data.y.iloc[0]))
            t.write(f'{answer_state}', align='center', font=('Courier', 8, 'normal'))

# coord_fetch
# turtle.onscreenclick(get_coord)
# turtle.mainloop()
# screen.exitonclick()
