class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return Complex(real_part, imaginary_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imaginary**2
            real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return Complex(real_part, imaginary_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
