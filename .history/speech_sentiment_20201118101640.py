from speech_helpers import convert_to_wav, show_pydub_stats, transcribe_audio
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
filename = ''

@convert_to_wav
trans_text = transcribe_audio(filename)
sid.polarity_scores(trans)