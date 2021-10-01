# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgSqlLayerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgSqlLayerWindow(object):
    def setupUi(self, DbManagerDlgSqlLayerWindow):
        DbManagerDlgSqlLayerWindow.setObjectName("DbManagerDlgSqlLayerWindow")
        DbManagerDlgSqlLayerWindow.resize(662, 525)
        self.gridLayout_2 = QtWidgets.QGridLayout(DbManagerDlgSqlLayerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.getColumnsBtn = QtWidgets.QPushButton(DbManagerDlgSqlLayerWindow)
        self.getColumnsBtn.setObjectName("getColumnsBtn")
        self.gridLayout_2.addWidget(self.getColumnsBtn, 1, 3, 1, 1)
        self.updateLayerBtn = QtWidgets.QPushButton(DbManagerDlgSqlLayerWindow)
        self.updateLayerBtn.setObjectName("updateLayerBtn")
        self.gridLayout_2.addWidget(self.updateLayerBtn, 3, 3, 1, 1)
        self.btnSetFilter = QtWidgets.QPushButton(DbManagerDlgSqlLayerWindow)
        self.btnSetFilter.setAutoDefault(False)
        self.btnSetFilter.setObjectName("btnSetFilter")
        self.gridLayout_2.addWidget(self.btnSetFilter, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.avoidSelectById = QtWidgets.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.avoidSelectById.setObjectName("avoidSelectById")
        self.gridLayout_2.addWidget(self.avoidSelectById, 3, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(DbManagerDlgSqlLayerWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.queryBuilderBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.queryBuilderBtn.setText("")
        self.queryBuilderBtn.setObjectName("queryBuilderBtn")
        self.horizontalLayout.addWidget(self.queryBuilderBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.presetCombo = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetCombo.sizePolicy().hasHeightForWidth())
        self.presetCombo.setSizePolicy(sizePolicy)
        self.presetCombo.setObjectName("presetCombo")
        self.horizontalLayout.addWidget(self.presetCombo)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.presetName = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetName.sizePolicy().hasHeightForWidth())
        self.presetName.setSizePolicy(sizePolicy)
        self.presetName.setText("")
        self.presetName.setObjectName("presetName")
        self.horizontalLayout.addWidget(self.presetName)
        self.presetStore = QtWidgets.QPushButton(self.layoutWidget)
        self.presetStore.setObjectName("presetStore")
        self.horizontalLayout.addWidget(self.presetStore)
        self.presetDelete = QtWidgets.QPushButton(self.layoutWidget)
        self.presetDelete.setObjectName("presetDelete")
        self.horizontalLayout.addWidget(self.presetDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.editSql = QgsCodeEditorSQL(self.layoutWidget)
        self.editSql.setObjectName("editSql")
        self.verticalLayout_2.addWidget(self.editSql)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.btnExecute = QtWidgets.QPushButton(self.layoutWidget)
        self.btnExecute.setObjectName("btnExecute")
        self.hboxlayout.addWidget(self.btnExecute)
        self.lblResult = QtWidgets.QLabel(self.layoutWidget)
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.hboxlayout.addWidget(self.lblResult)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.btnClear = QtWidgets.QPushButton(self.layoutWidget)
        self.btnClear.setObjectName("btnClear")
        self.hboxlayout.addWidget(self.btnClear)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewResult = QtWidgets.QTableView(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.viewResult.sizePolicy().hasHeightForWidth())
        self.viewResult.setSizePolicy(sizePolicy)
        self.viewResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.viewResult.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.viewResult.setObjectName("viewResult")
        self.verticalLayout.addWidget(self.viewResult)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(DbManagerDlgSqlLayerWindow)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.layerNameEdit = QtWidgets.QLineEdit(DbManagerDlgSqlLayerWindow)
        self.layerNameEdit.setEnabled(True)
        self.layerNameEdit.setText("")
        self.layerNameEdit.setReadOnly(True)
        self.layerNameEdit.setObjectName("layerNameEdit")
        self.horizontalLayout_7.addWidget(self.layerNameEdit)
        self.layerTypeWidget = QtWidgets.QWidget(DbManagerDlgSqlLayerWindow)
        self.layerTypeWidget.setObjectName("layerTypeWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layerTypeWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layerTypeWidget)
        self.label_6.setIndent(40)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.vectorRadio = QtWidgets.QRadioButton(self.layerTypeWidget)
        self.vectorRadio.setChecked(True)
        self.vectorRadio.setObjectName("vectorRadio")
        self.horizontalLayout_3.addWidget(self.vectorRadio)
        self.rasterRadio = QtWidgets.QRadioButton(self.layerTypeWidget)
        self.rasterRadio.setObjectName("rasterRadio")
        self.horizontalLayout_3.addWidget(self.rasterRadio)
        self.horizontalLayout_7.addWidget(self.layerTypeWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uniqueColumnCheck = QtWidgets.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.uniqueColumnCheck.setObjectName("uniqueColumnCheck")
        self.horizontalLayout_6.addWidget(self.uniqueColumnCheck)
        self.uniqueCombo = QtWidgets.QComboBox(DbManagerDlgSqlLayerWindow)
        self.uniqueCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniqueCombo.sizePolicy().hasHeightForWidth())
        self.uniqueCombo.setSizePolicy(sizePolicy)
        self.uniqueCombo.setEditable(True)
        self.uniqueCombo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.uniqueCombo.setObjectName("uniqueCombo")
        self.horizontalLayout_6.addWidget(self.uniqueCombo)
        self.hasGeometryCol = QtWidgets.QCheckBox(DbManagerDlgSqlLayerWindow)
        self.hasGeometryCol.setChecked(True)
        self.hasGeometryCol.setTristate(False)
        self.hasGeometryCol.setObjectName("hasGeometryCol")
        self.horizontalLayout_6.addWidget(self.hasGeometryCol)
        self.geomCombo = QtWidgets.QComboBox(DbManagerDlgSqlLayerWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geomCombo.sizePolicy().hasHeightForWidth())
        self.geomCombo.setSizePolicy(sizePolicy)
        self.geomCombo.setEditable(True)
        self.geomCombo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.geomCombo.setObjectName("geomCombo")
        self.horizontalLayout_6.addWidget(self.geomCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 3)

        self.retranslateUi(DbManagerDlgSqlLayerWindow)
        self.hasGeometryCol.toggled['bool'].connect(self.geomCombo.setEnabled)
        self.uniqueColumnCheck.toggled['bool'].connect(self.uniqueCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgSqlLayerWindow)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.queryBuilderBtn, self.presetCombo)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.presetCombo, self.presetName)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.presetName, self.presetStore)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.presetStore, self.presetDelete)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.presetDelete, self.editSql)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.editSql, self.btnExecute)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.btnExecute, self.btnClear)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.btnClear, self.viewResult)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.viewResult, self.uniqueColumnCheck)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.uniqueColumnCheck, self.uniqueCombo)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.uniqueCombo, self.hasGeometryCol)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.hasGeometryCol, self.geomCombo)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.geomCombo, self.getColumnsBtn)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.getColumnsBtn, self.layerNameEdit)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.layerNameEdit, self.vectorRadio)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.vectorRadio, self.rasterRadio)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.rasterRadio, self.btnSetFilter)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.btnSetFilter, self.avoidSelectById)
        DbManagerDlgSqlLayerWindow.setTabOrder(self.avoidSelectById, self.updateLayerBtn)

    def retranslateUi(self, DbManagerDlgSqlLayerWindow):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgSqlLayerWindow.setWindowTitle(_translate("DbManagerDlgSqlLayerWindow", "SQL Window"))
        self.getColumnsBtn.setText(_translate("DbManagerDlgSqlLayerWindow", "Retrieve\n"
"columns"))
        self.updateLayerBtn.setText(_translate("DbManagerDlgSqlLayerWindow", "Update"))
        self.btnSetFilter.setText(_translate("DbManagerDlgSqlLayerWindow", "Set filter"))
        self.avoidSelectById.setToolTip(_translate("DbManagerDlgSqlLayerWindow", "<html><head/><body><p>Avoid selecting feature by id. Sometimes - especially when running expensive queries/views - fetching the data sequentially instead of fetching features by id can be much quicker.</p></body></html>"))
        self.avoidSelectById.setText(_translate("DbManagerDlgSqlLayerWindow", "Avoid selecting by feature id"))
        self.label.setText(_translate("DbManagerDlgSqlLayerWindow", "Saved query"))
        self.label_2.setText(_translate("DbManagerDlgSqlLayerWindow", "Name"))
        self.presetStore.setText(_translate("DbManagerDlgSqlLayerWindow", "Save"))
        self.presetDelete.setText(_translate("DbManagerDlgSqlLayerWindow", "Delete"))
        self.btnExecute.setToolTip(_translate("DbManagerDlgSqlLayerWindow", "Execute query (Ctrl+R)"))
        self.btnExecute.setText(_translate("DbManagerDlgSqlLayerWindow", "Execute"))
        self.btnExecute.setShortcut(_translate("DbManagerDlgSqlLayerWindow", "Ctrl+R"))
        self.btnClear.setText(_translate("DbManagerDlgSqlLayerWindow", "&Clear"))
        self.label_5.setText(_translate("DbManagerDlgSqlLayerWindow", "Layer name (prefix)"))
        self.label_6.setText(_translate("DbManagerDlgSqlLayerWindow", "Type"))
        self.vectorRadio.setText(_translate("DbManagerDlgSqlLayerWindow", "Vector"))
        self.rasterRadio.setText(_translate("DbManagerDlgSqlLayerWindow", "Raster"))
        self.uniqueColumnCheck.setText(_translate("DbManagerDlgSqlLayerWindow", "Column(s) with\n"
"unique values"))
        self.hasGeometryCol.setText(_translate("DbManagerDlgSqlLayerWindow", "Geometry column"))

from qgis.gui import QgsCodeEditorSQL
