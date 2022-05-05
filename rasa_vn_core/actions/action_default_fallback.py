from typing import Any, Dict, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]):
        # output a message saying that the conversation will now be
        # continued by a human.

        message = "Sorry! Let me connect you to a human..."
        dispatcher.utter_message(text=message)
