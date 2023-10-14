import random
from faker import Faker
import numpy as np
from datetime import datetime

# Create a fake data generator
fake = Faker()

# Generate synthetic health data for a number of patients
num_patients = 100
synthetic_data = []

diagnosis_names = [
    "Hypertension",
    "Type 2 Diabetes",
    "Asthma",
    "Migraine",
    "Allergies",
    "Bronchitis",
    "Influenza",
    "Osteoarthritis",
    "Anxiety Disorder",
    "Depression",
]

treatment_sentences = [
    "Prescribed medication for the condition.",
    "Advised rest and hydration.",
    "Scheduled physical therapy sessions.",
    "Recommended lifestyle modifications.",
]

for _ in range(num_patients):
    if not diagnosis_names:
        # Make sure the diagnosis_names list is not empty
        raise ValueError("diagnosis_names list is empty")

    if not treatment_sentences:
        # Make sure the treatment_sentences list is not empty
        raise ValueError("treatment_sentences list is empty")

    patient = {
        "name": fake.name(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "gender": random.choice(["Male", "Female"]),
        "diagnosis": diagnosis_names[np.random.randint(0, len(diagnosis_names))],
        "treatment": treatment_sentences[np.random.randint(0, len(treatment_sentences))],
        "visitdate": fake.date_between(start_date="-1y", end_date="today"),
    }
    synthetic_data.append(patient)

sens = []

# Create the templated sentence and write to the file
with open("../anon-thingy/phi.txt", "a") as file:
    for data in synthetic_data:
        dob = data["dob"]
        current_year = datetime.now().year
        age = current_year - dob.year
        sentence = f"{data['name']} is a {age} year old {data['gender']} who visited the hospital on {data['visitdate']}. He was diagnosed with {data['diagnosis']}. The treatment recommended by the doctor is {data['treatment']}."
        sens.append(sentence)
        file.write(sentence + "\n")

# Print the generated sentences
for sentence in sens:
    print(sentence)