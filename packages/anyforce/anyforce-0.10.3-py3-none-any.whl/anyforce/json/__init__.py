from datetime import datetime

try:
    from ciso8601 import parse_datetime  # type: ignore
except ImportError:
    parse_datetime = datetime.fromisoformat
from typing import Any, Dict, List, Union, cast

import orjson
from fastapi.encoders import jsonable_encoder


def fast_dumps(o: Any) -> str:
    return orjson.dumps(o).decode("utf-8")


def raw_dumps(o: Any) -> bytes:
    return orjson.dumps(o, default=jsonable_encoder)


def dumps(o: Any) -> str:
    return orjson.dumps(o, default=jsonable_encoder).decode("utf-8")


def parse_iso_datetime(s: str) -> datetime:
    return cast(datetime, parse_datetime(s))


def decoder(input: Any) -> Any:
    if isinstance(input, dict):
        input = cast(Dict[Any, Any], input)
        for k, v in input.items():
            input[k] = decoder(v)
    elif isinstance(input, List):
        input = cast(List[Any], input)
        for i, v in enumerate(input):
            input[i] = decoder(v)
    elif isinstance(input, str) and input.find("T") == 10:
        try:
            return parse_iso_datetime(input)
        except ValueError:
            pass
    return input


def loads(raw: Union[bytes, bytearray, str]):
    if len(raw) == 0:
        return ""
    o = orjson.loads(raw)
    return decoder(o)
