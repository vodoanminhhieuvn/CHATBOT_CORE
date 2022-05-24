from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionPreviousRecipe(Action):
    def name(self) -> Text:
        return "action_previous_recipe"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        recipe_hits = tracker.get_slot('recipe_search_response')

        if recipe_hits:
            dispatcher.utter_message("Seem like you have had any recipe search yet")
            return []

        recipe_buttons = [{"title": f"{index}-{hit['recipe']['label']}", "payload": f"detail {index}"}
                          for index, hit in enumerate(recipe_hits)]

        dispatcher.utter_message(buttons=recipe_buttons)

        return []
