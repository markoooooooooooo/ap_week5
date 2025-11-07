# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
def extracting_information():
    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote.find("John F. Kennedy")) 
    famous_personality = quote[83:]
    print(famous_personality)