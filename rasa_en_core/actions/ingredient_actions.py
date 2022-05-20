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

        if not ingredient_entities:
            dispatcher.utter_message("Seem like you don't provide any ingredients ?")

        if not cook_technique_entities:
            dispatcher.utter_message("Seem like you don't provide any cook technique ?")

        # Step set slot and send message to user

        list_ingredient_string = " ".join(iter(ingredient_entities))

        slot_set_list = [SlotSet('ingredient_list', [iter(ingredient_entities)]),
                         SlotSet('cook_technique', cook_technique_entities[0])]

        dispatcher.utter_message(f"Your current ingredients: {list_ingredient_string}")
        dispatcher.utter_message(f"Your cook technique: {cook_technique_entities[0]}")

        return slot_set_list
