# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerrepositorybase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsPluginInstallerRepositoryDetailsDialogBase(object):
    def setupUi(self, QgsPluginInstallerRepositoryDetailsDialogBase):
        QgsPluginInstallerRepositoryDetailsDialogBase.setObjectName("QgsPluginInstallerRepositoryDetailsDialogBase")
        QgsPluginInstallerRepositoryDetailsDialogBase.resize(496, 289)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QgsPluginInstallerRepositoryDetailsDialogBase.sizePolicy().hasHeightForWidth())
        QgsPluginInstallerRepositoryDetailsDialogBase.setSizePolicy(sizePolicy)
        QgsPluginInstallerRepositoryDetailsDialogBase.setStatusTip("")
        QgsPluginInstallerRepositoryDetailsDialogBase.setWhatsThis("")
        self.gridlayout = QtWidgets.QGridLayout(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(351, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.editName.setObjectName("editName")
        self.gridlayout.addWidget(self.editName, 0, 1, 1, 2)
        self.editParams = QtWidgets.QLineEdit(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.editParams.setEnabled(False)
        self.editParams.setObjectName("editParams")
        self.gridlayout.addWidget(self.editParams, 3, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 9, 0, 1, 3)
        self.label = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.labelInfo = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.labelInfo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInfo.sizePolicy().hasHeightForWidth())
        self.labelInfo.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(175, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelInfo.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelInfo.setFont(font)
        self.labelInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        self.gridlayout.addWidget(self.labelInfo, 7, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.checkBoxEnabled = QtWidgets.QCheckBox(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.checkBoxEnabled.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxEnabled.sizePolicy().hasHeightForWidth())
        self.checkBoxEnabled.setSizePolicy(sizePolicy)
        self.checkBoxEnabled.setText("")
        self.checkBoxEnabled.setChecked(False)
        self.checkBoxEnabled.setObjectName("checkBoxEnabled")
        self.gridlayout.addWidget(self.checkBoxEnabled, 5, 1, 1, 1)
        self.editURL = QtWidgets.QLineEdit(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.editURL.setText("")
        self.editURL.setObjectName("editURL")
        self.gridlayout.addWidget(self.editURL, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 6, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.layoutAuthCfg = QtWidgets.QHBoxLayout()
        self.layoutAuthCfg.setSpacing(6)
        self.layoutAuthCfg.setObjectName("layoutAuthCfg")
        self.editAuthCfg = QtWidgets.QLineEdit(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.editAuthCfg.setReadOnly(True)
        self.editAuthCfg.setObjectName("editAuthCfg")
        self.layoutAuthCfg.addWidget(self.editAuthCfg)
        self.btnClearAuthCfg = QtWidgets.QToolButton(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.btnClearAuthCfg.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btnClearAuthCfg.setObjectName("btnClearAuthCfg")
        self.layoutAuthCfg.addWidget(self.btnClearAuthCfg)
        self.btnEditAuthCfg = QtWidgets.QToolButton(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.btnEditAuthCfg.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btnEditAuthCfg.setObjectName("btnEditAuthCfg")
        self.layoutAuthCfg.addWidget(self.btnEditAuthCfg)
        self.gridlayout.addLayout(self.layoutAuthCfg, 4, 1, 1, 2)
        self.label_2.setBuddy(self.editURL)
        self.label_4.setBuddy(self.checkBoxEnabled)
        self.label.setBuddy(self.editName)
        self.label_3.setBuddy(self.editParams)

        self.retranslateUi(QgsPluginInstallerRepositoryDetailsDialogBase)
        self.buttonBox.accepted.connect(QgsPluginInstallerRepositoryDetailsDialogBase.accept)
        self.buttonBox.rejected.connect(QgsPluginInstallerRepositoryDetailsDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerRepositoryDetailsDialogBase)
        QgsPluginInstallerRepositoryDetailsDialogBase.setTabOrder(self.editName, self.editURL)
        QgsPluginInstallerRepositoryDetailsDialogBase.setTabOrder(self.editURL, self.editParams)
        QgsPluginInstallerRepositoryDetailsDialogBase.setTabOrder(self.editParams, self.checkBoxEnabled)
        QgsPluginInstallerRepositoryDetailsDialogBase.setTabOrder(self.checkBoxEnabled, self.buttonBox)

    def retranslateUi(self, QgsPluginInstallerRepositoryDetailsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QgsPluginInstallerRepositoryDetailsDialogBase.setWindowTitle(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Repository details"))
        self.label_2.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "URL"))
        self.label_4.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enabled"))
        self.editName.setToolTip(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enter a name for the repository"))
        self.editName.setWhatsThis(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enter a name for the repository"))
        self.editParams.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "?qgis="))
        self.label.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Name"))
        self.label_3.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Parameters"))
        self.checkBoxEnabled.setToolTip(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enable or disable the repository (disabled repositories will be omitted)"))
        self.checkBoxEnabled.setWhatsThis(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enable or disable the repository (disabled repositories will be omitted)"))
        self.editURL.setToolTip(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enter the repository URL, beginning with \"http://\" or \"file:///\""))
        self.editURL.setWhatsThis(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Enter the repository URL, beginning with \"http://\" or \"file:///\""))
        self.label_5.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Authentication"))
        self.btnClearAuthCfg.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Clear"))
        self.btnEditAuthCfg.setText(_translate("QgsPluginInstallerRepositoryDetailsDialogBase", "Edit"))
