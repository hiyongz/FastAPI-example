#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

import uvicorn

root_path = os.getcwd()
sys.path.append(root_path)
from app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8001,
        reload=False,
    )
