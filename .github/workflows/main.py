from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label


KV = '''
#:import dp kivy.metrics.dp

ScreenManager:
    HomeScreen:
    AddPhoneScreen:
    InventoryScreen:
    AddCustomerScreen:
    CustomersScreen:

<HomeScreen>:
    name: "home"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        Label:
            text: "دکتر موبایل"
            font_size: dp(28)
            bold: True
            size_hint_y: None
            height: dp(60)

        Label:
            text: "سیستم مدیریت فروشگاه"
            font_size: dp(18)
            size_hint_y: None
            height: dp(40)

        Button:
            text: "📱 ورود گوشی"
            font_size: dp(18)
            on_release: app.root.current = "add_phone"

        Button:
            text: "📦 موجودی"
            font_size: dp(18)
            on_release: app.root.current = "inventory"

        Button:
            text: "👤 ثبت درخواست مشتری"
            font_size: dp(18)
            on_release: app.root.current = "add_customer"

        Button:
            text: "📋 درخواست‌های مشتریان"
            font_size: dp(18)
            on_release: app.root.current = "customers"


<AddPhoneScreen>:
    name: "add_phone"

    ScrollView:
        BoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            Label:
                text: "ورود گوشی به مغازه"
                font_size: dp(24)
                size_hint_y: None
                height: dp(50)

            TextInput:
                id: seller_name
                hint_text: "نام فروشنده / مالک"

            TextInput:
                id: seller_phone
                hint_text: "شماره تماس فروشنده"
                input_type: "number"

            TextInput:
                id: brand
                hint_text: "برند"

            TextInput:
                id: model
                hint_text: "مدل گوشی"

            TextInput:
                id: storage
                hint_text: "حافظه (مثلاً 128GB)"

            TextInput:
                id: color
                hint_text: "رنگ"

            TextInput:
                id: imei
                hint_text: "IMEI"

            TextInput:
                id: registration
                hint_text: "وضعیت رجیستری"

            TextInput:
                id: ownership
                hint_text: "وضعیت مالکیت / انتقال"

            TextInput:
                id: condition
                hint_text: "وضعیت ظاهری و فنی"

            TextInput:
                id: accessories
                hint_text: "جعبه و لوازم همراه"

            TextInput:
                id: battery
                hint_text: "سلامت باتری (در صورت وجود)"

            TextInput:
                id: repairs
                hint_text: "تعمیرات / قطعات تعویض شده"

            TextInput:
                id: purchase_price
                hint_text: "قیمت خرید"
                input_type: "number"

            Button:
                text: "ثبت گوشی"
                size_hint_y: None
                height: dp(55)
                on_release: root.save_phone()

            Button:
                text: "بازگشت"
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = "home"


<InventoryScreen>:
    name: "inventory"

    BoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)

        Label:
            text: "موجودی گوشی‌ها"
            font_size: dp(24)
            size_hint_y: None
            height: dp(50)

        ScrollView:
            Label:
                id: inventory_text
                text: "در حال بارگذاری..."
                text_size: self.width, None
                halign: "right"
                valign: "top"
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "بازگشت"
            size_hint_y: None
            height: dp(50)
            on_release: app.root.current = "home"


<AddCustomerScreen>:
    name: "add_customer"

    BoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)

        Label:
            text: "درخواست گوشی مشتری"
            font_size: dp(24)
            size_hint_y: None
            height: dp(50)

        TextInput:
            id: customer_name
            hint_text: "نام مشتری"

        TextInput:
            id: customer_phone
            hint_text: "شماره تماس"
            input_type: "number"

        TextInput:
            id: requested_model
            hint_text: "مدل مورد درخواست"

        TextInput:
            id: requested_storage
            hint_text: "حافظه"

        TextInput:
            id: budget
            hint_text: "حداکثر بودجه"
            input_type: "number"

        TextInput:
            id: desired_condition
            hint_text: "شرایط موردنظر"

        TextInput:
            id: notes
            hint_text: "توضیحات"

        Button:
            text: "ثبت درخواست"
            size_hint_y: None
            height: dp(55)
            on_release: root.save_customer()

        Button:
            text: "بازگشت"
            size_hint_y: None
            height: dp(50)
            on_release: app.root.current = "home"


<CustomersScreen>:
    name: "customers"

    BoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)

        Label:
            text: "درخواست‌های مشتریان"
            font_size: dp(24)
            size_hint_y: None
            height: dp(50)

        ScrollView:
            Label:
                id: customers_text
                text: "در حال بارگذاری..."
                text_size: self.width, None
                halign: "right"
                valign: "top"
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "بازگشت"
            size_hint_y: None
            height: dp(50)
            on_release: app.root.current = "home"
'''


class HomeScreen(Screen):
    pass


