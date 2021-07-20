class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.subscriptions = []
        self.plans = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_subscription(self, subscriptions):
        if subscriptions not in self.subscriptions:
            self.subscriptions.append(subscriptions)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def subscription_info(self, subscription_id):
        subscription = self.get_object(subscription_id, self.subscriptions)
        customer_id = subscription.customer_id
        customer = self.get_object(customer_id, self.customers)
        trainer_id = subscription.trainer_id
        trainer = self.get_object(trainer_id, self.trainers)
        exercise_id = subscription.exercise_id
        plan = self.get_object(exercise_id, self.plans)
        equipment_id = plan.equipment_id
        equipment = self.get_object(equipment_id, self.equipment)
        return f'{subscription}\n{customer}\n{trainer}\n{plan}\n{equipment}'

    @staticmethod
    def get_object(oid, cl_iterable):
        return list(filter(lambda x: x.id == oid, cl_iterable))[0]
