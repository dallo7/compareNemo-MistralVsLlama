from gradio_client import Client
import re
import json


def filterOutput(result_text):
    pattern = r"\{([^{}]*)\}"
    matches = re.findall(pattern, result_text)
    cleaned_string = matches[0].strip().replace('\n  ', '')
    data_dict = json.loads(f"{{{cleaned_string}}}")
    formatted_output = "\n".join([f" **{key}: {value}" for key, value in data_dict.items()])
    return formatted_output


def mistralNemo(inputText):
    client = Client("vilarin/Mistral-Nemo")

    user_prompt = """Jane Doe, Sales & Marketing Director at ABC Company (3373 Gregory Lane, 40601 Frankfort, t: (800) 555-1133, e: jane.doe@example.com, www.example.com) emailed Mike to follow up on a project discussed during a meeting, asking if he had any updates or needed assistance. The email, inspired by professional email signature examples from blog.hubspot.com/marketing/professional-email-signatures, notes its confidentiality and requests that it be deleted if received in error. [invalid URL removed] may offer further context on similar professional communications"""

    msg = f"""You are a helpful and meticulous assistant specializing in extracting structured information from text. Your primary task is to identify and extract the following entities from a given text and return them in JSON format:

    {{
    "Full Name": "...",
    "Email Address": "...",
    "Company Name": "...",
    "Location": "...",
    "Telephone Number": "..."
    }}

    If an entity is not found, its value should be set to "Not Found". 

    Prioritize accuracy and completeness when extracting information. If you are unsure about a value, indicate "Not Found" rather than guessing.
    * **Location:** This could be a full street address, city and state, or even just a country.
    * **Telephone Number:** Include country codes if present, and format as +[Country Code] [Number].


    Example:
    Text: "John Doe (john.doe@email.com) called from ACME Corp. in New York (123) 456-7890."

    Response:
    {{
    "Full Name": "John Doe",
    "Email Address": "john.doe@email.com",
    "Company Name": "ACME Corp.",
    "Location": "New York",
    "Telephone Number": "(123) 456-7890"
    }}

    Now extract information from this text:

    '{user_prompt}'
    """

    result = client.predict(
        message=msg,
        temperature=0.2,
        max_new_tokens=1024,
        top_p=0.95,
        api_name="/chat"
    )

    return result


def llama(inputText):
    from gradio_client import Client

    client = Client("vilarin/Llama-3.1-8B-Instruct")

    user_prompt = """Jane Doe, Sales & Marketing Director at ABC Company (3373 Gregory Lane, 40601 Frankfort, t: (800) 555-1133, e: jane.doe@example.com, www.example.com) emailed Mike to follow up on a project discussed during a meeting, asking if he had any updates or needed assistance. The email, inspired by professional email signature examples from blog.hubspot.com/marketing/professional-email-signatures, notes its confidentiality and requests that it be deleted if received in error. [invalid URL removed] may offer further context on similar professional communications"""

    msg = f"""Extract ONLY the email signature from the following text and return it in JSON format. If there is no signature, return "Not Found".
    {{
    "Full Name": "...",
    "Email Address": "...",
    "Company Name": "...",
    "Location": "...",
    "Telephone Number": "..."
    }}

    If an entity is not found, its value should be set to "Not Found". 

    Prioritize accuracy and completeness when extracting information. If you are unsure about a value, indicate "Not Found" rather than guessing.
    * **Location:** This could be a full street address, city and state, or even just a country.
    * **Telephone Number:** Include country codes if present, and format as +[Country Code] [Number].


    Example:
    Text: "John Doe (john.doe@email.com) called from ACME Corp. in New York (123) 456-7890."

    Response:
    {{
    "Full Name": "John Doe",
    "Email Address": "john.doe@acmecorp.com",
    "Company Name": "ACME Corp.",
    "Location": "Anytown, CA 12345",
    "Telephone Number": "(123) 456-7890"
    }}

    Now extract the signature from this text:

    '{user_prompt}'
    """

    result = client.predict(
        message=msg,
        temperature=0.2,
        max_new_tokens=1024,
        top_p=0.95,
        api_name="/chat"
    )

    return filterOutput(result)


