# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sean/code/pharynx_redox/pharynx_redox/gui/qt_ui_files/load_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 228)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.experimentDirectoryLabel = QtWidgets.QLabel(Dialog)
        self.experimentDirectoryLabel.setObjectName("experimentDirectoryLabel")
        self.horizontalLayout.addWidget(self.experimentDirectoryLabel)
        self.experimentDirectoryLineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentDirectoryLineEdit.sizePolicy().hasHeightForWidth())
        self.experimentDirectoryLineEdit.setSizePolicy(sizePolicy)
        self.experimentDirectoryLineEdit.setObjectName("experimentDirectoryLineEdit")
        self.horizontalLayout.addWidget(self.experimentDirectoryLineEdit)
        self.dirSelectToolButton = QtWidgets.QToolButton(Dialog)
        self.dirSelectToolButton.setObjectName("dirSelectToolButton")
        self.horizontalLayout.addWidget(self.dirSelectToolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.runButton = QtWidgets.QPushButton(Dialog)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_2.addWidget(self.runButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Analyze Experiment"))
        self.label.setText(_translate("Dialog", "Run analysis on an image stack."))
        self.experimentDirectoryLabel.setText(_translate("Dialog", "Experiment Directory"))
        self.dirSelectToolButton.setText(_translate("Dialog", "..."))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.runButton.setText(_translate("Dialog", "Run"))