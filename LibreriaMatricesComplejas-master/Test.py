import LibreriaMatricesComplejas as lib2

def test_sumaVector():
	
	A = [[(8, 3)], [(-1, -4)], [(0, -9)]]
	B = [[(8, -3)], [(2, 5)], [(3,0)]]
	C = [[(16, 0)], [(1, 1)], [(3, -9)]]

	assert lib2.sumaMatriz(A,B) == C, 'Debe ser [[(16, 0)], [(1, 1)], [(3, -9)]]'

def test_inversoAditivoVector():

	A = [[(-5, 2)], [(3, 0)], [(0, -1)]]
	B = [[(5, -2)], [(-3, 0)], [(0, 1)]]

	assert lib2.inversoAditivoMatriz(A) == B, 'Debe ser [[(5, -2)], [(-3, 0)], [(0, 1)]]'

def test_escalarVector():
	
	A = [[(-2, 5)], [(-1, -1)], [(2, -9)]]
	B = [[(-3, -7)], [(2, 0)], [(7, 11)]]
	k = (-1,1)

	assert lib2.escalarMatriz(A,k) == B, 'Debe ser [[(-3, -7)], [(2, 0)], [(7, 11)]]'

def test_sumaMatriz():
	A = [[(-8, -3), (-6, -4), (0, -4)], [(-1, 8), (6, -10), (8, -5)], [(4, 0), (8, 5), (-7, -9)]]
	B = [[(-7, -2), (-4, -2), (7, 7)], [(5, 9), (0, 3), (6, -5)], [(1, 5), (-6, -6), (5, 8)]]
	C = [[(-15, -5), (-10, -6), (7, 3)], [(4, 17), (6, -7), (14, -10)], [(5, 5), (2, -1), (-2, -1)]]

	assert lib2.sumaMatriz(A,B) == C, 'Debe ser [[(-15, -5), (-10, -6), (7, 3)], [(4, 17), (6, -7), (14, -10)], [(5, 5), (2, -1), (-2, -1)]]'

def test_inversoAditivoMatriz():

	A = [[(7, 3), (-1, 7)], [(-9, -4), (-7, -9)]]
	B = [[(-7, -3), (1, -7)], [(9, 4), (7, 9)]]

	assert lib2.inversoAditivoMatriz(A) == B, 'Debe ser [[(-7, -3), (1, -7)], [(9, 4), (7, 9)]]'

def test_escalarMatriz():
	
	A = [[(3, -2), (8, -4)], [(4, -10), (-2, -8)]]
	B = [[(0, 13), (-4, 32)], [(22, 32), (28, 10)]]
	k = (-2,3)

	assert lib2.escalarMatriz(A,k) == B, 'Debe ser [[(0, 13), (-4, 32)], [(22, 32), (28, 10)]]'

def test_transpuestaMatriz():
	
	A = [[(5, 9), (-7, -5), (-1, -4)], [(8, 2), (-3, -7), (7, -8)]]
	B = [[(5, 9), (8, 2)], [(-7, -5), (-3, -7)], [(-1, -4), (7, -8)]]

	assert lib2.transpuestaMatriz(A) == B, 'Debe ser [[(5, 9), (8, 2)], [(-7, -5), (-3, -7)], [(-1, -4), (7, -8)]]'

def test_conjugadaMatriz():

	A = [[(-6, 1), (3, 8)], [(2, -6), (3, 0)]]
	B = [[(-6, -1), (3, -8)], [(2, 6), (3, 0)]]
	
	assert lib2.conjugadaMatriz(A) == B, 'Debe ser [[(-6, -1), (3, -8)], [(2, 6), (3, 0)]]'

def test_dagaMatriz():

	A = [[(7, 7), (3, 8), (8, 4)], [(5, 0), (8, -6), (-10, -1)]]
	B = [[(7, -7), (5, 0)], [(3, -8), (8, 6)], [(8, -4), (-10, 1)]]

	assert lib2.dagaMatriz(A) == B, 'Debe ser [[(7, -7), (5, 0)], [(3, -8), (8, 6)], [(8, -4), (-10, 1)]]'

def test_productoMatriz():

	A = [[(2, 1), (3, 0), (1, -1)], [(0, 0), (0, -2), (7, -3)], [(3, 0), (0, 0), (1, -2)]]
	B = [[(0, -1), (1, 0)], [(0, 0), (0, 1)]]

	assert lib2.productoMatriz(A,B) == 'Dimensiones incorrectas', 'Debe ser Dimensiones incorrectas'

	C = [[(-6, 2), (0, 6), (7, 2)], [(6, 9), (7, 7), (-6, -6)], [(5, 8), (-6, 8), (6, 9)]]
	D = [[(9, -6), (-3, -4), (5, -2)], [(3, 6), (-1, -5), (0, -5)], [(9, 9), (8, -4), (-8, -4)]]
	E = [[(-33, 153), (120, 0), (-44, -22)], [(87, 0), (-26, -117), (107, 70)], [(0, 165), (147, 26), (69, -36)]]

	assert lib2.productoMatriz(C,D) == E, 'Debe ser [[(-33, 153), (120, 0), (-44, -22)], [(87, 0), (-26, -117), (107, 70)], [(0, 165), (147, 26), (69, -36)]]'

	F = [[(-1, 5), (1, -7), (-6, 3)], [(-3, -9), (2, -5), (1, -10)], [(-6, 5), (6, -5), (3, -2)]]
	G = [[(1, -3)], [(4, 3)], [(-3, 1)]]
	H = [[(54, -32)], [(0, 17)], [(41, 30)]]

	assert lib2.productoMatriz(F,G) == H, 'Debe ser [[(54, -32)], [(0, 17)], [(41, 30)]]'

