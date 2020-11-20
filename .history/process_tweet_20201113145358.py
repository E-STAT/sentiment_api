import re

REPLACE_BY_SPACE = re.compile('[/(){}\[\]\|,;&-_]') #punctuation to replace


def preprocess_text(text):
        
        """
        Function to preprocess text: removes links, punctuation, spaces, non-alpha words and stop_words
        
        Parameters
        ----------
        text: str
            a string to be preprocessed
            
        Returns
        -------
        text: str
            a preprocessed string
        """
        text = text.lower()                                    #lowercase
        text = re.sub(r"http\S+", "", text)                    #replace links with ""
        self.text = re.sub(r"\@\S+", "", text)                      #replace mentions with ""
        self.text = re.sub(r"#\S+", "", text)                       #replace hashtags with ""
        self.text = re.sub(r"won\'t", "would not", text)            #deal with contractions
        self.text = re.sub(r"n\'t", " not", text)                   #deal with contractions
        self.text = REPLACE_BY_SPACE.sub(' ', text)                 #replace punctuation with space
        self.text = [word.strip() for word in text.split()]         #strip space from words
        self.text = [word for word in text if len(word)>2]          #removing words less than 2 characters
        self.text = [word for word in text if word!='amp']          #removing twitter amp
        self.text = ' '.join(text)
        return self.text



test = preprocess_text("Hello, this is Ernest @OwojoriErnest. #EndSars")
print(test)