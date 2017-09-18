#Created by: Alireza Teimoori
#Created on: 18 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit 0-05
#This program solves the problem of Area and perimeter

import ui


def show_answer(sender):
    #show the answer
    
    view['area_lable'].text = ("Area = " + str(2*(2+5)) + " cm^2")
    view['perimeter_lable'].text = ("Perimeter = " + str(5*2) + " cm^2")

view = ui.load_view()
view.present('sheet')
