from __future__ import annotations

import requests


async def request_json_api(url: str, json: any) -> requests.Response:
    try:
        response = await requests.post(
            url=url, json=json)

        return response
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err
