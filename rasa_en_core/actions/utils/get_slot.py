from rasa_sdk import Tracker


def get_slot(tracker: Tracker, slot_name):
    return tracker.get_slot(slot_name)
