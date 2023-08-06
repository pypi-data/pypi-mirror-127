"""Base type for all data imported in nPDyn.

This module contains a :class:`BaseType` class definition which is used
for all data imported in nPDyn.

Its role is to handle files, importation of data, and common data processing
routines. Moreover, each dataset created with this class can have associated
data for corrections and fitting (see :class:`BaseType` documentation)

"""
from functools import wraps

import re

from collections import OrderedDict

import numpy as np

try:
    from lmfit import Model as lmModel
except ImportError:

    class lmModel:
        pass


from nPDyn.dataManipulation.binData import binData
from nPDyn.dataManipulation.slidingAverage import slidingAverage
from nPDyn.fileFormatParser import guessFileFormat, readFile
from nPDyn.dataParsers import IN16B_FWS, IN16B_QENS, IN16B_BATS

from nPDyn.models import Model, Component, Parameters
from nPDyn.models.presets import linear, calibratedD2O
from nPDyn.lmfit.convolvedModel import ConvolvedModel
from nPDyn.lmfit.lmfit_presets import hline
from nPDyn.lmfit.lmfit_presets import calibratedD2O as lmCalibratedD2O

try:
    from nPDyn.lib.pyabsco import py_absco_slab, py_absco_tube
except ImportError:
    print(
        "\nAbsorption correction libraries are not available. "
        "Paalman_Pings correction cannot be used.\n"
        "Verify that GSL libraries are available on this computer.\n"
    )


# -------------------------------------------------------
# Useful decorators for BaseType class
# -------------------------------------------------------
def ensure_attr(attr):
    """Ensures the attribute 'attr' is not None is the class."""

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if getattr(args[0], attr) is None:
                raise AttributeError(
                    "Attribute '%s' is None, please set it "
                    "before using this method." % attr
                )
            return func(*args, **kwargs)

        return wrapper

    return dec


