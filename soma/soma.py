# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soma.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 90, 80);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 721, 81))
        font = QtGui.QFont()
        font.setFamily("Freehand521 BT")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 441, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.f1_1_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.f1_1_10.setGeometry(QtCore.QRect(30, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f1_1_10.setFont(font)
        self.f1_1_10.setObjectName("f1_1_10")
        self.f1_1_99 = QtWidgets.QRadioButton(self.centralwidget)
        self.f1_1_99.setGeometry(QtCore.QRect(170, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f1_1_99.setFont(font)
        self.f1_1_99.setObjectName("f1_1_99")
        self.f1_1_999 = QtWidgets.QRadioButton(self.centralwidget)
        self.f1_1_999.setGeometry(QtCore.QRect(320, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f1_1_999.setFont(font)
        self.f1_1_999.setObjectName("f1_1_999")
        self.f2_1_999 = QtWidgets.QRadioButton(self.centralwidget)
        self.f2_1_999.setGeometry(QtCore.QRect(320, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f2_1_999.setFont(font)
        self.f2_1_999.setObjectName("f2_1_999")
        self.f2_1_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.f2_1_9.setGeometry(QtCore.QRect(30, 410, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f2_1_9.setFont(font)
        self.f2_1_9.setObjectName("f2_1_9")
        self.f2_1_99 = QtWidgets.QRadioButton(self.centralwidget)
        self.f2_1_99.setGeometry(QtCore.QRect(170, 410, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f2_1_99.setFont(font)
        self.f2_1_99.setObjectName("f2_1_99")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 441, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.f2_1_9999 = QtWidgets.QRadioButton(self.centralwidget)
        self.f2_1_9999.setGeometry(QtCore.QRect(480, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f2_1_9999.setFont(font)
        self.f2_1_9999.setObjectName("f2_1_9999")
        self.f1_1_9999 = QtWidgets.QRadioButton(self.centralwidget)
        self.f1_1_9999.setGeometry(QtCore.QRect(480, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f1_1_9999.setFont(font)
        self.f1_1_9999.setObjectName("f1_1_9999")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 460, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.qtd_exer10 = QtWidgets.QRadioButton(self.centralwidget)
        self.qtd_exer10.setGeometry(QtCore.QRect(20, 540, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qtd_exer10.setFont(font)
        self.qtd_exer10.setObjectName("qtd_exer10")
        self.qtd_exer20 = QtWidgets.QRadioButton(self.centralwidget)
        self.qtd_exer20.setGeometry(QtCore.QRect(200, 540, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qtd_exer20.setFont(font)
        self.qtd_exer20.setObjectName("qtd_exer20")
        self.qtd_exer30 = QtWidgets.QRadioButton(self.centralwidget)
        self.qtd_exer30.setGeometry(QtCore.QRect(380, 540, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qtd_exer30.setFont(font)
        self.qtd_exer30.setObjectName("qtd_exer30")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 590, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.ordem_sim = QtWidgets.QRadioButton(self.centralwidget)
        self.ordem_sim.setGeometry(QtCore.QRect(20, 680, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ordem_sim.setFont(font)
        self.ordem_sim.setObjectName("ordem_sim")
        self.ordem_nao = QtWidgets.QRadioButton(self.centralwidget)
        self.ordem_nao.setGeometry(QtCore.QRect(130, 680, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ordem_nao.setFont(font)
        self.ordem_nao.setObjectName("ordem_nao")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "+ SOMA +"))
        self.label_2.setText(_translate("MainWindow", "+ SOMA +"))
        self.label_3.setText(_translate("MainWindow", "Selecione a quantidade de caracteres do primeiro fator:"))
        self.f1_1_10.setText(_translate("MainWindow", "De 1 a 9"))
        self.f1_1_99.setText(_translate("MainWindow", "De 1 a 99"))
        self.f1_1_999.setText(_translate("MainWindow", "De 1 a 999"))
        self.f2_1_999.setText(_translate("MainWindow", "De 1 a 999"))
        self.f2_1_9.setText(_translate("MainWindow", "De 1 a 9"))
        self.f2_1_99.setText(_translate("MainWindow", "De 1 a 99"))
        self.label_4.setText(_translate("MainWindow", "Selecione a quantidade de caracteres do segundo fator:"))
        self.f2_1_9999.setText(_translate("MainWindow", "De 1 a 9999"))
        self.f1_1_9999.setText(_translate("MainWindow", "De 1 a 9999"))
        self.label_5.setText(_translate("MainWindow", "Quantos exercícios deseja criar?"))
        self.qtd_exer10.setText(_translate("MainWindow", "10 Exercícios"))
        self.qtd_exer20.setText(_translate("MainWindow", "20 Exercícios"))
        self.qtd_exer30.setText(_translate("MainWindow", "30 Exercícios"))
        self.label_6.setText(_translate("MainWindow", "Ordernar com o maior valor sempre primeiro?"))
        self.ordem_sim.setText(_translate("MainWindow", "SIM"))
        self.ordem_nao.setText(_translate("MainWindow", "NÃO"))