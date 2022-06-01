from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionSetIngredient(Action):
    def name(self) -> Text:
        return "action_set_ingredients"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        slot_set_list = []

        # step Extracting entities
        ingredient_entities = get_entities(
            tracker=tracker,
            entity='ingredient',
            extractor=ExtractorType.RegexEntityExtractor
        )

        cook_technique_entities = get_entities(
            tracker=tracker,
            entity='cook_technique',
            extractor=ExtractorType.RegexEntityExtractor
        )

        # step Check if contain ingredients or cook technique

        if not ingredient_entities and not cook_technique_entities:
            dispatcher.utter_message("I understand you want to provide searching params ?")
            dispatcher.utter_message("but I can't any infor")
            dispatcher.utter_message("can you repeat again ?")
            return []

        if not ingredient_entities:
            dispatcher.utter_message("Seem like you don't provide any ingredients ?")
            return []
        else:
            slot_set_list.append(SlotSet('ingredient_list', ingredient_entities))
            dispatcher.utter_message(f"Your current ingredients: {' '.join(iter(ingredient_entities))}")

        if not cook_technique_entities:
            dispatcher.utter_message("Seem like you don't provide any cook technique ?")
            slot_set_list.append(SlotSet('cook_technique', ''))
        else:
            slot_set_list.append(SlotSet('cook_technique', cook_technique_entities[0]))
            dispatcher.utter_message(f"Your cook technique: {cook_technique_entities[0]}")

        return slot_set_list
