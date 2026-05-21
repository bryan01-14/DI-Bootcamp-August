class Phone:
    """A class to represent a phone."""

    def __init__(self, phone_number):
        """Initialize a new Phone instance."""
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        """Call another phone and record the call in history."""
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    def show_call_history(self):
        """Print the call history."""
        for record in self.call_history:
            print(record)

    def send_message(self, other_phone, content):
        """Send a message to another phone."""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        """Print all outgoing messages."""
        print(f"Outgoing messages from {self.phone_number}:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"  To: {message['to']} | Content: {message['content']}")

    def show_incoming_messages(self):
        """Print all incoming messages."""
        print(f"Incoming messages for {self.phone_number}:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"  From: {message['from']} | Content: {message['content']}")

    def show_messages_from(self, other_phone):
        """Print all messages received from a specific phone."""
        print(f"Messages from {other_phone.phone_number} to {self.phone_number}:")
        for message in self.messages:
            if message["from"] == other_phone.phone_number and message["to"] == self.phone_number:
                print(f"  Content: {message['content']}")


def main():
    """Main function to test the Phone class."""
    # Create phone objects
    phone1 = Phone("123-456-7890")
    phone2 = Phone("987-654-3210")
    phone3 = Phone("555-555-5555")

    # Test call
    phone1.call(phone2)
    phone1.call(phone3)
    phone2.call(phone1)

    # Test show_call_history
    print("\n--- Call History ---")
    phone1.show_call_history()

    # Test send_message
    print("\n--- Sending Messages ---")
    phone1.send_message(phone2, "Hey, how are you?")
    phone1.send_message(phone2, "Are you free today?")
    phone2.send_message(phone1, "I'm good! Yes, I'm free.")
    phone3.send_message(phone1, "Hello from phone3!")

    # Test show_outgoing_messages
    print("\n--- Outgoing Messages (phone1) ---")
    phone1.show_outgoing_messages()

    # Test show_incoming_messages
    print("\n--- Incoming Messages (phone1) ---")
    phone1.show_incoming_messages()

    # Test show_messages_from
    print("\n--- Messages from phone2 to phone1 ---")
    phone1.show_messages_from(phone2)


if __name__ == "__main__":
    main()