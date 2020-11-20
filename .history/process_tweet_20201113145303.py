import re

REPLACE_BY_SPACE = re.compile('[/(){}\[\]\|,;&-_]') #punctuation to replace



pt = process_tweet()

test = pt.preprocess_text("Hello, this is Ernest @OwojoriErnest. #EndSars")
print(test)