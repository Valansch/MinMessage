from path import Path

class TraversablePath(Path):
    
    def __init__(self, path):
        super()
        for entry in reversed(path):
            if isinstance(entry, list):
                self.append(
                    [TraversablePath(subpath) for subpath in entry]
                )
            else:
                self.append(entry)

    