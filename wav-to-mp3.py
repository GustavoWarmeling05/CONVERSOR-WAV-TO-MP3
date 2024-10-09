from pydub import AudioSegment
import os

def convert_wav_to_mp3(input_wav, output_mp3):
    # Verificar se o arquivo de entrada existe
    if not os.path.exists(input_wav):
        raise FileNotFoundError(f"O arquivo {input_wav} não foi encontrado.")
    
    # Carregar o arquivo WAV
    audio = AudioSegment.from_wav(input_wav)

    # Exportar como MP3
    audio.export(output_mp3, format="mp3")
    print(f"Arquivo convertido para MP3: {output_mp3}")

# Exemplo de uso
input_wav = "NOMEDOARQUIVOWAV.wav"  # Substitua pelo nome do arquivo de entrada
output_mp3 = "RESULTADODACONVERSAO.mp3"  # Nome do arquivo de saída
convert_wav_to_mp3(input_wav, output_mp3)
