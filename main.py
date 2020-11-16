from PyQt5 import QtWidgets
from script import Ui_MainWindow
import os, subprocess, sys
import multiprocessing
from threading import Timer
#cmd = os.system("wp id")



output = int(subprocess.check_output("wp id", shell=True)) # Постоянный запрос wp id поступает в переменную и отоброжается в функциях, впихнул в integer потому что на выходе дает не допустимые символы 

#if output == "b" and "''":
#del output[b:'']

#command = (f"wp run mpv --wid={output} fair.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")

#output = str.split("'")[2]

#print(output)
#print(command)

#class optimization()




class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.run4Wallpaper) #смена обоев 1   
        self.ui.pushButton_2.clicked.connect(self.run6Wallpaper)
        self.ui.pushButton.clicked.connect(self.closeWallpaper) 
        self.ui.pushButton_4.clicked.connect(self.run3Wallpaper) 
        self.ui.pushButton_5.clicked.connect(self.run4Wallpaper)
        self.ui.pushButton_7.clicked.connect(self.run5Wallpaper)
        self.ui.pushButton_3.clicked.connect(self.closeWallpaper)
        self.ui.pushButton_5.clicked.connect(self.closeWallpaper)
        self.ui.pushButton_10.clicked.connect(self.closeWallpaper)
        self.ui.pushButton_6.clicked.connect(self.runWallpaper)
        self.ui.pushButton_11.clicked.connect(self.closeWallpaper) # Кнопка отвечает за закрытия процесса mpv        
        self.ui.pushButton_9.clicked.connect(self.run2wallpaper) 
        self.ui.pushButton_8.clicked.connect(self.closeWallpaper) 
        #self.ui.pushButton_12.clicked.connect(self.getfile) # Добавление обоев
        
    def runWallpaper(self):
        start_enjine = os.system(f"wp run mpv --wid={output} test1.wmv --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio ") #cmd команда отвечающая за смену обоев
    
    def closeWallpaper(self):
        close = os.system("taskkill /IM mpv.exe /F") # Это функция остонавливает процесс mpv для смены других обоев
    
    def run6Wallpaper(self):
    	start_4_enjine = os.system(f"wp run mpv --wid={output} fair.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")

    def run2wallpaper(self):
        start_2_enjine = os.system(f"wp run mpv --wid={output} Test.wmv --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")    

    def run3Wallpaper(self):
        start_3_enjine = os.system(f"wp run mpv --wid={output} forest.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")


    def run4Wallpaper(self):
        start_3_enjine = os.system(f"wp run mpv --wid={output} ok.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")


    def run5Wallpaper(self):
        start_3_enjine = os.system(f"wp run mpv --wid={output} Blue-Waves.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec_())

