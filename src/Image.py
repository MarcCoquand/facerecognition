import Utils

class Image:
    """ Image is a utility class that takes care of necessary
        interactions with images """

    def __init__(self, img):
        self.img = Utils.flatten(img)
        img.append(1)
        self.id = None
        self.ans = None

    def get_img(self):
        """Get image as 2d array""" 
        return self.img

    def set_ans(self, ans):
        """Answer should be an enum."""
        self.ans = ans
        return self

    def get_ans(self):
        """Get answer as enum"""
        return self.ans

    def set_id(self, id):
        self.id = str(id).rstrip()

    def get_id(self):
        return self.id

    def rotate(degrees):
        # TODO: IMPLEMENT
        # Rotation matrix is m = [cos(theta)-sin(theta); sin(theta) cos(theta)]
        return 
