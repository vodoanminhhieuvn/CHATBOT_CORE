from ast import ListComp
from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import get_entities
from actions.utils.get_entities import ExtractorType


class ActionSetIngredient(Action):
    def name(self) -> Text:
        return "action_set_ingredients"

    def check_contain(self) -> List:

        # Step 1: Check if contain infor in user input match with recipe list

        # Step 2: Return List

        return True

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        slot_set_list = []

        # step Extracting entities
        ingredient_entities = get_entities(
            tracker=tracker,
            entity='ingredient',
            extractor=ExtractorType.RegexEntityExtractor
        )

        cook_technique_entities = get_entities(
            tracker=tracker,
            entity='cook_technique',
            extractor=ExtractorType.RegexEntityExtractor
        )

        print(ingredient_entities, cook_technique_entities)

        # step Check if contain ingredients or cook technique

        if not ingredient_entities and not cook_technique_entities:
            dispatcher.utter_message("Mình biết là bạn muốn tìm đồ ăn ?")
            dispatcher.utter_message("nhưng mình chưa biết bạn cần gì")
            dispatcher.utter_message("bạn có thể nhập lại cho mình được không  ?")
            return []

        if not ingredient_entities:
            dispatcher.utter_message("Hình như bạn chưa cung cấp nguyên liệu nào thì phải ?")
            return []
        else:
            slot_set_list.append(SlotSet('ingredient_list', ingredient_entities))
            dispatcher.utter_message(f"Danh sách tìm của bạn: {' '.join(iter(ingredient_entities))}")

        if not cook_technique_entities:
            dispatcher.utter_message("Hình như bạn chưa cung cấp cách nấu thì phải ?")
            slot_set_list.append(SlotSet('cook_technique', ''))
        else:
            slot_set_list.append(SlotSet('cook_technique', cook_technique_entities[0]))
            dispatcher.utter_message(f"Cách nấu: {cook_technique_entities[0]}")

        if ingredient_entities:
            dispatcher.utter_message("Nhắn \"tìm món ăn\" để tìm các món ăn phù hợp với nguyên liệu của bạn")

        return slot_set_list
