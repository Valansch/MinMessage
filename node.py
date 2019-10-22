class Node:


    def advertise(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def has_neighbor(self, node):
        return node in self.neighbors

    def __str__(self):
        return str(self.id)

    def print(self):
        print(f'Node{self.id}: ', end='')
        for node in self.neighbors:
            print(f'{str(node)}, ', end='')
        print()

    def __init__(self, id):
        self.neighbors = []
        self.id = id
        
        