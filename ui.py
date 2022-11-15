import os
import random
import time
import wave
from array import array
from csv import writer
from struct import pack
from sys import byteorder

import librosa
import numpy
import numpy as np
import pyaudio
import pydub
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

THRESHOLD = 3000
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
SILENCE = 30


def extract_feature(file_name, **kwargs):
    """
    Extract feature from audio file `file_name`
        Features supported:
            - MFCC (mfcc)
            - Chroma (chroma)
            - MEL Spectrogram Frequency (mel)
            - Contrast (contrast)
            - Tonnetz (tonnetz)
        e.g:
        `features = extract_feature(path, mel=True, mfcc=True)`
    """
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")
    tonnetz = kwargs.get("tonnetz")
    X, sample_rate = librosa.core.load(file_name)
    if chroma or contrast:
        stft = np.abs(librosa.stft(X))
    result = np.array([])
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))
    if contrast:
        contrast = np.mean(
            librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0
        )
        result = np.hstack((result, contrast))
    if tonnetz:
        tonnetz = np.mean(
            librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,
            axis=0,
        )
        result = np.hstack((result, tonnetz))
    return result


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(982, 619)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")

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

    def is_silent(self, snd_data):
        "Returns 'True' if below the 'silent' threshold"
        return max(snd_data) < THRESHOLD

    def normalize(self, snd_data):
        "Average the volume out"
        MAXIMUM = 16384
        times = float(MAXIMUM) / max(abs(i) for i in snd_data)

        r = array("h")
        for i in snd_data:
            r.append(int(i * times))
        return r

    def trim(self, snd_data):
        "Trim the blank spots at the start and end"

        def _trim(snd_data):
            snd_started = False
            r = array("h")

            for i in snd_data:
                if not snd_started and abs(i) > THRESHOLD:
                    snd_started = True
                    r.append(i)

                elif snd_started:
                    r.append(i)
            return r

        # Trim to the left
        snd_data = _trim(snd_data)

        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data

    def add_silence(self, snd_data, seconds):
        "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
        r = array("h", [0 for i in range(int(seconds * RATE))])
        r.extend(snd_data)
        r.extend([0 for i in range(int(seconds * RATE))])
        return r

    def record(self):
        """
        Record a word or words from the microphone and
        return the data as an array of signed shorts.
        Normalizes the audio, trims silence from the
        start and end, and pads with 0.5 seconds of
        blank sound to make sure VLC et al can play
        it without getting chopped off.
        """
        self.startRecordBtn.setEnabled(False)
        self.startRecordBtn.setText("Recording...")
        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=1,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK_SIZE,
        )

        num_silent = 0
        snd_started = False

        r = array("h")

        while 1:
            # little endian, signed short
            snd_data = array("h", stream.read(CHUNK_SIZE))
            if byteorder == "big":
                snd_data.byteswap()
            r.extend(snd_data)

            silent = self.is_silent(snd_data)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > SILENCE:
                break

        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = self.normalize(r)
        r = self.trim(r)
        r = self.add_silence(r, 0.5)
        return sample_width, r

    def add_to_log(self, text):
        self.logListView.addItem(text)

    def record_to_file(self):
        "Records from the microphone and outputs the resulting data to 'path'"
        sample_width, data = self.record()
        data = pack("<" + ("h" * len(data)), *data)

        wf = wave.open("test.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
        self.add_to_log("[SUCCESS] Successfully recorded sound.")
        self.startRecordBtn.setEnabled(True)
        self.startRecordBtn.setText("Start")
        self.runBtn.setEnabled(True)

    def run(self):
        from utils import create_model, load_data, split_data

        model = create_model()
        model.load_weights("results/model.h5")
        features = extract_feature("test.wav", mel=True).reshape(1, -1)
        male_pred = model.predict(features)[0][0]
        female_pred = 1 - male_pred
        self.gender = "male" if male_pred > female_pred else "female"
        self.add_to_log("[RESULT] Probabilities:")
        self.add_to_log(
            "[RESULT] Male: "
            + str(male_pred * 100)
            + "; Female: "
            + str(female_pred * 100)
        )
        self.manLabel.setText(str(male_pred * 100))
        self.womanLabel.setText(str(female_pred * 100))
        self.runBtn.setEnabled(False)
        self.saveBtn.setEnabled(True)
        self.saveFileName.setEnabled(True)
        self.saveFileName.clear()
        self.saveFileName.insert("enter-your-file-name")

    def save_file(self):
        a = pydub.AudioSegment.from_mp3("test.wav")
        arr = np.array(a.get_array_of_samples())
        numpy.save(
            "data/cv-valid-train/" + self.saveFileName.text() + ".npy",
            arr,
            allow_pickle=True,
            fix_imports=True,
        )

        List = [
            ("data/cv-valid-selftrain/" + self.saveFileName.text() + ".npy"),
            self.gender,
        ]

        with open("balanced-all.csv", "a") as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
        self.add_to_log("[SUCCESS] Successfully saved file.")
        self.saveBtn.setEnabled(False)
        self.saveFileName.setEnabled(False)
        self.saveFileName.clear()

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
        self.startRecordBtn.clicked.connect(self.record_to_file)
        self.runBtn.clicked.connect(self.run)
        self.saveBtn.clicked.connect(self.save_file)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