class AddPhoneScreen(Screen):

    def save_phone(self):
        app = App.get_running_app()

        phone = {
            "seller_name": self.ids.seller_name.text,
            "seller_phone": self.ids.seller_phone.text,
            "brand": self.ids.brand.text,
            "model": self.ids.model.text,
            "storage": self.ids.storage.text,
            "color": self.ids.color.text,
            "imei": self.ids.imei.text,
            "registration": self.ids.registration.text,
            "ownership": self.ids.ownership.text,
            "condition": self.ids.condition.text,
            "accessories": self.ids.accessories.text,
            "battery": self.ids.battery.text,
            "repairs": self.ids.repairs.text,
            "purchase_price": self.ids.purchase_price.text,
            "status": "موجود",
        }

        if not phone["model"]:
            app.show_message("خطا", "حداقل مدل گوشی را وارد کنید.")
            return

        key = str(app.next_phone_id)
        app.store.put("phone_" + key, **phone)
        app.next_phone_id += 1
        app.store.put("settings", next_phone_id=app.next_phone_id)

        self.clear_form()
        app.show_message("ثبت شد", "گوشی با موفقیت ثبت شد.")
        app.root.current = "inventory"

    def clear_form(self):
        for field in [
            "seller_name",
            "seller_phone",
            "brand",
            "model",
            "storage",
            "color",
            "imei",
            "registration",
            "ownership",
            "condition",
            "accessories",
            "battery",
            "repairs",
            "purchase_price",
        ]:
            self.ids[field].text = ""


class InventoryScreen(Screen):

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        app = App.get_running_app()
        phones = []

        for key in app.store.keys():
            if key.startswith("phone_"):
                phones.append(app.store.get(key))

        if not phones:
            self.ids.inventory_text.text = "موجودی ثبت‌شده‌ای وجود ندارد."
            return

        lines = []

        for index, phone in enumerate(phones, 1):
            lines.append(
                f"{index}. {phone.get('brand', '')} "
                f"{phone.get('model', '')} "
                f"{phone.get('storage', '')}\n"
                f"IMEI: {phone.get('imei', '')}\n"
                f"خرید: {phone.get('purchase_price', '')}\n"
                f"وضعیت: {phone.get('status', '')}\n"
                f"-------------------------"
            )

        self.ids.inventory_text.text = "\n".join(lines)


class AddCustomerScreen(Screen):

    def save_customer(self):
        app = App.get_running_app()

        customer = {
            "name": self.ids.customer_name.text,
            "phone": self.ids.customer_phone.text,
            "model": self.ids.requested_model.text,
            "storage": self.ids.requested_storage.text,
            "budget": self.ids.budget.text,
            "condition": self.ids.desired_condition.text,
            "notes": self.ids.notes.text,
        }

        if not customer["phone"] or not customer["model"]:
            app.show_message(
                "خطا",
                "شماره تماس و مدل مورد درخواست را وارد کنید."
            )
            return

        key = str(app.next_customer_id)
        app.store.put("customer_" + key, **customer)

        app.next_customer_id += 1
        app.store.put(
            "settings",
            next_phone_id=app.next_phone_id,
            next_customer_id=app.next_customer_id
        )

        self.clear_form()
        app.show_message("ثبت شد", "درخواست مشتری ثبت شد.")
        app.root.current = "customers"

    def clear_form(self):
        for field in [
            "customer_name",
            "customer_phone",
            "requested_model",
            "requested_storage",
            "budget",
            "desired_condition",
            "notes",
        ]:
            self.ids[field].text = ""


class CustomersScreen(Screen):

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        app = App.get_running_app()
        customers = []

        for key in app.store.keys():
            if key.startswith("customer_"):
                customers.append(app.store.get(key))

        if not customers:
            self.ids.customers_text.text = "درخواستی ثبت نشده است."
            return

        lines = []

        for index, customer in enumerate(customers, 1):
            lines.append(
                f"{index}. {customer.get('name', '')}\n"
                f"تماس: {customer.get('phone', '')}\n"
                f"مدل: {customer.get('model', '')}\n"
                f"حافظه: {customer.get('storage', '')}\n"
                f"بودجه: {customer.get('budget', '')}\n"
                f"شرایط: {customer.get('condition', '')}\n"
                f"توضیحات: {customer.get('notes', '')}\n"
                f"-------------------------"
            )

        self.ids.customers_text.text = "\n".join(lines)


class DoctorMobileApp(App):

    def build(self):
        self.store = JsonStore("doctor_mobile.json")

        if self.store.exists("settings"):
            settings = self.store.get("settings")
            self.next_phone_id = settings.get("next_phone_id", 1)
            self.next_customer_id = settings.get("next_customer_id", 1)
        else:
            self.next_phone_id = 1
            self.next_customer_id = 1
            self.store.put(
                "settings",
                next_phone_id=1,
                next_customer_id=1
            )

        return Builder.load_string(KV)

    def show_message(self, title, message):
        Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3)
        ).open()


if __name__ == "__main__":
    DoctorMobileApp().run()