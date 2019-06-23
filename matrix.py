from copy import deepcopy
import math
from typing import List


class Matrix(object):

    def __init__(self, liste):
        self.set_matrix(liste)

    def get_matrix(self):
        return self.matrix

    def set_matrix(self, liste):  # input list controls to fit matrix requirements
        if type(liste) == list:
            if len(liste) != 0:
                for row in liste:
                    if len(liste[0]) == len(row):
                        for column in row:
                            if type(column) == int or type(column) == float:
                                continue
                            else:
                                raise TypeError('Matrix must be a list of digit lists.')
                    else:
                        raise ValueError('Number of columns must be equal for each row')
                self.matrix = liste
                self.row = len(liste)
                self.col = len(liste[0])
            else:
                raise ValueError('Matrix must refer to a list of lists.')
        else:
            raise TypeError('Matrix must be list type.')

    def index(self,i,j):
        if i== ":":
            return self.matrix[:][j]
        elif j==':':
            return self.matrix[i][:]
        return self.matrix[i][j]

    def scaler_multiplication(self, value):
        matrix = Matrix([[0] * self.col for _ in range(self.row)])
        for i in range(self.row):
            for j in range(self.col):
                matrix.matrix[i][j] = (self.index(i,j) * value)
        return matrix

    def trace(self):
        try:
            if self.row!=self.col:
                raise Exception("Dimensions must be NxN to find trace of matrix")
            sum = 0
            for i in range(self.row):
                sum = sum + (self.index(i,i))
            return sum
        except:
            raise Exception("Dimensions must be NxN to find trace of matrix!")

    def transpose(self):
        transposed_matrix = Matrix([[self.index(j,i) for j in range(self.row)] for i in range(self.col)])
        return transposed_matrix

    def multiplication(self, matrix2):
        try:
            if len(self.matrix[0])!=len(matrix2.matrix):
                raise Exception("Column number of First Matrix must be equal to row number of Second Matrix")
            rows, columns = len(self.matrix), len(matrix2.matrix[0])
            matrix=[[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    matrix[i][j] = sum(self.index(i,k) * matrix2.matrix[k][j] for k in range(len(matrix2.matrix)))
            return Matrix(matrix)
        except:
            raise Exception ("Column number of First Matrix must be equal to row number of Second Matrix")

    def minor(self, column):
        """Returns the Minor M_0i of matrix"""
        minor = deepcopy(self.matrix)
        minor= minor[1:]
        for i in range(len(minor)):
            minor[i] = minor[i][0:column] + minor[i][column + 1:]
        return minor

    def determinant(self):
        try:
            if self.row!=self.col:
                raise Exception("Dimensions must be NxN to determinant of matrix!")
            if self.row == 2:
                value = self.index(0,0) * self.index(1,1) - self.index(1,0) * self.index(0,1)
                return value
            total = 0
            for column in (range(self.row)):
                minor=Matrix(self.minor(column))
                sign = math.pow(-1, (1 + column + 1))
                det_A1j = minor.determinant()
                total += sign * self.index(0,column) * det_A1j
            return total
        except:
            raise Exception("Dimensions must be NxN to find determinant of matrix!")

    def inverse(self):
        try:
            X = deepcopy(self)
            if X.row!=X.col:
                raise ValueError("Dimensions must be NxN for inversions")
            identity = X.make_identity(X.row, X.col)
            for i in range(0, X.row):
                X.matrix[i] += identity[i]
            i = 0
            for j in range(0, X.col):
                sum_nz, first_nz = X.check_zeros(X.matrix,i, j)
                if first_nz != i:
                    X.matrix = X.swap_row(X.matrix,i, first_nz)
                X.matrix[i] = [m / X.index(i,j) for m in X.matrix[i]]
                for q in range(0, X.row):
                    if q != i:
                        scaled_row = [X.index(q,j) * m for m in X.matrix[i]]
                        X.matrix[q] = [X.index(q,m) - scaled_row[m] for m in range(0, len(scaled_row))]
                if i == X.row or j == X.col:
                    break
                i += 1
            # Get just the right hand matrix
            for i in range(0, X.row):
                X.matrix[i] = X.matrix[i][X.col:len(X.matrix[i])]
            return X
        except :
            raise Exception("Dimensions must be NxN for inversions")

    @staticmethod
    def check_zeros(matrix, i, j):
        # sum_nz - the count of non zero entries
        # first_nz - index of the first non zero
        non_zeros = []
        first_nz = -1
        for m in range(i, len(matrix)):
            non_zero = matrix[m][j] != 0
            non_zeros.append(non_zero)
            if first_nz == -1 and non_zero:
                first_nz = m
        sum_nz = sum(non_zeros)
        return sum_nz, first_nz

    @staticmethod
    def swap_row(matrix, i, p):
        matrix[p], matrix[i] = matrix[i], matrix[p]
        return matrix

    @staticmethod
    def make_identity(r, c):
        identity = []
        for i in range(0, r):
            row = []
            for j in range(0, c):
                element = 0
                if i == j:
                    element = 1
                row.append(element)
            identity.append(row)
        return identity



