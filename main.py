from connectoCCTV import ReadingCamera

urls = ["rtsp://CCTV:cctv2021@192.168.0.26:554/Streaming/Channels/01","rtsp://CCTV:cctv2021@192.168.0.27:554/Streaming/Channels/01"]

videoTest = ReadingCamera(urls)
videoTest.startReading()

