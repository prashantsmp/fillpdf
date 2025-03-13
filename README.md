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

https://eur02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fanaconda.cloud%2Fapi%2Fiam%2Femail%2Fverified%2F600ea48a-3ea5-4d4b-accb-8dbb0ec419a8&data=05%7C02%7Cprasanth.mathavan%40dewa.gov.ae%7C3eba86097a6b4647edd108dd61e503be%7Ca1104cac3f3e4e9da251a93724b1727b%7C0%7C0%7C638774358925749349%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C80000%7C%7C%7C&sdata=%2FN74LOnu7jT9OrXXYVg56a65rdqcipPqox1Yl3Ks9QE%3D&reserved=0
