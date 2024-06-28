# Contact Book Project Documentation Generation

## Documentation Generation Overview

The Contact Book Project leverages the power of LLMs to automate the generation of comprehensive documentation for software projects, streamlining the creation process and ensuring structured, detailed documentation.

## Features

- **LLM-Powered Documentation**: Automatically generates detailed documentation for Python scripts and modules.
- **MkDocs Integration**: Seamlessly integrates the generated documentation into MkDocs for easy access and navigation.

## How to Use the Contact Book Project

To use the Contact Book Project and view the generated documentation:

1. Open a terminal window and run the MkDocs server:
   ```
   mkdocs serve
   ```
2. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the MkDocs site.
3. In a separate terminal window, run the `update_docs.py` script from the `enhance_mkdocs` directory to generate documentation for a specific Python module. For example:
   ```
   python enhance_mkdocs/update_docs.py ../contact_book/utils.py
   ```
   This script will analyze the Python file and automatically generate detailed documentation.

4. Once the documentation is generated, MkDocs will create a new static page that includes the detailed documentation of the module. You'll notice this update as a new page in the MkDocs site, providing structured and comprehensive information about the `utils.py` module.

By following these steps, you can easily generate and view up-to-date documentation for your project, making it accessible for both developers and users.

## Improvement Suggestions

- **Instructor for Structured Outputs**: The [Instructor](https://github.com/jxnl/instructor) library can be used to improve adherence to desired documentation structure. It is a Python library that facilitates working with structured outputs from LLMs, providing a simple API to manage validation, retries, and streaming responses.

## Example Project: Contact Book

### Example Project Overview

The Contact Book Project is a Python application for managing contact information. It features a user-friendly interface for adding, removing, and viewing contacts.

### Example Project Features

- **Add Contacts**: Easily add new contact details.
- **Remove Contacts**: Remove contacts by specifying the name.
- **View Contacts**: Browse all stored contact information.

## Installation

Install the project dependencies using the provided `requirements.txt` file.

## Additional Tools

### litellm

The project utilizes `litellm` to enable calling various LLM APIs using a unified OpenAI format. This facilitates interaction with APIs from Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, and others.

#### Setting Up

To use `litellm`, set the appropriate environment variable, such as `OPENAI_API_KEY` or `COHERE_API_KEY`.

For more details, visit the [litellm](https://github.com/BerriAI/litellm) repository.
