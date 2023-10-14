from transformers import BertTokenizer, BertForTokenClassification, pipeline
import numpy as np

# Load the "bert-base-uncased" tokenizer and model for NER
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english", num_labels=3)

# Define NER labels for "diagnosis" and "treatment"
labels = ["O", "B-DIAGNOSIS", "B-TREATMENT"]

# Load the NER model
nlp_ner = pipeline("ner", model=model, tokenizer=tokenizer, ignore_labels=[])

phi_sentences = []

# Read PHI sentences from a text file
with open("phi.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        phi_sentences.append(cleaned_line)

def extract_and_structure_phi(phi_sentence):
    # Perform NER using the "bert-base-uncased" model
    entities = nlp_ner(phi_sentence)

    structured_info = {
        "name": None,
        "age": None,
        "gender": None,
        "visitdate": None,
        "diagnosis": None,
        "treatment": None,
    }

    current_label = None

    for entity in entities:
        label = entity["entity"]
        text = entity["word"]
        
        if label.startswith("B-"):
            current_label = label
        elif label == "O":
            current_label = None

        if current_label == "B-PERSON":
            structured_info["name"] = text
        elif current_label == "B-DATE":
            structured_info["age"] = text
        elif current_label == "B-GPE":
            structured_info["gender"] = text
        elif current_label == "B-DATE":
            structured_info["visitdate"] = text
        elif current_label == "B-DIAGNOSIS":
            structured_info["diagnosis"] = text
        elif current_label == "B-TREATMENT":
            structured_info["treatment"] = text

    return structured_info

struct = []
rand_names = [
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

for phi_sentence in phi_sentences:
    stru1 = extract_and_structure_phi(phi_sentence)
    struct.append(stru1)

for data in struct:
    template = (
        f"{rand_names[np.random.randint(0, len(rand_names))]} is a {data['age']} year old "
        f"{data['gender']} who visited the hospital on {data['visitdate']}. "
        f"He was diagnosed with {data['diagnosis']}. The treatment recommended by the doctor is {data['treatment']}."
    )
    print(template)
