from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities


class ActionSetDiet(Action):

    def name(self) -> Text:
        return "action_set_diet"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_diet = get_entities(tracker=tracker, entity='diet')

        message = "".join(
            f"{diet} \n"
            for diet in list_diet
        )

        dispatcher.utter_message("Your current diet setting:")
        dispatcher.utter_message(message)

        return [SlotSet('diet_list', list_diet)]
