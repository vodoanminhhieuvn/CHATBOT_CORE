from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionSetIngredient(Action):
    def name(self) -> Text:
        return "action_set_cook_technique"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        slot_set_list = []

        if cook_technique_entities := get_entities(tracker=tracker, entity='cook_technique',
                                                   extractor=ExtractorType.RegexEntityExtractor):
            slot_set_list.append(SlotSet('cook_technique', cook_technique_entities[0]))
            dispatcher.utter_message(f"Your cook technique: {cook_technique_entities[0]}")
        else:
            dispatcher.utter_message("I understand you want to provide cook technique ?")
            dispatcher.utter_message("but I can't any infor ?")
            dispatcher.utter_message("can you repeat again ?")

        return slot_set_list
