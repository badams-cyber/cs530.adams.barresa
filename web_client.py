import requests

def get_posts():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        posts = response.json()  # Parse the JSON response
        print("Retrieved Posts:")
        for post in posts:
            print(f"Title: {post['title']}")
    except requests.exceptions.HTTPError as http_err:
        handle_http_error(http_err)
    except Exception as err:
        print(f"An error occurred: {err}")

def post_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    sample_data = {
        "title": "Sample Title",
        "body": "This is a sample body.",
        "userId": 1
    }
    try:
        response = requests.post(url, json=sample_data)
        response.raise_for_status()  # Raise an error for bad responses
        print("Post successful!")
        print("Response data:", response.json())
    except requests.exceptions.HTTPError as http_err:
        handle_http_error(http_err)
    except Exception as err:
        print(f"An error occurred: {err}")

def handle_http_error(http_err):
    if http_err.response.status_code == 404:
        print("Error 404: Not Found.")
    elif http_err.response.status_code == 500:
        print("Error 500: Internal Server Error.")
    else:
        print(f"HTTP Error: {http_err}")

def main():
    print("Step 1: Making a GET request...")
    get_posts()
    print("\nStep 2: Making a POST request...")
    post_post()

if __name__ == "__main__":
    main()
