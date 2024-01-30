import socket
import threading

class PaymentServer:
    def __init__(self):
        self.client_accounts = {"001": 10000.0, "002": 20000.0}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", 8000))
        self.server_socket.listen(10)

    def start(self):
        print("Server listening on port 8000...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

    def handle_client(self, client_socket, client_address):
        print(f"Accepted connection from {client_address}")
        try:
            while True:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    break

                response = self.process_request(data)
                client_socket.send(response.encode("utf-8"))

        except Exception as e:
            print(f"Error handling client {client_address}: {e}")

        finally:
            print(f"Connection from {client_address} closed.")
            client_socket.close()

    def process_request(self, request):
        parts = request.split()
        command = parts[0]

        if command == "DEPOSIT":
            amount = float(parts[1])
            new_balance = self.deposit("001", amount)  # Assuming a fixed client ID for simplicity
            return f"Deposit of {amount} successfully processed. New balance: {new_balance}"

        elif command == "CHECK_BALANCE":
            balance = self.check_balance("001")  # Assuming a fixed client ID for simplicity
            return f"Your current balance: {balance}"

        elif command == "MAKE_PAYMENT":
            amount = float(parts[1])
            if self.make_payment("001", amount):  # Assuming a fixed client ID for simplicity
                return f"Payment of {amount} accepted. New balance: {self.client_accounts['001']}"
            else:
                return "Insufficient balance. Payment failed."
#
        if command == "DEPOSIT2":
            amount = float(parts[1])
            new_balance = self.deposit("002", amount)  # Assuming a fixed client ID for simplicity
            return f"Deposit of {amount} successfully processed. New balance: {new_balance}"

        elif command == "CHECK_BALANCE2":
            balance = self.check_balance("002")  # Assuming a fixed client ID for simplicity
            return f"Your current balance: {balance}"

        elif command == "MAKE_PAYMENT2":
            amount = float(parts[1])
            if self.make_payment("002", amount):  # Assuming a fixed client ID for simplicity
                return f"Payment of {amount} accepted. New balance: {self.client_accounts['002']}"
            else:
                return "Insufficient balance. Payment failed."

        else:
            return "Invalid command"

    def deposit(self, client_id, amount):
        if client_id in self.client_accounts:
            self.client_accounts[client_id] += amount
            return self.client_accounts[client_id]
        else:
            raise ValueError("Invalid client ID")

    def check_balance(self, client_id):
        return str(self.client_accounts.get(client_id, 0))

    def make_payment(self, client_id, amount):
        if client_id in self.client_accounts and self.client_accounts[client_id] >= amount:
            self.client_accounts[client_id] -= amount
            return True
#
    def deposit2(self, client_id, amount):
          if client_id in self.client_accounts:
            self.client_accounts[client_id] += amount
            return self.client_accounts[client_id]
          else:
            raise ValueError("Invalid client ID")

    def check_balance2(self, client_id):
        return str(self.client_accounts.get(client_id, 0))

    def make_payment2(self, client_id, amount):
        if client_id in self.client_accounts and self.client_accounts[client_id] >= amount:
            self.client_accounts[client_id] -= amount
            return True
        else:
            return False
        


if __name__ == "__main__":
    server = PaymentServer()
    server.start()


