import json
import requests

from sphinxcontrib.utils import configure_logger

logger = configure_logger(__name__)


def lookup(word, ordabok):
    word = word.lower()
    # look up in word in idord, returns the translation.
    try:
        url = "https://idord.arnastofnun.is/d/api/es/terms/?ord=" + word
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if the response was an error
        data = response.json()
        english_words = []

        for key in data.get("results", []):
            if ordabok == None or key.get("fkdictionary") == ordabok:
                for word_info in key.get("words", []):
                    if word_info.get("fklanguage") == "EN":
                        english_words.append(word_info.get("word"))

        
        entry = {}
        entry["enTerm"] = english_words
        entry["isTerm"] = word
        return entry
    except KeyError:
        # If 'word' is not found in idord, the look-up has failed and an empty
        # dict is returned.
        logger.error(f"{word} was not found in any vocabulary")
        return {}
