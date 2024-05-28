'''
Developed by Balum S.A. under supervision of Daniel Zambrano Acosta. 
This code is used to connect to the CCTV, which is paired with AWS through a site-to-site VPN.
'''

import cv2
import threading

class ReadingCamera:
    def __init__(self,rtsp):
        self.rtsp = rtsp
        self.threads = []

    def readVideo(self,rtsp):
        try:
            video_capture = cv2.VideoCapture(rtsp)
            if not video_capture.isOpened():
                raise Exception(f"fail connection to camera in {rtsp}")

            while video_capture.isOpened():
                ret, frame = video_capture.read()
                if not ret:
                    print(f"Error at reading camera at {rtsp}")
                    break
            
                #Display video
                cv2.imshow(f"Camera{rtsp}",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
            video_capture.release()
            cv2.destroyAllWindows()


        except Exception as e:
            print(f"Error at camera {rtsp}: {e}")
        
    def startReading (self):
        for url in self.rtsp:
            thread = threading.Thread(target=self.readVideo, args=(url,))
            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()

