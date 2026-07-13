import spacy

# Load spaCy English model only once
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Clean English text using spaCy.
    """

    doc = nlp(text)

    cleaned_words = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
        ):

            cleaned_words.append(token.lemma_.lower())

    cleaned_text = " ".join(cleaned_words)

    return cleaned_text