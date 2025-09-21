
#####################################################################

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import sys

from os import system 

system ("cls")

######################################################################

class Programming(QMainWindow):
    def __init__(slycon):
        super().__init__()
        QMainWindow.__init__(slycon)
        slycon.setWindowTitle("They Ball !!!")
        slycon.setGeometry(1500, 40, 350, 680)
        slycon.UiComponents()
        slycon.show()

        slycon.setStyleSheet("""background-color: black;
                             color: azure;
                             font-size:20pt;
                             """)
        
#####################################################################

    def UiComponents(slycon):
        slycon.label=QLabel(slycon)
        slycon.label.setGeometry(5, 180, 335, 70)
        slycon.label.setWordWrap(True)
        slycon.label.setStyleSheet("""
                                background: black;
                                font-size:60px""")
        
        slycon.label.setAlignment(Qt.AlignRight)
        slycon.setFont(QFont("Calibri", 70))

#####################################################################

        AC=QPushButton("AC", slycon)
        AC.setGeometry(25, 260, 70, 70)
        AC.setStyleSheet("""background-color: rgb(147, 145, 141);
                         color: azure;
                         border-radius: 35px;""")
        
        indication=QPushButton("+/-", slycon)
        indication.setGeometry(105, 260, 70, 70)
        indication.setStyleSheet("""background-color: rgb(147, 145, 141);
                                 color: azure;
                                 border-radius: 35px;""")
        
        percent=QPushButton("%", slycon)
        percent.setGeometry(185, 260, 70, 70)
        percent.setStyleSheet("""background-color: rgb(147, 145, 141);
                              color: azure;
                              border-radius: 35px;""")
        
        stay=QPushButton("/", slycon)
        stay.setGeometry(265, 260, 70, 70)
        stay.setStyleSheet("""background-color: rgb(208, 137, 13);
                           color: azure;
                           border-radius: 35px;""")
        
######################################################################

        seven=QPushButton("7", slycon)
        seven.setGeometry(25, 340, 70, 70)
        seven.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        eight=QPushButton("8", slycon)
        eight.setGeometry(105, 340, 70, 70)
        eight.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        nine=QPushButton("9", slycon)
        nine.setGeometry(185, 340, 70, 70)
        nine.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        multiplication=QPushButton("*", slycon)
        multiplication.setGeometry(265, 340, 70, 70)
        multiplication.setStyleSheet("""background-color: rgb(208, 137, 13);
                           color: azure;
                           border-radius: 35px;""")
        
#######################################################################

        
        four=QPushButton("4", slycon)
        four.setGeometry(25, 415, 70, 70)
        four.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        five=QPushButton("5", slycon)
        five.setGeometry(105, 415, 70, 70)
        five.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        six=QPushButton("6", slycon)
        six.setGeometry(185, 415, 70, 70)
        six.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        minus=QPushButton("-", slycon)
        minus.setGeometry(265, 415, 70, 70)
        minus.setStyleSheet("""background-color: rgb(208, 137, 13);
                           color: azure;
                           border-radius: 35px;""")
        
#########################################################################

        one=QPushButton("1", slycon)
        one.setGeometry(25, 490, 70, 70)
        one.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")

        two=QPushButton("4", slycon)
        two.setGeometry(105, 490, 70, 70)
        two.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        three=QPushButton("3", slycon)
        three.setGeometry(185, 490, 70, 70)
        three.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        plus=QPushButton("+", slycon)
        plus.setGeometry(265, 490, 70, 70)
        plus.setStyleSheet("""background-color: rgb(208, 137, 13);
                           color: azure;
                           border-radius: 35px;""")
        
########################################################################

        
        zero=QPushButton("0              ", slycon)
        zero.setGeometry(25, 565, 150, 70)
        zero.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        
        dot=QPushButton(".", slycon)
        dot.setGeometry(185, 565, 70, 70)
        dot.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
                        
        equal=QPushButton("=", slycon)
        equal.setGeometry(265, 565, 70, 70)
        equal.setStyleSheet("""background-color: rgb(58, 57, 55);
                           color: azure;
                           border-radius: 35px;""")
        

#########################################################################
        
        AC.clicked.connect(slycon.Mc_Din11_AC)
        indication.clicked.connect(slycon.Mc_Din11_indication)
        percent.clicked.connect(slycon.Mc_Din11_percent)
        stay.clicked.connect(slycon.Mc_Din11_stay)
        seven.clicked.connect(slycon.Mc_Din11_7)
        eight.clicked.connect(slycon.Mc_Din11_8)
        nine.clicked.connect(slycon.Mc_Din11_9)
        multiplication.clicked.connect(slycon.Mc_Din11_multiplication)
        four.clicked.connect(slycon.Mc_Din11_4)
        five.clicked.connect(slycon.Mc_Din11_5)
        six.clicked.connect(slycon.Mc_Din11_6)
        minus.clicked.connect(slycon.Mc_Din11_minus)
        one.clicked.connect(slycon.Mc_Din11_1)
        two.clicked.connect(slycon.Mc_Din11_2)
        three.clicked.connect(slycon.Mc_Din11_3)
        plus.clicked.connect(slycon.Mc_Din11_plus)
        zero.clicked.connect(slycon.Mc_Din11_0)
        dot.clicked.connect(slycon.Mc_Din11_dot)
        equal.clicked.connect(slycon.Mc_Din11_equal)


######################################################################

    
    def Mc_Din11_AC(slycon):
        text=slycon.label.setText("")

    def Mc_Din11_indication(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "+/-")

    def Mc_Din11_percent(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "%")

    def Mc_Din11_stay(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "/")

    def Mc_Din11_7 (slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "7")

    def Mc_Din11_8(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "8")

    def Mc_Din11_9(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "9")

    def Mc_Din11_multiplication(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "*")

    def Mc_Din11_4(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "4")

    def Mc_Din11_5(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "5")

    def Mc_Din11_6(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "6")

    def Mc_Din11_minus(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "-")

    def Mc_Din11_1(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "1")

    def Mc_Din11_2(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "2")

    def Mc_Din11_3(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "3")

    def Mc_Din11_plus(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "+")

    def Mc_Din11_0(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + "0")

    def Mc_Din11_dot(slycon):
        text=slycon.label.text()
        slycon.label.setText(text + ".")

    def Mc_Din11_equal(slycon):
        equal=slycon.label.text()
        try:
            answer=eval(equal)
            slycon.label.setText(str(answer))

        except:
            slycon.label.setText("Alert!")


####################################################################            



app=QApplication([])
programming=Programming()
sys.exit(app.exec_())





















