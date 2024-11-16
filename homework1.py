
class Orders:
    def __init__(self):
        self.__operator = "yucant3@gmail.com, Denis"

    json_data = {
        "state": 0,
        "data": [
            {
                "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
                "count": 1,
                "brand_id": 84375,
                "delay": 1,
                "startedAt": "2024-03-21T16:48:03.513Z",
                "completedAt": "2024-03-21T16:48:03.513Z",
                "completed": 0,
                "wait_refund": 0,
                "refunded": 0
            },
            {
                "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
                "count": 2,
                "brand_id": 88339,
                "delay": 2,
                "startedAt": "2024-03-21T16:27:32.062Z",
                "completedAt": "2024-03-21T16:28:32.062Z",
                "completed": 0,
                "wait_refund": 2,
                "refunded": 0
            },
            {
                "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
                "count": 16,
                "brand_id": 88339,
                "delay": 3,
                "startedAt": "2024-03-21T16:17:04.723Z",
                "completedAt": "2024-03-21T16:17:04.723Z",
                "completed": 7,
                "wait_refund": 3,
                "refunded": 6
            }
        ]
    }

    def orders_is_not_null(self):
        print("Заказы отсутствуют!!!") if len(self.json_data["data"]) > 0 else print("Все ок")

    def work_duration_orders(self):
        from datetime import datetime

        first_order_started_at = datetime.strptime(self.json_data["data"][0]["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        first_order_completed_at = datetime.strptime(self.json_data["data"][0]["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        second_order_started_at = datetime.strptime(self.json_data["data"][1]["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        second_order_completed_at = datetime.strptime(self.json_data["data"][1]["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

        first_order_duration_time = (first_order_completed_at - first_order_started_at).total_seconds() / 3600
        second_order_duration_time = (second_order_completed_at - second_order_started_at).total_seconds() / 3600

        if first_order_duration_time >= 6:
            print(f"Время выполнения первого заказа превышает 6 часов: {first_order_duration_time:.2f} часов")
        if second_order_duration_time >= 6:
            print(f"Время выполнения второго заказа превышает 6 часов: {second_order_duration_time:.2f} часов")
        if first_order_duration_time < 6 and second_order_duration_time < 6:
            print("Время выполнения первого и второго заказов укладывается в 6 часов.")

    def third_order(self):
        total_service_count = self.json_data["data"][2]["count"]
        completed_services = self.json_data["data"][2]["completed"]
        wait_refund_services = self.json_data["data"][2]["wait_refund"]
        refunded_services = self.json_data["data"][2]["refunded"]

        if completed_services < (total_service_count / 2):
            print("Ошибка: выполнено меньше половины всех услуг!")
        if not (completed_services > refunded_services > wait_refund_services):
            print("Ошибка: нарушено соотношение выполненных, возвращенных и ожидающих возврат услуг!")

    def create_ids_list(self):
        ids_list = [ids["_id"] for ids in self.json_data["data"]]
        ids_list.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")
        return ids_list

    def summarize_services(self):
        services_summ = {
            "total_completed": sum(order["completed"] for order in self.json_data["data"]),
            "total_refunded": sum(order["refunded"] for order in self.json_data["data"]),
            "total_wait_refund": sum(order["wait_refund"] for order in self.json_data["data"])
        }
        return services_summ

    def create_report(self):
        print({"author": self.__operator, "_ids": self.create_ids_list(), "services_summ": self.summarize_services()})


orders = Orders()
orders.create_report()