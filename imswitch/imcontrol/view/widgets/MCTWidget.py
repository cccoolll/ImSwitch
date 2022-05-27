import numpy as np
import pyqtgraph as pg
from qtpy import QtCore, QtWidgets

from imswitch.imcontrol.view import guitools
from .basewidgets import NapariHybridWidget


class MCTWidget(NapariHybridWidget):
    """ Widget containing mct interface. """


    sigMCTInitFilterPos = QtCore.Signal(bool)  # (enabled)
    sigMCTShowLast = QtCore.Signal(bool)  # (enabled)
    sigMCTStop = QtCore.Signal(bool)  # (enabled)
    sigMCTStart = QtCore.Signal(bool)  # (enabled)


    sigShowToggled = QtCore.Signal(bool)  # (enabled)
    sigPIDToggled = QtCore.Signal(bool)  # (enabled)
    sigUpdateRateChanged = QtCore.Signal(float)  # (rate)
    
    
    sigSliderLaser2ValueChanged = QtCore.Signal(float)  # (value)
    sigSliderLaser1ValueChanged = QtCore.Signal(float)  # (value)



    def __post_init__(self):
        #super().__init__(*args, **kwargs)


        self.mctFrame = pg.GraphicsLayoutWidget()
        
        # initialize all GUI elements
        
        # period
        self.mctLabelTimePeriod  = QtWidgets.QLabel('Period T (s):')
        self.mctValueTimePeriod = QtWidgets.QLineEdit('5')

        # z-stack
        self.mctLabelZStack  = QtWidgets.QLabel('Z-Stack (min,max,steps):')        
        self.mctValueZmin = QtWidgets.QLineEdit('0')
        self.mctValueZmax = QtWidgets.QLineEdit('100')
        self.mctValueZsteps = QtWidgets.QLineEdit('10')
        
        # Laser 1
        valueDecimalsLaser = 1
        valueRangeLaser = (0,2**15)
        tickIntervalLaser = 1
        singleStepLaser = 1
        
        self.mctLabelLaser1  = QtWidgets.QLabel('Intensity (Laser 1):')        
        self.mctLabelLaser2  = QtWidgets.QLabel('Intensity (Laser 2):')        
        
        valueRangeMinLaser, valueRangeMaxLaser = valueRangeLaser
        self.sliderLaser1 = guitools.FloatSlider(QtCore.Qt.Horizontal, self, allowScrollChanges=False,
                                        decimals=valueDecimalsLaser)
        self.sliderLaser1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sliderLaser1.setMinimum(valueRangeMinLaser)
        self.sliderLaser1.setMaximum(valueRangeMaxLaser)
        self.sliderLaser1.setTickInterval(tickIntervalLaser)
        self.sliderLaser1.setSingleStep(singleStepLaser)
        self.sliderLaser1.setValue(0)
        
        self.sliderLaser1.valueChanged.connect(
            lambda value: self.sigSliderLaser1ValueChanged.emit(value)
        )
                        
        self.sliderLaser2 = guitools.FloatSlider(QtCore.Qt.Horizontal, self, allowScrollChanges=False,
                                        decimals=valueDecimalsLaser)
        self.sliderLaser2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sliderLaser2.setMinimum(valueRangeMinLaser)
        self.sliderLaser2.setMaximum(valueRangeMaxLaser)
        self.sliderLaser2.setTickInterval(tickIntervalLaser)
        self.sliderLaser2.setSingleStep(singleStepLaser)
        self.sliderLaser2.setValue(0)
        self.sliderLaser2.valueChanged.connect(
            lambda value: self.sigSliderLaser2ValueChanged.emit(value)
        )
        
        self.mctLabelFileName  = QtWidgets.QLabel('FileName:')
        self.mctEditFileName  = QtWidgets.QLabel('Test')
        self.mctNImages  = QtWidgets.QLabel('Number of images: ')

        self.mctStartButton = guitools.BetterPushButton('Start')
        self.mctStartButton.setCheckable(False)
        self.mctStartButton.toggled.connect(self.sigMCTStart)

        self.mctStopButton = guitools.BetterPushButton('Stop')
        self.mctStopButton.setCheckable(False)
        self.mctStopButton.toggled.connect(self.sigMCTStop)

        self.mctShowLastButton = guitools.BetterPushButton('Show Last')
        self.mctShowLastButton.setCheckable(False)
        self.mctShowLastButton.toggled.connect(self.sigMCTShowLast)

        self.mctInitFilterButton = guitools.BetterPushButton('Init Filter Pos.')
        self.mctInitFilterButton.setCheckable(False)
        self.mctInitFilterButton.toggled.connect(self.sigMCTInitFilterPos)

        # enable
        self.mctDoBrightfield = QtWidgets.QCheckBox('Perform Brightfield')
        self.mctDoBrightfield.setCheckable(True)
        
        self.mctDoZStack = QtWidgets.QCheckBox('Perform Z-Stack')
        self.mctDoZStack.setCheckable(True)
        
        # Defining layout
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.grid.addWidget(self.mctLabelTimePeriod, 0, 0, 1, 1)
        self.grid.addWidget(self.mctValueTimePeriod, 0, 1, 1, 1)
        self.grid.addWidget(self.mctDoZStack, 0, 2, 1, 1)
        self.grid.addWidget(self.mctDoBrightfield, 0, 3, 1, 1)
        self.grid.addWidget(self.mctLabelZStack, 1, 0, 1, 1)
        self.grid.addWidget(self.mctValueZmin, 1, 1, 1, 1)
        self.grid.addWidget(self.mctValueZmax, 1, 2, 1, 1)
        self.grid.addWidget(self.mctValueZsteps, 1, 3, 1, 1)
        self.grid.addWidget(self.mctLabelLaser1, 2, 0, 1, 1)
        self.grid.addWidget(self.sliderLaser1, 2, 1, 1, 3)
        self.grid.addWidget(self.mctLabelLaser2, 3, 0, 1, 1)
        self.grid.addWidget(self.sliderLaser2, 3, 1, 1, 3)        
        self.grid.addWidget(self.mctLabelFileName, 4, 0, 1, 1)
        self.grid.addWidget(self.mctEditFileName, 4, 1, 1, 1)
        self.grid.addWidget(self.mctNImages, 4, 2, 1, 1)
        self.grid.addWidget(self.mctStartButton, 5, 0, 1, 1)
        self.grid.addWidget(self.mctStopButton, 5, 1, 1, 1)
        self.grid.addWidget(self.mctShowLastButton,5, 2, 1, 1)
        self.grid.addWidget(self.mctInitFilterButton,5, 3, 1, 1)
        
        
        
    def getImage(self):
        if self.layer is not None:
            return self.img.image
        
    def setImage(self, im):
        if self.layer is None or self.layer.name not in self.viewer.layers:
            self.layer = self.viewer.add_image(im, rgb=False, name="MCT Reconstruction", blending='additive')
        self.layer.data = im
        
        
    def getZStackValues(self):
        valueZmin = float(self.mctValueZmin.text())
        valueZmax = float(self.mctValueZmax.text())
        valueZsteps = float(self.mctValueZsteps.text())
        valueZenabled = bool(self.mctDoZStack.isChecked())
        
        return valueZmin, valueZmax, valueZsteps, valueZenabled
 
    def getTimelapseValues(self):
        mctValueTimePeriod = float(self.mctValueTimePeriod.text())
        return mctValueTimePeriod
     
    def getBrightfieldEnabled(self):
        valueBrightfield = bool(self.mctDoBrightfield.isChecked())
        return valueBrightfield
    
    def getFilename(self):
        mctEditFileName = self.mctEditFileName.text()
        from datetime import datetime
        date = datetime. now(). strftime("%Y_%m_%d-%I-%M-%S_%p")
        
        return f"{date}_mctEditFileName"
    
    def setNImages(self, nImages):
        self.mctNImages.setText('Number of images: '+str(nImages))
    
    
    
        
# Copyright (C) 2020-2021 ImSwitch developers
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
