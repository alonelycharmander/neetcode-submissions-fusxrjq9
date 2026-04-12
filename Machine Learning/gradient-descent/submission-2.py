class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        minimizer = init 

        for i in range(iterations):
            der = 2 * minimizer 
            minimizer = minimizer - (learning_rate * der)

        return round(minimizer, 5)