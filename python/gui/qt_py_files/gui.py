# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sean/code/wormAnalysis/python/gui/qt_ui_files/gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1035)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("assets/4x/icon@4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imagesGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.imagesGroupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.imagesGroupBox.setObjectName("imagesGroupBox")
        self.widget = QtWidgets.QWidget(self.imagesGroupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 481, 921))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addWidget(self.imagesGroupBox)
        self.plotsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.plotsGroupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.plotsGroupBox.setObjectName("plotsGroupBox")
        self.widget1 = QtWidgets.QWidget(self.plotsGroupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 30, 481, 921))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.plotsGroupBox)
        self.parametersLayout = QtWidgets.QVBoxLayout()
        self.parametersLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.parametersLayout.setObjectName("parametersLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.parametersLayout.addItem(spacerItem)
        self.flipLRpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.flipLRpushButton.setObjectName("flipLRpushButton")
        self.parametersLayout.addWidget(self.flipLRpushButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveMidlinesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveMidlinesPushButton.setObjectName("saveMidlinesPushButton")
        self.horizontalLayout_3.addWidget(self.saveMidlinesPushButton)
        self.resetMidlinesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetMidlinesPushButton.setObjectName("resetMidlinesPushButton")
        self.horizontalLayout_3.addWidget(self.resetMidlinesPushButton)
        self.parametersLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.i410_1MidlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.i410_1MidlineLabel.setObjectName("i410_1MidlineLabel")
        self.formLayout_6.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.i410_1MidlineLabel
        )
        self.i410_1MidlineComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.i410_1MidlineComboBox.setObjectName("i410_1MidlineComboBox")
        self.i410_1MidlineComboBox.addItem("")
        self.i410_1MidlineComboBox.addItem("")
        self.formLayout_6.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.i410_1MidlineComboBox
        )
        self.i470_1MidlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.i470_1MidlineLabel.setObjectName("i470_1MidlineLabel")
        self.formLayout_6.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.i470_1MidlineLabel
        )
        self.i470_1MidlineComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.i470_1MidlineComboBox.setObjectName("i470_1MidlineComboBox")
        self.i470_1MidlineComboBox.addItem("")
        self.i470_1MidlineComboBox.addItem("")
        self.formLayout_6.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.i470_1MidlineComboBox
        )
        self.horizontalLayout_6.addLayout(self.formLayout_6)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.i410_2MidlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.i410_2MidlineLabel.setObjectName("i410_2MidlineLabel")
        self.formLayout_7.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.i410_2MidlineLabel
        )
        self.i410_2MidlineComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.i410_2MidlineComboBox.setObjectName("i410_2MidlineComboBox")
        self.i410_2MidlineComboBox.addItem("")
        self.i410_2MidlineComboBox.addItem("")
        self.formLayout_7.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.i410_2MidlineComboBox
        )
        self.i470_2MidlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.i470_2MidlineLabel.setObjectName("i470_2MidlineLabel")
        self.formLayout_7.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.i470_2MidlineLabel
        )
        self.i470_2MidlineComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.i470_2MidlineComboBox.setObjectName("i470_2MidlineComboBox")
        self.i470_2MidlineComboBox.addItem("")
        self.i470_2MidlineComboBox.addItem("")
        self.formLayout_7.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.i470_2MidlineComboBox
        )
        self.horizontalLayout_6.addLayout(self.formLayout_7)
        self.parametersLayout.addLayout(self.horizontalLayout_6)
        self.showSegcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.showSegcheckBox.setObjectName("showSegcheckBox")
        self.parametersLayout.addWidget(self.showSegcheckBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.parametersLayout.addWidget(self.line)
        self.movementAnnotationLabel = QtWidgets.QLabel(self.centralwidget)
        self.movementAnnotationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.movementAnnotationLabel.setObjectName("movementAnnotationLabel")
        self.parametersLayout.addWidget(self.movementAnnotationLabel)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.FieldsStayAtSizeHint
        )
        self.formLayout_4.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout_4.setObjectName("formLayout_4")
        self.posteriorBulbLabel = QtWidgets.QLabel(self.centralwidget)
        self.posteriorBulbLabel.setObjectName("posteriorBulbLabel")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.posteriorBulbLabel
        )
        self.posteriorBulbSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.posteriorBulbSpinBox.setMaximum(3)
        self.posteriorBulbSpinBox.setObjectName("posteriorBulbSpinBox")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.posteriorBulbSpinBox
        )
        self.metacorpusLabel = QtWidgets.QLabel(self.centralwidget)
        self.metacorpusLabel.setObjectName("metacorpusLabel")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.metacorpusLabel
        )
        self.metacorpusSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.metacorpusSpinBox.setMaximum(3)
        self.metacorpusSpinBox.setObjectName("metacorpusSpinBox")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.metacorpusSpinBox
        )
        self.procorpusLabel = QtWidgets.QLabel(self.centralwidget)
        self.procorpusLabel.setObjectName("procorpusLabel")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.procorpusLabel
        )
        self.procorpusSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.procorpusSpinBox.setMaximum(3)
        self.procorpusSpinBox.setObjectName("procorpusSpinBox")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.procorpusSpinBox
        )
        self.parametersLayout.addLayout(self.formLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.parametersLayout.addWidget(self.line_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow
        )
        self.formLayout_3.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.formLayout_3.setObjectName("formLayout_3")
        self.midlineSplineTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.midlineSplineTypeLabel.setObjectName("midlineSplineTypeLabel")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.midlineSplineTypeLabel
        )
        self.midlineSplineTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.midlineSplineTypeComboBox.setObjectName("midlineSplineTypeComboBox")
        self.midlineSplineTypeComboBox.addItem("")
        self.midlineSplineTypeComboBox.addItem("")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.midlineSplineTypeComboBox
        )
        self.nPointsToMeasureLabel = QtWidgets.QLabel(self.centralwidget)
        self.nPointsToMeasureLabel.setObjectName("nPointsToMeasureLabel")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.nPointsToMeasureLabel
        )
        self.nPointsToMeasureSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.nPointsToMeasureSpinBox.setMinimum(100)
        self.nPointsToMeasureSpinBox.setMaximum(5000)
        self.nPointsToMeasureSpinBox.setSingleStep(100)
        self.nPointsToMeasureSpinBox.setObjectName("nPointsToMeasureSpinBox")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.nPointsToMeasureSpinBox
        )
        self.i410ThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.i410ThresholdLabel.setObjectName("i410ThresholdLabel")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.i410ThresholdLabel
        )
        self.i410ThresholdSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.i410ThresholdSpinBox.setMaximum(10000)
        self.i410ThresholdSpinBox.setSingleStep(100)
        self.i410ThresholdSpinBox.setProperty("value", 2000)
        self.i410ThresholdSpinBox.setObjectName("i410ThresholdSpinBox")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.i410ThresholdSpinBox
        )
        self.i470ThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.i470ThresholdLabel.setObjectName("i470ThresholdLabel")
        self.formLayout_3.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.i470ThresholdLabel
        )
        self.i470ThresholdSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.i470ThresholdSpinBox.setMaximum(10000)
        self.i470ThresholdSpinBox.setSingleStep(100)
        self.i470ThresholdSpinBox.setProperty("value", 2000)
        self.i470ThresholdSpinBox.setObjectName("i470ThresholdSpinBox")
        self.formLayout_3.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.i470ThresholdSpinBox
        )
        self.frameSpecificCentroidsLabel = QtWidgets.QLabel(self.centralwidget)
        self.frameSpecificCentroidsLabel.setObjectName("frameSpecificCentroidsLabel")
        self.formLayout_3.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.frameSpecificCentroidsLabel
        )
        self.frameSpecificCentroidsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.frameSpecificCentroidsCheckBox.setObjectName(
            "frameSpecificCentroidsCheckBox"
        )
        self.formLayout_3.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.frameSpecificCentroidsCheckBox
        )
        self.frameSpecificOrientationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.frameSpecificOrientationsLabel.setObjectName(
            "frameSpecificOrientationsLabel"
        )
        self.formLayout_3.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.frameSpecificOrientationsLabel
        )
        self.frameSpecificOrientationsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.frameSpecificOrientationsCheckBox.setObjectName(
            "frameSpecificOrientationsCheckBox"
        )
        self.formLayout_3.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.frameSpecificOrientationsCheckBox
        )
        self.parametersLayout.addLayout(self.formLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.parametersLayout.addWidget(self.line_3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.parametersLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.parametersLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.parametersLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.parametersLayout)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Raw_Image_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_Raw_Image_File.setObjectName("actionLoad_Raw_Image_File")
        self.actionLoad_Previous_Experiment = QtWidgets.QAction(MainWindow)
        self.actionLoad_Previous_Experiment.setObjectName(
            "actionLoad_Previous_Experiment"
        )
        self.actionSave_Experiment = QtWidgets.QAction(MainWindow)
        self.actionSave_Experiment.setObjectName("actionSave_Experiment")
        self.menuFile.addAction(self.actionLoad_Raw_Image_File)
        self.menuFile.addAction(self.actionLoad_Previous_Experiment)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Experiment)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Worm De-Wiggler"))
        self.imagesGroupBox.setTitle(_translate("MainWindow", "Images"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Rotated / Aligned Images"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Raw Images"))
        self.plotsGroupBox.setTitle(_translate("MainWindow", "Plots"))
        self.groupBox.setTitle(_translate("MainWindow", "Intensity"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Redox Potential"))
        self.flipLRpushButton.setText(_translate("MainWindow", "Flip L/R"))
        self.saveMidlinesPushButton.setText(_translate("MainWindow", "Save Midlines"))
        self.resetMidlinesPushButton.setText(_translate("MainWindow", "Reset Midlines"))
        self.i410_1MidlineLabel.setText(_translate("MainWindow", "i410_1 Midline"))
        self.i410_1MidlineComboBox.setItemText(0, _translate("MainWindow", "410_1"))
        self.i410_1MidlineComboBox.setItemText(1, _translate("MainWindow", "470_1"))
        self.i470_1MidlineLabel.setText(_translate("MainWindow", "470_1 Midline"))
        self.i470_1MidlineComboBox.setItemText(0, _translate("MainWindow", "470_1"))
        self.i470_1MidlineComboBox.setItemText(1, _translate("MainWindow", "410_1"))
        self.i410_2MidlineLabel.setText(_translate("MainWindow", "410_2 Midline"))
        self.i410_2MidlineComboBox.setItemText(0, _translate("MainWindow", "410_2"))
        self.i410_2MidlineComboBox.setItemText(1, _translate("MainWindow", "470_2"))
        self.i470_2MidlineLabel.setText(_translate("MainWindow", "470_2 Midline"))
        self.i470_2MidlineComboBox.setItemText(0, _translate("MainWindow", "470_2"))
        self.i470_2MidlineComboBox.setItemText(1, _translate("MainWindow", "410_2"))
        self.showSegcheckBox.setText(_translate("MainWindow", "Show Segmentation"))
        self.movementAnnotationLabel.setText(
            _translate("MainWindow", "Movement Annotation")
        )
        self.posteriorBulbLabel.setText(_translate("MainWindow", "Posterior Bulb"))
        self.metacorpusLabel.setText(_translate("MainWindow", "Metacorpus"))
        self.procorpusLabel.setText(_translate("MainWindow", "Procorpus"))
        self.midlineSplineTypeLabel.setText(
            _translate("MainWindow", "Measurement Interp")
        )
        self.midlineSplineTypeComboBox.setItemText(
            0, _translate("MainWindow", "Linear")
        )
        self.midlineSplineTypeComboBox.setItemText(1, _translate("MainWindow", "Cubic"))
        self.nPointsToMeasureLabel.setText(
            _translate("MainWindow", "N Points to Measure")
        )
        self.i410ThresholdLabel.setText(_translate("MainWindow", "i410 Threshold"))
        self.i470ThresholdLabel.setText(_translate("MainWindow", "i470 Threshold"))
        self.frameSpecificCentroidsLabel.setText(
            _translate("MainWindow", "Frame-Specific Centroids")
        )
        self.frameSpecificOrientationsLabel.setText(
            _translate("MainWindow", "Frame-Specific Orientations")
        )
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Index"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Strain"))
        self.label.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Raw_Image_File.setText(
            _translate("MainWindow", "Load Raw Image File")
        )
        self.actionLoad_Raw_Image_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionLoad_Previous_Experiment.setText(
            _translate("MainWindow", "Load Previous Experiment")
        )
        self.actionLoad_Previous_Experiment.setShortcut(
            _translate("MainWindow", "Ctrl+Shift+O")
        )
        self.actionSave_Experiment.setText(_translate("MainWindow", "Save Experiment"))
        self.actionSave_Experiment.setShortcut(_translate("MainWindow", "Ctrl+S"))
