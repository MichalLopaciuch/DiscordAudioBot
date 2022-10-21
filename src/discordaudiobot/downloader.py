from yt_dlp import YoutubeDL

class Downloader:
    options = {
        'format': 'm4a/bestaudio/best',
        'nooverwrites': True,
        'extractaudio': True,
        'noplaylist': True,
        'default_search': 'auto',
        'simulate': True
    }

    @classmethod
    def download(cls, search):
        with YoutubeDL(cls.options) as ytdl:
            try:
                return ytdl.extract_info(search, download=False)
            except:
                return None
