from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.const.cook_technique import COOK_TECHNIQUE_DESCRIPTION


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
            "Cooking is the art of preparing food for ingestion, commonly with the application of heat. \
              Cooking techniques and ingredients vary widely across the world, \
              reflecting unique environments, economics, cultural traditions, and trends. \
              The way that cooking takes place also depends on the skill and type of training of an individual cook"
        )

        dispatcher.utter_message("Here are list you can use for Cook technique")

        message = "".join(f"{key}\n" for key in COOK_TECHNIQUE_DESCRIPTION)

        dispatcher.utter_message(message)

        return []
