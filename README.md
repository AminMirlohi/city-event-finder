# city-event-finder

EventFinder is a Python program that uses the Eventbrite API to find events of a specific city. It takes the name of the city as input and returns information about the events happening in that city.

## Prerequisites

To use this program, you need to have the following:

- Python 3 installed on your system
- Eventbrite API key

## Installation

1. Clone the GitHub repository to your local machine or download the zip file and extract it.

2. Make sure you have Python 3 installed. You can check the version of Python installed on your system by running the following command:

   ```shell
   python --version
   ```

3. Install the required dependencies by navigating to the project directory and running the following command:

   ```shell
   pip install -r requirements.txt
   ```

4. Replace `YOUR API KEY` in the code with your Eventbrite API key. If you don't have an API key, you can obtain one by signing up on the Eventbrite website.

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the Python script by executing the following command:

   ```shell
   python event_finder.py
   ```

3. You will be prompted to enter the name of the city for which you want to find events. Enter the city name and press Enter.

4. The program will make a request to the Eventbrite API and display information about the events happening in the specified city. The information includes the event name, start date and time, end date and time, event summary, and the event URL.

5. The program will continue running until you choose to exit by pressing Ctrl+C.

## API Key

To use the Eventbrite API, you need to obtain an API key. You can sign up on the Eventbrite website and create a new API key in your account settings. Replace `YOUR API KEY` in the code with your actual API key.

## Contributing

If you find any issues with the program or would like to contribute to its development, feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details. 
