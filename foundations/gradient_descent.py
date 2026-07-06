class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x_updated = init if init > 0 else init * -1
        l = []
        for i in range(1, iterations+1):
            x = x_updated - learning_rate * 2 * x_updated
            x_updated = x
            l.append(x)
        if iterations == 0:
            l.append(init)
        minimum = round(min(l), 5) * -1 if init <0 else round(min(l), 5)
        return minimum
