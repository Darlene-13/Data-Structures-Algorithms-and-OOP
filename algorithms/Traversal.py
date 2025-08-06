"""
TRAVERSAL ALGORITHMS
This module contains implementations of various traversal algorithms
for different data structures.
"""
# 1. Array/List Traversal.
class ArrayTraversal:
    def __init__(self, arr):
        self.arr = arr
    
    def traverse(self):
        for num in self.arr:
            print(num, end="")
        print()    

ArrayTraversal([4, 2, 7, 1, 9]).traverse()


class SumTraversal:
    def __init__(self, arr):
        self.arr = arr

    def sum(self):
        total = 0
        for num in self.arr:
            total +=  num
        return total
    
print(SumTraversal([4, 2, 7, 1, 9]).sum())  # Output: 23




class CountGreaterThan:
    def __init__(self, arr):
        self.arr = arr

    def count(self, target):
        count = 0
        for num in self.arr:
            if num > target:
                count +=1
        return count
Target = 4
print(CountGreaterThan([4, 2, 7, 1, 9]).count(Target))  # Output: 2


class FilterGreaterThan:
    def __init__(self, arr):
        self.arr = arr

    def filter(self, target):
        result = []
        for num in self.arr:
            if num > target:
                result.append(num)
        print(*result)  # Print all numbers greater than target
Target = 4
FilterGreaterThan([4, 2, 7, 1, 9]).filter(Target)  # Output: 7 9



class CharPrinter:
    def __init__(self, string):
        self.string = string

    def print_chars(self):
        for letter in self.string:
            print(letter)

CharPrinter("Hello, World!").print_chars()  # Output: H e l l o ,   W o r l d !


class VowelCounter:
    def __init__(self, string):
        self.string = string

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for letter in self.string:
            if letter in vowels:
                count += 1
        return count
print(VowelCounter("Hello, World!").count_vowels())  # Output: 3 (e, o, o)


class MatrixPrinter:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        for row in self.matrix:
            for num in row:
                print(num, end=" ")
            print()

MatrixPrinter([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).print_matrix()