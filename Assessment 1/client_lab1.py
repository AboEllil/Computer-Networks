import socket

class PaymentClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8000))

    def send_request(self, request):
        try:
            self.client_socket.send(request.encode("utf-8"))
            response = self.client_socket.recv(1024).decode("utf-8")
            print(f"Received response: {response}")

        except ConnectionAbortedError as e:
            print(f"Connection to the server was aborted: {e}")

    def close_connection(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = PaymentClient()
    while True:
        user_input = int(input("Enter a number (1 or 2): "))

        if user_input == 1:
            print("Choose an action:")
            print("1. CHECK_BALANCE")
            print("2. DEPOSIT <amount>")
            print("3. MAKE_PAYMENT <amount>")
            print("4. EXIT")
            break
        elif user_input == 2:
            print("1. CHECK_BALANCE2")
            print("2. DEPOSIT2 <amount>")
            print("3. MAKE_PAYMENT2 <amount>")
            print("4. EXIT")
            break
        else:
            print("Invalid input. Please enter either 1 or 2.")
            break  # Exit the loop on invalid input
        
    while True:
  
        user_input = input("Enter your choice: ").split(maxsplit=1)
        action = user_input[0].upper()

        if action == "EXIT":
            break

        if action in ["CHECK_BALANCE", "DEPOSIT", "MAKE_PAYMENT","MAKE_PAYMENT2","CHECK_BALANCE2","DEPOSIT2"]:
            if len(user_input) == 2:
                amount = user_input[1]
                request = f"{action} {amount}"
            else:
                request = action

            client.send_request(request)

        else:
            print("Invalid command. Please choose a valid action.")

    # Close connection
    client.close_connection()
