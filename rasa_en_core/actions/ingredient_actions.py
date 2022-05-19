from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionSetIngredient(Action):
    def name(self) -> Text:
        return "action_set_ingredients"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        search_query = ''

        # step set food search query
        SlotSet('food_search_query', search_query)
        return []
