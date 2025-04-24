import os
import requests
import numpy as np
from PyPDF2 import PdfReader

class SampleClass:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

class AnotherClass:
    def compute(self, data: list[int]) -> float:
        return np.mean(data)
