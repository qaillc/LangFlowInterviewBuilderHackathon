{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import argparse\
import json\
from argparse import RawTextHelpFormatter\
import requests\
from typing import Optional\
import warnings\
try:\
    from langflow.load import upload_file\
except ImportError:\
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")\
    upload_file = None\
\
BASE_API_URL = "https://eaglelandsonce-langflowaiinnovators.hf.space/api/v1/run"\
FLOW_ID = "c43ce1ec-9d25-4068-8c4a-e74050b416c5"\
ENDPOINT = ""  # You can set a specific endpoint name in the flow settings\
\
# You can tweak the flow by adding a tweaks dictionary\
# e.g \{"OpenAI-XXXXX": \{"model_name": "gpt-4"\}\}\
TWEAKS = \{\
    "ChatInput-rNGAl": \{\},\
    "OpenAIModel-9GpqE": \{\},\
    "ChatOutput-1jzlA": \{\},\
    "Prompt-A2Q3n": \{\},\
    "File-1TA8M": \{\},\
    "ParseData-NRXOk": \{\}\
\}\
\
def run_flow(message: str,\
             endpoint: str,\
             output_type: str = "chat",\
             input_type: str = "chat",\
             tweaks: Optional[dict] = None,\
             api_key: Optional[str] = None) -> dict:\
    """\
    Run a flow with a given message and optional tweaks.\
\
    :param message: The message to send to the flow\
    :param endpoint: The ID or the endpoint name of the flow\
    :param tweaks: Optional tweaks to customize the flow\
    :return: The JSON response from the flow\
    """\
    api_url = f"\{BASE_API_URL\}/\{endpoint\}"\
\
    payload = \{\
        "input_value": message,\
        "output_type": output_type,\
        "input_type": input_type,\
    \}\
    headers = None\
    if tweaks:\
        payload["tweaks"] = tweaks\
    if api_key:\
        headers = \{"x-api-key": api_key\}\
    response = requests.post(api_url, json=payload, headers=headers)\
    return response.json()\
\
def main():\
    parser = argparse.ArgumentParser(description="""Run a flow with a given message and optional tweaks.\
Run it like: python <your file>.py "your message here" --endpoint "your_endpoint" --tweaks '\{"key": "value"\}'""",\
        formatter_class=RawTextHelpFormatter)\
    parser.add_argument("message", type=str, help="The message to send to the flow")\
    parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")\
    parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))\
    parser.add_argument("--api_key", type=str, help="API key for authentication", default=None)\
    parser.add_argument("--output_type", type=str, default="chat", help="The output type")\
    parser.add_argument("--input_type", type=str, default="chat", help="The input type")\
    parser.add_argument("--upload_file", type=str, help="Path to the file to upload", default=None)\
    parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)\
\
    args = parser.parse_args()\
    try:\
        tweaks = json.loads(args.tweaks)\
    except json.JSONDecodeError:\
        raise ValueError("Invalid tweaks JSON string")\
\
    if args.upload_file:\
        if not upload_file:\
            raise ImportError("Langflow is not installed. Please install it to use the upload_file function.")\
        elif not args.components:\
            raise ValueError("You need to provide the components to upload the file to.")\
        tweaks = upload_file(file_path=args.upload_file, host=BASE_API_URL, flow_id=ENDPOINT, components=args.components, tweaks=tweaks)\
\
    response = run_flow(\
        message=args.message,\
        endpoint=args.endpoint,\
        output_type=args.output_type,\
        input_type=args.input_type,\
        tweaks=tweaks,\
        api_key=args.api_key\
    )\
\
    print(json.dumps(response, indent=2))\
\
if __name__ == "__main__":\
    main()\
"""\
\
# Saving the corrected code to a Python file\
with open("/mnt/data/Python_API.py", "w") as file:\
    file.write(code) &#8203;:citation[oaicite:0]\{index=0\}&#8203;\
}