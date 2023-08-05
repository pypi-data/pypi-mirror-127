import os
import platform
import sys
import requests

from PySide6 import QtCore  # type: ignore
from PySide6.QtCore import Qt  # type: ignore
from PySide6 import QtGui  # type: ignore
from PySide6.QtWidgets import QApplication  # type: ignore
from PySide6.QtWidgets import QMessageBox  # type: ignore
from PySide6.QtWidgets import QPushButton  # type: ignore

from ..engine import InitializationResult
from ..engine import initialize
from ..utils.config import config

from .modules.main import MainWidget
from .styling import style
from ..utils.version import current_version as get_current_version
from ..utils.version import latest_version as get_latest_version
from ..utils.assets import path
from ..utils.assets import scripts

sys.path.append(os.path.dirname(os.path.abspath('__file__')))


def fix_npcap():
    os.system(scripts('fixnpcap.bat'))
    sys.exit(0)


def run():
    initialization_result = initialize()

    conf = config()
    window_config = conf['window']

    WIDTH = window_config['width']
    HEIGHT = window_config['height']

    app = QApplication(sys.argv)

    app.setStyleSheet(style)

    geometry = app.screens()[0].size()
    clipboard = app.clipboard()

    widget = MainWidget(clipboard)
    widget.setWindowOpacity(window_config['opacity'])
    widget.resize(WIDTH, HEIGHT)
    widget.move(0, geometry.height() - HEIGHT - 280)

    widget.setWindowTitle('Albion Online Stats')
    widget.setWindowIcon(QtGui.QIcon(path('albion-stats-icon.png')))

    if window_config['always_on_top']:
        widget.setWindowFlag(Qt.WindowStaysOnTopHint)
    if window_config['frameless']:
        widget.setWindowFlag(Qt.FramelessWindowHint)

    widget.show()

    current_version, latest_version = (
        get_current_version(), get_latest_version())

    if latest_version and current_version != latest_version:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Update available!")
        msg.setText("Another version of app is avaliable.")
        msg.setInformativeText("You are using app in version {}, latest version is {}".format(
            current_version, latest_version))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

    if initialization_result == InitializationResult.NetworkInterfaceListMissing:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Unable to track network traffic data!")
        msg.setText(
            "On windows make sure that WinPcap is installed in your system.")
        msg.setInformativeText("WinPcap can be installed from <a href='{}'>here</a> <br>\
            <b>Make sure to install with the \"Install Npcap in WinPcap API-compatible Mode\"<b> option<br><br>\
            In case where npcap is installed try to fix npcap and restart the app"
                               .format('https://nmap.org/npcap/dist/npcap-0.9990.exe'))
        msg.setStandardButtons(QMessageBox.Ok)
        button = QPushButton("Fix npcap")

        button.clicked.connect(fix_npcap)
        msg.addButton(button, QMessageBox.NoRole)
        msg.show()

    sys.exit(app.exec_())
