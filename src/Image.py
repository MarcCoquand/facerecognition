import Utils
# The images are quite grainy so filter away values that
# will only make the result ambiguous
FILTER_VAL = float(3)/float(32)


class Image:
    """ Image is a utility class that takes care of necessary
        interactions with images """

    def __init__(self, img):
        self.img = self._preprocess_img(img)
        self.id = None
        self.ans = None

    def _preprocess_img(self, img):
        i1 = Utils.flatten(img)
        i1.append(1)
        return map(self._filter_noise, i1)

    def _filter_noise(self, pix):
        return pix if pix > FILTER_VAL else float(0)

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
