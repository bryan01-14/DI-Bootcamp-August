

# Exercice 1 : Historique des appels
# Instructions
# Créez une classe appelée . Cette classe prend un paramètre appelé . Lors de l’instanciation d’un objet, créez un attribut appelé dont la valeur est une liste vide.Phonephone_numbercall_history

# Ajoutez une méthode appelée qui prend à la fois et (c’est-à-dire un autre objet) comme paramètres. La méthode doit imprimer une chaîne indiquant qui a appelé qui, et ajouter cette chaîne à la chaîne du téléphone.callselfother_phonePhonecall_history

# Ajoutez une méthode appelée . Cette méthode devrait imprimer le fichier .show_call_historycall_history

# Ajoutez un autre attribut appelé à votre méthode dont la valeur est une liste vide.messages__init__()

# Créez une méthode appelée qui est similaire à la méthode. Chaque message doit être enregistré sous forme de dictionnaire avec les clés suivantes :send_messagecall
# à : le nombre d’un autre objetPhone
# De : votre numéro de téléphone (également un objet)Phone
# Contenu

# Créez les méthodes suivantes : , , show_outgoing_messages(self)show_incoming_messages(self)show_messages_from(self)

# Testez votre code !!
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_record = f"{self.phone_number} a appelé {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)    
        other_phone.call_history.append(call_record)    
    def show_call_history(self):
        print(f"Historique des appels pour {self.phone_number} :")
        for call in self.call_history:
            print(call)    
    def send_message(self, other_phone, content):
        message_record = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message_record)
        other_phone.messages.append(message_record)
    def show_outgoing_messages(self):
        print(f"Messages sortants pour {self.phone_number} :")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"À {message['to']} : {message['content']}")
    def show_incoming_messages(self):
        print(f"Messages entrants pour {self.phone_number} :")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"De {message['from']} : {message['content']}")   
    def show_messages_from(self, other_phone):  
        print(f"Messages de {other_phone.phone_number} pour {self.phone_number} :")
        for message in self.messages:
            if message["from"] == other_phone.phone_number and message["to"] == self.phone_number:
                print(f"De {message['from']} : {message['content']}")
# Testez votre code !!
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")
phone1.call(phone2)
phone2.call(phone1)
phone1.send_message(phone2, "Salut !")
phone2.send_message(phone1, "Bonjour !")
phone1.show_call_history()
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)   
