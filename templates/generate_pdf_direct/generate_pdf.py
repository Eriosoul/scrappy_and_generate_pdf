from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from dotenv import load_dotenv
import os
import json


class Generate_pdf:
    def __init__(self):
        load_dotenv()
        self.json_path = os.getenv("JSON_PATH")
        self.output_folder = os.getenv("OUTPUT_FOLDER")

    def load_json(self):
        with open(self.json_path, "r") as json_file:
            quotes_list = json.load(json_file)
            return quotes_list

    def check_directory(self):
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_pdf(self, quotes_list=None):
        # Generar archivos PDF y guardarlos en la carpeta especificada
        for index, quote in enumerate(quotes_list):
            pdf_path = os.path.join(self.output_folder,
                                    f"quote_{index + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")

            pdf = canvas.Canvas(pdf_path, pagesize=A4)
            width, height = A4
            x = 50
            y = height - 50
            quote_text = list(quote.values())[0]
            quote_lines = quote_text.split("\n")

            for line in quote_lines:
                pdf.setFont("Helvetica", 16)
                pdf.drawString(x, y, line)
                y -= 20

            pdf.setFont("Helvetica-Bold", 14)
            pdf.setFillColorRGB(1, 0, 0)
            pdf.save()

        print("PDFs generated and saved in 'pdf_generados' folder")
