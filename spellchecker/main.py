from spellchecker.spellchecker import SpellChecker
import time
import Levenshtein
# record start time
start = time.time()
def spellcorrcetion(word):# put word  in prameter ok ace
    # define a sample code segment
    spell = SpellChecker(language=None,distance=3)
    spell.word_frequency.load_text_file( r"output.txt") # replace med.txt to my.txt to compre between the word and dictanry
    # put word in spell.unknown ([" my string"])
    misspelled = spell.unknown([word]) # for white space add "_" 


    for word in misspelled:
        print(str(word)+" it's corrction  "+str(spell.correction(word)))

def nearst_word1(word1):

    with open("med.txt", "r+",encoding='utf-8') as file1:
        word1 = '_'.join(word1.split())
        maxx_raito=0
        word=0
        with open(r"output.txt", 'r',encoding='utf-8') as file:
            words = [line.strip() for line in file]
            for i in words:
                word2=i
                max_length = max(len(word1), len(word2))
                lev_distance = Levenshtein.distance(word1, word2)
                similarity_ratio = 1 - lev_distance / max_length
                if similarity_ratio>maxx_raito:
                    maxx_raito= similarity_ratio
                    word=word2
            print(str(word)+ " it is ratio "+str(maxx_raito))
    
    file1.close() 

nearst_word1("vitamax")


# record end time
end = time.time()

# # print the difference between start 
# # and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
