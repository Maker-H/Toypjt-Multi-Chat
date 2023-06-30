import socket
import threading
import tkinter as tk

class ChatClient:
    def __init__(self, host, port):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

        self.init_ui()
        self.connect_to_server()

    def init_ui(self):
        self.root = tk.Tk()
        self.root.title("Chat Client")

        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    def connect_to_server(self):
        try:
            self.client_sock.connect((self.host, self.port))
            self.output_text.insert(tk.END, "Connected to {}:{}".format(self.host, self.port) + "\n")

            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.start()

        except Exception as e:
            self.output_text.insert(tk.END, "Connection failed: " + str(e) + "\n")

    def send_message(self):
        message = self.input_entry.get()
        self.output_text.insert(tk.END, "me >> " + message + "\n")

        self.input_entry.delete(0, tk.END)
        if message == "exit":
            self.client_sock.close()
            self.root.quit()
            return
        send_data = message.encode()
        self.client_sock.send(send_data)

    def receive_messages(self):
        while True:
            try:
                recv_data = self.client_sock.recv(1024).decode()
                if not recv_data:
                    break
                self.output_text.insert(tk.END, recv_data + "\n")
            except Exception as e:
                print(e)
                break

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    host = 'localhost'
    port = 9000

    client = ChatClient(host, port)
    client.run()