def ensure_fit(func):
    """Ensures the class has a fitted model."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0]._fit is []:
            raise ValueError(
                "Dataset (%s) has no fitted model associated with "
                "it, please fit a model before using it." % args[0].__repr__()
            )
        return func(*args, **kwargs)

    return wrapper


# -------------------------------------------------------
# BaseType class
# -------------------------------------------------------
class BaseType:
    """Initialize a base type that can handle files, their parsing
    and importation as well as common data processing routines.

    Note
    ----
    This class is usually not used directly, but rather decorated by
    more specialized class depending on the type of data that is
    imported (see :class:`QENSType`, :class:`FWSType`,
    :class:`TempRampType`)

    Parameters
    ----------
    fileName : str or list(str), optional
        name of the file(s) to be read, can also be a directory for
        raw data (in this case, all files in the directory are imported)
    data : data namedtuple, optional
        resulting namedtuple from data parsers
    rawData : data namedtuple, optional
        named tuple containing the imported data without any further
        processing. Used by the decorator for specialized classes
    resData : :class:`resType`, optional
        data for resolution function
    D2OData : :class:`D2OType` or :class:`fD2OType`, optional
        D2O (or buffer) data if needed
    ECData : :class:`ECType` or :class:`fECType`, optional
        empty cell measurement data

    """

    def __init__(
        self,
        fileName=None,
        data=None,
        rawData=None,
        resData=None,
        D2OData=None,
        ECData=None,
        model=None,
    ):
        self.fileName = fileName
        self.data = data
        self._rawData = rawData  # Used to reset data to its initial state

        self.resData = resData
        self.D2OData = D2OData
        self.ECData = ECData

        self._QENS_redAlgo = {"IN16B": IN16B_QENS, "BATS": IN16B_BATS}
        self._FWS_redAlgo = {"IN16B": IN16B_FWS}
        self._BATS_redAlgo = {"BATS": IN16B_BATS}

        self.model = model
        self._fit = []

    def importData(self, fileFormat=None):
        """Extract data from file and store them in *data* and *rawData*
        attributes.

        If no fileFormat is given, tries to guess it, try hdf5 format
        if format cannot be guessed.

        Parameters
        ----------
        fileFormat : str, optional
            file format to be used, can be 'inx' or 'mantid'

        """
        if fileFormat:
            data = readFile(fileFormat, self.fileName)
        else:
            data = guessFileFormat(self.fileName)

        self.data = data
        self._rawData = self.data._replace(
            qVals=np.copy(self.data.qVals),
            times=np.copy(self.data.times),
            intensities=np.copy(self.data.intensities),
            errors=np.copy(self.data.errors),
            temps=np.copy(self.data.temps),
            norm=False,
            qIdx=np.copy(self.data.qIdx),
            energies=np.copy(self.data.energies),
            observable=np.copy(self.data.observable),
            observable_name=np.copy(self.data.observable_name),
        )

    def importRawData(self, dataList, instrument, dataType, **kwargs):
        """This method uses instrument-specific algorithm to process raw data.

        :arg dataList:      a list of data files to be imported
        :arg instrument:    the instrument used to record data
                            (only 'IN16B' possible for now)
        :arg dataType:      type of data recorded (can be 'QENS' or 'FWS')
        :arg kwargs:        keyword arguments to be passed to the algorithm
                            (see algorithm in dataParsers for details)

        """
        if dataType in ["QENS", "res", "ec", "D2O"]:
            data = self._QENS_redAlgo[instrument](dataList, **kwargs)
            data.process()
            self.data = data.outTuple

        elif dataType in ["FWS", "fec", "fD2O"]:
            data = self._FWS_redAlgo[instrument](dataList, **kwargs)
            data.process()
            self.data = data.outTuple

        self._rawData = self.data._replace(
            qVals=np.copy(self.data.qVals),
            times=np.copy(self.data.times),
            intensities=np.copy(self.data.intensities),
            errors=np.copy(self.data.errors),
            temps=np.copy(self.data.temps),
            norm=False,
            qIdx=np.copy(self.data.qIdx),
            energies=np.copy(self.data.energies),
            observable=np.copy(self.data.observable),
            observable_name=np.copy(self.data.observable_name),
        )

    def resetData(self):
        """Reset *data* attrbute to its initial state by
        copying *rawData* attribute.

        """
        self.data = self.data._replace(
            qVals=np.copy(self._rawData.qVals),
            times=np.copy(self._rawData.times),
            intensities=np.copy(self._rawData.intensities),
            errors=np.copy(self._rawData.errors),
            temps=np.copy(self._rawData.temps),
            norm=False,
            qIdx=np.copy(self._rawData.qIdx),
            energies=np.copy(self._rawData.energies),
            observable=np.copy(self._rawData.observable),
            observable_name=np.copy(self._rawData.observable_name),
        )

    # accessors for the data attributes
    @property
    def intensities(self):
        """Return the intensities"""
        return self.data.intensities

    @property
    def errors(self):
        """Return the errors"""
        return self.data.errors

    @property
    def qVals(self):
        """Return the qVals"""
        return self.data.qVals

    @property
    def energies(self):
        """Return the energies"""
        return self.data.energies

    @property
    def observable(self):
        """Return the observable"""
        return self.data.observable

    @property
    def observable_name(self):
        """Return the observable_name"""
        return self.data.observable_name

    @property
    def times(self):
        """Return the times"""
        return self.data.times

    @property
    def temps(self):
        """Return the temps"""
        return self.data.temps

    @property
    def name(self):
        """Return the name"""
        if self.data.name is not None:
            return self.data.name
        else:
            return self.data.fileName

    @property
    def diffraction(self):
        """Return the diffraction data"""
        return self.data.diffraction

    @property
    def diff_qVals(self):
        """Return the momentum transfers for diffraction data"""
        return self.data.diff_qVals

    # accessors for associated datasets
    @property
    def resData(self):
        """Return the data for resolution function."""
        return self._resData

    @resData.setter
    def resData(self, data):
        """Setter for the resData attribute."""
        if data is not None:
            if not isinstance(data, BaseType):
                raise ValueError(
                    "This attribute should be an instance of class "
                    "'BaseType' or inherits from it."
                )
            self._resData = data
        else:
            self._resData = None

    @property
    def ECData(self):
        """Return the data for resolution function."""
        return self._ECData

    @ECData.setter
    def ECData(self, data):
        """Setter for the resData attribute."""
        if data is not None:
            if not isinstance(data, BaseType):
                raise ValueError(
                    "This attribute should be an instance of class "
                    "'BaseType' or inherits from it."
                )
            self._ECData = data
        else:
            self._ECData = None

    @property
    def D2OData(self):
        """Return the data for resolution function."""
        return self._D2OData

    @D2OData.setter
    def D2OData(self, data):
        """Setter for the resData attribute."""
        if data is not None:
            if not isinstance(data, BaseType):
                raise ValueError(
                    "This attribute should be an instance of class "
                    "'BaseType' or inherits from it."
                )
            self._D2OData = data
        else:
            self._D2OData = None

    def binData(self, binSize, axis):
        """Bin *data* attribute using the given *binSize*."""
        self.data = binData(self.data, binSize, axis)

    def slidingAverage(self, windowLength):
        """Sliding average of the data along the observables"""
        self.data = slidingAverage(self.data, windowLength)

    def scaleData(self, scale):
        """Scale intensities and errors using the provided `scale`."""
        self.data = self.data._replace(
            intensities=scale * self.data.intensities,
            errors=scale * self.data.errors,
        )

    def addData(self, values, errors=None):
        """Add values to intensities using the `values` argument."""
        if errors is None:
            errors = np.zeros_like(values)

        self.data = self.data._replace(
            intensities=values + self.data.intensities,
            errors=np.sqrt(self.data.errors ** 2 + errors ** 2),
        )

    @ensure_attr("resData")
    def normalize_usingResFunc(self):
        """Normalizes data using integral of `resData.fit_best()`
        or experimental measurement of `resData`.

        """
        if not self.data.norm:
            intensities = self.data.intensities
            errors = self.data.errors

            norm = self._getNormRes()

            # Applying normalization
            self.data = self.data._replace(
                intensities=intensities / norm, errors=errors / norm, norm=True
            )

    def normalize_usingLowTemp(self, nbrBins):
        """Normalizes data using low temperature signal.

        An average is performed over the given number of bins for each q value
        and data are divided by the result.

        """
        normFList = np.mean(self.data.intensities[:nbrBins, :, :], axis=0)[
            np.newaxis, :, :
        ]

        self.data = self.data._replace(
            intensities=self.data.intensities / normFList,
            errors=self.data.errors / normFList,
            norm=True,
        )

    def normalize_usingSelf(self):
        """Normalized data using the integral of the model or experimental."""
        if not self.data.norm:
            intensities = self.data.intensities
            energies = self.data.energies
            errors = self.data.errors

            if len(self._fit) > 0:
                x = self._fit[0].userkws["x"]
                norm = self.fit_best()
            else:
                x = energies
                norm = np.copy(intensities)

            norm = (norm.sum(2) * (x[1] - x[0]))[:, :, np.newaxis]

            # Applying normalization
            self.data = self.data._replace(
                intensities=intensities / norm, errors=errors / norm, norm=True
            )

    @ensure_attr("ECData")
    def subtractEC(self, scaleFactor=0.95, useModel=True):
        """Use the assigned empty cell data for subtraction to loaded data.

        Parameters
        ----------
        scaleFactor : float
            Empty cell data are scaled using the given
            factor prior to subtraction.
        useModel : bool
            For QENS data, use the fitted model instead of experimental
            points to perform the subtraction if True.

        """
        if useModel and self.ECData.model is not None:  # Use a fitted model
            ECFunc = self.ECData.fit_best(x=self.data.energies)
        else:
            ECData = self.ECData.data.intensities
            if ECData.shape == self.data.intensities.shape:
                ECFunc = self.ECData.data.intensities
            else:
                ids = np.argmin(
                    [
                        (self.ECData.data.energies - val) ** 2
                        for val in self.data.energies
                    ],
                    axis=1,
                )
                ECFunc = ECData[:, :, ids]

        normEC = np.zeros_like(self.data.intensities) + ECFunc

        intensities = self.data.intensities

        # If data are normalized, uses the same normalization
        # factor for empty cell data
        if self.data.norm and not self.ECData.data.norm:
            norm = self._getNormRes()
            normEC /= norm

        self.data = self.data._replace(
            intensities=intensities - scaleFactor * normEC
        )

    @ensure_attr("ECData")
    def absorptionCorrection(
        self,
        canType="tube",
        canScaling=0.9,
        neutron_wavelength=6.27,
        absco_kwargs=None,
        useModel=True,
    ):
        """Computes absorption Paalman-Pings coefficients

        Can be used for sample in a flat or tubular can and apply corrections
        to data, for each q-value in *data.qVals* attribute.

        Parameters
        ----------
        canType : {'tube', 'slab'}
            type of can used, either 'tube' or 'slab'
            (default 'tube')
        canScaling : float
            scaling factor for empty can contribution term, set it to 0
            to use only correction of sample self-attenuation
        neutron_wavelength : float
            incident neutrons wavelength
        absco_kwargs : dict
            geometry arguments for absco library
            from Joachim Wuttke [#]_.

        References
        ----------

        .. [#] http://apps.jcns.fz-juelich.de/doku/sc/absco

        """
        # Defining some defaults arguments
        kwargs = {
            "mu_i_S": 0.660,
            "mu_f_S": 0.660,
            "mu_i_C": 0.147,
            "mu_f_C": 0.147,
        }

        if canType == "slab":
            kwargs["slab_angle"] = 45
            kwargs["thickness_S"] = 0.03
            kwargs["thickness_C_front"] = 0.5
            kwargs["thickness_C_rear"] = 0.5

        if canType == "tube":
            kwargs["radius"] = 2.15
            kwargs["thickness_S"] = 0.03
            kwargs["thickness_C_inner"] = 0.1
            kwargs["thickness_C_outer"] = 0.1

        # Modifies default arguments with given ones, if any
        if absco_kwargs is not None:
            kwargs.update(absco_kwargs)

        sampleSignal = self.data.intensities

        if useModel and self.ECData.model is not None:  # Use a fitted model
            ECFunc = self.ECData.fit_best(x=self.data.energies)
        else:
            ECData = self.ECData.data.intensities
            if ECData.shape == self.data.intensities.shape:
                ECFunc = self.ECData.data.intensities
            else:
                ids = np.argmin(
                    [
                        (self.ECData.data.energies - val) ** 2
                        for val in self.data.energies
                    ],
                    axis=1,
                )
                ECFunc = ECData[:, :, ids]

        normEC = np.zeros_like(self.data.intensities) + ECFunc

        # If data are normalized, uses the same normalization
        # factor for empty cell data
        if self.data.norm and not self.ECData.data.norm:
            norm = self._getNormRes()
            normEC /= norm

        for qIdx, angle in enumerate(self.data.qVals):
            angle = np.arcsin(neutron_wavelength * angle / (4 * np.pi))
            if canType == "slab":
                A_S_SC, A_C_SC, A_C_C = py_absco_slab(angle, **kwargs)
            if canType == "tube":
                A_S_SC, A_C_SC, A_C_C = py_absco_tube(angle, **kwargs)

            # Applies correction
            sampleSignal[:, qIdx] = (1 / A_S_SC) * sampleSignal[
                :, qIdx
            ] - A_C_SC / (A_S_SC * A_C_C) * canScaling * normEC[:, qIdx]

        self.data = self.data._replace(intensities=sampleSignal)

    def discardDetectors(self, *qIdx):
        """Remove detectors (q-values)."""
        ids = np.array(
            [idx for idx, val in enumerate(self.data.qIdx) if val not in qIdx]
        )

        self.data = self.data._replace(
            intensities=self.data.intensities[:, ids],
            errors=self.data.errors[:, ids],
            qVals=self.data.qVals[ids],
            qIdx=self.data.qIdx[ids],
        )

    def setQRange(self, minQ, maxQ):
        """Discard detectors that do not lie inside required q-range

        Parameters
        ----------
        minQ : float
            Minimum value of the range.
        maxQ : float
            Maximum value of the range.

        """
        ids = np.argwhere(
            np.logical_and(self.data.qVals > minQ, self.data.qVals < maxQ)
        ).flatten()
        self.data = self.data._replace(
            intensities=self.data.intensities[:, ids],
            errors=self.data.errors[:, ids],
            qVals=self.data.qVals[ids],
            qIdx=ids,
        )

    @ensure_attr("resData")
    def _getNormRes(self):
        """Return the normalization factors from `resData`."""
        if len(self.resData._fit) > 0:
            res = self.resData.fit_best()
            x = self.resData.model.userkws["x"]
        else:
            x = self.resData.data.energies
            res = self.resData.data.intensities

        norm = res.sum(2) * (x[1] - x[0])

        return norm[:, :, np.newaxis]

    # -------------------------------------------------------
    # Methods related to data fitting
    # -------------------------------------------------------
    @property
    def model(self):
        """Return the model instance."""
        return self._model

    @model.setter
    def model(self, model):
        """Setter for the model attribute."""
        if model is not None:
            if not isinstance(model, (lmModel, Model)):
                raise ValueError(
                    "The model should be an instance of the "
                    "Model class or of the "
                    "'lmfit.Model' class or a class instance "
                    "that inherits from it."
                )
            self._model = model
        else:
            self._model = None

    @ensure_fit
    def getFixedOptParams(self, obsIdx):
        """Return the fixed optimal parameters

        The parameters are return for the given observable
        value at index `obsIdx` or the first entry if there is only
        one observable.

        """
        fitList = self._fit

        # check if the obsIdx is within the size, use the first index if not.
        if not obsIdx <= len(fitList):
            obsIdx = 0

        bestModel = fitList[obsIdx]

        if isinstance(self.model, Model):
            params = bestModel.optParams
            for key, par in params.items():
                params.set(key, fixed=True)
        else:
            params = {}
            opt = bestModel.params
            for key, par in opt.items():
                params[key] = OrderedDict(
                    {
                        "value": par.value,
                        "min": par.min,
                        "max": par.max,
                        "vary": False,
                        "expr": par.expr,
                    }
                )

        return params

    def fit(
        self,
        model=None,
        cleanData="replace",
        convolveRes=False,
        addEC=False,
        addD2O=False,
        volFractionD2O=0.95,
        **kwargs
    ):
        """Fit the dataset using the `model` attribute.

        Parameters
        ----------
        model : :class:`Model` instance
            The model to be used for fitting.
            If None, will look for a model instance in 'model' attribute of
            the class instance.
            If not None, will override the model attribute of the class
            instance.
        cleanData : {'replace', 'omit'} or anything else for no, optional
            If set to 'replace' the locations of null or inf values in data
            are set to *np.inf* in weights prior to fitting.
            If set to 'omit' the locations of null or inf values in data
            are removed from data, weights and x prior to fitting.
            Else, nothing is done.
        convolveRes : bool, optional
            If True, will use the attribute `resData`, fix the parameters,
            and convolve it with the data using:
            ``model = ConvolvedModel(self, resModel)``
        addEC : bool, optional
            If True, will use the attribute `ECData`, fix the parameters,
            model by calling:
            ``ECModel = self.ECData.fixedModel``
            and generate a new model by calling:
            ``model = self.model + ECModel``
        addD2O : bool, optional
            If True, will use the attribute `D2OData` to obtain the fixed
            model by calling:
            ``D2OModel = self.D2OData.fixedModel``
            and generate a new model by calling:
            ``model = self.model + D2OModel``
        volFractionD2O : float [0, 1]
            Volume fraction for the D2O in the sample.
            (default 0.95)
        kwargs : dict, optional
            Additional keyword arguments to pass to `Model.fit` method.
            It can override any parameters obtained from the dataset, which are
            passed to the fit function ('data', 'errors', 'x',...).

        """
        print("Fitting dataset: %s" % self.name)

        if model is None:
            if self.model is None:
                raise ValueError(
                    "The dataset has no model associated "
                    "with it.\n"
                    "Please assign one before using this method "
                    "without specifying a model."
                )
            model = self.model
        self.model = model

        # reset the state of '_fit'
        self._fit = []

        q = self.data.qVals[:, np.newaxis]

        if "data" not in kwargs.keys():
            data = np.copy(self.data.intensities)
        else:
            data = kwargs["data"]
        if "errors" not in kwargs.keys():
            errors = np.copy(self.data.errors)
        else:
            errors = kwargs["errors"]
        if isinstance(self.model, lmModel):
            errors = 1 / errors

        x = np.copy(self.data.energies)

        if cleanData in ["replace", "omit"]:
            data, errors, x = self._cleanData(data, errors, x, cleanData)

        if isinstance(self.model, Model):
            kwParams = self.model.params._paramsToList()
        else:
            kwParams = None

        fit_kwargs = {"x": x, "q": q, "params": kwParams}

        if kwargs is not None:
            fit_kwargs.update(kwargs)

        if convolveRes:
            if isinstance(self.model, Model):
                resModel = self.resData.model.copy()
                if self.data.norm and not self.resData.data.norm:
                    resModel /= Component(
                        "norm", linear, a=0.0, b=self._getNormRes()[0]
                    )
                fit_kwargs["convolve"] = resModel
            else:
                resModel = self.resData.model
                if self.data.norm and not self.resData.data.norm:
                    resModel = resModel / lmModel(
                        lambda x: self._getNormRes()[0], prefix="res_"
                    )
                model = ConvolvedModel(model, resModel)
                model.param_hints.update(self.resData.getFixedOptParams(0))

        if addEC:
            if isinstance(self.model, Model):
                ecModel = self.ECData.model.copy()
                for key, item in ecModel.components.items():
                    item.skip_convolve = True
                if self.data.norm and not self.ECData.data.norm:
                    ecModel /= Component(
                        "norm", linear, a=0.0, b=self._getNormRes()[0]
                    )
                model = model + ecModel
            else:
                ecModel = self.ECData.model
                if self.data.norm and not self.ECData.data.norm:
                    ecModel /= lmModel(
                        lambda x: self._getNormRes()[0], prefix="ec_"
                    )
                model.param_hints.update(self.ECData.getFixedOptParams(0))

        if addD2O:
            if self.data.norm and not self.D2OData.data.norm:
                norm = 1 / self._getNormRes()[0]
            else:
                norm = 1
            if isinstance(self.model, Model):
                model.addComponent(
                    Component(
                        "$D_2O$",
                        lambda x: norm
                        * volFractionD2O
                        * self.D2OData.fit_best(x=x, q=q)[0],
                        skip_convolve=True,
                    )
                )
            else:
                model += self.D2OData.model
                model *= lmModel(lambda x: volFractionD2O, prefix="D2O_")
                model /= lmModel(lambda x: norm, prefix="D2O_")
                model.param_hints.update(self.D2OData.getFixedOptParams(0))

        for idx, obs in enumerate(self.data.observable):
            # get the right observable index for data and errors
            fit_kwargs["data"] = data[idx]
            fit_kwargs["weights"] = errors[idx]

            print(
                "\tFit of observable %i of %i (%s=%s)"
                % (
                    idx + 1,
                    self.data.intensities.shape[0],
                    self.data.observable_name,
                    obs,
                ),
                end="\r",
            )

            fitRes = model.fit(**fit_kwargs)

            if isinstance(self.model, Model):
                tmp = model.copy()
                self._fit.append(tmp)
            else:
                self._fit.append(fitRes)

        if isinstance(self.model, Model):
            self.model = model.copy()
        else:
            self.model = model

        print("\nDone.\n")

    @property
    @ensure_fit
    def params(self):
        """Return the best values and errors from the fit result."""
        out = []
        for val in self._fit:
            if isinstance(self.model, Model):
                out.append(val.optParams)
            else:
                out.append(self._extract_lmfit_params(val))

        return out

    @ensure_fit
    def fit_best(self, **kwargs):
        """Return the fitted model.

        Parameters
        ----------
        kwargs : dict
            Additional keyword arguments to pass to
            `ModelResult.eval`.

        """
        kws = self._fit[0].userkws
        kws.update(**kwargs)

        out = []
        for fit in self._fit:
            if isinstance(self.model, Model):
                kws["params"] = fit.optParams
            else:
                kws["params"] = fit.params

            out.append(self.model.eval(**kws))

        return np.array(out)

    @ensure_fit
    def fit_components(self, **kwargs):
        """Return the fitted components.

        Parameters
        ----------
        kwargs : dict
            Additional keyword arguments to pass to
            `ModelResult.eval_components`.

        """
        kws = self._fit[0].userkws
        kws.update(**kwargs)

        comps = {}
        for fit in self._fit:
            if isinstance(self.model, Model):
                kws["params"] = fit.optParams
            else:
                kws["params"] = fit.params

            for key, val in self.model.eval_components(**kws).items():
                if key not in comps.keys():
                    comps[key] = []
                comps[key].append(val)

        for key, val in comps.items():
            comps[key] = np.array(val)

        return comps

    @property
    @ensure_fit
    def model_best(self):
        """Return the model with the fitted parameters."""
        return self._fit

    @property
    @ensure_fit
    def fit_result(self):
        """Return the full result of the fit, if available."""
        res = [fit.fitResult for fit in self._fit]
        return res

    def _cleanData(self, data, errors, x, processType="replace"):
        """Remove inf and null values from the input arrays.

        Parameters
        ----------
        processType : {'omit', 'replace'}
            Type of processing to be performed.
                - 'omit': discard the bad entries from the input arrays.
                - 'replace': replace the bad entries by inf.

        """
        if processType == "omit":
            mask = ~(data <= 0.0) & ~(data == np.inf) & ~(errors == np.inf)
            for obs in mask:
                for q in obs:
                    mask[0, 0] = mask[0, 0] & q

            data = data[:, :, mask[0, 0]]
            errors = errors[:, :, mask[0, 0]]
            x = x[mask[0, 0]]

        if processType == "replace":
            np.place(errors, data <= 0.0, np.inf)
            np.place(errors, data == np.inf, np.inf)

        return data, errors, x

    def _extract_lmfit_params(self, modelRes):
        """Convert lmfit parameters into the format used in nPDyn."""
        out = Parameters()

        tmp = {}
        for key, val in modelRes.params.items():
            if re.search(r"_\d+$", key):
                key = key[: key.rfind("_")]
            if key not in tmp.keys():
                tmp[key] = {
                    "value": [],
                    "error": [],
                    "fixed": False,
                    "bounds": (-np.inf, np.inf),
                }
            tmp[key]["value"].append(val.value)
            tmp[key]["error"].append(
                val.stderr if val.stderr is not None else 0
            )
            tmp[key]["fixed"] = not val.vary
            tmp[key]["bounds"] = (val.min, val.max)

        out.update(**tmp)

        return out
