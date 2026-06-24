class Value:
    def __init__(self, data, children=()):
        self.data = data
        self.grad = 0.0
        self._prev = set(children)
        
    def __add__(self, other):
        out = Value(
            self.data + other.data,
            (self, other)
        )
        return out
    
    def __mul__(self, other):
        out = Value(
            self.data * other.data,
            (self, other)
        )
        return out
    
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
