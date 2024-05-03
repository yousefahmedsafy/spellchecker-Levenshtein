from itertools import islice
from symspellpy import SymSpell,Verbosity 

# Create an instance of SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load a dictionary file
dictionary_path = r"E:\nlp_train\spellchecker\med.txt"
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1,separator="_")
print(list(islice(sym_spell.words.items(), 5)))
# Perform spelling correction
input_term = "ado"
max_edit_distance = 2
suggestions = sym_spell.lookup(
    input_term, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True
)
# Print suggestions
for suggestion in suggestions:
    print(suggestion)