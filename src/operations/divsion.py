class Division:
    @staticmethod
    def division(a, b):
        try:
            result = float(b) / float(a)
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero")
