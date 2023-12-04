import spacy
from spacy.matcher import Matcher
import re

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a custom pattern for email addresses using regular expression
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Define a custom pattern for addresses using Matcher
address_pattern = [
    {"TEXT": {"REGEX": r"\d+"}},  # House number
    {"TEXT": {"REGEX": r"\w+"}},  # Street name
    {"LOWER": {"IN": ["street", "st.", "avenue", "ave.", "road", "rd.", "lane", "ln.", "boulevard", "blvd."]}}
]

matcher = Matcher(nlp.vocab)
matcher.add("ADDRESS", [address_pattern])

def extract_entities(sentence):
    doc = nlp(sentence)

    # Extract various entities and custom patterns
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    matches = matcher(doc)
    addresses = [doc[start:end].text for match_id, start, end in matches]

    emails = re.findall(email_pattern, sentence)

    return {
        "entities": entities,
        "addresses": addresses,
        "emails": emails
    }

# Example usage:
def process_sentence(new_sentence):
    results = extract_entities(new_sentence)

    # Display extracted entities, addresses, and emails
    print("Entities:")
    for entity, label in results['entities']:
        print(f"{entity}: {label}")

    print("\nAddresses:")
    for address in results['addresses']:
        print(address)

    print("\nEmails:")
    for email in results['emails']:
        print(email)

# Usage example:
sentence_to_process = "John Doe lives at 123 Main Street, New York. Contact him at john.doe@email.com."
process_sentence(sentence_to_process)
