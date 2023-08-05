"""
Command line interface for interacting with FSM data server

Usage:
fsm-pull --org-id=<org-id> --lang-code=<lang-code> --start=<DDMMYYYY> --output-json=<output-json> [--end=<DDMMYYYY>] \
[--call-quantity=<call-quantity>]
fsm-pull (-h|--help)

Options:
--org-id=<org-id>                   Client Organisation ID for the client for which data is to be downloaded
--lang-code=<lang-code>             Language code, en for english, hi for hindi etc
--start=<DDMMYYYY>                  Start Date from which data is to be downloaded,
                                                If start date is 15th August 1947, Please enter 15081947
--end=<DDMMYYYY>                    End Date till which data is to be downloaded,
                                                If start date is 15th August 1947, Please enter 15081947
                                                Default is end of current date
--call-quantity=<call-quantity>     Number of call to be downloaded, Default is 0(all the calls)
"""

import json
import os
import time
from concurrent import futures
from datetime import datetime
from typing import Optional

import pytz
from docopt import docopt
from loguru import logger
from tqdm import tqdm

from fsm_pull import __version__
from fsm_pull.connection import Connection


def convert_date(date_string: str, trailing=False, timezone="Asia/Kolkata") -> str:
    if not isinstance(date_string, str):
        raise ValueError("Date should be ddmmyyyy format")

    if date_string != "now" and len(date_string) != 8:
        raise ValueError("Date should be ddmmyyyy format")

    current_time = datetime.now()
    current_time = current_time.replace(
        hour=23, minute=59, tzinfo=pytz.timezone(timezone)
    )
    start_limit = datetime(2016, 1, 6).replace(tzinfo=pytz.timezone(timezone))

    if date_string == "now":
        return current_time.isoformat()
    else:
        given_date = datetime.strptime(date_string, "%d%m%Y")
        if trailing:
            given_date = given_date.replace(
                hour=23, minute=59, tzinfo=pytz.timezone(timezone)
            )
        else:
            given_date = given_date.replace(tzinfo=pytz.timezone(timezone))

        if start_limit <= given_date <= current_time:
            return given_date.isoformat()
        else:
            raise ValueError(
                f"Date {date_string} is not in the range of {start_limit} to {current_time}"
            )


def parse_metadata_json(conversations):
    if not conversations:
        return []
    for conversation in conversations:
        if "metadata" in conversation:
            conversation["metadata"] = json.loads(conversation["metadata"])
    return conversations


def add_turns_to_call(conn, call):
    turns = conn.fetch_turns(call["uuid"])
    turns["conversations"] = parse_metadata_json(turns["conversations"])
    if "virtual_number" in turns:
        call["virtual_number"] = turns["virtual_number"]
    call["turns"] = turns
    return call


def get_turns_via_threaded_req(conn, calls, workers=20):
    with futures.ThreadPoolExecutor(workers) as executor:
        call_list = [executor.submit(add_turns_to_call, conn, call) for call in calls]
    return [call.result() for call in call_list]


def get_call_list(
    org_id: int,
    lang_code: str,
    start: str,
    end: str = "now",
    call_quantity: int = 0,
    flow_uuid: Optional[str] = None,
    custom_search_key: Optional[str] = None,
    custom_search_value: Optional[str] = None,
    subtesting=False,
):
    start = convert_date(start)
    end = convert_date(end, trailing=True)

    conn = Connection(org_id)
    proc_start_time = time.time()
    print(
        f"Downloading {call_quantity if call_quantity else 'all'} Call(s) made between {start} and {end}"
    )

    call_list = []
    calls = conn.fetch_calls(
        lang_code,
        start,
        end,
        call_quantity,
        flow_uuid=flow_uuid,
        custom_search_key=custom_search_key,
        custom_search_value=custom_search_value,
        subtesting=subtesting,
    )

    call_list = get_turns_via_threaded_req(conn, calls)

    logger.info(f"pulled {len(calls)} calls in {time.time() - proc_start_time:.2f}s")
    return call_list


def pull(
    org_id: int,
    lang_code: str,
    start: str,
    end: str = "now",
    call_quantity: int = 0,
    output_json: Optional[str] = None,
):

    if output_json and os.path.exists(output_json):
        raise FileExistsError(f"{output_json} already present")

    call_list = get_call_list(
        org_id, lang_code, start, end=end, call_quantity=call_quantity
    )

    if output_json:
        print(f"Writing {len(call_list)} call(s) to {output_json}")
        with open(output_json, "w") as f:
            json.dump(call_list, f)
    else:
        print(f"Returning {len(call_list)} call(s)")
        return call_list


def main():
    args = docopt(__doc__, version=__version__)

    org_id = args["--org-id"]
    lang_code = args["--lang-code"]
    start = args["--start"]
    output_json = args["--output-json"]

    end = args["--end"] or "now"
    call_quantity = int(args["--call-quantity"] or 0)

    pull(org_id, lang_code, start, end, call_quantity, output_json)
