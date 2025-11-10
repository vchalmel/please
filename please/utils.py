from typing import (
    List,
    Dict,
    Any
)


def clean_dict(d: Dict[str, Any] = None, keep_keys: bool = False):
    if d is None or len(d.items()) == 0:
        return d

    cleaned = {}

    if keep_keys:
        cleaned = {
          k: (
            clean_dict(v) if isinstance(v, dict)
            else clean_list(v) if isinstance(v, list)
            else None if (v in ('', {}, []))
            else v
          ) for k, v in d.items()
        }
    else:
        cleaned = {
            k: (
                clean_dict(v) if isinstance(v, dict)
                else clean_list(v) if isinstance(v, list)
                else v
            ) for k, v in d.items() if (
                clean_dict(v) if isinstance(v, dict)
                else clean_list(v) if isinstance(v, list)
                else v
            ) not in ('', None, {}, [])
        }

    if len(cleaned.items()) > 0:
        return cleaned
    else:
        return None


def clean_list(a: List[Any] = None):
    if a is None:
        return a
    cleaned = [(
            clean_list(it) if isinstance(it, list)
            else clean_dict(it) if isinstance(it, dict)
            else it
        ) for it in a if (
            clean_list(it) if isinstance(it, list)
            else clean_dict(it) if isinstance(it, dict)
            else it
        ) not in ('', None, {}, [])
    ]
    if len(cleaned) > 0:
        return cleaned
    else:
        return None
