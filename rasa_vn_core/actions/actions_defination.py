from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import json

from actions.utils.getEntities import get_entities
from actions.data.definations import valid_defination
from actions.data.definations import get_defination_data


class ActionDefination(Action):

    def name(self) -> Text:
        return "action_defination"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        list_defination_entities = get_entities(
            tracker=tracker, entity='defination')

        for defination in list_defination_entities:
            if (valid_defination(defination)):

                for text in get_defination_data(defination):
                    dispatcher.utter_message(text)

        return []
