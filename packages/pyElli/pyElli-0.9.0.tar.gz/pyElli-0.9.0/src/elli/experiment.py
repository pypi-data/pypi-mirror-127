# Encoding: utf-8
import numpy as np
import numpy.typing as npt

from .solver4x4 import Solver4x4
from .solver import Solver
from .result import Result


class Experiment:
    """Description of an experiment."""

    structure = None
    jonesVector = None
    stokesVector = None
    theta_i = None
    lbda = None

    def __init__(self, structure: "Structure", lbda: npt.ArrayLike, theta_i: float, vector: npt.ArrayLike = [1, 0, 1, 0]) -> None:
        """Creates an empty structure.

        'structure' : Structure object
        'lbda' : single or list of wavelengths in nm or tuple (wavelength, unit)
        'theta_i' : incident angle in degrees
        'vector' : Jones or Stokes vector of incident light
        """
        self.setStructure(structure)
        self.setTheta(theta_i)
        self.setLbda(lbda)
        self.setVector(vector)

    def setStructure(self, structure: "Structure") -> None:
        """Defines the Structure.

        'structure' : Structure object
        """
        self.structure = structure

    def setVector(self, vector: npt.ArrayLike) -> None:
        """Defines the Jones or Stokes vector of the incident Light.

        Jones:
        [1, 0]: horizontal polarized
        [0, 1]: vertical polarized
        [1/sqrt(2), 1/sqrt(2)]: diagonal polarized
        [1/sqrt(2),-1/sqrt(2)]: anti-diagonal polarized

        Stokes:
        [1,0,0,0]: unpolarized light
        [1,1,0,0]: horizontal polarized
        [1,-1,0,0]: vertical polarized
        [1,0,1,0]: diagonal polarized
        [1,0,-1,0]: anti-diagonal polarized
        """
        vectorArray = np.asarray(vector)

        if vectorArray.shape == (2,):
            self.jonesVector = vectorArray

            self.stokesVector = np.array([
                np.abs(self.jonesVector[0])**2 + np.abs(self.jonesVector[1])**2,
                np.abs(self.jonesVector[0])**2 - np.abs(self.jonesVector[1])**2,
                2 * np.real(self.jonesVector[0] * np.conjugate(self.jonesVector[1])),
                -2 * np.imag(self.jonesVector[0] * np.conjugate(self.jonesVector[1]))])

        elif vectorArray.shape == (4,):
            self.stokesVector = vectorArray

            p = np.sqrt(self.stokesVector[1]**2 +
                        self.stokesVector[2]**2 +
                        self.stokesVector[3]**2) / self.stokesVector[0]
            Q = self.stokesVector[1] / (self.stokesVector[0] * p)
            U = self.stokesVector[2] / (self.stokesVector[0] * p)
            V = self.stokesVector[3] / (self.stokesVector[0] * p)

            if Q == -1:
                a = 0
                b = 1
            else:
                a = np.sqrt((1 + Q) / 2)
                b = U / (2 * a) - 1j * V / (2 * a)

            self.jonesVector = np.array([a, b])

    def setTheta(self, theta_i: float) -> None:
        """Set incident angle, or list of angles to evaluate.

        'theta_i' : incident angle in degrees
        """
        self.theta_i = theta_i

    def setLbda(self, lbda: npt.ArrayLike) -> None:
        """Set experiment wavelengths.

        'lbda' : single or list of wavelengths in nm
        """
        lbda_array = np.asarray(lbda)
        if np.shape(lbda_array) == ():
            lbda_array = np.asarray([lbda])
        self.lbda = lbda_array

    def evaluate(self, solver: Solver = Solver4x4, **solver_kwargs) -> Result:
        """Return the Evaluation of the structure for the given parameters"""
        if solver_kwargs == {}:
            solv = solver(self)
        else:
            solv = solver(self, **solver_kwargs)
        return solv.calculate()
