"""This module is used for importation of raw data from IN16B instrument.

"""

import os

from dateutil.parser import parse

import h5py
import numpy as np

from collections import namedtuple

from scipy.signal import savgol_filter
from scipy.optimize import curve_fit

from nPDyn.dataParsers.xml_detector_grouping import IN16B_XML
from nPDyn.dataParsers.stringParser import parseString
from nPDyn.dataParsers.instruments.in16b import getDiffDetXAxis

from nPDyn import Sample


class IN16B_QENS:
    """This class can handle raw QENS data from IN16B
    at the ILL in the hdf5 format.

    :arg scanList:    a string or a list of files to be read and
                      parsed to extract the data.
                      It can be a path to a folder as well.
    :arg sumScans:    whether the scans should be summed or not.
    :arg unmirroring: whether the data should be unmirrored or not.
    :arg vanadiumRef: if :arg unmirroring: is True, then the peaks
                      positions are identified
                      using the data provided with this argument.
                      If it is None, then the peaks positions are
                      identified using the data in scanList.
    :arg detGroup:    detector grouping, i.e. the channels that
                      are summed over along the position-sensitive
                      detector tubes. It can be an integer, then the
                      same number is used for all detectors, where
                      the integer defines a region (middle of the
                      detector +/- detGroup). It can be a list of
                      integers, then each integers of the list
                      should corresponds to a detector. Or it can
                      be a string, defining a path to an xml file
                      as used in Mantid.
                      If set to `no`, no detector gouping is performed
                      and the data represents the signal for each
                      pixel on the detectors. In this case, the
                      observable become the momentum transfer q in
                      the vertical direction.
    :arg normalize:   whether the data should be normalized to the
                      monitor
    :arg strip:       an integer defining the number of points that
                      are ignored at each extremity of the spectrum.
    :arg observable:  the observable that might be changing over scans.
                      It can be `time` or `temperature`
    :arg roll:        Amount of shift on the energy axis to be given to
                      the measured data in case they are not properly aligned
                      with the monitor.
    :arg slidingSum:  If not None, the size of the window to perform a
                      sliding sum over the observables (default None).

    """

    def __init__(
        self,
        scanList,
        sumScans=True,
        unmirroring=True,
        vanadiumRef=None,
        peakFindingMask=None,
        detGroup=None,
        normalize=True,
        strip=10,
        observable="time",
        roll=0,
        slidingSum=None,
    ):

        self.data = namedtuple(
            "data",
            "intensities errors energies "
            "temps times name qVals "
            "qIdx observable "
            "observable_name norm "
            "diffraction diff_qVals",
        )

        self.scanList = parseString(scanList)

        self.sumScans = sumScans

        self.peaks = None
        self.unmirroring = unmirroring

        # Process the vanadiumRef argument in case a single string is given
        self.vanadiumRef = vanadiumRef
        if isinstance(scanList, str):
            if os.path.isdir(scanList):
                fList = os.listdir(scanList)
                scanList = [scanList.strip("/") + "/" + val for val in fList]
            else:
                scanList = [scanList]

        self.peakFindingMask = peakFindingMask
        self.detGroup = detGroup
        self.normalize = normalize
        self.observable = observable
        self.strip = strip
        self.roll = roll
        self.slidingSum = slidingSum

        self.dataList = []
        self.diffList = []
        self.diffQList = []
        self.errList = []
        self.energyList = []
        self.qList = []
        self.tempList = []
        self.qzList = []

        self.outTuple = None

    def process(self):
        """Extract data from the provided files and
        reduce them using the given parameters.

        """
        self.dataList = []
        self.diffList = []
        self.diffQList = []
        self.energyList = []
        self.qList = []
        self.qzList = []
        self.tempList = []
        self.startTimeList = []
        self.monitor = []

        for dataFile in self.scanList:
            dataset = h5py.File(dataFile, mode="r")

            data = dataset["entry0/data/PSD_data"][()]
            data = np.roll(data, self.roll, axis=-1)

            wavelength = dataset["entry0/wavelength"][()]

            monitor = (
                dataset["entry0/monitor/data"][()].squeeze().astype("float")
            )
            self.monitor.append(monitor)

            if "dataDiffDet" in dataset["entry0"].keys():
                diffraction = dataset["entry0/dataDiffDet/DiffDet_data"][()]
                self.diffQList = getDiffDetXAxis(wavelength)
                if self.normalize:
                    np.place(monitor, monitor <= 0, -np.inf)
                    diffraction = (
                        diffraction / monitor[np.newaxis, np.newaxis, :]
                    )
                self.diffList.append(diffraction.squeeze().mean(-1))

            self.name = dataset["entry0/subtitle"][(0)].astype(str)

            if self.detGroup == "no":
                self.observable = "$q_z$"
                nbrDet = data.shape[0]
                nbrChn = int(data.shape[2] / 2)
                nbrYPixels = int(data.shape[1])
                sampleToDec = (
                    dataset["entry0/instrument/PSD/distance_to_sample"][()]
                    * 10
                )
                tubeHeight = dataset["entry0/instrument/PSD/tubes_size"][()]
                qZ = np.arange(nbrYPixels) - nbrYPixels / 2
                qZ *= tubeHeight / nbrYPixels
                qZ *= 4 * np.pi / (sampleToDec * wavelength)
                self.qzList = qZ
            else:
                # Sum along the selected region of the tubes
                data = self._detGrouping(data)
                nbrDet = data.shape[0]
                nbrChn = int(data.shape[1] / 2)

            maxDeltaE = dataset[
                "entry0/instrument/Doppler/maximum_delta_energy"
            ][()]
            energies = 2 * np.arange(nbrChn)
            energies = energies * (maxDeltaE / nbrChn) - maxDeltaE

            angles = np.array(
                [
                    dataset[
                        "entry0/instrument/PSD/PSD angle %s" % int(val + 1)
                    ][()]
                    for val in range(nbrDet)
                ]
            )

            data, angles = self._getSingleD(dataset, data, angles)

            angles = (
                4
                * np.pi
                * np.sin(np.pi * np.array(angles).squeeze() / 360)
                / wavelength
            )

            temp = dataset["entry0/sample/temperature"][()]
            time = parse(dataset["entry0/start_time"][0])

            self.dataList.append(np.copy(data))
            self.energyList.append(np.copy(energies))
            self.qList.append(np.copy(angles))
            self.tempList.append(np.copy(temp))
            self.startTimeList.append(time)

            dataset.close()

        if self.slidingSum is not None:
            self._slidingSum(self.slidingSum)

        if self.sumScans:
            self.monitor = [np.sum(np.array(self.monitor), 0)]
            self.dataList = [np.sum(np.array(self.dataList), 0)]
            self.diffList = np.sum(np.array(self.diffList), 0)

        for idx, data in enumerate(self.dataList):
            if self.unmirroring:
                if self.vanadiumRef is not None:
                    vana = IN16B_QENS(self.vanadiumRef, detGroup=None)
                    vana.process()
                    self.leftPeak = vana.leftPeak
                    self.rightPeak = vana.rightPeak
                else:
                    self._findPeaks(data)

                data = self._unmirrorData(data)
                self.monitor[idx] = self._unmirrorData(
                    self.monitor[idx]
                ).squeeze()

            errData = np.sqrt(data)

            if self.normalize:
                np.place(self.monitor[idx], self.monitor[idx] <= 0, -np.inf)

                if self.detGroup == "no":
                    monitor = self.monitor[idx][:, np.newaxis, np.newaxis]
                else:
                    monitor = self.monitor[idx]

                data = data / monitor
                errData = errData / monitor

            self.dataList[idx] = data
            self.errList.append(errData)

        self._convertDataset()

        out = Sample(
            self.outTuple.intensities,
            errors=self.outTuple.errors,
            q=self.outTuple.qVals,
            name=self.outTuple.name,
            time=self.outTuple.times,
            temperature=self.outTuple.temps,
            energies=self.outTuple.energies,
            diffraction=self.outTuple.diffraction,
            qdiff=self.outTuple.diff_qVals,
            observable=self.outTuple.observable_name,
            axes=[self.outTuple.observable_name, "q", "energies"],
        )

        return out

    def _getSingleD(self, dataset, data, angles):
        """Determines the number of single detector used and add the data
        and angles to the existing data and angles arrays.

        :returns: data and angles arrays with the single detector data.

        """
        dataSD = []
        anglesSD = []

        keysSD = [
            "SD1 angle",
            "SD2 angle",
            "SD3 angle",
            "SD4 angle",
            "SD5 angle",
            "SD6 angle",
            "SD7 angle",
            "SD8 angle",
        ]

        for idx, key in enumerate(keysSD):
            angle = dataset["entry0/instrument/SingleD/%s" % key][()]

            if angle > 0:
                anglesSD.append(angle)
                dataSD.append(
                    dataset["entry0/instrument/SingleD/data"][(idx)].squeeze()
                )

        if self.observable == "$q_z$":
            tmpSD = np.zeros((len(dataSD), data.shape[1], data.shape[2]))
            tmpSD[:, 64] += np.array(dataSD)
            data = np.row_stack((tmpSD, data)).transpose(0, 2, 1)
        else:
            data = np.row_stack((np.array(dataSD).squeeze(), data))

        angles = np.concatenate((anglesSD, angles))

        return data, angles

    def _convertDataset(self):
        """Converts the data lists of the class into namedtuple(s)
        that can be directly used by nPDyn.

        """
        if self.strip > 0:
            data = np.array(self.dataList)[:, :, self.strip : -self.strip]
            errors = np.array(self.errList)[:, :, self.strip : -self.strip]
            energies = self.energyList[0][self.strip : -self.strip]
        else:
            data = np.array(self.dataList)
            errors = np.array(self.errList)
            energies = self.energyList[0]

        # converts the times to hours
        times = np.array(self.startTimeList)

        if self.sumScans:
            temps = np.array([np.mean(self.tempList)])
            times = np.array([0.0])
        else:
            times = times - times[0]
            for idx, t in enumerate(times):
                times[idx] = t.total_seconds() / 3600
            temps = np.array(self.tempList).squeeze()

        if self.observable == "time":
            Y = times
        elif self.observable == "temperature":
            Y = temps
        elif self.observable == "$q_z$":
            data = data.transpose(3, 1, 2, 0).squeeze()
            errors = errors.transpose(3, 1, 2, 0).squeeze()
            Y = self.qzList
            midPos = int(data.shape[0] / 2)
            data = (data[:midPos][::-1] + data[midPos:]) / 2
            errors = (errors[:midPos][::-1] + errors[midPos:]) / 2
            Y = (-Y[:midPos][::-1] + Y[midPos:]) / 2

        self.outTuple = self.data(
            data,
            errors,
            energies,
            temps,
            times,
            self.name,
            self.qList[0],
            np.arange(self.qList[0].shape[0]),
            Y,
            self.observable,
            False,
            np.array(self.diffList),
            self.diffQList,
        )

    def _findPeaks(self, data):
        """Find the peaks in each subset of mirrored data
        using the selected method.

        """
        data = np.array(data)
        if data.ndim == 1:
            data = data[np.newaxis, :]
        # if detGroup is none, sum over all vertical positions to find
        # peaks more effectively
        if data.ndim == 3:
            data = data.sum(2)

        nbrChannels = data.shape[1]
        midChannel = int(nbrChannels / 2)
        window = (
            int(midChannel / 2 - nbrChannels / 5),
            int(midChannel / 2 + nbrChannels / 5),
            3 * int(midChannel / 2 - nbrChannels / 5),
            3 * int(midChannel / 2 + nbrChannels / 5),
        )

        if self.peakFindingMask is None:
            mask = np.zeros_like(data)
            mask[:, window[0] : window[1]] = 1
            mask[:, window[2] : window[3]] = 1

        maskedData = data * mask

        # Finds the peaks by using a Gaussian function to fit the data
        Gaussian = lambda x, normF, gauW, shift: (
            normF
            * np.exp(-((x - shift) ** 2) / (2 * gauW ** 2))
            / (gauW * np.sqrt(2 * np.pi))
        )

        try:
            leftPeaks = []
            rightPeaks = []
            for qData in maskedData:
                # qData = np.convolve(qData, np.ones(12), mode="same")
                errors = np.sqrt(qData)
                np.place(errors, errors == 0, np.inf)

                params = curve_fit(
                    Gaussian,
                    np.arange(qData[:midChannel].size),
                    qData[:midChannel],
                    sigma=errors[:midChannel],
                    bounds=(0.0, np.inf),
                    p0=[qData[:midChannel].max(), 1, midChannel / 2],
                )
                leftPeaks.append(params[0][2])

                params = curve_fit(
                    Gaussian,
                    np.arange(qData[midChannel:].size),
                    qData[midChannel:],
                    sigma=errors[midChannel:],
                    bounds=(0.0, np.inf),
                    p0=[qData[midChannel:].max(), 1, midChannel / 2],
                )
                rightPeaks.append(params[0][2])

            gauss_leftPeak = np.array(leftPeaks)
            gauss_rightPeak = np.array(rightPeaks)

            self.leftPeak = np.rint(gauss_leftPeak).astype(int)
            self.rightPeak = np.rint(gauss_rightPeak).astype(int)

        except RuntimeError:
            # Finds the peaks using a Savitsky-Golay filter to
            # smooth the data, and extract the position of the maximum
            filters = np.array(
                [
                    savgol_filter(maskedData, 5, 4),
                    savgol_filter(maskedData, 11, 4),
                    savgol_filter(maskedData, 19, 3),
                    savgol_filter(maskedData, 25, 3),
                ]
            )

            savGol_leftPeak = np.mean(
                np.argmax(filters[:, :, :midChannel], 2), 0
            )
            savGol_rightPeak = np.mean(
                np.argmax(filters[:, :, midChannel:], 2), 0
            )

            self.leftPeak = savGol_leftPeak.astype(int)
            self.rightPeak = savGol_rightPeak.astype(int)

    def _unmirrorData(self, data):
        """If unmirroring is required, unmirror data using the
        peaks found. Basically, the two mirror dataset are aligned
        on their respective peaks and summed.

        It should be called after the summation on vertical positions
        of the PSD was performed.

        """
        data = np.array(data)
        if data.ndim == 1:
            data = data[np.newaxis, :]

        nbrChannels = data.shape[1]
        midChannel = int(nbrChannels / 2)

        for qIdx, qData in enumerate(data):
            data[qIdx] = np.roll(
                qData, midChannel - self.leftPeak[qIdx]
            ) + np.roll(
                qData, midChannel - (midChannel + self.rightPeak[qIdx])
            )

        return data[:, int(midChannel / 2) : 3 * int(midChannel / 2)]

    def _detGrouping(self, data):
        """The method performs a sum along detector tubes using the provided
        range to be kept.

        It makes use of the :arg detGroup: argument.

        If the argument is a scalar, it sums over all
        values that are in the range
        [center of the tube - detGroup : center of the tube + detGroup].

        If the argument is a list of integers, then each element of the
        list is assumed to correspond to a range for each corresponding
        detector in ascending order.

        If the argument is a mantid-related xml file (a python string),
        the xml_detector_grouping module is then used to parse the xml
        file and the provided values are used to define the range.

        :arg data:  PSD data for the file being processed

        """
        if isinstance(self.detGroup, int):
            midPos = int(data.shape[1] / 2)
            data = data[:, midPos - self.detGroup : midPos + self.detGroup, :]
            out = np.sum(data, 1)

        elif isinstance(self.detGroup, (list, tuple, np.ndarray)):
            midPos = int(data.shape[1] / 2)

            out = np.zeros((data.shape[0], data.shape[2]))
            for detId, detData in enumerate(data):
                detData = detData[
                    midPos
                    - self.detGroup[detId] : midPos
                    + self.detGroup[detId]
                ]
                out[detId] = np.sum(detData, 0)

        elif isinstance(self.detGroup, str):
            numTubes = data.shape[0]
            xmlData = IN16B_XML(self.detGroup, numTubes)

            detRanges = xmlData.getPSDValues()

            out = np.zeros((data.shape[0], data.shape[2]))
            for detId, vals in enumerate(detRanges):
                out[detId] = data[detId, vals[0] : vals[1]].sum(0)

        elif self.detGroup is None:
            out = np.sum(data, 1)

        return out.astype("float")

    def _slidingSum(self, size):
        """Performs a sliding sum over scans.

        Parameters
        ----------
        size : int
            The size of the window to be summed over.
        data : list
            The list of datasets/scans.
        monitor : list
            The list of monitor data corresponding to each dataset.

        """
        outData = []
        outDiff = []
        outMonitor = []
        outTemp = []

        data = np.array(self.dataList)
        diff = np.array(self.diffList)
        monitor = np.array(self.monitor)
        temp = np.array(self.tempList)
        for idx, val in enumerate(data[:-size]):
            outData.append(np.sum(data[idx : idx + size], 0))
            outDiff.append(np.sum(diff[idx : idx + size], 0))
            outMonitor.append(np.sum(monitor[idx : idx + size], 0))
            outTemp.append(np.mean(temp[idx : idx + size], 0))

        self.dataList = outData
        self.diffList = outDiff
        self.monitor = outMonitor
        self.tempList = outTemp
        self.startTimeList = self.startTimeList[:-size]
