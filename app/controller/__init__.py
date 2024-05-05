#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 10:41
# @Author  : hiyongz
# @File    : __init__.py
# @Project: FastAPIDemo

from app.controller import users, hello


def router_init(app):
    app.include_router(
        users.router,
        prefix="/api/v1",
        tags=["demo"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )

    app.include_router(
        hello.router,
        prefix="/api/v1",
        tags=["hello"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
