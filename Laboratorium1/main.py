import math
import numpy as np
from numpy.linalg import inv, det

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if h <= 0 or r <= 0:
        return np.NaN #zwróć Nan w razie ujemnych argumentów
    else:
        return 2*math.pi*pow(r,2)+2*math.pi*r*h #zwróć pole walca
def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    fibsequence = np.array([1])#inicjalizacja wektora
    if isinstance(n, int):#sprawdź czy argument jest typu całkowitego
        if n <= 0:
            return None#zwróć None jeżeli argument mniejszy od zera
        elif n == 1:
            return fibsequence
        elif n == 2:
            fibsequence = [1,1]
        else:
            fibsequence = [1,1]
            while len(fibsequence) < n:#Wykonuj instrukcje do momentu kiedy długość wektora jest mniejsza od argumentu
                new_element = fibsequence[-1] + fibsequence[-2]
                fibsequence = np.append(fibsequence, new_element)
        return fibsequence.reshape(1, n)#zamień macierz na wektor i zwróć go gdy argument jest poprawny
    else:
        return None#zwróć None jeżeli argument nie jest typu całkowitego


def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    matrix = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    m_det = det(matrix)#wyznacz wyznacznik
    if m_det == 0:
        min_v = np.NaN#zwróć NaN jeżeli wyznacznik jest równy 0
    else:
        min_v = inv(matrix)#odwrócenie macierzy
    mt = np.transpose(matrix)#transpozycja macierzy
    return min_v, mt, m_det#zwróć krotkę macierzy odwrotnej, macierzy transponowanej i wyznacznika

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if isinstance(m, int):#sprawdź czy argument jest typu całkowitego
        if isinstance(n, int):#sprawdź czy argument jest typu całkowitego
            value = 0
            if m <= 0 or n <= 0:
                return None #zwróć None jeżeli argumenty mniejsze od zera
            matrix = np.zeros((m, n))#zainicjalizuj macierz zerową
            for i in range(0, m):
                for j in range(0, n):
                    if j >= i:
                        value = j
                    elif j < i:
                        value = i
                    matrix[i,j] = value

            return matrix#zwróć macierz jeżeli argumenty są poprawne
        else:
            return None#zwróć None jeżeli argumenty nie są typu całkowitego
    else:
        return None#zwróć None jeżeli argumenty nie są typu całkowitego