class Item:

    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value

    def __str__(self):
        return f'Key = {self.key}, value = {self.value}'
