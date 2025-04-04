from locust import HttpUser, task, between
import json

class ChatUser(HttpUser):
    host = "https://v2.customizeyourfood.com"
    wait_time = between(1, 3)  # Wait time between actions

    # Assign the user ID (chatId) here
    user_id = "vimal"  # Example user ID, change it dynamically for multiple users
    cookies = {}
    csrf_token = ""

    @task
    def send_message(self):
        """Simulate sending a chat message."""
        # Prepare the message payload
        payload = {
            "chatId": self.user_id,  # User ID
            "message": "hello"
        }

        # Ensure CSRF token is available in headers
        headers = {
            "X-CSRF-TOKEN": self.csrf_token
        }

        # Send the message with cookies for session persistence
        response = self.client.post(f"/admin/chat/send", json=payload, cookies=self.cookies, headers=headers)

        # If needed, you can log the response for debugging
        if response.status_code == 200:
            print(f"Message sent successfully: {response.text}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")

    @task
    def fetch_messages(self):
        """Simulate fetching messages."""
        response = self.client.get(f"/admin/chat/vimal", cookies=self.cookies)

        # Check if the request was successful
        if response.status_code == 200:
            try:
                messages = response.json()
                for message in messages:
                    username = message.get("username", "Unknown")
                    message_text = message.get("message", "No message")
                    print(f"New Message: {username}: {message_text}")
            except Exception as e:
                print(f"Error parsing messages: {e}")
        else:
            print(f"Failed to fetch messages. Status code: {response.status_code}")

    def on_start(self):
        """Runs when a simulated user starts."""
        # Get the CSRF token from the initial GET request (first request before sending messages)
        response = self.client.get(f"/admin/chat/{self.user_id}")
        if response.status_code == 200:
            # Extract the CSRF token and session cookies from the response
            self.csrf_token = response.cookies.get("XSRF-TOKEN", "")
            self.cookies = response.cookies
            print(f"Session started with CSRF token: {self.csrf_token}")
        else:
            print("Failed to initialize session.")
