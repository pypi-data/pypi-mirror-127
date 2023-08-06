from typing import Any, Optional
from urllib.parse import urljoin

import aiohttp

from huum.schemas import HuumStatusResponse
from huum.settings import settings

API_BASE = "https://api.huum.eu/action/home/"


class Huum:
    """
    Usage:
        # Usage with env vars
        huum = Huum()

        # Setting auth variables explicitly
        huum = Huum(username="foo", password="bar)

        # If you don't have an existing aiohttp session
        # then run `open_session()` after initilizing
        huum.open_session()
    """

    min_temp = 40
    max_temp = 110

    session: aiohttp.ClientSession

    def __init__(
        self,
        username: Optional[str] = settings.huum_username,
        password: Optional[str] = settings.huum_password,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        if session:
            self.session = session

        if not username or not password:
            raise ValueError(
                "No username or password provided either by the environment nor explicitly"
            )
        self.auth = aiohttp.BasicAuth(username, password)

    async def handle_response(self, response: aiohttp.ClientResponse) -> Any:
        if response.status != 200:
            response_text = await response.text()
            raise aiohttp.ClientError(
                f"Request failed with status code {response.status}. {response_text}"
            )
        return await response.json()

    async def status(self) -> HuumStatusResponse:
        url = urljoin(API_BASE, "status")

        response = await self.session.get(url, auth=self.auth)
        json_data = await self.handle_response(response)

        return HuumStatusResponse(**json_data)

    async def turn_on(self, temperature: int) -> HuumStatusResponse:
        if temperature not in range(self.min_temp, self.max_temp):
            raise ValueError(
                f"Temperature '{temperature}' must be between {self.min_temp}-{self.max_temp}"
            )

        url = urljoin(API_BASE, "start")
        data = {"targetTemperature": temperature}

        response = await self.session.post(url, json=data, auth=self.auth)
        json_data = await self.handle_response(response)

        return HuumStatusResponse(**json_data)

    async def turn_off(self) -> HuumStatusResponse:
        url = urljoin(API_BASE, "stop")

        response = await self.session.post(url, auth=self.auth)
        json_data = await self.handle_response(response)

        return HuumStatusResponse(**json_data)

    async def open_session(self) -> None:
        self.session = aiohttp.ClientSession()

    async def close_session(self) -> None:
        await self.session.close()
