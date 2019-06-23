import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):

    def test_scaler_multiplication(self):
        matrix1 = Matrix([[1,5],[2,3],[5,5]])
        scaler_multiplication=(matrix1.scaler_multiplication(3))
        self.assertEqual(scaler_multiplication.matrix,[[3, 15], [6, 9], [15, 15]])

    #trace is determined in NxN matrix correctly.
    #if matrix NxM than it raises error.
    def test_trace(self):
        matrix1 = Matrix([[9,8],[4,5]])
        trace=matrix1.trace()
        matrix3 = Matrix([[2,3,5],[4,5,6]])
        self.assertEqual(trace,14)
        self.assertRaises(Exception,matrix3.trace())

    def test_transpose(self):
        matrix2 = Matrix([[36, 32], [16, 20]])
        transpose=matrix2.transpose()
        self.assertEqual(transpose.matrix, [[36, 16], [32, 20]])

    # multiplication  is determined correctly, if first matrix column number equals to second matrix row number.
    # if matrix NxM than it raises error.
    def test_multiplication(self):
        matrix1 = Matrix([[9,8],[4,5]])
        matrix2 = Matrix([[2, 3], [1, 7], [3, 4]])
        matrix3 = Matrix([[1, 4, 4], [2, 3, 5], [4, 5, 6]])
        multiplication1=matrix2.multiplication(matrix1)
        multiplication2 = matrix3.multiplication(matrix1)
        self.assertEqual(multiplication1.matrix,[[30, 31], [37, 43], [43, 44]])
        self.assertRaises(Exception,multiplication2)

    # determinant is calculated in NxN matrix correctly, .
    # if matrix NxM than it raises error.
    def test_determinanat(self):
        matrix1 = Matrix([[9,8],[4,5]])
        matrix2 = Matrix([[2,3,5],[4,5,6]])
        self.assertEqual(matrix1.determinant(),13)
        self.assertRaises(Exception,matrix2.determinant())

    # matrix inverse is calculated in NxN matrix correctly, .
    # if matrix NxM than it raises error.
    def test_inverse(self):
        matrix1 = Matrix([[1,4,4],[2,3,5],[4,5,6]])
        inverse=matrix1.inverse()
        matrix2 = Matrix([[2,3,5],[4,5,6]])
        inverse2 = matrix2.inverse()
        self.assertEqual(inverse.matrix,[[-0.41176470588235287, -0.23529411764705888, 0.4705882352941176], [0.47058823529411775, -0.5882352941176471, 0.17647058823529407], [-0.11764705882352951, 0.6470588235294118, -0.2941176470588235]])
        self.assertRaises(Exception, inverse2.matrix)

if __name__ == '__main__':
    unittest.main()
