
import PyPDF2
 
def split_pdf(input_pdf_path, output_directory, start_page, end_page):
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
 
        for page_number in range(start_page, end_page):
            output_pdf_path = f"{output_directory}/招待报销_{page_number + 1}.pdf"
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_number])
 
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)
 
# 使用示例
split_pdf('split-pdf\完整.PDF', 'output', 0, 5)