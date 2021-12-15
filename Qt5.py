from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import getgcpprojects

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("K8SConnect-Discover")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        self.lblproject = QLabel(self)
        # setting geometry of the label
        self.lblproject.setGeometry(20, 15, 500, 100)
        self.lblproject.setText("Select GCP Project:")

        # creating a combo box widget
        self.cboproject = QComboBox(self)

        # setting geometry of combo box
        self.cboproject.setGeometry(120, 50, 200, 25)

        # geek list
        geek_list = getgcpprojects.getProjectList()

        # adding list of items to combo box
        self.cboproject.addItems(geek_list)
        # k8s
        self.lblK8S = QLabel(self)
        self.lblK8S.setGeometry(20, 55, 500, 100)
        self.lblK8S.setText("Select K8S:")
        self.cbok8slist = QComboBox(self)
        self.cbok8slist.setGeometry(120, 90, 200, 25)
        # NS

        project = self.cboproject.currentText()
        k8slist = getgcpprojects.getK8SClusterList(project)
        self.cbok8slist.clear()
        self.cbok8slist.addItems(k8slist)

        # creating push button
        button = QPushButton("Connect", self)

        print(self.cboproject.count())

        # adding action to button
        button.pressed.connect(self.connect)
        button.setGeometry(120, 140, 100, 25)
        self.cboproject.activated.connect(self.getk8s)

        # creating label to
        self.label = QLabel(self)

        # setting geometry of the label
        self.label.setGeometry(120, 170, 500, 100)

    def connect(self):
        # finding the content of current item in combo box
        project = self.cboproject.currentText()
        k8s = self.cbok8slist.currentText()
        cluster = k8s.replace("\r", "") .replace("\n","")
        print("Cluster", cluster)
        # showing content on the screen though label
        self.label.setText("Connecting  : " + cluster + " in " + project + "..")
        self.label.setText("Connecting  : " + cluster + " in " + project + "....")
        k8sconnect = "gcloud container clusters get-credentials " + cluster + " --project " + project
        self.label.setText(k8sconnect)

        getgcpprojects.connectK8S(cluster, project)

    def getk8s(self):
        project = self.cboproject.currentText()
        k8slist = getgcpprojects.getK8SClusterList(project)
        self.cbok8slist.clear()
        self.cbok8slist.addItems(k8slist)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
