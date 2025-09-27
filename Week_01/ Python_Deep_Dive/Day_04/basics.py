class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Inside __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Inside __init__")
        self.value = value

obj = MyClass(10)



class User:
    def __init__(self, username):
        self.username = username

    @classmethod
    def from_dict(cls, d):
        return cls(d['username'])

    @staticmethod
    def is_valid_username(s):
        return isinstance(s, str) and 3 <= len(s) <= 30

# Usage
u = User.from_dict({'username': 'alice'})
User.is_valid_username('bob')


from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj) -> str:
        pass

class JsonSerializer(Serializer):
    def serialize(self, obj):
        import json
        return json.dumps(obj)
    
    
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

a = Singleton(10)
b = Singleton(20)
print(a.value, b.value)  # 20 20
print(a is b)  # True