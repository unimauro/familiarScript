import yt_dlp

def descargar_video(url, carpeta_destino="."):
    ydl_opts = {
        "outtmpl": f"{carpeta_destino}/%(title)s.%(ext)s",
        "format": "best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube: ")
    descargar_video(url)
