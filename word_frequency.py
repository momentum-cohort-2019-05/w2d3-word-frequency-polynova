STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def clean_text(text):
    """ Removes punctuation from file """
    text = text.replace(",","").replace(".", "").replace("!", "")
    text = text.lower()
    for word in text:
        if word in STOP_WORDS:
            text = text.replace(word, "")
    return text 

    
    
# original list = ["the", "car",....]
#  newlst = []
#  frequency = []
#  for word in the original list
#        if word not in newlst:
#            newlst.append(word)
#            set frequency = 1
#        else
#            increase the frequency
#  sort newlst based on frequency list

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pass
    #open read file 
    #remove punctuation 
    #lowercase
    #remove stop words that are in this file above
    #keep count of how often words are used
    #use dictionary to print out frequency
    #calculate frequency 


    with open (file) as my_file:
        my_file = my_file.read()
    my_file = clean_text(my_file) 
    print(my_file)
    


    


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
