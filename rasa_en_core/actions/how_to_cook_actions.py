from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionHowToCook(Action):
    def name(self) -> Text:
        return "action_how_to_cook"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        recipe_hits = tracker.get_slot('recipe_search_response')['hits']

        if recipe_index := get_entities(tracker=tracker, entity='detail_index'):
            recipe_user_need = recipe_hits[int(recipe_index[0])]['recipe']

        else:
            dispatcher.utter_message("Seem like you missing position of food")
            return[]

        ingredient_buttons = [{"title": f"{index}- {ingredient}", "payload": f"ingredient detail {index}"}
                              for index, ingredient in enumerate(recipe_user_need['ingredientLines'])]

        ingredient_messages = "".join(
            f"{ingredient} \n"
            for ingredient in recipe_user_need['ingredientLines']
        )

        dispatcher.utter_message(ingredient_messages)
        dispatcher.utter_message(buttons=ingredient_buttons)

        return [SlotSet('ingredient_search', recipe_user_need['ingredients'])]
