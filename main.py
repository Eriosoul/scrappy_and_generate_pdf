from templates.scrapp_direct.scrapp import Scrappy
from templates.generate_pdf_direct.generate_pdf import Generate_pdf

if __name__ == '__main__':
    scrp = Scrappy()  # Crear una instancia de la clase Scrapp
    pdf_generator = Generate_pdf()
    scrappy_result = scrp.get_scrappy()  # Llamar al método scrapp() de la instancia
    if scrappy_result:
        quotes_list = pdf_generator.load_json()  # Llamada a load_json() y captura del valor devuelto

        output_folder = pdf_generator.check_directory()  # Llamada a check_directory() y captura del valor devuelto

        pdf_generator.generate_pdf(quotes_list)
    else:
        print("Error in scrapping progress")
