'''
Visitor

Separates the operations / behaviours from the data structures that need them. The 'visitor' holds the operation, potentially with different implementations for all the different data structures that will use them. The data structures can then plug-in, or 'accept' the visitor, and call the relevant behaviour on the visitor object itself(delegate to the visitor to complete the action).

Pros:
- Allows you to add new operations without having to change the many similar but different classes that use them.
- Definitions for an operation type can all be found in the same place, making it easier to find and modify the code.

An example could be in document processing. There are many different types of document, which share the same type of processes but implement them in ways unique to the data structure. The visitor pattern allows all implementations of the same operation to be defined in a visitor class. The document types then onboard the visitor object and call the correct implementation on the visitor.
'''


class DocumentVisitor:
    def visit_pdf(self, pdf_document):
        pass

    def visit_word(self, word_document):
        pass

    def visit_excel(self, excel_document):
        pass


class PDFDocument:
    def accept(self, visitor):
        visitor.visit_pdf(self)
        # Calls the PDF implementation of whatever operation the visitor completes.


class WordDocument:
    def accept(self, visitor):
        visitor.visit_word(self)
        # Calls the Word implementation of whatever operation the visitor completes.


class ExcelDocument:
    def accept(self, visitor):
        visitor.visit_excel(self)
        # Calls the Excel implementation of whatever operation the visitor completes.


class TextExtractorVisitor(DocumentVisitor):
    def visit_pdf(self, pdf_document):
        print("Extracting text from PDF document")

    def visit_word(self, word_document):
        print("Extracting text from Word document")

    def visit_excel(self, excel_document):
        print("Extracting text from Excel document")


class StatisticsVisitor(DocumentVisitor):
    def visit_pdf(self, pdf_document):
        print("Generating statistics for PDF document")

    def visit_word(self, word_document):
        print("Generating statistics for Word document")

    def visit_excel(self, excel_document):
        print("Generating statistics for Excel document")


# Usage example
documents = [PDFDocument(), WordDocument(), ExcelDocument()]
text_extractor = TextExtractorVisitor()
statistics_generator = StatisticsVisitor()

for document in documents:
    document.accept(text_extractor)

for document in documents:
    document.accept(statistics_generator)
