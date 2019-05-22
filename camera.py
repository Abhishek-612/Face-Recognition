import cv2,time
import matplotlib.pyplot as plt


def main():
    print("Looking for you...")
    print('Please look into the camera!')
    print()
    time.sleep(3)
    
    cap=cv2.VideoCapture(0)

    if(cap.isOpened()):
       ret, frame=cap.read()
       #print(ret)
       #print(frame)

    else:
       ret=False

    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #print(img)

    '''
    plt.imshow(img)
    plt.title("Me")
    plt.xticks([])
    plt.yticks([])
    plt.show()'''


    cap.release()

    return img


if __name__ == "__main__":
    main()
       
