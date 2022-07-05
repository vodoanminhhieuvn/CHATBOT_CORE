from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.get_entities import ExtractorType, get_entities


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Xin chào bạn mình là bot sẽ giúp bạn trong viêc tìm kiếm món ăn")
        dispatcher.utter_message(
            text="mình sẽ tìm đồ ăn dựa trên nguyên liệu, công thức nấu ăn và chế độ dinh dưỡng của bạn")

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

        slot_set_list = []

        if not ingredient_entities:
            dispatcher.utter_message(text="Hiện tại bạn chưa có nguyên liệu nào để tìm kiếm ")
            dispatcher.utter_message("Bạn có thể thêm nguyên liệu bằng cách nhập: \"Nguyên liệu trứng\" ")
            dispatcher.utter_message(
                "Mình đã có thể tìm món ăn dựa trên nguyên liệu hoặc chế độ ăn mà không cần cách nấu ăn")
        else:
            dispatcher.utter_message(text=f"Bạn vừa nhập nguyên liệu: {' '.join(iter(ingredient_entities))}")
            slot_set_list.append(SlotSet('ingredient_list', ingredient_entities))

        if not cook_technique_entities:
            dispatcher.utter_message(text="Hiện tại bạn chưa có cách nấu nào để tìm kiếm")
            dispatcher.utter_message("Bạn có thể thêm cách nấu bằng cách nhập: \"Mình muốn chiên\" ")
        else:
            dispatcher.utter_message(text=f"Bạn vừa nhập cách nấu: {cook_technique_entities[0]}")
            slot_set_list.append(SlotSet('cook_technique', cook_technique_entities[0]))

        dispatcher.utter_message("Nhắn \"tìm món ăn\" nếu đã đủ nguyên liệu để tìm các món ăn phù hợp với của bạn")

        return slot_set_list
