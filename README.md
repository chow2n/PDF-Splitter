# PDF-Splitter

This was just a quick Python script that is able to split PDF files by page number. You must change the source variable to the folder path where all of the PDF files you would like to split are. The use-case for me and my team was to separate the individual document types within large, 200+ page PDF files. Doing so allowed us to organize specified documents for clustering and eventual machine learning model training.

### Libraries Used:
- [os](https://docs.python.org/3/library/os.html)
- [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/)
