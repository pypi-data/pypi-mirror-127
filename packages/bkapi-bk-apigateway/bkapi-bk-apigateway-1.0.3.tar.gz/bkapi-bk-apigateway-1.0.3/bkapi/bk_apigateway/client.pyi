# -*- coding: utf-8 -*-
"""
 * TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-蓝鲸 PaaS 平台(BlueKing-PaaS) available.
 * Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
 * Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://opensource.org/licenses/MIT
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
"""
from bkapi_client_core.apigateway import APIGatewayClient, Operation, OperationGroup


class Group(OperationGroup):

    @property
    def apply_permissions(self) -> Operation:
        """
        申请网关API访问权限
        """

    @property
    def create_resource_version(self) -> Operation:
        """
        创建资源版本
        """

    @property
    def get_apigw_public_key(self) -> Operation:
        """
        获取网关公钥
        """

    @property
    def get_latest_resource_version(self) -> Operation:
        """
        获取网关最新版本
        """

    @property
    def grant_permissions(self) -> Operation:
        """
        网关为应用主动授权
        """

    @property
    def import_resource_docs_by_archive(self) -> Operation:
        """
        通过文档归档文件导入资源文档
        """

    @property
    def import_resource_docs_by_swagger(self) -> Operation:
        """

        """

    @property
    def release(self) -> Operation:
        """
        发布版本
        """

    @property
    def sync_access_strategy(self) -> Operation:
        """
        同步策略
        """

    @property
    def sync_api(self) -> Operation:
        """
        同步网关
        """

    @property
    def sync_resources(self) -> Operation:
        """
        同步资源
        """

    @property
    def sync_stage(self) -> Operation:
        """
        同步环境
        """


class Client(APIGatewayClient):
    """bk-apigateway
    蓝鲸API网关
    """

    @property
    def api(self) -> Group:
        """api resources"""
