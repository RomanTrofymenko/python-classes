altitudeParams = [
    # alt   g       press   density
    [0000,	9.807,	10.13,	1.225],
    [1000,	9.804,	8.988,	1.112],
    [2000,	9.801,	7.950,	1.007],
    [3000,	9.797,	7.012,	0.909],
    [4000,	9.794,	6.166,	0.819],
    [5000,	9.791,	5.405,	0.736],
    [6000,	9.788,	4.722,	0.660],
    [7000,	9.785,	4.111,	0.590],
    [8000,	9.782,	3.565,	0.526],
    [9000,	9.779,	3.080,	0.467],
    [10000,	9.776,	2.650,	0.413],
    [15000,	9.761,	1.211,	0.194],
    [20000,	9.745,	0.553,	0.089],
    [25000,	9.730,	0.255,	0.040],
    [30000,	9.715,	0.120,	0.018],
    [40000,	9.684,	0.029,	0.004],
    [50000,	9.654,	0.008,	0.001],
    [60000,	9.624,	0.002,	0.000],
    [70000,	9.594,	0.000,	0.000],
    [80000,	9.564,	0.000,	0.000],
]

class AltParams:
    altitude = 0
    g = 9.8
    pressure = 10.13
    density = 1.225
    
    def __init__(self, a, g, p, d) -> None:
        self.altitude = a
        self.g = g
        self.pressure = p
        self.density = d
    
    def __str__(self):
        return f"Altitude: {self.altitude}, g: {self.g}, Pressure: {self.pressure}, Density: {self.density}"

def getParameters():
    result = []
    for par in altitudeParams:
        result.append(AltParams(par[0], par[1], par[2], par[3]))
    return result