def test_productoInternoVectores():

	A = [[(2, -1)], [(-8, -5)], [(-2, -6)]]
	B = [[(6, -3)], [(5, -1)], [(-6, -2)]]

	assert lib2.productoInternoVectores(A,B) == (4, 1), 'Debe ser (4, 1)'

def test_normaVector():

	A = [[(4, 5)], [(3, 1)], [(0, -7)]]


	assert lib2.normaVector(A) == 10.0, 'Debe ser 10.0'

def test_distanciaVectores():

	A = [[(2, 7)], [(4, -1)], [(2, -4)]]
	B = [[(7, 8)], [(2, -8)], [(1, 4)]]

	assert lib2.distanciaVectores(A,B) == 12.0, 'Debe ser 12.0'

	C = [[(9, -7)], [(-1, -6)]]
	D = [[(7, -8)], [(5, -9)]]

	assert round(lib2.distanciaVectores(C,D),2) == round(7.0710678118654755,2), 'Debe ser 7.07'

def test_esMatrizUnitaria():
	
	A = [[(1/(2**0.5), 0), (0,1/(2**0.5))], [(0, 1/(2**0.5)), (1/(2**0.5),0)]]

	assert lib2.esMatrizUnitaria(A) == True, 'Debe ser True'

	B = [[(0, 1), (1, 0), (0, 0)], [(0, 0), (0, 1), (1, 0)], [(1, 0), (0, 0), (0, 1)]]

	assert lib2.esMatrizUnitaria(B) == False, 'Debe ser False'

def test_esMatrizHermitiana():
	
	A = [[(3, 0), (2, -1), (0, -3)], [(2, 1), (0, 0), (1, -1)], [(0, 3), (1, 1), (0, 0)]]

	assert lib2.esMatrizHermitiana(A) == True, 'Debe ser True'

	B = [[(1, 0), (3, -1)], [(3, 1), (0, 1)]]

	assert lib2.esMatrizHermitiana(B) == False, 'Debe ser False'

def test_productoTensorial():
	
	A = [[(1, 1), (0, 0)], [(1, 0), (0, 1)]]
	B = [[(-1, 2), (-2, -2), (0, 2)], [(2, 3), (3, 1), (2, 2)], [(-2, 1), (1, -1), (2, 1)]]
	C = [[(-3, 1), (0, -4), (-2, 2), (0, 0), (0, 0), (0, 0)], [(-1, 5), (2, 4), (0, 4), (0, 0), (0, 0), (0, 0)], [(-3, -1), (2, 0), (1, 3), (0, 0), (0, 0), (0, 0)], [(-1, 2), (-2, -2), (0, 2), (-2, -1), (2, -2), (-2, 0)], [(2, 3), (3, 1), (2, 2), (-3, 2), (-1, 3), (-2, 2)], [(-2, 1), (1, -1), (2, 1), (-1, -2), (1, 1), (-1, 2)]]

	assert lib2.productoTensorial(A,B) == C, 'Debe ser [[(-3, 1), (0, -4), (-2, 2), (0, 0), (0, 0), (0, 0)], [(-1, 5), (2, 4), (0, 4), (0, 0), (0, 0), (0, 0)], [(-3, -1), (2, 0), (1, 3), (0, 0), (0, 0), (0, 0)], [(-1, 2), (-2, -2), (0, 2), (-2, -1), (2, -2), (-2, 0)], [(2, 3), (3, 1), (2, 2), (-3, 2), (-1, 3), (-2, 2)], [(-2, 1), (1, -1), (2, 1), (-1, -2), (1, 1), (-1, 2)]]'

if __name__=='__main__':

	test_sumaVector()
	test_inversoAditivoVector()
	test_escalarVector()
	test_sumaMatriz()
	test_inversoAditivoMatriz()
	test_escalarMatriz()
	test_transpuestaMatriz()
	test_conjugadaMatriz()
	test_dagaMatriz()
	test_productoMatriz()
	test_productoInternoVectores()
	test_normaVector()
	test_distanciaVectores()
	test_esMatrizUnitaria()
	test_esMatrizHermitiana()
	test_productoTensorial()
	print('Prueba exitosa')