#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.controller import router_init
from app.middleware import middleware_init
from app.utils.common_util import write_log
from app.utils.exception import global_exception_handlers


def create_app():
    app = FastAPI(title="USER_API",
                  description="接口文档",
                  version="1.0.0",
                  exception_handlers=global_exception_handlers
                  )
    add_pagination(app)
    # 初始化路由配置
    router_init(app)
    # 初始化中间件
    middleware_init(app)

    return app
