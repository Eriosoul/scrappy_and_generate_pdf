# scrappy_and_generate_pdf

# Project Overview

Welcome to our project! This repository demonstrates an application that utilizes a diverse directory structure to accomplish a specific task. The project involves a series of steps, starting with data collection using web scraping and culminating in the generation of PDFs based on the scraped information.

## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python and the required dependencies installed. You can set up a virtual environment to manage your dependencies if desired.
3. Navigate to the project directory in your terminal.

## Running the Application

1. Execute the `main.py` script to kickstart the application.
2. The `scrappy_directori` module will be invoked, collecting information via web scraping.
3. If the scraping process is successful, a JSON file will be generated containing the scraped data.
4. The JSON data will then be used to generate PDFs using the `generate_pdf_direct` module.

## Project Structure

The project directory structure is designed to efficiently handle different steps of the process:

- `main.py`: This is the starting point of the application. It orchestrates the flow by invoking the scraping and PDF generation processes.

- `templates/scrapp_direct`: Contains the code responsible for web scraping. The `scrapp.py` module extracts information from a specific website.

- `templates/generate_pdf_direct`: Holds the code for generating PDFs. The `generate_pdf.py` module uses the data collected through scraping to create PDF files.

## Dependencies

The application relies on the following libraries:

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For web scraping and parsing HTML.
- `reportlab`: For generating PDF documents.
- `python-dotenv`: For loading environment variables from a `.env` file.

## How It Works

1. The `main.py` script initializes the process by invoking the `scrapp_directori` module.
2. After successful scraping, a JSON file is generated containing the scraped data.
3. The JSON data is used as input for generating PDFs using the `generate_pdf_direct` module.

Please note that this is a simplified explanation. For a more detailed understanding of the project flow and functionality, refer to the code and comments within the files.

Feel free to explore, modify, and adapt the project to your needs!

## License

This project is licensed under the [MIT License](LICENSE). You are free to use and modify the code according to the terms of the license.

