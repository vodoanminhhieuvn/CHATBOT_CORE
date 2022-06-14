from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionSetCookTechnique(Action):
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
            dispatcher.utter_message(f"Cách nấu: {cook_technique_entities[0]}")
        else:
            dispatcher.utter_message("Mình biết là bạn muốn cung cấp cách nấu ăn ?")
            dispatcher.utter_message("nhưng mình chưa thấy")
            dispatcher.utter_message("bạn nhập lại dùm mình được không ?")

        return slot_set_list
