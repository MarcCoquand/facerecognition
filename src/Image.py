
class Image:
    """ Image is a utility class that takes care of necessary
        interactions with images """

    def __init__(self, img):
        for i in len(img):
            img_arr = img[i].split(' ')
        self.img.append(img_arr)
    
    def get_img(self):
        return self.img

    def set_ans(self,ans):
        self.ans = ans

    def get_ans(self):
        return self.ans

    def rotate(degrees):
        # TODO: IMPLEMENT
        # Rotation matrix is m = [cos(theta) -sin(theta); sin(theta) cos(theta)]
        return 
