import copy


class Message:
    """
        Abstraction for a message send through Network via a Node using a NetworkInterface
    """

    def __init__(self, path_tree, body):
        """
            Constructs the message

            Parameters
            ---------
                path_tree: HashTree
                    The tree containing all destinations of this message

                body: Any
                    The data to send

            Returns
            -------
                Message
        """
        self.header = dict()
        self.header["path_tree"] = path_tree
        self.body = body

    def clone(self):
        return Message(copy.copy(self.header), copy.copy(self.body))
