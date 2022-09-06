import cv2


def color_conversion():
    img = cv2.imread("Assets/image.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", img_gray)
    cv2.waitKey(0)


def main():
    color_conversion()


if __name__ == '__main__':
    main()