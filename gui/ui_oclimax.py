# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oclimax.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OCLIMAX(object):
    def setupUi(self, OCLIMAX):
        OCLIMAX.setObjectName("OCLIMAX")
        OCLIMAX.resize(697, 484)
        self.verticalLayout = QtWidgets.QVBoxLayout(OCLIMAX)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(OCLIMAX)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_mesh1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_mesh1.setMinimum(1)
        self.spinBox_mesh1.setObjectName("spinBox_mesh1")
        self.horizontalLayout.addWidget(self.spinBox_mesh1)
        self.spinBox_mesh2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_mesh2.setMinimum(1)
        self.spinBox_mesh2.setObjectName("spinBox_mesh2")
        self.horizontalLayout.addWidget(self.spinBox_mesh2)
        self.spinBox_mesh3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_mesh3.setMinimum(1)
        self.spinBox_mesh3.setObjectName("spinBox_mesh3")
        self.horizontalLayout.addWidget(self.spinBox_mesh3)
        self.pushButton_ph_default = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ph_default.setObjectName("pushButton_ph_default")
        self.horizontalLayout.addWidget(self.pushButton_ph_default)
        self.pushButton_ph_save = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ph_save.setObjectName("pushButton_ph_save")
        self.horizontalLayout.addWidget(self.pushButton_ph_save)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(OCLIMAX)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Emax = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Emax.setObjectName("lineEdit_Emax")
        self.gridLayout.addWidget(self.lineEdit_Emax, 7, 2, 1, 1)
        self.lineEdit_Eres = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Eres.setObjectName("lineEdit_Eres")
        self.gridLayout.addWidget(self.lineEdit_Eres, 10, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_output = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.gridLayout.addWidget(self.lineEdit_output, 0, 4, 1, 1)
        self.lineEdit_temp = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.gridLayout.addWidget(self.lineEdit_temp, 1, 2, 1, 1)
        self.lineEdit_maxo = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_maxo.setObjectName("lineEdit_maxo")
        self.gridLayout.addWidget(self.lineEdit_maxo, 1, 4, 1, 1)
        self.lineEdit_Emin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Emin.setObjectName("lineEdit_Emin")
        self.gridLayout.addWidget(self.lineEdit_Emin, 6, 2, 1, 1)
        self.lineEdit_Qmax = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Qmax.setObjectName("lineEdit_Qmax")
        self.gridLayout.addWidget(self.lineEdit_Qmax, 7, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)
        self.lineEdit_Qres = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Qres.setObjectName("lineEdit_Qres")
        self.gridLayout.addWidget(self.lineEdit_Qres, 10, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.comboBox_task = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_task.setObjectName("comboBox_task")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.gridLayout.addWidget(self.comboBox_task, 0, 2, 1, 1)
        self.comboBox_Eunit = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Eunit.setObjectName("comboBox_Eunit")
        self.comboBox_Eunit.addItem("")
        self.comboBox_Eunit.addItem("")
        self.comboBox_Eunit.addItem("")
        self.gridLayout.addWidget(self.comboBox_Eunit, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.lineEdit_dQ = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dQ.setObjectName("lineEdit_dQ")
        self.gridLayout.addWidget(self.lineEdit_dQ, 9, 4, 1, 1)
        self.lineEdit_Qmin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Qmin.setObjectName("lineEdit_Qmin")
        self.gridLayout.addWidget(self.lineEdit_Qmin, 6, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.lineEdit_theta = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_theta.setObjectName("lineEdit_theta")
        self.gridLayout.addWidget(self.lineEdit_theta, 3, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 3, 1, 1)
        self.lineEdit_mask = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.gridLayout.addWidget(self.lineEdit_mask, 3, 2, 1, 1)
        self.lineEdit_dE = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dE.setObjectName("lineEdit_dE")
        self.gridLayout.addWidget(self.lineEdit_dE, 9, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)
        self.lineEdit_Ei = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Ei.setObjectName("lineEdit_Ei")
        self.gridLayout.addWidget(self.lineEdit_Ei, 5, 2, 1, 1)
        self.lineEdit_Ecut = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Ecut.setObjectName("lineEdit_Ecut")
        self.gridLayout.addWidget(self.lineEdit_Ecut, 5, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 3, 1, 1)
        self.lineEdit_norm = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_norm.setObjectName("lineEdit_norm")
        self.gridLayout.addWidget(self.lineEdit_norm, 4, 4, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_oclimax_load = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_oclimax_load.setObjectName("pushButton_oclimax_load")
        self.horizontalLayout_2.addWidget(self.pushButton_oclimax_load)
        self.pushButton_oclimax_default = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_oclimax_default.setObjectName("pushButton_oclimax_default")
        self.horizontalLayout_2.addWidget(self.pushButton_oclimax_default)
        self.pushButton_oclimax_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_oclimax_save.setObjectName("pushButton_oclimax_save")
        self.horizontalLayout_2.addWidget(self.pushButton_oclimax_save)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Q2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q2.setObjectName("lineEdit_Q2")
        self.gridLayout_2.addWidget(self.lineEdit_Q2, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 4, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 5, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.lineEdit_Q1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q1.setObjectName("lineEdit_Q1")
        self.gridLayout_2.addWidget(self.lineEdit_Q1, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 7, 0, 1, 1)
        self.lineEdit_Q1bin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q1bin.setObjectName("lineEdit_Q1bin")
        self.gridLayout_2.addWidget(self.lineEdit_Q1bin, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.lineEdit_Q3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q3.setObjectName("lineEdit_Q3")
        self.gridLayout_2.addWidget(self.lineEdit_Q3, 2, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 8, 0, 1, 1)
        self.lineEdit_Q2bin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q2bin.setObjectName("lineEdit_Q2bin")
        self.gridLayout_2.addWidget(self.lineEdit_Q2bin, 4, 1, 1, 1)
        self.lineEdit_Q3bin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Q3bin.setObjectName("lineEdit_Q3bin")
        self.gridLayout_2.addWidget(self.lineEdit_Q3bin, 5, 1, 1, 1)
        self.lineEdit_Ebin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Ebin.setObjectName("lineEdit_Ebin")
        self.gridLayout_2.addWidget(self.lineEdit_Ebin, 6, 1, 1, 1)
        self.comboBox_xaxis = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_xaxis.setObjectName("comboBox_xaxis")
        self.comboBox_xaxis.addItem("")
        self.comboBox_xaxis.addItem("")
        self.comboBox_xaxis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_xaxis, 7, 1, 1, 1)
        self.comboBox_yaxis = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_yaxis.setObjectName("comboBox_yaxis")
        self.comboBox_yaxis.addItem("")
        self.comboBox_yaxis.addItem("")
        self.comboBox_yaxis.addItem("")
        self.comboBox_yaxis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_yaxis, 8, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.toolButton_help_oclimax = QtWidgets.QToolButton(OCLIMAX)
        self.toolButton_help_oclimax.setObjectName("toolButton_help_oclimax")
        self.verticalLayout.addWidget(self.toolButton_help_oclimax, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(OCLIMAX)
        self.pushButton_ph_default.clicked.connect(OCLIMAX.use_default_mesh) # type: ignore
        self.pushButton_ph_save.clicked.connect(OCLIMAX.save_mesh) # type: ignore
        self.pushButton_oclimax_load.clicked.connect(OCLIMAX.load_parameters) # type: ignore
        self.pushButton_oclimax_default.clicked.connect(OCLIMAX.use_default_parameters) # type: ignore
        self.pushButton_oclimax_save.clicked.connect(OCLIMAX.save_parameters) # type: ignore
        self.toolButton_help_oclimax.clicked.connect(OCLIMAX.open_help_oclimax) # type: ignore
        self.comboBox_task.currentIndexChanged['int'].connect(OCLIMAX.task_changed) # type: ignore
        self.comboBox_Eunit.currentIndexChanged['int'].connect(OCLIMAX.unit_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OCLIMAX)

    def retranslateUi(self, OCLIMAX):
        _translate = QtCore.QCoreApplication.translate
        OCLIMAX.setWindowTitle(_translate("OCLIMAX", "Set up simulation"))
        self.groupBox.setTitle(_translate("OCLIMAX", "Phonon calculation"))
        self.label.setText(_translate("OCLIMAX", "Q mesh"))
        self.pushButton_ph_default.setText(_translate("OCLIMAX", "Default"))
        self.pushButton_ph_save.setText(_translate("OCLIMAX", "Save mesh"))
        self.groupBox_2.setTitle(_translate("OCLIMAX", "OCLIMAX parameters                                                                                                                  Single crystal parameters"))
        self.label_4.setText(_translate("OCLIMAX", "Temperature"))
        self.label_9.setText(_translate("OCLIMAX", "Emax"))
        self.label_17.setText(_translate("OCLIMAX", "E Unit"))
        self.label_11.setText(_translate("OCLIMAX", "Qmax"))
        self.label_10.setText(_translate("OCLIMAX", "Qmin"))
        self.label_18.setText(_translate("OCLIMAX", "Output"))
        self.label_6.setText(_translate("OCLIMAX", "ERES"))
        self.comboBox_task.setItemText(0, _translate("OCLIMAX", "1D VISION/TOSCA inc"))
        self.comboBox_task.setItemText(1, _translate("OCLIMAX", "2D S(Q,E) inc"))
        self.comboBox_task.setItemText(2, _translate("OCLIMAX", "1D VISION/TOSCA full"))
        self.comboBox_task.setItemText(3, _translate("OCLIMAX", "2D S(Q,E) full"))
        self.comboBox_task.setItemText(4, _translate("OCLIMAX", "2D S(Q,E) single crystal"))
        self.comboBox_task.setItemText(5, _translate("OCLIMAX", "2D S(Q,Q) single crystal"))
        self.comboBox_task.setItemText(6, _translate("OCLIMAX", "Others (defined in params file)"))
        self.comboBox_Eunit.setItemText(0, _translate("OCLIMAX", "cm\u207B\u00B9"))
        self.comboBox_Eunit.setItemText(1, _translate("OCLIMAX", "meV"))
        self.comboBox_Eunit.setItemText(2, _translate("OCLIMAX", "THz"))
        self.label_2.setText(_translate("OCLIMAX", "Task"))
        self.label_13.setText(_translate("OCLIMAX", "dQ"))
        self.label_19.setText(_translate("OCLIMAX", "Mask"))
        self.label_5.setText(_translate("OCLIMAX", "MAXO"))
        self.label_21.setText(_translate("OCLIMAX", "Theta"))
        self.label_8.setText(_translate("OCLIMAX", "Emin"))
        self.label_12.setText(_translate("OCLIMAX", "dE"))
        self.label_7.setText(_translate("OCLIMAX", "QRES"))
        self.label_3.setText(_translate("OCLIMAX", "Ecut"))
        self.label_22.setText(_translate("OCLIMAX", "Ei"))
        self.label_20.setText(_translate("OCLIMAX", "Norm"))
        self.pushButton_oclimax_load.setText(_translate("OCLIMAX", "Load parameters"))
        self.pushButton_oclimax_default.setText(_translate("OCLIMAX", "Use default"))
        self.pushButton_oclimax_save.setText(_translate("OCLIMAX", "Save parameters"))
        self.label_24.setText(_translate("OCLIMAX", "Q2_bin"))
        self.label_25.setText(_translate("OCLIMAX", "Q3_bin"))
        self.label_14.setText(_translate("OCLIMAX", "Q1"))
        self.label_16.setText(_translate("OCLIMAX", "Q3"))
        self.label_23.setText(_translate("OCLIMAX", "Q1_bin"))
        self.label_27.setText(_translate("OCLIMAX", "x-axis"))
        self.label_15.setText(_translate("OCLIMAX", "Q2"))
        self.label_26.setText(_translate("OCLIMAX", "E_bin"))
        self.label_28.setText(_translate("OCLIMAX", "y-axis"))
        self.comboBox_xaxis.setItemText(0, _translate("OCLIMAX", "Q1"))
        self.comboBox_xaxis.setItemText(1, _translate("OCLIMAX", "Q2"))
        self.comboBox_xaxis.setItemText(2, _translate("OCLIMAX", "Q3"))
        self.comboBox_yaxis.setItemText(0, _translate("OCLIMAX", "E"))
        self.comboBox_yaxis.setItemText(1, _translate("OCLIMAX", "Q1"))
        self.comboBox_yaxis.setItemText(2, _translate("OCLIMAX", "Q2"))
        self.comboBox_yaxis.setItemText(3, _translate("OCLIMAX", "Q3"))
        self.toolButton_help_oclimax.setText(_translate("OCLIMAX", "Help"))
