import re

import aiohttp
import asyncio

from typing import List

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


async def read_file(filename: str) -> List[List[int]]:
    async with aiohttp.ClientSession() as session:
        async with session.get(filename) as response:
            matrix = await response.text()
            result = []
            result_matrix = []
            len_matrix = int(len(re.findall(r'\b\d+\b', matrix)) ** 0.5)
            for item in matrix.split(' '):
                if item.strip().isdigit():
                    if len(result) < len_matrix:
                        result.append(int(item))
                    else:
                        result_matrix.append(result)
                        result = []
                        result.append(int(item))
            result_matrix.append(result)
            return result_matrix


async def get_matrix(url: str) -> List[int]:
    matrix_in = await read_file(url)
    # Для обхода матрицы против часовой стрелки повернем ее на 90 градусов,
    # чтобы колонка стала строкой
    matrix = [list(row) for row in list(zip(*matrix_in))[::-1]]
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

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_matrix(SOURCE_URL))


