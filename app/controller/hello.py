#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/30 19:52
# @Author  : hiyongz
# @File    : hello.py
# @Project: FastAPIDemo
import asyncio
import time

from fastapi import APIRouter

from app.log.logger import logger
from app.schema.request.baseParams import DeviceIdsIN
from app.service.userService import worker_1
from app.utils.constant import HTTP

router = APIRouter()


@router.get("/{name}")
async def root(name):
    logger.info("Root path is Visited")
    hello()
    logger.info(f"{name} Visited")
    return {"message": f"Hello {name}"}


def hello():
    logger.info("hello() called")


@router.post("/coroutine_test")
async def coroutine_test(ids: DeviceIdsIN):
    # # 方法1: 异步
    start_time = time.time()
    tasks = [worker_1(int(id)) for id in ids.ids]
    results = await asyncio.gather(*tasks)

    # # 方法2: 异步
    # tasks = []
    # for id in ids.ids:
    #     tasks.append(worker_1(int(id)))
    # results = await asyncio.gather(*tasks)

    # 方法3: 同步
    # results = []
    # for id in ids.ids:
    #     results.append(await worker_1(int(id)))
    end_time = time.time()
    print("共耗时：{}秒".format(end_time - start_time))
    return {'code': HTTP.HTTP_200_OK, 'msg': "Success", 'data': results}
