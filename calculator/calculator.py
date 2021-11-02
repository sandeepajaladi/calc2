""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
    @staticmethod
    def get_last_calculation_result():
        return Calculator.history[-1].getResult()
    @staticmethod
    def get_last_calculation_object():
        return Calculator.history[-1]
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return Calculator.count_history()
    @staticmethod
    def count_history():
        return len(Calculator.history)
    @staticmethod
    def add_number(value_a, value_b):
        """ Instantiating Addition object and passing value a and b to the constructor """
        # This is using a factory create method to return an instance of the class
        Calculator.add_calculation_to_history(Addition.create(value_a,value_b))
        #the -1 gets the last item added to the history
        return Calculator.get_last_calculation_result()
    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        Calculator.add_calculation_to_history(Subtraction.create(value_a,value_b))
        return Calculator.get_last_calculation_result()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_last_calculation_result()