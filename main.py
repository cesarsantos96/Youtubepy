from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error while downloading the video")
        print("This dowload has completed!")

        link = input("Put your Youtube link here: URL: ")
        Download(link)
