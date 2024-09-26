from pythainlp.tokenize import syllable_tokenize,DEFAULT_SYLLABLE_TOKENIZE_ENGINE

EXIST_CODES = ["X", "x", "exit", "exit()"]
word_dict = {}

def add_new_word(raw_word):
    tokenized_words = syllable_tokenize(raw_word, engine=DEFAULT_SYLLABLE_TOKENIZE_ENGINE)
    for word in tokenized_words:
        word_in_dict = word_dict.get(word)
        if word_in_dict is not None:
            return (False, word_in_dict, word)
        
        word_dict[word] = raw_word
    return (True, "", "")

while True:
    raw_word = str(input("word: "))
    
    if raw_word in EXIST_CODES:
        print("existing...")
        break
    
    (is_valid, used_word, duplicate_on) = add_new_word(raw_word)
    # print(word_dict)
    if not is_valid:
        print(f"used word detect: {used_word}, duplicated on: {duplicate_on}")