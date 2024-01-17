import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0 (by /u/your_username)'}

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        subreddit_info = response.json()

        # Extract and return the number of subscribers
        return subreddit_info['data']['subscribers']
    elif response.status_code == 404:
        # Invalid subreddit, return 0
        return 0
    else:
        # Handle other errors by printing the status code
        print(f"Error: {response.status_code}")
        return 0

# Example usage
subreddit_name = 'python'
subscribers = number_of_subscribers(subreddit_name)

if subscribers != 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print(f"Invalid subreddit: '{subreddit_name}'.")
