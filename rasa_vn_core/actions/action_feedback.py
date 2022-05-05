from __future__ import annotations

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from requests import Response

from actions.request.http_url import FEEDBACK_URL
from actions.request.request import request_json_api
from actions.utils.getEntities import ExtractorType, get_entities


class ActionSubmitFeedback(Action):

    def name(self) -> Text:
        return "action_submit_feedback"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text='Bạn đợi mình xíu nha ....')

        sentiment_entity = get_entities(
            tracker=tracker, entity='sentiment', extractor=ExtractorType.SentimentExtractor)

        response: Response = await request_json_api(
            url=FEEDBACK_URL,
            json={"text": tracker.latest_message['text'],
                  "sentiment": f"{sentiment_entity[0]}"})

        if response.status_code == 201:
            dispatcher.utter_message(text="Cảm ơn bạn đóng góp ý kiến")
        else:
            dispatcher.utter_message(text="Đã xảy ra lỗi bên phía bọn mình")
            # dispatcher.utter_message(text=tracker.latest_message.values)
        return []