import sys
import getgcpprojects

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5 import QtGui, QtCore

from pyqt5_plugins.examplebuttonplugin import QtGui


class mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(200, 200))
        self.setWindowTitle("")
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Select GCP Project:", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)
        self.cb1 = bindprojects()
        gridLayout.addWidget(self.cb1, 0, 1)
        self.cb1.currentIndexChanged.connect(bindK8s)
        currentproject = self.cb1.currentText()
        print(currentproject)
        self.cb2 = bindK8s(currentproject)
        self.cb2.currentIndexChanged.connect(bindns)
        gridLayout.addWidget(self.cb2, 0, 3)
        title1 = QLabel("Select K8S:", self)
        title1.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title1, 0, 2)


def bindprojects():
    prjlist = getgcpprojects.getProjectList()
    cb = QtWidgets.QComboBox()
    for prj in prjlist:
        cb.addItem(prj)
    cb.move(50, 250)
    # comboBox.activated[str].connect(obj.style_choice)
    return cb


def bindK8s(project):
    print("list of project", project)

    k8s = getgcpprojects.getK8SClusterList(project)
    cb = QtWidgets.QComboBox()
    for k8 in k8s:
        print(k8)
        cb.addItem(k8)
    cb.move(50, 250)
    bindevents(cb)
    return cb


def bindns(k8s):
    print("k8s selected")


def bindevents(cb):
    print("calling bind events")
    cb.currentIndexChanged.connect(updateK8SList)


def updateK8SList():
    print("calling update k8s list")
    #bindK8s(self.cb1.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = mainwindow()
    mainWin.show()
    bindprojects()
    sys.exit(app.exec_())
