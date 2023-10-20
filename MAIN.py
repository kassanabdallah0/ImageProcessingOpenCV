import os.path
import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import math
from decimal import *
from PIL import ImageQt
import pandas as pd
from GOTablComment import *
from GoToGraphecomment import *
from GoTorepercomment import *
from mkworddoc import *
from GUI_MAIN import Ui_MainWindow
from fonction_gra import *
from GoTocautationchange import *
from GoToEchelle import *
from GOCLABEL import commentlabel
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QSplashScreen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from Gotocamera import root
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.counter = 0
        self.n = 300
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(20)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.frame = QFrame()
        layout.addWidget(self.frame)
        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        self.labelTitle.resize(self.width() - 40, 130)
        self.labelTitle.move(0, 40)
        self.labelTitle.setPixmap(QPixmap("Photos/icon.png"))
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 30 - 10, 30)
        self.progressBar.move(10, self.labelTitle.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        self.progressBar.setStyleSheet("QProgressBar { "
                                       "background-color: #4084EC;"
                                       "border-radius: 10px;"
                                       "chunk-color: #501BE2;"
                                       "}"
                                       "QProgressBar::chunk {"
                                       "border-radius: 3px;"
                                       "background-color: #5028BD;"
                                       "}")
        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 30)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')

    def loading(self):
        self.progressBar.setValue(self.counter)
        if self.counter >= self.n:
            self.timer.stop()
            self.close()
            time.sleep(1)
            self.myApp = Prog()
            self.myApp.showFullScreen()
        self.counter += 1

# Pour voir les images de fenêtres quadrillage avec la librairie matplotlib.
class DoubleClickLabel_Quadrillage(QtWidgets.QLabel):
    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            if self.pixmap():
                img1 = ImageQt.fromqpixmap(self.pixmap())
                plt.figure('Quadrillage')
                plt.imshow(img1)
                plt.title('Quadrillage')
                plt.show()

class DoubleClickLabel(QtWidgets.QLabel):
    def mouseDoubleClickEvent(self, QMouseEvent):
        # Pour ecrire un commentaire sur la partie gravillonnage.
        if QMouseEvent.button() == Qt.RightButton:
            self.comment = commentlabel() # Pour ouvrir la fenêtre de commentaire pour la partie gravillonnage.
            self.comment.show()
        # Pour voir l'image de fenêtre gravillonnage avec la librairie matplotlib.
        if QMouseEvent.button() == Qt.LeftButton:
            if self.pixmap():
                img = ImageQt.fromqpixmap(self.pixmap())
                plt.figure('Gravillonnage')
                plt.imshow(img)
                plt.title('Gravillonnage')
                plt.show()

class DoubleClickTabel(QtWidgets.QTableWidget):
    img = cv2.imread(r'./Photos/Default.jpg')
    x = []# list pour les abscisses des impacts détecter dans l'image traitée.
    y = []# list pour les ordonnées des impacts détecter dans l'image traitée.
    s_t = 1# surface totale de l'image en mm².
    s = 0# surface totale des impacts détectés dans l'image en mm².
    def mouseDoubleClickEvent(self, QMouseEvent):
        # Pour ecrire un commentaire sur le tableau
        if QMouseEvent.button() == Qt.RightButton:
            self.comment = commenttable()# Pour ouvrir la fenêtre de commentaire pour le tableau.
            self.comment.show()
        # Pour voir les documents du tableau avec la librairie matplotlib.
        if QMouseEvent.button() == Qt.LeftButton:
            # Pour voir les cotations de la dimension des impacts dans un histogramme
            if self.item(0, 6).isSelected():# En double clickant on peut selecter la colonne du cotation pour ouvrir
                # la fenêtre de l'histogramme.
                cotation_list = []
                self.selectColumn(6)
                cotation_list = self.selectedItems().copy()# mettre touts les cotations de la dimension des impacts
                # dans une lists cotation_list.
                # Le boucle for est pour mettre dans la liste cotation_mlist au lieur
                # de PAS BON une cotation egale à 6 pour être cappable de l'illustrer dans l'histogramme.
                for item in range(1, len(cotation_list)):
                    if not cotation_list[item].text() == 'PAS BON':
                        cotation_list[item] = int(cotation_list[item].text())
                    else:
                        cotation_list[item] = 6
                cotation_list[0] = 0
                fig = plt.figure('Histogramme')
                ax = fig.add_subplot()
                fig.suptitle('Cotation pour chaque impact')
                ax.set_ylabel("nombre d'impacts")
                ax.set_xlabel("Surface (mm²)")
                ax.hist(cotation_list)
                plt.show()
            if self.item(0, 1).isSelected() or self.item(0, 2).isSelected():# Si la calonne de X ou de Y est selectée, une fenêtre contient l'image traitée avec les coordonnées de chaque impacts doit être illustrer
                fig = plt.figure('Gravillonnage')
                ax = fig.add_subplot()
                fig.suptitle('Coordonées')
                ax.plot(self.x, self.y, 'ro')
                ax.imshow(self.img)
                plt.show()
            if self.item(0, 5).isSelected():# Pour dessiner un diagramme circulaire, en clickant sur la colonne pourcentage
                fig = plt.figure('Diagramme circulaire')
                ax = fig.add_subplot()
                fig.suptitle("Répartition des impacts sur la surface totale de l'échantillon (%)")
                tasks = [self.s, self.s_t]
                ax.pie(tasks, labels=['surface des impacts', 'surface totale'],autopct='%1.1f%%')
                ax.axis('equal')
                plt.show()

# Pour écrire un commentaire sur la partie courbe.
class DoubleClickCourbe(FigureCanvas):
    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.comment = commentgraphe()
            self.comment.show()

# Pour écrire un commentaire sur la partie graphique.
class DoubleClickreper(FigureCanvas):
    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.comment = commentrepere()
            self.comment.show()

class testcomment(QMainWindow):
    def __init__(self):
        super(testcomment, self).__init__()
        self.widget = QtWidgets.QWidget()
        self.widget.resize(400, 300)
        self.grid_layout = QtWidgets.QGridLayout(self.widget)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.LineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.grid_layout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.LineEdit_2, 0, 2, 1, 1)
        self.LineEdit.textChanged.connect(self.text_1_fct)
        self.LineEdit_2.textChanged.connect(self.text_2_fct)

    def text_1_fct(self):
        Prog.text_1 = self.lineEdit.text()

    def text_2_fct(self):
        Prog.text_2 = self.LineEdit_2.text()

