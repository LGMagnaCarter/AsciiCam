from ConvertImageToAscii import convertImageToAscii
import cv2
import numpy

# main() function
def main():
    cap = cv2.VideoCapture(1);
    
    r, f = cap.read()
    
    cols = 80
    scale = 0.43
    columnWidth = int(f.shape[1] / cols)
    rowHeight = 19

    while(True):
        ret, frame = cap.read()
        if frame is not None:
            textArray = convertImageToAscii(frame, cols, scale, True)
            
            x = 10

            cv2.rectangle(frame,(0,0),(int(frame.shape[1]), int(frame.shape[0])), (0,0,0), -1)
            for text in textArray:
                y = 10
                for char, colour in text:
                    cv2.putText(frame, char, (y,x), cv2.FONT_HERSHEY_SIMPLEX, scale, colour, 2)
                    y = y + columnWidth
                x = x + rowHeight

            cv2.imshow('AsciiCam', frame)
        else:
            print("empty frame")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


# call main
if __name__ == '__main__':
	main()
