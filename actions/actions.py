from asyncore import dispatcher
import email
from typing import Any, Text, Dict, List
from unicodedata import name

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.action_quote_price  import quotes
from actions.action_get_weather import weather
from actions.action_store_to_database import store


class ActionQuotePrice(Action):

    def name(self) -> Text:
        return "action_quote_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ticker = next(tracker.get_latest_entity_values("tickers"), None)

        if not ticker:
            dispatcher.utter_message('Im sorry I didnt get that ticker')

        quote = quotes(ticker)

        dispatcher.utter_message(f'The quote for {ticker} is {quote}')

        return []

class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text, Any]]:
        location = next(tracker.get_latest_entity_values("location"), None)

        if not location:
            dispatcher.utter_message("I'm sorry. I did not get that location")

        temp=weather(location)

        dispatcher.utter_message(f"The weather for today in {location}, is a high of {temp['high']} a low of {temp['low']}. \n The weather has a feel of {temp['feel']}, with a humidity level of {temp['humid']}.")

        return []

class StoreToDatabase(Action):

    def name(self) -> Text:
        return "action_store_to_database"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text, Any]]:
        names = tracker.get_slot('full_name')
        emails = tracker.get_slot('email_address')

        if not names:
            dispatcher.utter_message("I'm sorry, I didnt catch your name. Could you please repeat it")
        elif not emails:
           dispatcher.utter_message("I'm sorry, I didnt catch your e-mail. Could you please repeat it")
        
        store(names,emails)


        dispatcher.utter_message(f'Name {names} and email {emails} were both stored in the online database')

        return []