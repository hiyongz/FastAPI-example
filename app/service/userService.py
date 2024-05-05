#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 11:02
# @Author  : hiyongz
# @File    : userService.py
# @Project: FastAPIDemo
import asyncio
import time
from app.log.logger import logger


async def worker_1(num):
    start_time = time.time()
    logger.info(f"worker_{num} start")
    await asyncio.sleep(num)
    logger.info(f"worker_{num} done")
    end_time = time.time()
    logger.info("worker_{} 耗时： {}秒".format(num, end_time - start_time))
    return num
