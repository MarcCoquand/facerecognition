import Utils
FILTER_VAL = float(3)/float(32)  # Derived from experiments


class Image:
    """
    Image represents an image that holds a list of pixels, id, and what
    facial expression the image represents.
    Attributes:
        img: list of pixel values
        id: the id of the image on format ImageXX
        ans: integer 1-4 representing what facial expression the img represents
    """
    def __init__(self, img):
        self.img = self._preprocess_img(img)
        self.id = None
        self.ans = None

    def _preprocess_img(self, img):
        """
        Performs preprocessing operations in order to sanitize
        the input data so that it contains what we expects.
        """
        i1 = Utils.flatten(img)
        i1.append(1)
        return map(self._filter_noise, i1)

    def _filter_noise(self, pix):
        """
        Since the images contains a lot of noise, we're filtering
        away those pixels that wont't impact the result other than
        to make it unambiguous.
        """
        return pix if pix > FILTER_VAL else float(0)

    def get_img(self):
        """
        Returns the pixel data for the image as a list of integers
        """
        return self.img

    def set_ans(self, ans):
        """
        Updates the answer for the image. Should be a single integer
        between 1-4
        """
        self.ans = ans
        return self

    def get_ans(self):
        """
        Returns the answer as an integer between 1-4
        """
        return self.ans

    def set_id(self, id):
        """
        Updates the id of the image
        """
        self.id = str(id).rstrip()
        return self

    def get_id(self):
        """
        Returns the id of the image
        """
        return self.id