# La classe qui contient le logiciel et ces fonctions.
class Prog(QMainWindow, Ui_MainWindow):
    # Les variables :
    # ##Principale
    top = None# Pour mettre le toplevel de treewidget.
    messagebool = False# Pour les messages des informations.
    item = None# Pour les items de treewidget.
    plaque_name = None# pour mettre le nom de plaque dans le top level de treewidget.
    file_name_indx = 0# indice pour les noms des fichiers des tests deja faire.
    plaque_name_list = []# Pour sauvegarder touts les plaques de top level du treewidget.
    gravillonage_list = []# Pour sauvegarder les tests gravillonnages qui sont mis dans le treewidget.
    quadrillage_list = []# Pour sauvegarder les tests quadrillages qui sont mis dans le treewidget.
    imgOrg = ''
    bidx = False# Pour mettre les indices de chaque impact sur l'image traitée.
    barea = False# Pour mettre les surfaces de chaque impact sur l'image traitée.
    bperimetre = False# Pour mettre les perimeters de chaque impact sur l'image traitée.
    org = True# Pour visualiser l'image originale au lieu l'image traitée.
    imgName = ''# contenir le chemin de l'image de plaque.
    child = None# Pour les childs des tops level dans le treewidget.
    text_1 = ''
    text_2 = ''
    label_taille = 0
    # ##Gravillonage
    value = [1, 0, 1]# [filtre, seuil, contours]
    data = None# Contenir touts les informations nécessaires pour chaque impact détecté dans l'image (indice, surface,
    # perimeter, x, y).
    area = None# list contenant les surfaces des impacts.
    cx = None# list contenant les abscisses des impacts.
    cy = None# list contenant les ordonnées des impacts.
    length = None# Le nombre des impacts détectés.
    perimetre = None# list contenant les perimeters des impacts.
    img = None# Matrice contient l'image traitée.
    charge = False
    # ##Analyse
    # Lists pour la cotation de la densité de l'écaillage.
    dlistint = [9, 24, 74, 150, 160]
    dlistsym = ['A', 'B', 'C', 'D', 'E']
    # Lists pour la cotation de la dimension des impacts.
    clist = [0.85, 1.20, 1.70, 3.30, 6.30]
    csylist = [1, 2, 3, 4, 5]
    selectedlist = []
    maxavalue = 0# La surface maximale entre touts les impacts détectés.
    maxpvalue = 0# Le perimeter maximal entre touts les impacts détectés.
    ia = 1
    ip = 1
    si = 0
    a = 1
    cautp = 0# La valeur de la cotation de l'écaillage.
    sym = 'A'# Le symbole de la cotation de l'écaillage.
    info = []
    b = True
    q = False
    countcanvas = 0
    countechelle = 0
    canvaswidgetlist = []
    ispressed = False
    # ##Quadrillage
    background_Color = 0# Pour le fond de l'image traitée si 0 alors noir si 1 alors bland.
    thresh = None
    self_img_trait = None# Contenir une matrice de l'image de quadrillage traitée.
    self_img_original = None# Contenir une matrice de l'image de quadrillage originale.
    thresh_changed = False
    cautationName = 'Défaut(Stellantis)'# Le norme de classification qu'on a utilisé.
    percent = 0# Pourcentage de la surface de la partie arraché par rapport à la surface totale de l'image.
    niveau = None# Pour la classification de la partie quadrillage.

    # Classification de STELLANTIS :
    listInfoInt = [0, 5, 15, 35, 65]
    listInfoSym = ['a', 'b', 'c', 'd', 'e']

    def __init__(self):
        super(Prog, self).__init__()
        self.scrollArea_tableau = None
        self.setupUi(self)
        self.windowcamera = root()
        self.windowcamera.cap.release()
        self.windowcotation = None
        self.testcom = None
        self.charge_tree_from_file()
        self.deleteitem()
        self.setMouseTracking(True)
        self.Image_principale.setMouseTracking(True)

        # ##Definition
        self.treeWidget_Plaque.setColumnCount(1)

        # ##Gravillonage_Label
        self.label = DoubleClickLabel(self.scrollAreaWidgetContents_Image)
        self.label.setStyleSheet("border-color: transparent;\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.image = None

        # ##Quadrillage_Labels
        self.Img_org =DoubleClickLabel_Quadrillage(self.Originale)
        self.Img_org.setStyleSheet("border-color: transparent;\n"
                                   "\n"
                                   "")
        self.Img_org.setObjectName("Img_org")
        self.gridLayout_17.addWidget(self.Img_org, 0, 0, 1, 1)
        self.Img_bin = DoubleClickLabel_Quadrillage(self.Binaire)
        self.Img_bin.setStyleSheet("border-color: transparent;\n"
                                   "")
        self.Img_bin.setObjectName("Img_bin")
        self.gridLayout_26.addWidget(self.Img_bin, 0, 0, 1, 1)
        self.Img_trait_2 = DoubleClickLabel_Quadrillage(self.Traite)
        self.Img_trait_2.setStyleSheet("border-color: transparent;\n"
                                       "")
        self.Img_trait_2.setObjectName("Img_trait_2")
        self.gridLayout_27.addWidget(self.Img_trait_2, 0, 0, 1, 1)
        self.Img_cont = DoubleClickLabel_Quadrillage(self.Contours)
        self.Img_cont.setStyleSheet("border-color: transparent;\n"
                                    "")
        self.Img_cont.setObjectName("Img_cont")
        self.gridLayout_28.addWidget(self.Img_cont, 0, 0, 1, 1)
        self.Img_org.setText("Image originale")
        self.Img_bin.setText("Image binaire")
        self.Img_trait_2.setText("Image traitée")
        self.Img_cont.setText("Image avec contours")
        self.Img_org.setAlignment(QtCore.Qt.AlignCenter)
        self.Img_bin.setAlignment(QtCore.Qt.AlignCenter)
        self.Img_cont.setAlignment(QtCore.Qt.AlignCenter)
        self.Img_trait_2.setAlignment(QtCore.Qt.AlignCenter)

        # ##Analyse_Label and tableau
        self.scrollArea_tableau = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_Analyse)
        self.scrollArea_tableau.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\nstop:0 rgb(0, 170, 255), stop:1 rgb(61, 123, 184));")
        self.scrollArea_tableau.setWidgetResizable(True)
        self.scrollArea_tableau.setObjectName("scrollArea_tableau")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 410, 296))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color:white;\n"
                                   "border-style:outset;\n"
                                   "border-width:1px;\n"
                                   "border-radius:3px;\n"
                                   "border-color:rgb(170, 0, 0);\n"
                                   "width: 5px;\n"
                                   "color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Tableau d\'informations: ")
        self.verticale_tableau = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticale_tableau.addWidget(self.label_4)
        self.gridLayout_3.addLayout(self.verticale_tableau, 0, 0, 1, 1)
        self.scrollArea_tableau.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea_tableau, 1, 0, 6, 1)
        self.tableWidget = DoubleClickTabel(self.scrollAreaWidgetContents_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticale_tableau.addWidget(self.tableWidget)
        self.tableWidget.setStyleSheet("background-color:white;")
        self.label.setScaledContents(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msg_top = QMessageBox()
        self.msg_top.setWindowIcon(icon)
        self.msg_top.setIcon(QMessageBox.Warning)
        self.msg_top.setWindowTitle("Attention")
        self.yesbutton = self.msg_top.addButton('Oui', QMessageBox.YesRole)
        self.nobutton = self.msg_top.addButton('Non', QMessageBox.NoRole)
        self.nobutton.clicked.connect(self.msg_top.close)
        self.yesbutton.clicked.connect(self.deletetoplevel)

        # ##Principale
        self.actionImport.triggered.connect(self.openImage)
        self.pushButton_Importer.clicked.connect(self.openImage)
        self.pushButton_Gravillonage.clicked.connect(self.gotoGravillonage)
        self.pushButton_Quadrillage.clicked.connect(self.gotoQuadrillage)
        self.actionSave.triggered.connect(self.file_save)
        self.pusButton_Sauvegarder.clicked.connect(self.file_save)
        self.actionNouveau_Cotation.triggered.connect(self.NouveauCotation)
        self.actionOuvrire_Cotation.triggered.connect(self.opencot)
        self.actionOuvrire_Echelle.triggered.connect(self.openechelle)
        self.actionNouveau_Echelle.triggered.connect(self.nouveauechelle)
        self.actionDefault_Echelle.triggered.connect(self.defaultechelle)
        self.defaultechelle()
        self.actionExit.triggered.connect(self.close)
        self.pushButton_Camera.clicked.connect(self.open_camera)
        self.windowcamera.pushButton_Import.clicked.connect(self.importer)
        self.treeWidget_Plaque.doubleClicked.connect(self.selectedItem)
        self.pushButton_Aide.clicked.connect(self.messageinfoappear)
        self.pushButton_tree.clicked.connect(self.treeapear)

        # ##Gravillonage
        self.filtreplus.clicked.connect(self.plus_filtre)
        self.filtremoins.clicked.connect(self.moins_filtre)
        self.contoursmoins.clicked.connect(self.moins_contours)
        self.contoursplus.clicked.connect(self.plus_contours)
        self.tresh.valueChanged.connect(self.t_change)
        self.checkBox.toggled.connect(self.orgimage)
        self.textEdit_commentaire_grav.textChanged.connect(self.savegravecommentaire)

        # ##PuttextGravillonage
        self.surface.toggled.connect(self.putextarea)
        self.perimetre.toggled.connect(self.putextperimetre)
        self.indice.toggled.connect(self.putextindx)

        # ##Analyse
        self.actionAnalyse.triggered.connect(self.tablecreation)
        self.pushButton_Analyse.clicked.connect(self.tablecreation)

        # ##Quadrillage
        self.hideAll()
        self.tabWidget_Image.setCurrentIndex(0)
        self.h_horizontalSlider.valueChanged.connect(self.changeVal)
        self.v_horizontalSlider.valueChanged.connect(self.changeVal)
        self.h_spinBox.valueChanged.connect(self.changeVal)
        self.v_spinBox.valueChanged.connect(self.changeVal)
        self.dark_radio_button.toggled.connect(self.bg_color)
        self.t_horizontalSlider.valueChanged.connect(self.changeVal)
        self.t_spinBox.valueChanged.connect(self.changeVal)
        self.e_horizontalSlider.valueChanged.connect(self.changeVal)
        self.e_spinBox.valueChanged.connect(self.changeVal)
        self.actionDefault_Cotation.triggered.connect(self.Default)
        self.tabWidget_Image.currentChanged.connect(self.tabChoose)

    # ##Event
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.showMaximized()

    def mouseDoubleClickEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            if self.isFullScreen():
                self.showMaximized()
            else:
                self.showFullScreen()
    # ##Caméra
    def open_camera(self):
        self.splash = QSplashScreen()
        self.splash.setPixmap(QPixmap("Photos/loading.gif"))
        self.splash.show()
        self.movie = QMovie("Photos/loading.gif")
        self.movie.start()
        self.movie.frameChanged.connect(self.moviechanged)
        self.stopsplash()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.messagebool:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Info sur Camera")
            self.msg.setText(
                "C'est la fenêtre nécessaire pour prendre une photo d'une plaque.\n\nLa fenêtre camera est formée de 2 widgets (Capturer et Résultats).")
            self.msg.setDetailedText(
                "Le widget Capturer est formée d’un label, 3 boutons et un ligne texte. Le label est pour visualiser le camera. Le bouton Capturer est pour prendre une photo. Le bouton Naviguer pour choisir le lieu où la photo sera sauvegardée. Le bouton Fermer pour fermer le camera et la fenêtre de camera. Le widget Résultats est formée d’un label et 2 boutons (importer et fermer). Le label est pour visualiser la photo capturer et on peut prendre un rectangle de l’image (contenant le plaque) et pour importer sur la fenêtre principale de logiciel l’image de plaque. Le bouton importer pour importer une image de plaque dans le logiciel. (Il faut que l’image contient seulement le plaque).")
            self.msg.show()

    def moviechanged(self):
        pixmap = self.movie.currentPixmap()
        self.splash.setPixmap(pixmap)

    def stopsplash(self):
        if cv2.VideoCapture(self.windowcamera.i).grab():
            self.windowcamera.cap = cv2.VideoCapture(self.windowcamera.i)
        self.splash.finish(self.windowcamera)
        self.windowcamera.show()

    def importer(self):
        if self.windowcamera.imageLabel.capturePixmap:
            self.windowcamera.imageLabel.capturePixmap.save("./img/img_camera_cut.jpg","JPG", 100)
            image_path = self.windowcamera.saveLocationEntry.text()
            if image_path == "":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setWindowTitle("ERREUR")
                self.msg.setText("L'image n'est pas sauvegarder")
                self.msg.show()
                return None
            self.Image_principale.clear()
            self.imgName = image_path
            self.Image_principale.setPixmap(QPixmap("./img/img_camera_cut.jpg"))
            im = cv2.imread("./img/img_camera_cut.jpg")
            try:
                with open('txt/defaultechelle.bin', 'rb') as file:
                    long = pickle.load(file)
                    larg = pickle.load(file)
                    ech = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
                sp = int(im.shape[0]) * int(im.shape[1])
                div = (long * larg) / sp
                echelle = math.sqrt(div)
                self.echelle_number = echelle
                try:
                    with open('txt/echell.bin', 'wb') as file:
                        pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')
            self.Image_principale.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_2.setText('Resolution: 'f'{im.shape[0]}x'f'{im.shape[1]} dpi')
            self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')
            self.pushButton_Quadrillage.setEnabled(True)
            self.pushButton_Gravillonage.setEnabled(True)
            self.tabWidget.setCurrentIndex(0)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Information")
            self.msg.setText(
                "L'image est importée")
            self.msg.show()
            file_name = os.path.basename(image_path)
            i = 0
            if not len(self.plaque_name_list) == 0:
                while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                    i += 1
            if i == len(self.plaque_name_list):
                self.plaque_name_list.append(file_name)
                self.file_name_indx = -1
            else:
                self.file_name_indx = i
                self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
            self.treeplaque()
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setWindowTitle("ERREUR")
            self.msg.setText("Aucune partie est choisie pour importer")
            self.msg.show()
            return None

    # ##focntion_Principale
    def gotoQuadrillage(self):
        if self.Image_principale.capturePixmap:
            self.Image_principale.capturePixmap.save("./img/img_cut_quad.jpg", "JPG", 100)
            self.Img_org.setPixmap(QPixmap("./img/img_cut_quad.jpg"))
            self.self_img_original = cv2.imread(os.path.split(os.path.realpath(__file__))[0] + r'\img\img_cut_quad.jpg')
            org = cv2.cvtColor(self.self_img_original, cv2.COLOR_BGR2GRAY)
            self.self_img_trait, img_bi = eliminate(org)
            QIm_draw = draw_contours(self.self_img_trait, self.self_img_original)
            cv2.imwrite('img\QIm_draw.png',QIm_draw)
            self.Img_cont.setPixmap(self.convert_nparray_to_QPixmap(QIm_draw))
            self.Img_bin.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(img_bi))
            self.Img_trait_2.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(self.self_img_trait))
            cv2.imwrite('img\Img_trait.png', self.self_img_trait)
            self.t_horizontalSlider.setTracking(False)
            self.t_horizontalSlider.setSliderPosition(0)
            self.t_horizontalSlider.setTracking(True)
            self.t_spinBox.setValue(self.t_horizontalSlider.TickPosition())
            self.percent = get_surface(self.self_img_trait)
            self.classification()
            self.showResult()
            self.Quadrillage.setEnabled(True)
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setTabVisible(2, True)
            self.tabWidget.setCurrentIndex(2)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if self.messagebool:
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Info sur quadrillage")
                self.msg.setText("Les 4 fenêtres sont pour traiter et analyser l'image\n\nOn double clicquant sur les fenêtres vous ouvrirez une fenêtre avec des boutons pour mieux visualiser l'image")
                self.msg.setDetailedText(
                    "Originale: pour visualiser l'image originale.\nBinaire: pour visualiser l'image après seuillage.\nTraité: pour visualiser l'image filtré.\nContours: pour visualiser les contours detectés dans l'image traités")
                self.msg.show()
            item = self.treeWidget_Plaque.selectedItems()
            if item != []:
                i = 0
                file_name = item[-1].parent().text(0)
                if not len(self.plaque_name_list) == 0:
                    while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                        i += 1
                if i == len(self.plaque_name_list):
                    self.plaque_name_list.append(file_name)
                    self.file_name_indx = -1
                else:
                    self.file_name_indx = i
                    self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
                self.treeWidget_Plaque.clearSelection()

            if not len(self.plaque_name_list) == len(self.gravillonage_list):
                self.gravillonage_list.append(0)
                self.quadrillage_list.append(1)
                quad_name = "Quadrillage_" + str(self.quadrillage_list[-1])
                self.treechild(quad_name)
            else:
                self.quadrillage_list[self.file_name_indx] += 1
                self.gravillonage_list[self.file_name_indx] += 0
                quad_name = "Quadrillage_" + str(self.quadrillage_list[self.file_name_indx])
                self.treechild(quad_name)
            self.pusButton_Sauvegarder.setEnabled(True)
            self.actionSave.setEnabled(True)

    def gotoGravillonage(self):
        _translate = QtCore.QCoreApplication.translate
        print(self.countechelle)
        if self.Image_principale.capturePixmap:
            try:
                self.Image_principale.capturePixmap.save("./img/img_cut_grav.jpg", "JPG", 100)
                self.label.setPixmap(QPixmap("./img/img_cut_grav.jpg"))
                self.value[0] = 1
                self.value[1] = 0
                self.value[2] = 1
                self.filtre.setText('filtre: 1')
                self.contours.setText('contours: 1')
                self.tresh.setTracking(False)
                self.tresh.setSliderPosition(0)
                self.tresh.setTracking(True)
                self.threshlabel.setText('seuil: 0')
                self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimètre = main(self.value[0],
                                                                                                     self.value[1],
                                                                                                     self.value[2])
                self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
                self.nbr.setText(_translate("MainWindow", 'Nombre d impacts: 'f'{self.length}'))
                self.Gravillonage.setEnabled(True)
                self.tabWidget.setTabVisible(1, True)
                self.tabWidget.setTabEnabled(1, True)
                self.tabWidget.setCurrentIndex(1)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                if self.messagebool:
                    self.msg = QMessageBox()
                    self.msg.setWindowIcon(icon)
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowTitle("Info sur Gravillonage")
                    self.msg.setText(
                        "C'est la fenêtre nécessaire pour filtrer l'image de la partie gravillonage.\n\nAprès avoir fini filtrer d'image, cliquez sur le bouton Analyse (au-dessus de la fenêtre principale) pour passer à la fenêtre d'analyse de gravillonnage")
                    self.msg.setDetailedText(
                        "Filtre: filtre: pour eleminer les bruits dans l'image.\tcontours: pour dessiner en vert les contours detecter sur l'image.\t seuil: nécessaire pour la seuillage de l'image.\n\nParamètres: indice: le logiciel met directement un indice pour chaque contour detecter.\tsurface: pour visualiser la surface de chaque contour detecter sur l'image.\tperimètres: pour visualiser le perimètre de chaque contour detecter sur l'image.\timage originale: pour visualiser l'image originale\n\nNombre d'impacts: signifie le nombre de contours detecter dans l'image\n\nCommentaire: on peut le trouve dans la partie gravillonage du rapport après de cliquer sur le bouton sauvegarder")
                    self.msg.show()
                item = self.treeWidget_Plaque.selectedItems()
                if item != []:
                    i = 0
                    file_name = item[-1].parent().text(0)
                    if not len(self.plaque_name_list) == 0:
                        while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                            i += 1
                    if i == len(self.plaque_name_list):
                        self.plaque_name_list.append(file_name)
                        self.file_name_indx = -1
                    else:
                        self.file_name_indx = i
                        self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
                    self.treeWidget_Plaque.clearSelection()
                if len(self.plaque_name_list) != len(self.gravillonage_list):
                    self.gravillonage_list.append(1)
                    grav_name = "Gravillonage_" + str(self.gravillonage_list[-1])
                    self.treechild(grav_name)
                    self.quadrillage_list.append(0)
                else:
                    self.gravillonage_list[self.file_name_indx] += 1
                    self.quadrillage_list[self.file_name_indx] += 0
                    grav_name = "Gravillonage_" + str(self.gravillonage_list[self.file_name_indx])
                    self.treechild(grav_name)
                self.pushButton_Analyse.setEnabled(True)
                self.actionAnalyse.setEnabled(True)
                self.pusButton_Sauvegarder.setEnabled(True)
                self.actionSave.setEnabled(True)
            except Exception as err:
                print(err)

    def setImageSize(self, im):
        return im.scaled(self.img_import.width(), self.img_import.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def openImage(self):
        bool_1 = False
        self.treeWidget_Plaque.clearSelection()
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        imgName, imgType = QFileDialog.getOpenFileName(self, "Import image", ".", "*.jpg;*.tif;*.png;;All Files(*)")
        if imgName == "":
            return 0
        else:
            if self.imgName != imgName:
                self.imgName = imgName
                bool_1 = True
            self.Image_principale.clear()
            self.imgOrg = QPixmap(self.imgName).toImage()
            im = cv2.imread(self.imgName)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            try:
                with open('txt/defaultechelle.bin', 'rb') as file:
                    long = pickle.load(file)
                    larg = pickle.load(file)
                    ech = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
                sp = int(im.shape[0]) * int(im.shape[1])
                div = (long * larg) / sp
                echelle = math.sqrt(div)
                self.echelle_number = echelle
                try:
                    with open('txt/echell.bin', 'wb') as file:
                        pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')
            self.Image_principale.setPixmap(QPixmap(self.imgName))
            self.Image_principale.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_2.setText('Resolution: 'f'{im.shape[0]}x'f'{im.shape[1]} dpi')
            self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')
            self.pushButton_Quadrillage.setEnabled(True)
            self.pushButton_Gravillonage.setEnabled(True)
        file_name = os.path.basename(self.imgName)
        i = 0
        if not len(self.plaque_name_list) == 0:
            while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                i += 1
        if i == len(self.plaque_name_list):
            self.plaque_name_list.append(file_name)
            self.file_name_indx = -1
        else:
            self.file_name_indx = i
            self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
        self.treeplaque()
        self.countechelle = 0

    def file_save(self):
        g = False
        q = False
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save_File', ".",
                                                     "*.docx;;*.pdf")
        if name == ('',''):
            return
        else:
            if self.tabWidget.widget(1).isEnabled():
                g = True
                h = int(self.img.shape[0] * self.echelle_number)
                l = int(self.img.shape[1] * self.echelle_number)
            if self.tabWidget.widget(2).isEnabled():
                self.saveResult()
                q = True
                h = int(self.self_img_trait.shape[0] * self.echelle_number)
                l = int(self.self_img_trait.shape[1] * self.echelle_number)
            makeworddoc(name[0], self.cautp, self.sym, self.imgName, q, g, self.imgName, taille=(h, l), cg=self.comboBox.currentText(), cq=self.comBox_quad.currentText(), surface_total=self.tableWidget.s_t, surface_impatcs=self.tableWidget.s, thresh_quad=self.t_horizontalSlider.value(), thresh_grav=self.tresh.value(), img=self.img)
            if self.tabWidget.widget(1).isEnabled() and self.tabWidget.widget(3).isEnabled():
                self.tableWidget.selectColumn(6)
                cotation_list = self.tableWidget.selectedItems().copy()
                for item in range(1, len(cotation_list)):
                    if not cotation_list[item].text() == 'PAS BON':
                        cotation_list[item] = int(cotation_list[item].text())
                    else:
                        cotation_list[item] = 'Pas Bon'
                cotation_list[0] = 0
                data = pd.DataFrame({"Surface": self.area, "Perimètre": self.perimetre, "Cotation": cotation_list[1:]})
                namelist = name[0].split('.docx')
                name_csv = namelist[0]
                data.to_excel(''f'{name_csv}.xlsx')
                if os.path.exists('comments/txt/commentlabel.txt'):
                    os.remove('comments/txt/commentlabel.txt')
                if os.path.exists('comments/txt/commentcourbe.txt'):
                    os.remove('comments/txt/commentcourbe.txt')
                if os.path.exists('comments/txt/commentquadrillage.txt'):
                    os.remove('comments/txt/commentquadrillage.txt')
                if os.path.exists('comments/txt/commentreper.txt'):
                    os.remove('comments/txt/commentreper.txt')
                if os.path.exists('comments/txt/commenttable.txt'):
                    os.remove('comments/txt/commenttable.txt')
            if q == True:
                self.tabWidget.setTabEnabled(2, False)
                q = False
            if g == True:
                self.tabWidget.setTabEnabled(1, False)
                g = False
            self.tabWidget.setCurrentIndex(0)

    def orgimage(self):
        if not self.org:
            self.label.setPixmap(QtGui.QPixmap(r'./img/img_cut_grav.jpg'))
            self.org = True
        else:
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0], self.value[1], self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
            self.org = False

    def saveactionappear(self):
        if self.label.pixmap() or self.Img_org.pixmap() or self.Img_trait_2.pixmap():
            self.actionSave.setEnabled(True)
            self.pusButton_Sauvegarder.setEnabled(True)

    # ##fonctiontreewidget
    def treeplaque(self):
        plaque = QtWidgets.QTreeWidgetItem([self.plaque_name_list[-1]])
        if self.treeWidget_Plaque.topLevelItemCount() < len(self.plaque_name_list):
            self.plaque_name = plaque
            self.treeWidget_Plaque.addTopLevelItem(self.plaque_name)

    def treechild(self, value):
        if not self.child == None :
            self.child.setSelected(False)
        self.child = QtWidgets.QTreeWidgetItem([value])
        item = self.treeWidget_Plaque.selectedItems()
        if not item == []:
            if item[-1].parent().text(0) != self.plaque_name.text(0):
                self.plaque_name = item[-1].parent()
                self.treeWidget_Plaque.clearSelection()
        self.plaque_name.addChild(self.child)
        if not self.child == None:
            self.child.setSelected(True)
        self.save_tree_in_file()

    def save_tree_in_file(self):
        if self.treeWidget_Plaque.topLevelItemCount() > 0:
            self.item = self.treeWidget_Plaque.selectedItems()
            if self.item[0].parent() is None:
                return None
            else:
                path = self.item[0].parent().text(0) + self.item[0].text(0)
                Prog_name = self.item[0].text(0)
                Prog_name = Prog_name.split('_', -1)
                data_list = []
                if Prog_name[0] == 'Gravillonage':
                    im = cv2.imread(self.imgName)
                    self.img = cv2.imread(r'./img/img_cut_grav.jpg')
                    data_list = [self.img, self.value[0], self.value[1], self.value[2], im]
                    self.tabWidget.setTabEnabled(1, True)
                    self.tabWidget.setTabEnabled(2, False)
                elif Prog_name[0] == 'Quadrillage':
                    im = cv2.imread(self.imgName)
                    data_list = [self.t_horizontalSlider.value(), self.h_horizontalSlider.value(), self.v_horizontalSlider.value(), self.cautationName, self.niveau, self.percent, self.self_img_original, im]
                    self.tabWidget.setTabEnabled(2, True)
                    self.tabWidget.setTabEnabled(1, False)
                photo_name = path.split('.jpg', -1)
                file_name = photo_name[0] + '_' + Prog_name[0] + '_' + Prog_name[1]
                if os.path.exists('filtres_data/'f'{file_name}.bin'):
                    os.remove('filtres_data/'f'{file_name}.bin')
                try:
                    with open('filtres_data/'f'{file_name}.bin', 'wb') as file:
                        pickle.dump(data_list, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')

    def charge_tree_from_file(self):
        thisdir = os.getcwd()
        # r=root, d=directories, f = files
        for r, d, f in os.walk('filtres_data'):
            break
        photo_exist = ''
        for file in f:
            file_list = file.split('_', 1)
            photo = file_list[0] + '.jpg'
            filtre = file_list[1]
            filtre_list = filtre.split('.bin', -1)
            filtre_name = filtre_list[0]
            #print(f"Photo:{photo}, \t Filtre:{filtre_name}")
            if not photo_exist == photo:
                photo_view = QtWidgets.QTreeWidgetItem([photo])
                self.plaque_name = photo_view
                self.treeWidget_Plaque.addTopLevelItem(self.plaque_name)
                i = 0
                file_name = photo
                if not len(self.plaque_name_list) == 0:
                    while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                        i += 1
                if i == len(self.plaque_name_list):
                    self.plaque_name_list.append(file_name)
                    self.file_name_indx = -1
                else:
                    self.file_name_indx = i
                    if not self.treeWidget_Plaque.topLevelItem(self.file_name_indx) == None:
                        self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
                if not len(self.plaque_name_list) == len(self.gravillonage_list):
                    if filtre_name[0] == 'Q':
                        self.gravillonage_list.append(0)
                        self.quadrillage_list.append(1)
                        quad_name = filtre_name
                        self.child = QtWidgets.QTreeWidgetItem([quad_name])
                        self.plaque_name.addChild(self.child)
                    elif filtre_name[0] == 'G':
                        self.gravillonage_list.append(1)
                        grav_name = filtre_name
                        self.child = QtWidgets.QTreeWidgetItem([grav_name])
                        self.plaque_name.addChild(self.child)
                        self.quadrillage_list.append(0)
                else:
                    if filtre_name[0] == 'Q':
                        self.quadrillage_list[self.file_name_indx] += 1
                        self.gravillonage_list[self.file_name_indx] += 0
                        quad_name = filtre_name
                        self.child = QtWidgets.QTreeWidgetItem([quad_name])
                        self.plaque_name.addChild(self.child)
                    elif filtre_name[0] == 'G':
                        self.gravillonage_list[self.file_name_indx] += 1
                        self.quadrillage_list[self.file_name_indx] += 0
                        grav_name = filtre_name
                        self.child = QtWidgets.QTreeWidgetItem([grav_name])
                        self.plaque_name.addChild(self.child)
            else:
                i = 0
                file_name = photo
                if not len(self.plaque_name_list) == 0:
                    while i < len(self.plaque_name_list) and not (file_name == self.plaque_name_list[i]):
                        i += 1
                if i == len(self.plaque_name_list):
                    self.plaque_name_list.append(file_name)
                    self.file_name_indx = -1
                else:
                    self.file_name_indx = i
                    if not self.treeWidget_Plaque.topLevelItem(self.file_name_indx) == None:
                        self.plaque_name = self.treeWidget_Plaque.topLevelItem(self.file_name_indx)
                if not len(self.plaque_name_list) == len(self.gravillonage_list):
                    if filtre_name[0] == 'Q':
                        self.gravillonage_list.append(0)
                        self.quadrillage_list.append(1)
                        quad_name = "Quadrillage_" + str(self.quadrillage_list[-1])
                        self.child = QtWidgets.QTreeWidgetItem([quad_name])
                        self.plaque_name.addChild(self.child)
                    elif filtre_name[0] == 'G':
                        self.gravillonage_list.append(1)
                        grav_name = "Gravillonage_" + str(self.gravillonage_list[-1])
                        self.child = QtWidgets.QTreeWidgetItem([grav_name])
                        self.plaque_name.addChild(self.child)
                        self.quadrillage_list.append(0)
                else:
                    if filtre_name[0] == 'Q':
                        self.quadrillage_list[self.file_name_indx] += 1
                        self.gravillonage_list[self.file_name_indx] += 0
                        quad_name = "Quadrillage_" + str(self.quadrillage_list[self.file_name_indx])
                        self.child = QtWidgets.QTreeWidgetItem([quad_name])
                        self.plaque_name.addChild(self.child)
                    elif filtre_name[0] == 'G':
                        self.gravillonage_list[self.file_name_indx] += 1
                        self.quadrillage_list[self.file_name_indx] += 0
                        grav_name = "Gravillonage_" + str(self.gravillonage_list[self.file_name_indx])
                        self.child = QtWidgets.QTreeWidgetItem([grav_name])
                        self.plaque_name.addChild(self.child)
            photo_exist = photo

    def selectedItem(self):
        self.item = self.treeWidget_Plaque.selectedItems()
        if self.item == None:
            return None
        name = self.item[0].text(0)
        if name[0] == 'G':
            path = self.item[0].parent().text(0) + self.item[0].text(0)
            Prog_name = self.item[0].text(0)
            Prog_name = Prog_name.split('_', -1)
            photo_name = path.split('.jpg', -1)
            file_name = photo_name[0] + '_' + Prog_name[0] + '_' + Prog_name[1]
            data_list = []
            self.img = None
            try:
                with open('filtres_data/'f'{file_name}.bin', 'rb') as file:
                    data_list = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
            self.img = data_list[0]
            cv2.imwrite('./img/img_cut_grav.jpg', self.img)
            self.value[0] = int(data_list[1])
            self.value[1] = int(data_list[2])
            self.value[2] = int(data_list[3])
            self.filtre.setText('filtre: 'f'{self.value[0]}')
            self.contours.setText('contours: 'f'{self.value[2]}')
            self.tresh.setValue(self.value[1])
            if self.value[1] == 0:
                t = True
            else:
                t = False
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2], auto=t)
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
            im = cv2.cvtColor(data_list[4], cv2.COLOR_BGR2RGB)
            self.Image_principale.setPixmap(self.convert_nparray_to_QPixmap(im))
            try:
                with open('txt/defaultechelle.bin', 'rb') as file:
                    long = pickle.load(file)
                    larg = pickle.load(file)
                    ech = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
                sp = int(im.shape[0]) * int(im.shape[1])
                div = (long * larg) / sp
                echelle = math.sqrt(div)
                self.echelle_number = echelle
                try:
                    with open('txt/echell.bin', 'wb') as file:
                        pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')
            self.label_2.setText('Resolution: 'f'{im.shape[0]}x'f'{im.shape[1]} dpi')
            self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')
            cv2.imwrite('./img/'f'{self.item[0].parent().text(0)}.jpg', data_list[4])
            self.imgName = './img/'f'{self.item[0].parent().text(0)}.jpg'
            self.nbr.setText('Nombre d impacts: 'f'{self.length}')
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, False)
            self.tabWidget.setTabVisible(1, True)
            self.tabWidget.setTabEnabled(3, True)
            self.tabWidget.setTabVisible(3, True)
            self.pushButton_Quadrillage.setEnabled(True)
            self.pushButton_Gravillonage.setEnabled(True)
            self.tabWidget.setCurrentIndex(1)
            a = int(self.value[1])
            self.ispressed = True
            self.countechelle = 0
            self.pusButton_Sauvegarder.setEnabled(True)
            self.actionSave.setEnabled(True)
            if self.messagebool:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Info sur Gravillonage")
                self.msg.setText(
                    "C'est la fenêtre nécessaire pour filtrer l'image de la partie gravillonage.\n\nAprès avoir fini filtrer d'image, cliquez sur le bouton Analyse (au-dessus de la fenêtre principale) pour passer à la fenêtre d'analyse de gravillonnage")
                self.msg.setDetailedText(
                    "Filtre: filtre: pour eleminer les bruits dans l'image.\tcontours: pour dessiner en vert les contours detecter sur l'image.\t seuil: nécessaire pour la seuillage de l'image.\n\nParamètres: indice: le logiciel met directement un indice pour chaque contour detecter.\tsurface: pour visualiser la surface de chaque contour detecter sur l'image.\tperimètres: pour visualiser le perimètre de chaque contour detecter sur l'image.\timage originale: pour visualiser l'image originale\n\nNombre d'impacts: signifie le nombre de contours detecter dans l'image\n\nCommentaire: on peut le trouve dans la partie gravillonage du rapport après de cliquer sur le bouton sauvegarder")
                self.msg.show()
            self.defaultechelle()
        elif name[0] == 'Q':
            path = self.item[0].parent().text(0) + self.item[0].text(0)
            Prog_name = self.item[0].text(0)
            Prog_name = Prog_name.split('_', -1)
            photo_name = path.split('.jpg', -1)
            file_name = photo_name[0] + '_' + Prog_name[0] + '_' + Prog_name[1]
            data_list = []
            try:
                with open('filtres_data/'f'{file_name}.bin', 'rb') as file:
                    data_list = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
            self.t_horizontalSlider.setValue(data_list[0])
            self.h_horizontalSlider.setValue(data_list[1])
            self.v_horizontalSlider.setValue(data_list[2])
            self.cautationName = data_list[3]
            self.niveau = data_list[4]
            self.percent = data_list[5]
            array_img = np.array(data_list[6])
            self.self_img_original = array_img
            cv2.imwrite('./img/img_cut_quad.jpg', self.self_img_original)
            self.Img_org.setPixmap(QPixmap('./img/img_cut_quad.jpg'))
            im = cv2.cvtColor(data_list[7], cv2.COLOR_BGR2RGB)
            self.Image_principale.setPixmap(self.convert_nparray_to_QPixmap(im))
            try:
                with open('txt/defaultechelle.bin', 'rb') as file:
                    long = pickle.load(file)
                    larg = pickle.load(file)
                    ech = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
                sp = int(im.shape[0]) * int(im.shape[1])
                div = (long * larg) / sp
                echelle = math.sqrt(div)
                self.echelle_number = echelle
                try:
                    with open('txt/echell.bin', 'wb') as file:
                        pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')
            self.label_2.setText('Resolution: 'f'{im.shape[0]}x'f'{im.shape[1]} dpi')
            self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')
            cv2.imwrite('./img/'f'{self.item[0].parent().text(0)}.jpg', data_list[7])
            self.imgName = './img/'f'{self.item[0].parent().text(0)}.jpg'
            org = cv2.cvtColor(self.self_img_original, cv2.COLOR_BGR2GRAY)
            self.self_img_trait, img_bi = eliminate(org)
            QIm_draw = draw_contours(self.self_img_trait, self.self_img_original)
            cv2.imwrite('img\QIm_draw.png', QIm_draw)
            self.Img_cont.setPixmap(self.convert_nparray_to_QPixmap(QIm_draw))
            self.Img_bin.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(img_bi))
            self.Img_trait_2.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(self.self_img_trait))
            cv2.imwrite('img\Img_trait.png', self.self_img_trait)
            self.percent = get_surface(self.self_img_trait)
            self.classification()
            self.showResult()
            self.Quadrillage.setEnabled(True)
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setTabVisible(2, True)
            self.tabWidget.setCurrentIndex(2)
            if self.t_horizontalSlider.value() != 0:
                self.deleteLineButton_function()
                self.changeThresh(self.t_horizontalSlider.value())
                self.Quadrillage.setEnabled(True)
                self.tabWidget.setTabVisible(2, True)
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setCurrentIndex(2)
            else:
                self.t_horizontalSlider.setTracking(False)
                self.t_horizontalSlider.setSliderPosition(0)
                self.t_horizontalSlider.setTracking(True)
                self.t_spinBox.setValue(self.t_horizontalSlider.TickPosition())
            self.Gravillonage.setEnabled(False)
            self.tabWidget.setTabEnabled(1, False)
            self.pushButton_Quadrillage.setEnabled(True)
            self.pushButton_Gravillonage.setEnabled(True)
            self.pusButton_Sauvegarder.setEnabled(True)
            self.actionSave.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if self.messagebool:
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Info sur quadrillage")
                self.msg.setText(
                    "Les 4 fenêtres sont pour traiter et analyser l'image\n\nOn double clicquant sur les fenêtres vous ouvrirez une fenêtre avec des boutons pour mieux visualiser l'image")
                self.msg.setDetailedText(
                    "Originale: pour visualiser l'image originale.\nBinaire: pour visualiser l'image après seuillage.\nTraité: pour visualiser l'image filtré.\nContours: pour visualiser les contours detectés dans l'image traités")
                self.msg.show()
        else:
            return None
        return None

    def deleteitem(self):
        def delItem(e):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if e.reason() == QContextMenuEvent.Mouse:
                Item = self.treeWidget_Plaque.selectedItems()
                if Item != []:
                    item = Item[-1]
                    if item.isSelected():
                        parent = item.parent()
                        if parent == None:
                            self.top = item
                            self.msg_top.setText(f"Vous êtes sûre de supprimer les informations de plaque {item.text(0)}")
                            self.msg_top.show()
                        else:
                            self.top = item
                            self.deletechildfile()
                            parent.removeChild(item)
        self.treeWidget_Plaque.contextMenuEvent = delItem

    def deletetopfile(self):
        for r, d, f in os.walk('filtres_data'):
            break
        for file in f:
            print(f"file: {file}")
            file_split = file.split('_', -1)
            print(f"file_split: {file_split}")
            plaque_number = file_split[0] + '.jpg'
            top_text = self.top.text(0)
            print(f"top : {top_text}")
            if plaque_number == top_text:
                os.remove(f"filtres_data/{file}")

    def deletechildfile(self):
        for r, d, f in os.walk('filtres_data'):
            break
        for file in f:
            print(f"file: {file}")
            file_split = file.split('.', -1)
            print(f"file_split: {file_split}")
            item_file_name = file_split[0]
            print(f"top: {self.top.text(0)}")
            print(f"top_parent : {self.top.parent().text(0)}")
            parent_text = self.top.parent().text(0)
            plaque_name_list = parent_text.split('.')
            plaque_name = plaque_name_list[0]
            print(f"plaque_name {plaque_name}")
            echantillon_name = plaque_name + "_" + self.top.text(0)
            if item_file_name == echantillon_name:
                os.remove(f"filtres_data/{file}")
                self.plaque_name = self.top.parent()
                print("Done")
                break

    def deletetoplevel(self):
        for top in range(0, self.treeWidget_Plaque.topLevelItemCount()):
            if self.top == self.treeWidget_Plaque.topLevelItem(top):
                self.deletetopfile()
                self.treeWidget_Plaque.takeTopLevelItem(top)
                if len(self.gravillonage_list) > top:
                    self.gravillonage_list.remove(self.gravillonage_list[top])
                if len(self.quadrillage_list) > top:
                    self.quadrillage_list.remove(self.quadrillage_list[top])
                if len(self.plaque_name_list) > top:
                    self.plaque_name_list.remove(self.plaque_name_list[top])
                if top != 0:
                    self.plaque_name = self.treeWidget_Plaque.topLevelItem(top-1)
                    self.file_name_indx = top-1
                else:
                    self.plaque_name = None
                    self.file_name_indx = 0
                break

    def treeapear(self):
        self.dockWidget_Plaque.show()

    # ##fonction_Gravillonage
    def Apearr(self):
        self.actionAnalyse.setEnabled(True)
        self.pushButton_Analyse.setEnabled(True)
        self.saveactionappear()

    def convert_nparray_to_QPixmap_Quadrillage(self, img):
        h = img.shape[1]
        w = img.shape[0]
        # Convert resulting image to pixmap
        if img.ndim <= 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888)
        qpixmap = QPixmap(qimg)
        return qpixmap

    def convert_nparray_to_QPixmap(self, img):
        w, h, ch = img.shape
        # Convert resulting image to pixmap
        if img.ndim == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888)
        qpixmap = QPixmap(qimg)
        return qpixmap

    def f_change(self):
        _translate = QtCore.QCoreApplication.translate
        self.Apearr()
        self.org = False
        content = self.filtre.text()
        astringlist = content.split('filtre: ', 1)
        a = int(astringlist[1])
        self.value[0] = int(a)
        self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0], self.value[1], self.value[2], auto=False)
        self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        self.nbr.setText(_translate("MainWindow", 'Nombre d impacts: 'f'{self.length}'))
        try:
            with open('comments/txt/value.bin', 'wb') as file:
                pickle.dump(self.value[1], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[0], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[2], file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        self.save_tree_in_file()
        self.img = None

    def t_change(self):
        self.Apearr()
        self.org = False
        _translate = QtCore.QCoreApplication.translate
        self.value[1] = int(self.tresh.value())
        self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                             self.value[1],
                                                                                             self.value[2], auto=False)
        self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        self.nbr.setText(_translate("MainWindow", 'Nombre d impacts: 'f'{self.length}'))
        try:
            with open('comments/txt/value.bin', 'wb') as file:
                pickle.dump(self.value[1], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[0], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[2], file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        self.threshlabel.setText('seuil: 'f'{self.tresh.value()}')
        self.save_tree_in_file()
        self.img = None

    def c_change(self):
        _translate = QtCore.QCoreApplication.translate
        self.Apearr()
        self.org = False
        content = self.contours.text()
        astringlist = content.split('contours: ', 1)
        a = int(astringlist[1])
        self.value[2] = int(a)
        self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                             self.value[1],
                                                                                             self.value[2], auto=False)
        self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        self.nbr.setText(_translate("MainWindow", 'Nombre d impacts: 'f'{self.length}'))
        try:
            with open('comments/txt/value.bin', 'wb') as file:
                pickle.dump(self.value[1], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[0], file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.value[2], file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        self.save_tree_in_file()
        self.img = None

    def plus_filtre(self):
        _translate = QtCore.QCoreApplication.translate
        self.org = False
        content = self.filtre.text()
        astringlist = content.split('filtre: ', 1)
        a = int(astringlist[1])
        a += 1
        astringlist[1] = str(a)
        if a <= 10:
            self.filtre.setText(_translate("MainWindow", 'filtre: 'f'{astringlist[1]}'))
            self.f_change()

    def plus_contours(self):
        self.org = False
        _translate = QtCore.QCoreApplication.translate
        content = self.contours.text()
        astringlist = content.split('contours: ', 1)
        a = int(astringlist[1])
        a += 1
        astringlist[1] = str(a)
        if a <= 10:
            self.contours.setText(_translate("MainWindow", 'contours: 'f'{astringlist[1]}'))
            self.c_change()

    def moins_filtre(self):
        self.org = False
        _translate = QtCore.QCoreApplication.translate
        content = self.filtre.text()
        astringlist = content.split('filtre: ', 1)
        a = int(astringlist[1])
        if a < 1:
            a = 1
        a -= 1
        astringlist[1] = str(a)
        if 10 >= a >= 1:
            self.filtre.setText(_translate("MainWindow", 'filtre: 'f'{astringlist[1]}'))
            self.f_change()
        else:
            a = 1

    def moins_contours(self):
        self.org = False
        _translate = QtCore.QCoreApplication.translate
        content = self.contours.text()
        astringlist = content.split('contours: ', 1)
        a = int(astringlist[1])
        if a < 1:
            a = 1
        a -= 1
        astringlist[1] = str(a)
        if 10 >= a >= 1:
            self.contours.setText(_translate("MainWindow", 'contours: 'f'{astringlist[1]}'))
            self.c_change()
        else:
            a = 1

    def putextindx(self):
        if not self.bidx:
            self.bidx = True
            try:
                with open('txt/boolindx.bin', 'wb') as file:
                    pickle.dump(self.bidx, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        else:
            self.bidx = False
            try:
                with open('txt/boolindx.bin', 'wb') as file:
                    pickle.dump(self.bidx, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')

            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
            self.img = None

    def putextarea(self):
        if not self.barea:
            self.barea = True
            try:
                with open('txt/boolarea.bin', 'wb') as file:
                    pickle.dump(self.barea, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        else:
            self.barea = False
            try:
                with open('txt/boolarea.bin', 'wb') as file:
                    pickle.dump(self.barea, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écritur.')
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
            self.img = None

    def putextperimetre(self):
        if not self.bperimetre:
            self.bperimetre = True
            try:
                with open('txt/boolperimètre.bin', 'wb') as file:
                    pickle.dump(self.bperimetre, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
        else:
            self.bperimetre = False
            try:
                with open('txt/boolperimètre.bin', 'wb') as file:
                    pickle.dump(self.bperimetre, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écritur.')
            self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                 self.value[1],
                                                                                                 self.value[2])
            self.label.setPixmap(self.convert_nparray_to_QPixmap(self.img))
            self.img = None

    def savegravecommentaire(self):
        s = (self.textEdit_commentaire_grav.toPlainText())
        myFile = open('comments/txt/commentlabel.txt', "w")
        myFile.write(''f'{s}')
        myFile.close()

    # ##fonction_Analyse
    # ####Definition_tablewidget

    def tablecreation(self):
        # ##Analyse
        print(self.countechelle)
        self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                             self.value[1],
                                                                                             self.value[2])
        self.tableWidget.img = self.img
        self.tableWidget.x = self.cx
        self.tableWidget.y = self.cy
        self.Analyse.setEnabled(True)
        self.tabWidget.setTabVisible(3, True)
        area1 = self.area
        length = len(self.area)
        perimetre1 = self.perimetre
        cx1 = self.cx
        cy1 = self.cy
        im = cv2.imread('./img/img_cut_grav.jpg')
        echelle = ECHELLE()
        self.a = im.shape[1] * im.shape[0] * echelle * echelle
        for i in range(0, length):
            area1[i] = area1[i] * echelle * echelle
            perimetre1[i] = perimetre1[i] * echelle
        somme = sum(area1)
        v = Decimal(somme)
        varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
        self.tableWidget.s = varr
        self.itotal.setText('Somme surface des impacts: 'f'{varr}')
        v = Decimal(self.a)
        varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
        self.tableWidget.s_t = varr
        self.atotal.setText('Surface totale: 'f'{varr}')
        self.maxavalue = max(area1)
        self.ia = area1.index(self.maxavalue) + 1
        v = Decimal(self.maxavalue)
        varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
        self.maxa.setText('Surfacemax des impacts: 'f'{varr} mm²   indice: 'f'{self.ia}')
        self.tableWidget.setRowCount(length + 1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setItem(0, 0, QTableWidgetItem('numero d impact:'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('X'))
        self.tableWidget.setItem(0, 2, QTableWidgetItem('Y'))
        self.tableWidget.setItem(0, 3, QTableWidgetItem('perimètre (mm)'))
        self.tableWidget.setItem(0, 4, QTableWidgetItem('surface (mm²)'))
        self.tableWidget.setItem(0, 5, QTableWidgetItem('pourcentage'))
        self.tableWidget.setItem(0, 6, QTableWidgetItem('cotation'))
        i = 0
        j = 1
        while i < length:
            self.tableWidget.setItem(j, 0, QTableWidgetItem(f'{i + 1}'))
            v = Decimal(cx1[i])
            varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.tableWidget.setItem(j, 1, QTableWidgetItem(f'{varr}'))
            v = Decimal(cy1[i])
            varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.tableWidget.setItem(j, 2, QTableWidgetItem(f'{varr}'))
            v = Decimal(area1[i])
            varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.tableWidget.setItem(j, 4, QTableWidgetItem(f'{varr}'))
            v = Decimal(perimetre1[i])
            varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.tableWidget.setItem(j, 3, QTableWidgetItem(f'{varr}'))
            p = (area1[i] / self.a) * 100
            v = Decimal(p)
            varr = v.quantize(Decimal('.00001'), rounding=ROUND_HALF_UP)
            self.tableWidget.setItem(j, 5, QTableWidgetItem(f'{varr}%'))
            i += 1
            j += 1
        self.maxpvalue = max(perimetre1)
        self.ip = perimetre1.index(self.maxpvalue) + 1
        v = Decimal(self.maxpvalue)
        varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
        self.maxp.setText('Perimètremax des impacts: 'f'{varr}     indice: 'f'{self.ip}')
        im = cv2.imread('./img/img_cut_grav.jpg', 0)
        echelle = ECHELLE()
        sp = int(im.shape[1]) * int(im.shape[0])
        s = sp * (echelle * echelle)
        self.catintable()
        self.sym, self.cautp = self.cotp()
        _translate = QtCore.QCoreApplication.translate
        i = 0
        while i < len(self.dlistint):
            self.caut.setText(
            _translate("MainWindow", 'Cotation:   'f'{self.cautp}_'f'{self.sym}'))
            i += 1
            _translate = QtCore.QCoreApplication.translate
            v = Decimal(self.maxavalue)
            varr = v.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.maxa.setText(_translate("MainWindow", 'Surfacemax des impacts: 'f'{varr} mm²    indice: 'f'{self.ia}'))
            v1 = Decimal(self.maxpvalue)
            varr1 = v1.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.maxp.setText(_translate("MainWindow", 'Perimètremax des impacts: 'f'{varr1} mm     indice: 'f'{self.ip}'))
            v3 = Decimal(self.a)
            varr3 = v3.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.atotal.setText(_translate("MainWindow", 'Surface totale: 'f'{varr3} mm²'))
            v2 = Decimal(somme)
            varr2 = v2.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
            self.itotal.setText(_translate("MainWindow", 'Somme surface des impacts: 'f'{varr2} mm²'))
        self.tableWidget.selectionModel().selectionChanged.connect(self.select)
        if self.countcanvas > 0:
            self.verticalLayout_Courbe.removeWidget(self.canvaswidgetlist[0])
            self.verticalLayout_Graphe.removeWidget(self.canvaswidgetlist[1])
            self.canvaswidgetlist.clear()
        canvas = DoubleClickCourbe(Figure())
        ax = canvas.figure.add_subplot(111)
        toolbar = NavigationToolbar(canvas, self)
        container = QWidget()
        lay = QVBoxLayout(container)
        lay.addWidget(canvas)
        lay.addWidget(toolbar)
        self.verticalLayout_Courbe.addWidget(container)
        container.setMinimumWidth(100)
        var = sta.variance(area1)
        ecartype = math.sqrt(var)
        bornarealist = []
        i = 0
        x = min(area1)
        y = max(area1)
        while x <= y:
            x += ecartype
            if x <= y:
                bornarealist.insert(i, x)
            else:
                bornarealist.insert(i, y)
                break
            i += 1
        i = 0
        medianlist = []
        while i < len(bornarealist) - 1:
            x = (bornarealist[i] + bornarealist[i + 1]) / 2
            medianlist.insert(i, x)
            i += 1
        medarealist = []
        i = 0
        while i < int(self.length):
            j = 0
            h = False
            while j < len(medianlist):
                if j < (len(medianlist) - 1):
                    if area1[i] <= medianlist[j] and h == False:
                        medarealist.insert(i, medianlist[j])
                        h = True
                else:
                    if j == (len(medianlist) - 1) and h == False:
                        medarealist.insert(i, medianlist[-1])
                        h = True
                j += 1
            i += 1
        length = len(area1)
        nbridcb = np.zeros(len(medianlist))
        i = 0
        while i < len(medarealist):
            x = medarealist[i]
            j = 0
            while j < len(medianlist):
                y = medianlist[j]
                if x == y:
                    nbridcb[j] += 1
                j += 1
            i += 1
        comb = np.zeros(len(nbridcb))
        prob = np.zeros(len(comb))
        i = 0
        while i < len(nbridcb):
            prob[i] += float(nbridcb[i] / length)
            i += 1
        try:
            with open("comments/txt/courbe_XY.bin", "wb") as file:
                pickle.dump(medianlist, file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(prob, file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        area1 = np.sort(area1)
        vaiance = np.var(area1)
        moyen = np.mean(area1)
        area2 = (area1 - moyen)/vaiance
        #ax.plot(medianlist, prob)
        ax.plot(area1, norm.pdf(area2, 0, 1))
        ax.set_ylabel("nombre d'impacts")
        ax.set_xlabel("Surface (mm²)")
        ax.set_title("Probabilité de nombre d'impacts / Surfaces")
        ax.grid()
        try:
            with open("comments/txt/surfacegraphe_XY.bin", "wb") as file:
                pickle.dump(area1, file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        canvas1 = DoubleClickreper(Figure())
        ax1 = canvas1.figure.add_subplot(111)
        toolbar1 = NavigationToolbar(canvas1, self)
        container1 = QWidget()
        lay1 = QVBoxLayout(container1)
        lay1.addWidget(canvas1)
        lay1.addWidget(toolbar1)
        self.verticalLayout_Graphe.addWidget(container1)
        container1.setMinimumWidth(100)
        ax1.plot(area1)
        ax1.set_ylabel("surface des impacts (mm²)")
        ax1.set_title("surface de chaque impact / indice des impacts")
        ax1.grid()
        self.canvaswidgetlist.insert(0, container)
        self.canvaswidgetlist.insert(1, container1)
        self.countcanvas += 1
        self.ispressed = True
        self.cotp()
        self.tabWidget.setTabEnabled(3, True)
        self.tabWidget.setTabVisible(3, True)
        self.tabWidget.setCurrentIndex(3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.messagebool:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Info sur Analyse")
            self.msg.setText(
                "C'est la fenêtre nécessaire pour afficher les résultats des analyse de l'image traité de la partie gravillonage.\n\nEn réalisant un double clique droit sur la courbe une fenêtre de commentaires sera apparue pour écrire un commentaire pour la courbe, et le commentaire sera sauvegarder et mis dans le rapport une fois sauvegardé (de même  pour l'illustration graphique).")
            self.msg.setDetailedText(
                "Résultats: Surfacemax des impacts: donne la surface la plus grande entre les impacts détécter et son indice dans le tableau d'information.\tCotation: c'est le cotation totale de la partie gravillonage.\tPerimètremax des impacts: donne le perimètre le plus grand entre les impacts détécter et son indice dans le tableau d'information. \tSurface totale: donne le surface totale de 'image en mm². \tSomme surface des impacts: c'est le somme totale des surfaces des impacts détécter.\n\nTableau d'information: numero d'impact: le logiciel met directement un indice pour chaque contour detecter.\tX et Y: les coordonnées des impacts detecter dans l'image en vue matriciel.\tperimètres: colonne du perimètre (en mm) des impacts détécter.\tsurface: colonne de surface (en mm²) des impacts détécter.\tpourcentage: signifie la surface de chaque impact par rapport à la surface totale de l’image traitée pour cent. \tCotation: la cotation de chaque impact détecter dans l’image traitée.\n\nCourbe: illustration de Probabilité de Nombre d'impacts par rapport au surfaces des impacts détécter\n\nGraphique: contient une visualisation graphique illustre les surfaces des impacts détecter dans l’image traitée.")
            self.msg.show()
        if self.countechelle == 0:
            self.defaultechelle()

    def catintable(self):
        area1 = self.area
        length = len(area1)
        list_cot = self.clist
        i = 0
        j = 1
        while i < length:
            s = 0
            while s < len(list_cot):
                if area1[i] < list_cot[s]:
                    self.tableWidget.setItem(j, 6, QTableWidgetItem(f'{s+1}'))
                    break
                s += 1
            if area1[i] > list_cot[-1]:
                self.tableWidget.setItem(j, 6, QTableWidgetItem('PAS BON'))
            i += 1
            j += 1

    def select(self):
        for i in self.tableWidget.selectedItems():
            self.selectedlist.append(i.row())
        longueure = math.fabs(self.selectedlist[0] - self.selectedlist[-1]) + 1
        if self.selectedlist[0] <= self.selectedlist[-1]:
            debut = self.selectedlist[0]
            fin = self.selectedlist[-1]
        else:
            debut = self.selectedlist[-1]
            fin = self.selectedlist[0]
        indicepremierwhile = debut
        try:
            with open('comments/txt/table.bin', 'wb') as file:
                pickle.dump(longueure, file, pickle.HIGHEST_PROTOCOL)
                while indicepremierwhile <= fin:
                    x1 = self.tableWidget.item(indicepremierwhile, 0).text()
                    x2 = self.tableWidget.item(indicepremierwhile, 1).text()
                    x3 = self.tableWidget.item(indicepremierwhile, 2).text()
                    x4 = self.tableWidget.item(indicepremierwhile, 3).text()
                    x5 = self.tableWidget.item(indicepremierwhile, 4).text()
                    x6 = self.tableWidget.item(indicepremierwhile, 5).text()
                    x7 = self.tableWidget.item(indicepremierwhile, 6).text()
                    datalist = [x1, x2, x3, x4, x5, x6, x7]
                    pickle.dump(datalist, file, pickle.HIGHEST_PROTOCOL)
                    indicepremierwhile += 1
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        self.selectedlist.clear()

    def cotationhist(self):
        if self.countcanvas > 0:
            cont = self.canvaswidgetlist(2)
            self.verticalLayout_cotation.removeWidget(cont)
        self.canvaswidgetlist.clear()
        cotation_list = []
        self.tableWidget.selectColumn(6)
        cotation_list = self.tableWidget.selectedItems().copy()
        for item in range(1, len(cotation_list)):
            cotation_list[item] = int(cotation_list[item].text())
        cotation_list[0] = 0
        canvas2 = FigureCanvas(Figure())
        ax2 = canvas2.figure.add_subplot(111)
        toolbar2 = NavigationToolbar(canvas2, self)
        container2 = QWidget()
        lay2 = QVBoxLayout(container2)
        lay2.addWidget(canvas2)
        lay2.addWidget(toolbar2)
        self.verticalLayout_cotation.addWidget(container2)
        container2.setMinimumWidth(100)
        ax2.hist(cotation_list)
        ax2.grid()
        self.canvaswidgetlist.insert(2, container2)

    def cotp(self):
        self.tableWidget.selectColumn(6)
        cotation_list = self.tableWidget.selectedItems().copy()
        for item in range(1, len(cotation_list)):
            if not cotation_list[item].text() == 'PAS BON':
                cotation_list[item] = int(cotation_list[item].text())
            else:
                cotation_list[item] = 6
        cotation_list[0] = 0
        cotation_array = np.array(cotation_list)
        unique, counts = np.unique(cotation_array, return_counts=True)
        cotation_symbole ='E'
        length = len(unique)
        if length == 1:
            cotation_number = unique[length - 1]
            if counts[length - 1] <= 9:
                cotation_symbole = 'A'
            elif 9 < counts[length - 1] <= 24:
                cotation_symbole = 'B'
            elif 24 < counts[length - 1] <= 74:
                cotation_symbole = 'C'
            elif 74 < counts[length - 1] <= 150:
                cotation_symbole = 'D'
            elif 150 < counts[length - 1]:
                cotation_symbole = 'E'
        elif length == 0:
            return None
        else:
            if counts[-1] < 74:
                cotation_number = unique[length-2]
                if counts[length-2] <= 9:
                    cotation_symbole = 'A'
                elif 9 < counts[length-2] <= 24:
                    cotation_symbole = 'B'
                elif 24 < counts[length-2] <= 74:
                    cotation_symbole = 'C'
                elif 74 < counts[length-2] <= 150:
                    cotation_symbole = 'D'
                elif 150 < counts[length-2]:
                    cotation_symbole = 'E'
            else:
                cotation_number = unique[-1]
                if 74 < counts[-1] <= 150:
                    cotation_symbole = 'D'
                elif 150 < counts[-1]:
                    cotation_symbole = 'E'
        return cotation_symbole, cotation_number

    # ###fonction_Quadrillage
    def tabChoose(self, index):
        try:
            if index == 0:
                self.hideAll()
            elif index == 1:
                self.showAll()
                self.hideHVU()
            else:
                if self.Img_trait_2.pixmap() or self.Img_bin.pixmap():
                    self.showAll()
                    self.showHVU()
                else:
                    self.showAll()
                    self.hideHVU()
        except Exception as err:
            print(err)
    # ##Fonction quadrillage
    def hideAll(self):
        self.parametre_groupBox.hide()
        self.autres_groupBox.hide()
        self.Resultats_groupBox.hide()
        self.Commentaire_groupBox.hide()
        self.comBox_quad.hide()

    def showAll(self):
        self.parametre_groupBox.show()
        self.autres_groupBox.show()
        self.Resultats_groupBox.show()
        self.Commentaire_groupBox.show()
        self.comBox_quad.show()

    def showHVU(self):
        self.Horizontale_label.setEnabled(True)
        self.h_horizontalSlider.setEnabled(True)
        self.h_spinBox.setEnabled(True)
        self.Vertical_label.setEnabled(True)
        self.v_horizontalSlider.setEnabled(True)
        self.v_spinBox.setEnabled(True)
        self.Expension_label.setEnabled(True)
        self.e_horizontalSlider.setEnabled(True)
        self.e_spinBox.setEnabled(True)
        self.saveactionappear()

    def hideHVU(self):
        self.Horizontale_label.setEnabled(False)
        self.h_horizontalSlider.setEnabled(False)
        self.h_spinBox.setEnabled(False)
        self.Vertical_label.setEnabled(False)
        self.v_horizontalSlider.setEnabled(False)
        self.v_spinBox.setEnabled(False)
        self.Expension_label.setEnabled(False)
        self.e_horizontalSlider.setEnabled(False)
        self.e_spinBox.setEnabled(False)

    def bg_color(self):
        if self.dark_radio_button.isChecked():
            self.background_Color = 1
        else:
            self.background_Color = 0

    def defaultCautation_quad(self):
        if self.Img_trait_2.pixmap():
            self.percent = get_surface(self.self_img_trait)
            self.listInfoInt = [0, 5, 15, 35, 65]
            self.listInfoSym = ['a', 'b', 'c', 'd', 'e']
            self.classification()
            self.cautationName = 'Défaut(Stellantis)'
            self.showResult()

    def openCautation(self):
        try:
            with open(self.cautationName, 'rb') as file:
                info = pickle.load(file)
        except (IOError, pickle.UnpicklingError):
            print('Erreur de lecture.')
        self.listInfoInt = []
        self.listInfoSym = []
        i = 0
        while i < len(info):
            self.listInfoInt.insert(i, int(info[i][0]))
            self.listInfoSym.insert(i, str(info[i][1]))
            i += 1
        if self.Img_trait_2.pixmap():
            self.percent = get_surface(self.self_img_trait)
            self.classification()
            self.showResult()

    def classification(self):
        i = 0
        lenArr = len(self.listInfoInt) - 1
        while i < lenArr:
            if self.percent <= self.listInfoInt[i]:
                self.niveau = self.listInfoSym[i]
                break
            if self.percent > self.listInfoInt[lenArr - i]:
                self.niveau = '> ' + self.listInfoSym[lenArr - i]
                break
            i += 1

    def showResult(self):
        # self.result_label.setText(res_str)
        v = Decimal(self.percent)
        varr = v.quantize(Decimal('.000001'), rounding=ROUND_HALF_UP)
        self.surface_label.setText('Surface: 'f'{varr} %')
        self.classification_label.setText('Cotation: 'f'{self.niveau}')
        self.norme_label.setText('Norme: 'f'{self.cautationName}')

    def saveResult(self):
        try:
            with open('txt/horizontaleslider.bin', 'wb') as file:
                pickle.dump(self.t_horizontalSlider.value(), file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.h_horizontalSlider.value(), file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.v_horizontalSlider.value(), file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        if not self.percent == '> 70%':
            v = Decimal(self.percent)
            self.percent = v.quantize(Decimal('.000001'), rounding=ROUND_HALF_UP)
        try:
            with open('txt/cotationquadrillage.bin', 'wb') as file:
                pickle.dump(self.cautationName, file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.niveau, file, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.percent, file, pickle.HIGHEST_PROTOCOL)

        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')
        s = (self.textEdit_commentaire.toPlainText())
        myFile = open("comments/txt/commentquadrillage.txt", "w")
        myFile.write(s)
        myFile.close()
        cv2.imwrite('img\Img_trait.png',self.self_img_trait)

    def changeVal(self, value):
        value = int(value)
        sender = self.sender()
        if sender == self.h_horizontalSlider or sender == self.h_spinBox:
            self.h_horizontalSlider.setValue(value)
            self.h_spinBox.setValue(value)
            self.deleteLineButton_function()
            self.save_tree_in_file()
        elif sender == self.v_horizontalSlider or sender == self.v_spinBox:
            self.v_horizontalSlider.setValue(value)
            self.v_spinBox.setValue(value)
            self.deleteLineButton_function()
            self.save_tree_in_file()
        elif sender == self.t_horizontalSlider or sender == self.t_spinBox:
            self.t_horizontalSlider.setValue(value)
            self.t_spinBox.setValue(value)
            self.changeThresh(value)
            self.save_tree_in_file()
            index = self.tabWidget_Image.currentIndex()
            if index == 2 or index == 3:
                self.showHVU()
        else:
            self.e_horizontalSlider.setValue(value)
            self.e_spinBox.setValue(value)
            self.delete_unexpected_lines(value)
            self.save_tree_in_file()
        self.saveactionappear()
        self.save_tree_in_file()

    def changeThresh(self, thresh_value):
        thresh_value = int(thresh_value)
        if self.self_img_original is None:
            return None
        self.thresh_changed = True
        self.thresh = img_binary(self.self_img_original, thresh_value, 255, self.background_Color)
        img_bi = self.convert_nparray_to_QPixmap_Quadrillage(self.thresh)
        self.save_tree_in_file()
        if self.Img_trait_2.pixmap():
            if get_surface(self.thresh) >= 70:

                self.percent = '> 70%'
                self.niveau = '> e '
                # self.result_label.setText(res_str)
                self.surface_label.setText('Surface: 'f'{self.percent} %')
                self.classification_label.setText('Cotation: 'f'{self.niveau}')
                self.save_tree_in_file()
            else:
                self.deleteLineButton_function()
                self.save_tree_in_file()
        else:
            self.Img_trait_2.setPixmap(img_bi)
            self.save_tree_in_file()
        self.Img_bin.setPixmap(img_bi)
        self.save_tree_in_file()

    def delete_unexpected_lines(self, value):
        if self.thresh is None:
            return None
        self.self_img_trait = morph_close_cross(self.thresh, value)
        self.Img_trait_2.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(self.self_img_trait))
        self.save_tree_in_file()

    def deleteLineButton_function(self):
        if self.self_img_original is None:
            return None
        if self.thresh is None:
            return None
        h_value = int(self.h_horizontalSlider.value())
        v_value = int(self.v_horizontalSlider.value())
        self.self_img_trait = delete_line(self.thresh, h_value, v_value, 5)
        self.Img_trait_2.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(self.self_img_trait))
        QIm_draw = draw_contours(self.self_img_trait, self.self_img_original)
        self.Img_cont.setPixmap(self.convert_nparray_to_QPixmap_Quadrillage(QIm_draw))
        cv2.imwrite('img\QIm_draw.png',QIm_draw)
        self.percent = get_surface(self.self_img_trait)
        self.classification()
        self.showResult()
        self.save_tree_in_file()

    # ##fonctionCotation
    def opencot(self):
        _translate = QtCore.QCoreApplication.translate
        cautName, cautType = QFileDialog.getOpenFileName(self, "Import cotation", ".",
                                                         "*.bin;;;All Files(*)")
        if cautName == "":
            return 0
        try:
            with open(cautName, 'rb') as file:
                self.info = pickle.load(file)
                self.b = pickle.load(file)
                self.q = pickle.load(file)
        except (IOError, pickle.UnpicklingError):
            print('Erreur de lecture.')
        if self.ispressed:
            if self.b == False and self.q == False:
                l = len(self.info)
                listinfint = []
                listinfosym = []
                i = 0
                while i < l:
                    listinfint.insert(i, int(self.info[i][0]))
                    listinfosym.insert(i, int(self.info[i][1]))
                    i += 1
                i = 0
                self.caut.setText(_translate("MainWindow", 'Cotation:   'f'{self.cautp}_'f'{self.sym}'))
            elif self.b == True and self.q == False:
                l = len(self.info)
                listinfint = []
                listinfosym = []
                i = 0
                while i < l:
                    listinfint.insert(i, float(self.info[i][0]))
                    listinfosym.insert(i, str(self.info[i][1]))
                    i += 1
                area1 = self.area
                length = self.length
                i = 0
                j = 1
                while i < length:
                    s = 0
                    while s < l:
                        if area1[i] < float(listinfint[s]):
                            self.tableWidget.setItem(j, 6, QTableWidgetItem(f'{listinfosym[s]}'))
                            break
                        s += 1
                    if area1[i] > float(listinfint[-1]):
                        self.tableWidget.setItem(j, 6, QTableWidgetItem('PAS BON'))
                    i += 1
                    j += 1
            else:
                self.listInfoInt = []
                self.listInfoSym = []
                i = 0
                while i < len(self.info):
                    self.listInfoInt.insert(i, int(self.info[i][0]))
                    self.listInfoSym.insert(i, str(self.info[i][1]))
                    i += 1
                if self.Img_trait_2.pixmap():
                    self.percent = get_surface(self.self_img_trait)
                    self.classification()
                    self.showResult()
        else:
            return None

    def NouveauCotation(self):
        self.windowcotation = cotationWindow()
        self.windowcotation.show()

    def Default(self):
        if self.ispressed:
            self.sym, self.cautp = self.cotp()
            self.caut.setText('Cotation:   'f'{self.cautp}_'f'{self.sym}')
            self.catintable()
            self.defaultCautation_quad()
        else:
            return None

    # ##Echelle
    def openechelle(self):
        _translate = QtCore.QCoreApplication.translate
        echelleName, echelleType = QFileDialog.getOpenFileName(self, "Import echelle", ".", "*.bin;;;All Files(*)")
        if echelleName == "":
            return None
        try:
            with open(echelleName, 'rb') as file:
                long = pickle.load(file)
                larg = pickle.load(file)
        except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
        if type(long) == int and type(larg) == int:
            if long / 1000 < 1 and larg / 1000 < 1:
                if self.imgName == '':
                    return None
                else:
                    im = cv2.imread(self.imgName)
                    sp = int(im.shape[1]) * int(im.shape[0])

                    div = (long * larg) / sp
                    echelle = math.sqrt(div)
                    try:
                        with open('txt/echell.bin', 'wb') as file:
                            pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
                    except (IOError, pickle.PicklingError):
                            print('Erreur d\'écriture.')
                    if self.label.pixmap():
                        self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(
                            self.value[0],
                            self.value[1],
                            self.value[2])
                        self.tablecreation()
                    self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')

            else:
                return None
        else:
            return None

    def nouveauechelle(self):
        self.echelle = None
        self.echelle = echelle()
        self.echelle.show()

    def defaultechelle(self):
        if self.ispressed:
            im = cv2.imread(self.imgName)
            try:
                with open('txt/defaultechelle.bin', 'rb') as file:
                    long = pickle.load(file)
                    larg = pickle.load(file)
                    ech = pickle.load(file)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')
            sp = int(im.shape[0]) * int(im.shape[1])
            div = (long * larg) / sp
            echelle = math.sqrt(div)
            self.echelle_number = echelle
            try:
                with open('txt/echell.bin', 'wb') as file:
                    pickle.dump(echelle, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
            self.label_3.setText('Echelle: 'f'{long}x'f'{larg} mm²')
            if self.label.pixmap():
                self.data, self.cx, self.cy, self.img, self.length, self.area, self.perimetre = main(self.value[0],
                                                                                                     self.value[1],
                                                                                                     self.value[2])
                self.countechelle += 1
                self.tablecreation()

    def messageinfoappear(self):
        if self.messagebool == False:
            self.messagebool = True
            self.label_aide.setVisible(True)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Information")
            self.msg.setText(
                "Le mode d'aide est activé, maintenant dans chaque fenêtre du logiciel une boîte de message d'information devrait apparaître pour expliquer la fonctionnalité de cette fenêtre.\n\n"
                "Pour commencer importer une image de plaque puis choisir de l'image avec un rectangle rouge l'échantillon à traiter: \n"
                "* Si l'échantillon est gravillonné cliquer sur le bouton gravillonnage au dessus de fenêtre principale pour passer au fenêtre gravillonnage.\n"
                "* Si l'échantillon est quadrillé cliquer sur le bouton quadrillage au dessus de fenêtre principale pour passer au fenêtre quadrillage.")
            self.msg.show()
        else:
            self.messagebool = False
            self.label_aide.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
