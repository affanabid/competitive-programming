class Solution:
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            curr_image = image[i][::-1]
            for j in range(len(curr_image)):
                curr_bit = curr_image[j]
                new_bit = curr_bit ^ 1
                image[i][j] = new_bit

        return image