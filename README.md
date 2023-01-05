## Repository Name Finder
This script extracts repository names from a text using natural language processing (NLP) techniques. The script first loads a specific NLP model (specified by your_NLP_model) using the 'spacy' library. Then, it processes a given text (e.g., 'I like to save my data in Odum Institute Archive Dataverse') and searches for repository names in it.

The script has three different methods to search for repository names in the text:

1.Token-based search: This method looks for specific tokens (e.g., 'SURFsara', 'DRYAD') in the text. If a matching token is found, the method returns 'True'. Otherwise, it returns 'False'.

2.Pattern-based search: This method uses a pre-defined pattern (e.g., [{'ORTH': 'Odum Institute Archive Dataverse'}]) to search for repository names in the text. It returns a list of matches.

3.PDF-based search: This method reads a series of PDF files from a specified directory ('files_path') and extracts text from them using the 'PyMuPDF' library ('fitz'). Then, it processes the extracted text using the previously loaded NLP model and extracts entities (i.e., named entities) from it. The method stores the extracted entities and their labels (i.e., entity types) in a Pandas dataframe, and then creates a pivot table to summarize the data. Finally, it exports the pivot table as an Excel file ('DMP_info.xlsx').

# Dependencies

'spacy'

'pandas'

'PyMuPDF' ('fitz')

# Usage

1. Install the dependencies.

2. Replace 'your_NLP_model' with the desired NLP model.

3. Specify the path to the PDF files in files_path.

4. Run the script.

5. The pivot table will be saved as an Excel file in the current working directory.
