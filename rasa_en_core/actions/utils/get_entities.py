from typing import Any, Dict, Text

from rasa_sdk import Tracker


class ExtractorType:
    RegexEntityExtractor: str = 'RegexEntityExtractor'
    DIETClassifier: str = 'DIETClassifier'
    SentimentExtractor: str = 'SentimentExtractor'


def get_entities(
        tracker: Tracker,
        entity,
        extractor: str = ExtractorType.DIETClassifier) -> list:
    blobs = tracker.latest_message['entities']
    return [blob['value']
            for blob in blobs
            if blob['entity'] == entity and blob['extractor'] == extractor]
