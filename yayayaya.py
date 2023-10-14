import spacy
import numpy as np

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

phi_sentences = []

# Read PHI sentences from a text file
with open("phi.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        phi_sentences.append(cleaned_line)

def extract_and_structure_phi(phi_sentence):
    doc = nlp(phi_sentence)
    
    structured_info = {
        "name": None,
        "age": None,
        "gender": None,
        "visitdate": None,
        "diagnosis": None,
        "treatment": None,
    }
    
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            structured_info["name"] = ent.text
        elif ent.label_ == "DATE":
            structured_info["age"] = ent.text
        elif ent.label_ == "GPE":
            structured_info["gender"] = ent.text
        elif ent.label_ == "DATE":
            structured_info["visitdate"] = ent.text
        elif ent.label_ == "DIAGNOSIS":
            structured_info["diagnosis"] = ent.text
        elif ent.label_ == "TREATMENT":
            structured_info["treatment"] = ent.text
    
    tokenized_sentence = (
        f"{structured_info['name']} is a {structured_info['age']} year old "
        f"{structured_info['gender']} who visited the hospital on {structured_info['visitdate']}. "
        f"He was diagnosed with {structured_info['diagnosis']}. The treatment recommended by the doctor is {structured_info['treatment']}."
    )
    return structured_info

struct=[]
for phi_sentence in phi_sentences:
    stru1 = extract_and_structure_phi(phi_sentence)
    struct.append(stru1)
    print(struct)


for phi_sentence in phi_sentences:
    structs = extract_and_structure_phi(phi_sentence)

rand_names=[
    "John Smith",
    "Jane Doe",
    "Alice Johnson",
    "Bob Williams",
    "Eva Wilson",
    "David Brown",
    "Linda Davis",
    "Mike Anderson",
    "Sophia Lee",
    "Henry Martinez",
    "Olivia White",
    "William Taylor",
    "Emily Harris",
    "James Jackson",
    "Grace Clark",
    "Daniel Turner",
    "Sarah Moore",
    "Michael Miller",
    "Emma Hall",
    "Robert King"
]

for data in structs:
    template=f"{rand_names[np.random.randint(0, len(rand_names))]} is a {data['age']} year old {data['gender']} who visited the hospital on {data['visitdate']}. He was diagnosed with {data['diagnosis']}. The treatment recommended by the doctor is {data['treatment']}."