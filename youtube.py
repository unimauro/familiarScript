from pytube import YouTube

def descargar_video(url, carpeta_destino="."):
    try:
        yt = YouTube(url)
        print(f"Descargando: {yt.title}")

        # Selecciona la mejor calidad de video disponible
        stream = yt.streams.get_highest_resolution()
        
        # Descarga el video en la carpeta especificada
        stream.download(carpeta_destino)
        print("Descarga completada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube: ")
    descargar_video(url)

