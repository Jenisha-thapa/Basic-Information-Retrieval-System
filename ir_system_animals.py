import string

# ---------------------------------------------------
# Step 1: Document Collection
# ---------------------------------------------------
documents = {
    1: "The lion is a large carnivorous mammal found in Africa known as the king of the jungle and lives in groups called prides.",
    2: "The elephant is the largest land mammal found in Africa and Asia known for its long trunk and large ears.",
    3: "The dolphin is an intelligent marine mammal found in oceans worldwide known for its playful behavior and echolocation.",
    4: "The eagle is a powerful bird found in mountains and forests known for its sharp vision and strong talons.",
    5: "The penguin is a flightless bird found in Antarctica known for its ability to swim and its black and white feathers.",
    6: "The kangaroo is a marsupial mammal found in Australia known for its powerful hind legs and ability to hop long distances.",
    7: "The tiger is a large carnivorous mammal found in Asia known for its orange coat with black stripes and solitary hunting.",
    8: "The crocodile is a large carnivorous reptile found in rivers and lakes known for its powerful jaws and ambush hunting."
}

def add_document(doc_id, text):
    documents[doc_id] = text

# ---------------------------------------------------
# Step 2: Preprocessing
# ---------------------------------------------------
def preprocess(text):
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, " ")
    tokens = text.split()
    return tokens

# ---------------------------------------------------
# Step 3: Build Dictionary and Inverted Index
# ---------------------------------------------------
def build_index(documents):
    dictionary = set()
    inverted_index = {}
    for doc_id, text in documents.items():
        tokens = preprocess(text)
        for token in tokens:
            dictionary.add(token)
            if token not in inverted_index:
                inverted_index[token] = set()
            inverted_index[token].add(doc_id)
    return sorted(dictionary), inverted_index

# ---------------------------------------------------
# Step 4: Boolean Retrieval Functions
# ---------------------------------------------------
def get_postings(term, inverted_index):
    return inverted_index.get(term.lower(), set())

def boolean_and(term1, term2, inverted_index):
    return get_postings(term1, inverted_index) & get_postings(term2, inverted_index)

def boolean_or(term1, term2, inverted_index):
    return get_postings(term1, inverted_index) | get_postings(term2, inverted_index)

def boolean_not(term, inverted_index, all_doc_ids):
    return all_doc_ids - get_postings(term, inverted_index)

# ---------------------------------------------------
# Step 5: Run the System
# ---------------------------------------------------
if __name__ == "__main__":
    dictionary, inverted_index = build_index(documents)
    all_doc_ids = set(documents.keys())

    print("Documents:")
    for doc_id, text in documents.items():
        print(doc_id, ":", text)

    print("\nDictionary (Vocabulary):")
    print(dictionary)

    print("\nInverted Index:")
    for term in dictionary:
        print(term, "->", sorted(inverted_index[term]))

    print("\nSample Boolean Queries:")
    print("mammal ->", get_postings("mammal", inverted_index))
    print("africa AND mammal ->", boolean_and("africa", "mammal", inverted_index))
    print("bird OR reptile ->", boolean_or("bird", "reptile", inverted_index))
    print("mammal AND NOT africa ->", get_postings("mammal", inverted_index) & boolean_not("africa", inverted_index, all_doc_ids))
    print("NOT carnivorous ->", boolean_not("carnivorous", inverted_index, all_doc_ids))
