from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.request.http_url import FIND_RECIPE_CONFIG


class ActionFindRecipe(Action):

    def name(self) -> Text:
        return "action_find_recipe"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_query = ''

        # step- Check if slot has value or not

        ingredient_list = tracker.get_slot('ingredient_list')
        cook_technique = tracker.get_slot('cook_technique')

        if not ingredient_list:
            dispatcher.utter_message("Seem like you haven't provided nay ingredieny yet")
            dispatcher.utter_message('Please provide me at least one ingredient')

        # step- Send request API

        # step- Create button for user to choose

        return []
