# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sean/code/pharynx_redox/pharynx_redox/gui/qt_ui_files/image_stack_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XArrayDisplayWidget(object):
    def setupUi(self, XArrayDisplayWidget):
        XArrayDisplayWidget.setObjectName("XArrayDisplayWidget")
        XArrayDisplayWidget.resize(1680, 1005)
        self.horizontalLayout = QtWidgets.QHBoxLayout(XArrayDisplayWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(XArrayDisplayWidget)
        self.widget.setMinimumSize(QtCore.QSize(200, 0))
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.wvlBox = QtWidgets.QComboBox(self.groupBox_2)
        self.wvlBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wvlBox.setObjectName("wvlBox")
        self.verticalLayout_3.addWidget(self.wvlBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pairSlider = QtWidgets.QSlider(self.groupBox_2)
        self.pairSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pairSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pairSlider.setObjectName("pairSlider")
        self.verticalLayout_3.addWidget(self.pairSlider)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(XArrayDisplayWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.ImageViewBox = ImageView(self.tab)
        self.ImageViewBox.setMinimumSize(QtCore.QSize(400, 0))
        self.ImageViewBox.setObjectName("ImageViewBox")
        self.gridLayout.addWidget(self.ImageViewBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(XArrayDisplayWidget)
        QtCore.QMetaObject.connectSlotsByName(XArrayDisplayWidget)

    def retranslateUi(self, XArrayDisplayWidget):
        _translate = QtCore.QCoreApplication.translate
        XArrayDisplayWidget.setWindowTitle(_translate("XArrayDisplayWidget", "Form"))
        self.groupBox_2.setTitle(_translate("XArrayDisplayWidget", "Controls"))
        self.label.setText(_translate("XArrayDisplayWidget", "Wavelength"))
        self.label_2.setText(_translate("XArrayDisplayWidget", "Pair"))
        self.pushButton.setText(_translate("XArrayDisplayWidget", "View Mask"))
        self.groupBox.setTitle(_translate("XArrayDisplayWidget", "Properties"))
        self.label_4.setText(_translate("XArrayDisplayWidget", "property"))
        self.label_3.setText(_translate("XArrayDisplayWidget", "value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("XArrayDisplayWidget", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("XArrayDisplayWidget", "Tab 2"))

from pyqtgraph import ImageView
