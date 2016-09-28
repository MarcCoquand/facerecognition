
class Image:
    """ Image is a utility class that takes care of necessary
        interactions with images """

    def __init__(self, img):
        self.img = []
        for i in range(len(img)):
            img_arr = img[i].rstrip().split(' ')
            for j in range(len(img_arr)):
                img_arr[j] = int(img_arr[j])
            self.img.append(img_arr)
        return
    
    def get_img(self):
        """Get image as 2d array""" 
        return self.img

    def set_ans(self,ans):
        """Answer should be an enum."""
        self.ans = ans

    def get_ans(self):
        """Get answer as enum"""
        return self.ans

    def rotate(degrees):
        # TODO: IMPLEMENT
        # Rotation matrix is m = [cos(theta)-sin(theta); sin(theta) cos(theta)]
        return 
