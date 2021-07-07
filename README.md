# CMA-ES-z-regu-definiowania-macierzy-kowariancji-poprzez-redni-arytmetyczn-na-horyzoncie
Implementacja CMA-ES z regułą definiowania macierzy kowariancji poprzez średnią arytmetyczną na horyzoncie, porównanie z oryginalnym CMA-ES, strojenie

# Korzystanie z programu

	Najpierw w głównym folderze:
	$ gcc -fPIC -shared -lm -o cec17_test_func.so cec17_test_func.c

	aby uruchomić testy CMAES (dla oryginalnego <długość bufora>=-1):
	$ python3 test.py <liczba wymiarów> <numer funkcji> <długość bufora>

Oryginalny CMA-ES(purecma.py):
https://github.com/CMA-ES/pycma

Testy:
https://github.com/P-N-Suganthan/CEC2017-BoundContrained/blob/master/codes.rar

python wrapper(cec17_functions.py):
https://github.com/lacerdamarcelo/cec17_python
