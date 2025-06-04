import json
import csv
import io


class ReportGenerator:
    def __init__(self):
        self.report_data = []

    def set_data(self, data):

        self.report_data = data

    def report_format_decorator(self, format_type):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if format_type == "text":
                    print("Формат отчета: Текстовый")
                    result = func(*args, **kwargs)
                    print(result)
                elif format_type == "json":
                    print("Формат отчета: JSON")
                    result = func(*args, **kwargs)
                    print(json.dumps(result, indent=4, ensure_ascii=False))
                elif format_type == "csv":
                    print("Формат отчета: CSV")
                    result = func(*args, **kwargs)
                    output = io.StringIO()
                    writer = csv.writer(output)
                    writer.writerow(["Организация", "Отчет"])
                    for row in result:
                        writer.writerow(row)
                    print(output.getvalue())
                return result
            return wrapper
        return decorator

    def generate_report_text(self):
        """Генерирует текстовый отчет."""
        @self.report_format_decorator("text")
        def report():
            return "\n".join(f"Организация: {item['name']}, Отчет: {item['report']}" for item in self.report_data)
        return report()

    def generate_report_json(self):
        """Генерирует отчет в формате JSON."""
        @self.report_format_decorator("json")
        def report():
            return [{"name": item['name'], "report": item['report']} for item in self.report_data]
        return report()

    def generate_report_csv(self):
        """Генерирует отчет в формате CSV."""
        @self.report_format_decorator("csv")
        def report():
            return [(item['name'], item['report']) for item in self.report_data]
        return report()

    def __del__(self):
        pass

    def __str__(self):
        return f"Отчет предоставлен {len(self.report_data)} фирмам."


if __name__ == "__main__":
    report_generator = ReportGenerator()
    report_data = [
        {"name": "Организация 1", "report": "Отчет за 2024 год"},
        {"name": "Организация 2", "report": "Отчет за 2024 год"},
    ]
    report_generator.set_data(report_data)

    report_generator.generate_report_text()
    report_generator.generate_report_json()
    report_generator.generate_report_csv()
    print(report_generator)
