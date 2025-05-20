import json
import logging
import sys
from pathlib import Path
import requests

from sphinxcontrib.utils import configure_logger

logger = configure_logger(__name__)
# Look up icelandic searchterm 'word' in the dictionaries 'minstae' and 'binstae'
# and return a dict containing the english and icelandic citation forms of the word.
base_dir = Path(__file__).parent.resolve()
data_file = base_dir / "hoverrole/data" / "minstae.json"
minstae_data = json.loads(data_file.read_text())

data_file = base_dir / "hoverrole/data" / "binstae.json"
binstae_data = json.loads(data_file.read_text())


def lookup(word):
    word = word.lower()
    # If 'word' is in citation form, look up in 'minstae' returns the translation.
    try:
        url = "https://idord.arnastofnun.is/d/api/es/terms/?ord=" + word
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if the response was an error
        data = response.json()
        english_words = []

        for key in data.get("results", []):
            for word_info in key.get("words", []):
                if word_info.get("fklanguage") == "EN":
                    english_words.append(word_info.get("word"))

        
        entry = minstae_data[word]
        entry["enTerm"] = english_words
        entry["isTerm"] = word
        return entry
    # If 'word' is not found in 'minstae', it may not be in citation form and a
    # look up in 'binstae' is performed instead.
    except KeyError:
        try:
            entry = binstae_data[word]
            return entry
        # If 'word' is not found in 'binstae', the look-up has failed and an empty
        # dict is returned.
        except KeyError:
            logger.error(f"{word} was not found in any vocabulary")
            return {}
