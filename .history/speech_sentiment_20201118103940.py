from speech_helpers import convert_to_wav, show_pydub_stats, transcribe_audio
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
filename = 'ex4_call_1_stereo_mp3'

con
trans_text = transcribe_audio(filename)
sid.polarity_scores(trans_text)

