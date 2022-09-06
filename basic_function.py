import cv2

img = cv2.imread("Assets/image.jpg")


def color_conversion():
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # COLOR_BGR2GRAY is an opencv color space >>
    # to convert an image from blue-green-red to grayscale.
    cv2.imshow("Gray Image", img_gray)
    cv2.waitKey(0)


def blur():
    img_blur = cv2.GaussianBlur(img, (11, 11), 0)   # Used to reduce noise from image
    # Has 4 parameter (image, K-size( X, Y), sigma-X, sigma-Y)
    # K-size must be an odd integer
    # Sigma X and Y - standard deviation in X,Y direction respectively.
    # Sigma-Y is taken Sigma-X value as default value
    cv2.imshow("Blur Image", img_blur)
    cv2.waitKey(0)


def main():
    color_conversion()
    blur()


if __name__ == '__main__':
    main()
