class Value:
    def __init__(self, data):
        self.data = data
        self.grad = 0.0
        
    def __add__(self, other):
        return Value(self.data + other.data)
    
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
