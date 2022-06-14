from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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


class ActionExplainSpecificTechnique(Action):
    def name(self) -> Text:
        return "action_explain_specific_technique"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return []


class ActionExplainCookTechnique(Action):
    def name(self) -> Text:
        return "action_what_is_cook_technique"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Phương thức nấu ăn là cách chế biến món ăn")
        dispatcher.utter_message(
            "Nấu ăn là một nghệ thuật còn người nấu ăn là một nghệ sỹ, từ việc chuẩn bị nguyên liệu cho đến sơ chế.\n"
            "Chế biến thức ăn rồi cả khâu trang trí sắp xếp bố cục món ăn sao cho hợp lý đẹp mắt là cả một quá trình\n"
        )

        dispatcher.utter_message("Đây là một số phương pháp nấu ăn")

        custom_message = list(COOK_TECHNIQUE_DESCRIPTION)

        dispatcher.utter_message(
            json_message={"cook_techinque": custom_message}
        )

        return []
