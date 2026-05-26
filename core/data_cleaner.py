from core.data_cleaner import DataCleaner

cleaner = DataCleaner()
cleaned_text = cleaner.clean("book.pdf")  # outputs clean text

with open("book_cleaned.md", "w") as f:
    f.write(cleaned_text)
