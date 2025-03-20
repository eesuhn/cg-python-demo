import json

from typing import Optional


def print_json(
    data: Optional[dict]
) -> None:
    print(json.dumps(data, indent=2))
