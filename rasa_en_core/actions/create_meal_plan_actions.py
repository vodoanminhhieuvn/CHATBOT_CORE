from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.request.request import request_get_api
from actions.request.http_url import GENERATE_MEAL_URL, CREATE_MEAL_PLAN_CONFIG
from actions.utils.get_entities import get_entities
from actions.dataclass.meal_plan_respnose import MealPlanResponse


class ActionCreateMealPlan(Action):

    def name(self) -> Text:
        return "action_create_meal_plan"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            target_calories = get_entities(tracker, 'target_calories')[0]
        except IndexError:
            target_calories = 2000

        if diet_slot := tracker.get_slot('diet_list'):
            list_diet = diet_slot
        else:
            list_diet = get_entities(tracker, 'diet')

        # Step get slot nutrient value
        params = {
            'timeFrame': 'day',
            'targetCalories': f"{target_calories}",
            **CREATE_MEAL_PLAN_CONFIG
        }

        if list_diet:
            params['diet'] = list_diet
            diet_message = "".join(
                f"{diet} \n"
                for diet in list_diet
            )
            dispatcher.utter_message(diet_message)

        # Step request to API
        response = request_get_api(url=GENERATE_MEAL_URL, params=params)
        meal_plan = MealPlanResponse(**response.json())

        for meal in meal_plan.meals:
            dispatcher.utter_message(meal['title'])

        return [SlotSet('meal_plan_response', response.json())]
