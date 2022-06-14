from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.request.request import request_get_api
from actions.request.http_url import SEARCH_URL

# TODO Tìm kiếm món ăn


class ActionFindRecipe(Action):

    def name(self) -> Text:
        return "action_find_recipe"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # step- Check if slot has value or not

        ingredient_list = tracker.get_slot('ingredient_list')
        cook_technique = tracker.get_slot('cook_technique')

        if not ingredient_list:
            dispatcher.utter_message(
                "Seem like you haven't provided any ingredieny yet")
            dispatcher.utter_message(
                'Please provide me at least one ingredient')

        # step- Send request API
        params = {
            'q': f"{' '.join(str(ingredient) for ingredient in ingredient_list)} {cook_technique}",
        }

        response = request_get_api(url=SEARCH_URL, params=params)

        # step- Create button for user to choose
        buttons = [{"title": f"{index}-{hit['Name']}", "payload": f"chế biến món {index}"}
                   for index, hit in enumerate(response.json()['recipes'])]

        dispatcher.utter_message(buttons=buttons)

        return [SlotSet('recipe_search_response', response.json())]
