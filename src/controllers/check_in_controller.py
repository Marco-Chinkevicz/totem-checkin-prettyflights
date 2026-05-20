"""
Check-in Controller Module
Controlador da lógica de check-in
"""

class CheckInController:
    def __init__(self):
        self.passengers = []
    
    def register_passenger(self, name, flight_number):
        """Registra um passageiro no check-in"""
        passenger = {
            'name': name,
            'flight_number': flight_number,
            'checked_in': True
        }
        self.passengers.append(passenger)
        return passenger
    
    def get_check_in_status(self, flight_number):
        """Retorna status de check-in de um voo"""
        return [p for p in self.passengers if p['flight_number'] == flight_number]

if __name__ == "__main__":
    controller = CheckInController()
    print(controller.register_passenger("João Silva", "PF123"))