# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QTreeView, QWidget)
import apprcc_rc
import test_rc
import test_test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 889)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setFont(font)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionClose.setFont(font)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u":/pic/images/Devices (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionAAA = QAction(MainWindow)
        self.actionAAA.setObjectName(u"actionAAA")
        icon1 = QIcon()
        icon1.addFile(u":/pic_test/images_test/cartoon1.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAAA.setIcon(icon1)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        icon2 = QIcon()
        icon2.addFile(u":/pic/images/Arrows and States (9).png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRun.setIcon(icon2)
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionSetting.setCheckable(False)
        self.actionSetting.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/pic/images/icons8-settings_01-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSetting.setIcon(icon3)
        self.actionSetting.setAutoRepeat(True)
        self.actionSetting.setVisible(True)
        self.actionFileManager = QAction(MainWindow)
        self.actionFileManager.setObjectName(u"actionFileManager")
        icon4 = QIcon()
        icon4.addFile(u":/pic/images/folder_512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFileManager.setIcon(icon4)
        self.actionCallList = QAction(MainWindow)
        self.actionCallList.setObjectName(u"actionCallList")
        self.actionCallList.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/pic/images/list_981x878.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCallList.setIcon(icon5)
        self.actionAP = QAction(MainWindow)
        self.actionAP.setObjectName(u"actionAP")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionseven = QAction(MainWindow)
        self.actionseven.setObjectName(u"actionseven")
        icon6 = QIcon()
        icon6.addFile(u":/seven/images_test/kid-goku-4k.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionseven.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(0, 1, 281, 731))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 633, 26))
        font1 = QFont()
        font1.setPointSize(12)
        self.menubar.setFont(font1)
        self.menuFile_F = QMenu(self.menubar)
        self.menuFile_F.setObjectName(u"menuFile_F")
        font2 = QFont()
        font2.setPointSize(10)
        self.menuFile_F.setFont(font2)
        self.menuEdit_E = QMenu(self.menubar)
        self.menuEdit_E.setObjectName(u"menuEdit_E")
        self.menuEdit_E.setFont(font2)
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setFont(font2)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar_2.sizePolicy().hasHeightForWidth())
        self.toolBar_2.setSizePolicy(sizePolicy)
        self.toolBar_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolBar_2.setAcceptDrops(False)
        self.toolBar_2.setLayoutDirection(Qt.LeftToRight)
        self.toolBar_2.setAutoFillBackground(False)
        self.toolBar_2.setInputMethodHints(Qt.ImhNone)
        self.toolBar_2.setAllowedAreas(Qt.LeftToolBarArea)
        self.toolBar_2.setOrientation(Qt.Vertical)
        self.toolBar_2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar_2.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuEdit_E.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuFile_F.addAction(self.actionNew)
        self.menuFile_F.addAction(self.actionOpen)
        self.menuFile_F.addAction(self.actionClose)
        self.menuhelp.addAction(self.actionAP)
        self.menuhelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionFileManager)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionAAA)
        self.toolBar.addAction(self.actionseven)
        self.toolBar_2.addAction(self.actionCallList)
        self.toolBar_2.addAction(self.actionSetting)

        self.retranslateUi(MainWindow)
        self.actionAAA.triggered.connect(MainWindow.close)
        self.actionseven.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">New</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(tooltip)
        self.actionClose.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Close</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAAA.setText(QCoreApplication.translate("MainWindow", u"AAA", None))
#if QT_CONFIG(tooltip)
        self.actionAAA.setToolTip(QCoreApplication.translate("MainWindow", u"AAA", None))
#endif // QT_CONFIG(tooltip)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(tooltip)
        self.actionRun.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.actionFileManager.setText(QCoreApplication.translate("MainWindow", u"FileManager", None))
        self.actionCallList.setText(QCoreApplication.translate("MainWindow", u"CallList", None))
#if QT_CONFIG(tooltip)
        self.actionCallList.setToolTip(QCoreApplication.translate("MainWindow", u"CallList", None))
#endif // QT_CONFIG(tooltip)
        self.actionAP.setText(QCoreApplication.translate("MainWindow", u"AP explain", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionseven.setText(QCoreApplication.translate("MainWindow", u"seven", None))
#if QT_CONFIG(tooltip)
        self.actionseven.setToolTip(QCoreApplication.translate("MainWindow", u"seven", None))
#endif // QT_CONFIG(tooltip)
        self.menuFile_F.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit_E.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

