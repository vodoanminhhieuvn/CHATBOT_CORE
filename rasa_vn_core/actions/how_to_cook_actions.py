from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType
from actions.request.http_url import GET_DETAIL_URL
from actions.request.request import request_get_api

# TODO Hướng dẫn nấu món ăn


class ActionHowToCook(Action):
    def name(self) -> Text:
        return "action_how_to_cook"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        recipe_hits = tracker.get_slot('recipe_search_response')['recipes']

        if recipe_index := get_entities(tracker=tracker, entity='detail_index'):
            recipe_user_need = recipe_hits[int(recipe_index[0])]
            response = request_get_api(url=f"{GET_DETAIL_URL}{recipe_user_need['Id']}")

        else:
            dispatcher.utter_message("Hình như bạn nhầm vị trí món thì phải")
            return[]

        # ingredient_buttons = [{"title": f"{index}- {ingredient}", "payload": f"ingredient detail {index}"}
        #                       for index, ingredient in enumerate(recipe_user_need['ingredientLines'])]

        recipe_data = response.json()['data']

        ingredient_messages = "".join(
            f"{ingredient['name']} \n"
            for ingredient in recipe_data['ingredients']
        )

        dispatcher.utter_message(image=recipe_user_need['Img'])
        dispatcher.utter_message(f"Tổng thời gian: {recipe_data['totalTime']} phút")
        dispatcher.utter_message(ingredient_messages)
        dispatcher.utter_custom_json(json_message={'youtubeId': recipe_user_need['Video']})

        return []
