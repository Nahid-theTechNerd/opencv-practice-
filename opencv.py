import cv2


def photo_viewer():
    img = cv2.imread("Assets/image.jpg")   # To read an image and store it in a variable
    cv2.imshow("Output", img)   # To show image
    cv2.waitKey(0)  # WaitKey define how many times the output will being showing. Here waitKey 0 means infinite time.
    # If assertion error occurs then it means that image path is wrong


def video_viewer():
    capture = cv2.VideoCapture("Assets/video.mp4")
    while True:     # To show each frame as an image
        success, img = capture.read()
        cv2.imshow("Output", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to quit
            break


def webcam():
    capture = cv2.VideoCapture(0)   # parameter of VideoCapture function is the id of webcam

    capture.set(3, 640)     # ID 3 is to set frame width
    capture.set(4, 480)     # ID 4 is to set frame height
    capture.set(10, 100)    # ID 10 is to set brightness

    while True:  # To show each frame as an image
        success, img = capture.read()
        img = cv2.flip(img, 1)  # Flip image ( Flip value 0 is for vertical and 1 is for horizontal -1 is for both)
        cv2.imshow("Output", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
            break


# This is main function. All functions are called from here.
# This part is only for testing a function.
def main():
    # photo_viewer()
    # video_viewer()
    webcam()


if __name__ == '__main__':
    main()
