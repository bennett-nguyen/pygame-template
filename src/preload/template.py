class Scene:
    def __init__(self):
        self.id = 0xAA0000

    def input(self):
        """
        Take inputs from the player
        """
        pass

    def redraw(self):
        """
        Redraw screen
        """
        pass

    def update(self):
        """
        Update object's and game's state (moving, transitioning, etc.)
        """
        pass

    def reset(self):
        """
        Reset the entire scene
        """
        pass