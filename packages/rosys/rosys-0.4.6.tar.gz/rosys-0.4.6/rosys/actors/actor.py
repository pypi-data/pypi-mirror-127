import asyncio
import logging
from typing import Callable
from concurrent.futures import ProcessPoolExecutor


class Actor:
    interval: float = None
    process_pool = ProcessPoolExecutor()

    def __init__(self) -> None:
        name = __name__[:-5] + self.__class__.__name__
        self.log = logging.getLogger(name)

    async def step(self):
        pass

    async def tear_down(self):
        pass

    async def sleep(self, seconds: float):
        '''delay execution; in tests this method will be replaced'''
        await asyncio.sleep(seconds)

    async def run_io_bound(self, callback: Callable, *args: any):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, callback, *args)

    async def run_cpu_bound(self, callback: Callable, *args: any):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, callback, *args)

    async def pause_automations(self, *, because: str):
        pass  # NOTE the runtime implements this

    def __str__(self) -> str:
        return type(self).__name__
