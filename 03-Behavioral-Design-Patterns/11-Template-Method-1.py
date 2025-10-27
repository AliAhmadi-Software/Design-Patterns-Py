from abc import ABC, abstractmethod

class Feature(ABC):
    def execute(self):
        # سایر عملیات فیچر اینجا تعریف می‌شود
        self.export_to_xml()

    @abstractmethod
    def export_to_xml(self):
        pass

class UserFeature(Feature):
    def export_to_xml(self):
        print("Exporting user data to XML...")

class ProductFeature(Feature):
    def export_to_xml(self):
        print("Exporting product data to XML...")