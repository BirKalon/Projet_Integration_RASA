# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetAnimalPicture (Action):
    def name(self) -> Text:
        return "action_get_animal_picture"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Assuming 'animal' is an entity extracted from the user's message
        animal = next(tracker.get_latest_entity_values("animals"), None)
        
        # Path to the folder containing pictures of the specified animal
        folder_path = f"/CHATBOT_DELAUNAY/pictures/{animal}.jpg"
        
        if folder_path :
            
            dispatcher.utter_message(image=folder_path)
        else:
            dispatcher.utter_message(f"Sorry, I do not have picture for that")
        
        return []
