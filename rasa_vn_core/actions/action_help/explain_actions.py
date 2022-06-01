from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sanic import json

from actions.const.cook_technique import COOK_TECHNIQUE_DESCRIPTION


class ActionExplainIngredient(Action):
    def name(self) -> Text:
        return "action_what_ingredients"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            'A food ingredient is any substance that is added to a food to achieve a desired effect.')
        dispatcher.utter_message('The term “food ingredient” includes food additives.')
        dispatcher.utter_message(
            'You can type: cook chicken ---or--- I want to cook fish to provide ingredients')

        return []


class ActionExplainCookTechniqie(Action):
    def name(self) -> Text:
        return "action_what_is_cook_technique"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Cook technique is the way you want to cook your food")
        dispatcher.utter_message(
            "Cooking is the art of preparing food for ingestion, commonly with the application of heat.\n"
            "Cooking techniques and ingredients vary widely across the world\n"
            "Reflecting unique environments, economics, cultural traditions, and trends.\n"
            "The way that cooking takes place also depends on the skill and type of training of an individual cook\n")

        dispatcher.utter_message("Here are list you can use for Cook technique")

        custom_message = list(COOK_TECHNIQUE_DESCRIPTION)

        dispatcher.utter_message(
            json_message={"cook_techinque": custom_message}
        )

        return []
