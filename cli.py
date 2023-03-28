class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_person)
        self.add_command("read", self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_person(self):
        titulo = input("Enter the title: ")
        autor =  input("Enter the autor: ")
        ano = int(input("Enter the year: "))
        preco = float(input("Enter the price:"))
        self.person_model.create_person(titulo, autor,ano,preco)

    def read_person(self):
        id = input("Enter the id: ")
        person = self.person_model.read_person_by_id(id)
        if person:
            print(f"Titulo: {person['titulo']}")
            print(f"autor: {person['autor']}")
            print(f"ano: {person['ano']}")
            print(f"preco: {person['preco']}")

    def update_person(self):
        id = input("Enter the id: ")
        titulo = input("Enter the new title: ")
        autor = input("Enter the new autor: ")
        ano = int(input("Enter the new year: "))
        preco = float(input("Enter the new price:"))
        self.person_model.update_person(id, titulo, autor,ano,preco)

    def delete_person(self):
        id = input("Enter the id: ")
        self.person_model.delete_person(id)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
