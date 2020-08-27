import joblib


class Thing:
    def __init__(self, a, b):
        self.a = a
        self.b = b


joblib.dump(Thing(1, 2), 'data/t.pkl')
