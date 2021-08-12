from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumptions: {total_consumption:0.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            new_budget = room.budget
            if room.budget >= (room.expenses + room.room_cost):
                new_budget -= (room.expenses + room.room_cost)
                result += f"{room.family_name} paid {room.expenses + room.room_cost:0.2f}$ and have {new_budget:0.2f}$ left.\n"
                room.budget = new_budget
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return result.strip()

    def status(self):
        result = ''
        all_people_in_the_hotel = 0
        for room in self.rooms:
            all_people_in_the_hotel += room.members_count
        result += f'Total population: {all_people_in_the_hotel}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:0.2f}$, Expenses: {room.expenses:0.2f}$\n'
            if room.children:
                for n, child in enumerate(room.children):
                    result += f'--- Child {n+1} monthly cost: {child.get_monthly_expense():0.2f}$\n'
            cost_of_all_appliances_for_one_month = 0
            for appliance in room.appliances:
                cost_of_all_appliances_for_one_month += appliance.get_monthly_expense()
            result += f'--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:0.2f}$\n'
        return result.strip()
