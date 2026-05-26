sent_message = 'Hey there! I need a fully automatic rifle.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'

    # Truncate the file to remove the original message
    file.truncate(0)
    file.write(unsent_message)