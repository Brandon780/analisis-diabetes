
class BMICalculator:
    def __init__(self, data):
        self.data = data  # Almacenar los datos directamente

    def calculate_bmi(self):
        if self.data is None:
            raise ValueError("Data is missing. Pass the data to the constructor.")

        # Calcular altura en metros y peso en kilogramos
        self.data["height_si"] = self.data["height"] * 0.0254
        self.data["weight_si"] = self.data["weight"] * 0.453592

        # Calcular el índice de masa corporal (BMI)
        self.data["bmi"] = self.data["weight_si"] / self.data["height_si"] ** 2
        
        return self.data
    