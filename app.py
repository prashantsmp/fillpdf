from fillpdf import fillpdfs
import datetime

pdf_file_template_path = "./template.pdf"
pdf_file_output_path = "./generated_templated.pdf"

def generate_pdf_from_data(title, description):
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
        print(e)
        
    

if __name__ == "__main__":
    generate_pdf_from_data(title= "", description= "")