import requests
import json

class EventFinder:
    # Initialize the EventFinder class with the API key and the base URL for the Eventbrite API
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.eventbriteapi.com/v3/events/search/"

    def get_events(self, location):
        # Set the parameters for the API request, including the location
        params = {"location.address": location}
        # Set the headers for the API request, including the API key
        headers = {'Authorization': f"Bearer {self.api_key}"}

        try:
            # Send a GET request to the Eventbrite API, passing the URL, headers, and parameters
            response = requests.get(self.url, headers=headers, params=params)
            # Raise an exception if the HTTP response status is not successful
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)
            return
        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)
            return
        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)
            return
        except requests.exceptions.RequestException as err:
            print("An Unknown Error occurred", err)
            return

        # Get the JSON data from the API response
        data = response.json()

        # Loop through each event in the data and print relevant information
        for event in data['events']:
            print(f"Event Name: {event['name']['text']}")
            print(f"Start Date and Time: {event['start']['local']}")
            print(f"End Date and Time: {event['end']['local']}")
            print(f"Event Summary: {event['summary']}")
            print(f"Event URL: {event['url']}")
            print("----------------------------")

# Create an instance of the EventFinder class with your API key
event_finder = EventFinder("YOUR API KEY")
# Call the get_events method with the desired location (e.g. "New York") to retrieve events
event_finder.get_events("New York")
