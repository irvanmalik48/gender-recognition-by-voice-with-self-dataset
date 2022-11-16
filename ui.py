from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from test import record_to_file, run_analyze, save_sound
import traceback


class BuilderSignals(QObject):
    started = Signal()
    finished = Signal()
    result = Signal()


class Builder(QRunnable):
    def __init__(self, parent=None):
        super(Builder, self).__init__()
        self.signals = BuilderSignals()

    def run(self):
        self.signals.started.emit()

        try:
            self.signals.result.emit()
        except:
            traceback.print_exc()
        else:
            self.signals.finished.emit()
        finally:
            pass


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(982, 619)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.threadpool = QThreadPool()

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())

        self.groupBox.setSizePolicy(sizePolicy)

        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(4)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 40))

        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.startRecordBtn = QPushButton(self.groupBox_3)
        self.startRecordBtn.setObjectName("startRecordBtn")

        self.runBtn = QPushButton(self.groupBox_3)
        self.runBtn.setObjectName("runBtn")
        self.runBtn.setEnabled(False)

        self.horizontalLayout.addWidget(self.startRecordBtn)
        self.horizontalLayout.addWidget(self.runBtn)

        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName("groupBox_7")

        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.retrainBtn = QPushButton(self.groupBox_7)
        self.retrainBtn.setObjectName("retrainBtn")

        self.gridLayout_5.addWidget(self.retrainBtn, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 40))

        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(4)

        self.saveFileName = QLineEdit(self.groupBox_2)
        self.saveFileName.setObjectName("saveFileName")
        self.saveFileName.setEnabled(False)

        self.gridLayout.addWidget(self.saveFileName, 0, 0, 1, 1)

        self.saveBtn = QPushButton(self.groupBox_2)
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.setEnabled(False)

        self.gridLayout.addWidget(self.saveBtn, 0, 1, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.verticalLayout_7.addWidget(self.frame_4)

        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 1)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")

        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())

        self.groupBox_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")

        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame = QFrame(self.groupBox_4)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.manLabel = QLabel(self.frame)
        self.manLabel.setObjectName("manLabel")
        self.manLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.manLabel)

        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.frame_2 = QFrame(self.groupBox_4)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.womanLabel = QLabel(self.frame_2)
        self.womanLabel.setObjectName("womanLabel")
        self.womanLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.womanLabel)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 2, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName("frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_3)
        self.groupBox_6.setObjectName("groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.groupBox_6.setMinimumSize(QSize(0, 40))

        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")

        self.listWidget = QListWidget(self.groupBox_6)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)

        self.listWidget.setObjectName("listWidget")

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())

        self.listWidget.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.listWidget)

        self.gridLayout_4.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")

        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.logListView = QListWidget(self.groupBox_5)
        self.logListView.setObjectName("logListView")

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logListView.sizePolicy().hasHeightForWidth())

        self.logListView.setSizePolicy(sizePolicy3)
        self.logListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.logListView.setLayoutMode(QListWidget.SinglePass)

        self.verticalLayout_8.addWidget(self.logListView)

        self.gridLayout_3.addWidget(self.groupBox_5, 0, 1, 4, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def add_to_log(self, text):
        self.logListView.addItem(text)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", "Actions", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", "Record", None))
        self.startRecordBtn.setText(QCoreApplication.translate("Form", "Start", None))
        self.runBtn.setText(QCoreApplication.translate("Form", "Analyse", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", "Retrain", None))
        self.retrainBtn.setText(QCoreApplication.translate("Form", "Retrain AI", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Form", "Save Current", None)
        )
        self.saveFileName.setToolTip(
            QCoreApplication.translate(
                "Form", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.saveBtn.setText(QCoreApplication.translate("Form", "Save", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", "Result", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Man", None))
        self.manLabel.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt;">50</span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(QCoreApplication.translate("Form", "Woman", None))
        self.womanLabel.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt;">50</span></p></body></html>',
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">Gender Recognition Through Voice With Deep FNN</span></p></body></html>',
                None,
            )
        )
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", "Kelompok 6", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("Form", "M. Bintang Khadafi", None)
        )
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate("Form", "Irvan Malik Azantha", None)
        )
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(
            QCoreApplication.translate("Form", "Annisa Syawalia", None)
        )
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(
            QCoreApplication.translate("Form", "Lastri Rahelita", None)
        )
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(
            QCoreApplication.translate("Form", "Bayu Daru Pangestu", None)
        )
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_5.setTitle(QCoreApplication.translate("Form", "Logs", None))

        self.bindEvents()

    def bindEvents(self):
        self.startRecordBtn.clicked.connect(self.start_button_clicked)
        self.runBtn.clicked.connect(self.run_clicked)
        self.saveBtn.clicked.connect(self.save_clicked)
        
        # todo: add retrain button event
        # self.retrainBtn.clicked.connect(self.retrain_clicked)



    # startRecordBtn event handling
    def start_button_preclick(self):
        self.add_to_log("[EVENT] Start recording.")
        self.startRecordBtn.setEnabled(False)
        self.startRecordBtn.setText("Recording...")

    def start_button_event(self):
        record_to_file("test.wav")

    def start_button_postclick(self):
        self.add_to_log("[SUCCESS] Successfully recorded sound.")
        self.startRecordBtn.setEnabled(True)
        self.startRecordBtn.setText("Start")
        self.runBtn.setEnabled(True)

    def start_button_clicked(self):
        builder = Builder()

        builder.signals.started.connect(self.start_button_preclick)
        builder.signals.result.connect(self.start_button_event)
        builder.signals.finished.connect(self.start_button_postclick)

        self.threadpool.start(builder)

    # runBtn event handling
    def run_preclick(self):
        self.add_to_log("[EVENT] Analyzing sound.")
        self.runBtn.setEnabled(False)
        self.runBtn.setText("Analyzing...")

    def run_event(self):
        male_pred, female_pred, gender = run_analyze("test.wav")
        self.gender = gender
        self.male_pred = male_pred
        self.female_pred = female_pred

    def run_postclick(self):
        self.add_to_log("[SUCCESS] Successfully analyzed sound.")
        self.runBtn.setEnabled(True)
        self.runBtn.setText("Analyse")
        self.add_to_log("[RESULT] Probabilities:")
        self.add_to_log(
            "[RESULT] Male: "
            + str(self.male_pred * 100)
            + "; Female: "
            + str(self.female_pred * 100)
        )
        self.manLabel.setText(str(self.male_pred * 100))
        self.womanLabel.setText(str(self.female_pred * 100))
        self.runBtn.setEnabled(False)
        self.saveBtn.setEnabled(True)
        self.saveFileName.setEnabled(True)
        self.saveFileName.clear()
        self.saveFileName.insert("enter-your-file-name")

    def run_clicked(self):
        builder = Builder()

        builder.signals.started.connect(self.run_preclick)
        builder.signals.result.connect(self.run_event)
        builder.signals.finished.connect(self.run_postclick)

        self.threadpool.start(builder)

    # saveBtn event handling
    def save_preclick(self):
        self.add_to_log("[EVENT] Saving result.")

    def save_event(self):
        save_sound("test.wav", self.saveFileName.text(), self.gender)

    def save_postclick(self):
        self.add_to_log("[SUCCESS] Successfully saved file.")
        self.saveBtn.setEnabled(False)
        self.saveFileName.setEnabled(False)
        self.saveFileName.clear()

    def save_clicked(self):
        builder = Builder()

        builder.signals.started.connect(self.save_preclick)
        builder.signals.result.connect(self.save_event)
        builder.signals.finished.connect(self.save_postclick)

        self.threadpool.start(builder)
    
    # todo: add retrain button event handling
    # def retrain_preclick(self):
    #     self.add_to_log("[EVENT] Retrain start.")

    # def retrain_event(self):
    #     # add retrain code here

    # def retrain_postclick(self):
    #     self.add_to_log("[SUCCESS] Retrain complete.")

    # def retrain_clicked(self):
    #     builder = Builder()

    #     builder.signals.started.connect(self.retrain_preclick)
    #     builder.signals.result.connect(self.retrain_event)
    #     builder.signals.finished.connect(self.retrain_postclick)

    #     self.threadpool.start(builder)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
