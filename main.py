import re

import aiohttp
import asyncio

from typing import List

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


async def read_file(filename: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(filename) as response:
            return await response.text()


def text_to_matrix(text: str) -> List[List[int]]:
    result = []
    result_matrix = []
    len_matrix = int(len(re.findall(r'\b\d+\b', text)) ** 0.5)
    for item in text.split(' '):
        if item.strip().isdigit():
            if len(result) < len_matrix:
                result.append(int(item))
            else:
                result_matrix.append(result)
                result = []
                result.append(int(item))
    result_matrix.append(result)
    return result_matrix


def read_matrix_counterclock_wise(matrix: List[List[int]]) -> List[int]:
    matrix = [list(row) for row in list(zip(*matrix))[::-1]]
    result = []
    while True:
        matrix.reverse()
        result.append(matrix[0])
        del matrix[0]
        if len(matrix) == 0:
            break
        matrix = list(zip(*matrix))
    lst = []
    for row in result:
        for item in row:
            lst.append(item)
    return lst


async def get_matrix(url: str) -> List[int]:
    response = await read_file(url)
    matrix_in = text_to_matrix(response)
    return read_matrix_counterclock_wise(matrix_in)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_matrix(SOURCE_URL))


