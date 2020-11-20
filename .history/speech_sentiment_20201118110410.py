from speech_helpers import convert_to_wav, show_pydub_stats, transcribe_audio
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
filename = 'ex4_call_1_stereo_mp3.mp3'
new_name = 'ex4_call_1_stereo_mp3.wav'
convert_to_wav(filename)
# trans_text = transcribe_audio(new_name)
# sid.polarity_scores(trans_text)

