"""
Check-in Interface Module
Módulo responsável pela interface do totem de check-in
"""

class CheckInInterface:
    def __init__(self):
        self.title = "PrettyFlights Check-in"
        self.version = "1.0.0"
    
    def display_welcome(self):
        """Exibe mensagem de boas-vindas"""
        return f"Bem-vindo ao {self.title}"
    
    def get_passenger_info(self):
        """Coleta informações do passageiro"""
        pass
    
    def display_boarding_pass(self):
        """Exibe cartão de embarque"""
        pass

if __name__ == "__main__":
    interface = CheckInInterface()
    print(interface.display_welcome())