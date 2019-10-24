class Path(list):
    def __init__(self):
        super()
    
    def __repr__(self):
        result = "["
        length = len(self)
        for index, entry in enumerate(self, start=0):
            result += f"{str(entry)}, " if (index != length - 1) else str(entry)
        return f"{result}]"
        
