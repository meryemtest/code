import unittest
def add(a, b):
    return a + b
class Testaddfunction(unittest.TestCase):
   def test_add_positive(self):
        result=add(3,4)
        self.assertEqual(result,7)
   def test_add_negative(self):
        result=add(-3,-4)
        self.assertEqual(result,-7)
if __name__ == '__main__':
    unittest.main()

def divide(a, b):
    return a / b
class Testdividefunction(unittest.TestCase):
    def test_divide(self):
        result=divide(10,3)
        self.assertAlmostEqual(result,3.333333,places=5)  #pour vérifier si la valeur result est approximativement égale à 3.333333 jusqu'à n=5 décimales près. 
if __name__ == '__main__':
    unittest.main()    

#une fct qui prend deux listes et retourne une liste contenant les éléments uniques des deux listes combinées    
def elements(liste1,liste2):
    combined = liste1+liste2
    return list(set(combined))
class Testelementsfunction(unittest.TestCase):
    def test_elements(self):
        result=elements([1, 2, 3], [2, 3, 4])
        self.assertCountEqual(result, [1,2,3,4])
if __name__ == '__main__':
     unittest.main() 

# une fct qui fusionne deux dictionnaires en un seul
def fusion(dict1,dict2):
    dictt= dict1.copy()
    dictt.update(dict2)
    return dictt
#print(fusion({'a':1,'b':2,'c':3},{'d':6,'e':8}))
class Testfusionfunction(unittest.TestCase):
    def test_fusion(self):
        result=fusion({'a':1,'b':2,'c':3},{'d':6,'e':8})
        self.assertDictEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 6, 'e': 8})
if __name__ == '__main__':
     unittest.main() 

#une fct qui vérifie si un nombre est pair
def pair(number):
     if number % 2 == 0:
         return True
     else: 
        return False
print(pair(4))
class Testpairfunction(unittest.TestCase):
   def test_pair1(self):
       result=pair(4)
       self.assertFalse(result)        #pour vérifier si le résultat obtenu est évalué comme False
   def test_pair2(self):
      result=pair(7)
      self.assertFalse(result)
if __name__ == '__main__':
     unittest.main()

# fct qui vérifie si un nombre est positif
def positive(number):
    return number > 0
class Testpositivefunction(unittest.TestCase):

    def test_positive(self):
        result = positive(5)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

def calcul(montant):
    if montant > 100:
        return 0.1 * montant
    else:
        return 0
class Testcalculfunction(unittest.TestCase):

    def test_calcul(self):
        result = calcul(150)
        self.assertGreater(result, 0)

    def test_calcul(self):
        result = calcul(75)
        self.assertGreater(result, 0)
if __name__ == '__main__':
    unittest.main()

def find(word, list):
    if word in list:
        return True
    else:
        return False
class Testfindfunction(unittest.TestCase):

    def test_find(self):
        result = find('apple', ['apple', 'banana', 'orange'])
        self.assertIn(result, [True])

if __name__ == '__main__':
    unittest.main()

#fct qui calcule le coût en fonction du poids 
def calculate(weight):
    rate_kg = 2.5
    return weight * rate_kg
class Testcalculatefunction(unittest.TestCase):

    def test_calculate(self):
        result = calculate(5)
        self.assertLess(result, 20)   #vérifier si le coût calculé est strictement inférieur à 20

if __name__ == '__main__':
    unittest.main()

#fct qui filtre les nombres positifs d'une liste de nombres :
def positive_numbers(numbers):
       nums=[]
       for num in numbers:
          if num > 0:
              nums.append(num)
       return nums 
print(positive_numbers([1, -2, 3, -4, 5]))
class TestpositiveFunction(unittest.TestCase):

    def test_positive(self):
        result = positive_numbers([1, -2, 3, -4, 5])
        self.assertListEqual(result, [1,3,5])
if __name__ == '__main__':
    unittest.main()

def characters(text):
    return set(text)
class Testcharactersfunction(unittest.TestCase):

    def test_characters(self):
        result = characters("hello")
        self.assertSetEqual(result, {'h', 'l', 'e', 'o'})  
if __name__ == '__main__':
    unittest.main()        