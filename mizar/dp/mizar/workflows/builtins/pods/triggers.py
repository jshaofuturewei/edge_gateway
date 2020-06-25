# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Authors.

# Authors: Sherif Abdelwahab <@zasherif>
#          Phu Tran          <@phudtran>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:The above copyright
# notice and this permission notice shall be included in all copies or
# substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS",
# WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import kopf
import logging
import luigi
from mizar.common.common import *
from mizar.common.constants import *
from mizar.common.wf_factory import *
from mizar.common.wf_param import *

logger = logging.getLogger()


@kopf.on.resume('', 'v1', 'pods')
@kopf.on.update('', 'v1', 'pods')
@kopf.on.create('', 'v1', 'pods')
async def builtins_on_pod(body, spec, **kwargs):
    param = HandlerParam()
    param.name = kwargs['name']
    param.body = body
    param.spec = spec

    logger.info("body: {}".format(body))

    logger.info("metadata: ---- ")
    for k in param.body['metadata']:
        print("metadata k:{}, v:{}".format(
            k, param.body['metadata'].get(k, None)))

    logger.info("status: ---- ")
    for k in param.body['status']:
        print("status k:{}, v:{}".format(k, param.body['status'].get(k, None)))

    logger.info("spec: ---- ")
    for k in param.spec:
        print("spec k:{}, v:{}".format(k, param.spec.get(k, None)))
    run_workflow(wffactory().k8sPodCreate(param=param))