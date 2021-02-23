class PollutionMagnitudeDto():
    def __init__(self, id, name, formula, measurement_unit, measurements_count):
        self.id = id
        self.name = name
        self.formula = formula
        self.measurement_unit = measurement_unit
        self.measurements_count = measurements_count
