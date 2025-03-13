# Dynamic PDF Generation with Python

## Introduction

This Python script leverages the `fillpdfs` library to create customized PDF documents by dynamically filling a PDF template with specified data. It's a powerful tool for automating PDF generation workflows.

Create Fillable PDF online using https://www.sejda.com/pdf-forms

## Code Implementation

```python
from fillpdf import fillpdfs
import datetime

pdf_file_template_path = "./template.pdf"
pdf_file_output_path = "./generated_templated.pdf"

def generate_pdf_from_data(title, description):
    """
    Generates a PDF document from a template with provided title and description.

    Args:
        title (str): The title to be inserted into the PDF.
        description (str): The description to be inserted into the PDF.

    """

    # Automatically generate the current date in the desired format (MM/DD/YYYY)
    x = datetime.datetime.now()
    date_str = x.strftime("%m/%d/%Y")

    data_dict = {
        'date': date_str,
        'title': title,
        'description': description
    }

    try:
        fillpdfs.write_fillable_pdf(pdf_file_template_path, pdf_file_output_path, data_dict, flatten=True)
    except Exception as e:
        print(f"An error occurred: {e}")  # Improved error handling

if __name__ == "__main__":
    generate_pdf_from_data(title="", description="")

```

### 'date', 'title', 'description' are ids of the template.pdf