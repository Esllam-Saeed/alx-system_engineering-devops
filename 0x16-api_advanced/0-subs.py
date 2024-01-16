import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'CustomUserAgent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # The subreddit does not exist, return 0
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = number_of_subscribers(subreddit_name)
        print(f"{result}")
