import pytest

import numpy as np

from nPDyn.models.builtins import modelPVoigt, modelD2OBackground
from nPDyn.models.presets import calibratedD2O


def test_fitRes_PVoigt(fullQENSDataset):
    qens, res, ec, bkgd = fullQENSDataset
    q = res.q[:, np.newaxis]
    res.fit(model=modelPVoigt(q))
    assert np.sum((res - res.fit_best()) ** 2) < 0.004


def test_fitD2O_Builtin(fullQENSDataset):
    qens, res, ec, bkgd = fullQENSDataset
    q = bkgd.q[:, np.newaxis]
    bkgd.fit(modelD2OBackground(q))
    assert np.sum((bkgd - bkgd.fit_best()) ** 2) < 0.005
