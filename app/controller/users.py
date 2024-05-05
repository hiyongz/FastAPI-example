#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 11:04
# @Author  : hiyongz
# @File    : users.py
# @Project: FastAPIDemo

from fastapi import APIRouter, Depends
from fastapi_pagination import paginate, Params

from app.log.logger import logger
from app.schema.response.user import UsersResponse
from app.utils.constant import HTTP

router = APIRouter()


# @router.get("/user", response_model=UserResponse)
@router.get("/user")
async def getUser():
    """
    读取用户
    """
    cdn_user = {"name": "zhangsan"}
    logger.info("666666666")
    return {'status_code': HTTP.HTTP_200_OK, "msg": "系统配置信息如下", 'data': cdn_user}


@router.get("/users", response_model=UsersResponse)
async def getUsers(params: Params = Depends()):
    """
    读取用户
    """
    user_list = [{"name": "zhangsan"}, {"name": "lishi"}]
    user_page = paginate(user_list, params)
    page_dict = {
        'total': user_page.total,
        'page': user_page.page,
        'pages': user_page.pages,
        'items': user_page.items
    }
    return {'code': HTTP.HTTP_200_OK, "msg": "Success", 'data': page_dict}







