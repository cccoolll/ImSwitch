from qtpy import QtCore, QtWidgets

import imswitch


class CheckUpdatesDialog(QtWidgets.QDialog):
    """ Dialog for checking for ImSwitch updates. """

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint,
                         *args, **kwargs)
        self.setWindowTitle('Check for updates')
        self.setMinimumWidth(480)

        self.informationLabel = QtWidgets.QLabel()
        self.informationLabel.setWordWrap(True)
        self.informationLabel.setStyleSheet('font-size: 10pt')

        self.linkLabel = QtWidgets.QLabel()
        self.linkLabel.setTextFormat(QtCore.Qt.RichText)
        self.linkLabel.setOpenExternalLinks(True)
        self.linkLabel.setVisible(False)
        self.linkLabel.setStyleSheet('font-size: 10pt')

        self.buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok,
            QtCore.Qt.Horizontal,
            self
        )
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(16)
        layout.addWidget(self.informationLabel)
        layout.addWidget(self.linkLabel)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def resetUpdateInfo(self):
        self.informationLabel.setText('Checking for updates, please wait…')
        self.linkLabel.setText('')
        self.linkLabel.setVisible(False)

    def showFailed(self):
        self.informationLabel.setText('Failed to check for updates.')
        self.linkLabel.setText('')
        self.linkLabel.setVisible(False)

    def showNoUpdateAvailable(self):
        self.informationLabel.setText('No updates available.')
        self.linkLabel.setText('')
        self.linkLabel.setVisible(False)

    def showPyInstallerUpdate(self, newVersion):
        self.informationLabel.setText(
            f'ImSwitch {newVersion} is now available. '
            f' Your current version is {imswitch.__version__}.'
            f'\n\nTo update, download the new version archive from the link below and extract it into'
            f' a new folder. Do NOT overwrite your current installation; instead, delete it after'
            f' you have updated.'
        )
        self.linkLabel.setText(
            'The new version may be downloaded from <a href="https://github.com/kasasxav/ImSwitch/releases" style="color: orange">the GitHub releases page</a>.'
        )
        self.linkLabel.setVisible(True)

    def showPyPIUpdate(self, newVersion):
        self.informationLabel.setText(
            f'ImSwitch {newVersion} is now available. '
            f' Your current version is {imswitch.__version__}.'
            f'\n\nTo update, run the command: pip install --upgrade imswitch'
        )
        self.linkLabel.setText(
            'The changelog is available on <a href="https://github.com/kasasxav/ImSwitch/releases" style="color: orange">the GitHub releases page</a>.'
        )
        self.linkLabel.setVisible(True)


# Copyright (C) 2020, 2021 TestaLab
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
