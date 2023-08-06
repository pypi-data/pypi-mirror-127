# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vod20170321 import models as vod_20170321_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'vod.aliyuncs.com',
            'ap-southeast-2': 'vod.aliyuncs.com',
            'ap-southeast-3': 'vod.aliyuncs.com',
            'cn-beijing-finance-1': 'vod.aliyuncs.com',
            'cn-beijing-finance-pop': 'vod.aliyuncs.com',
            'cn-beijing-gov-1': 'vod.aliyuncs.com',
            'cn-beijing-nu16-b01': 'vod.aliyuncs.com',
            'cn-chengdu': 'vod.aliyuncs.com',
            'cn-edge-1': 'vod.aliyuncs.com',
            'cn-fujian': 'vod.aliyuncs.com',
            'cn-haidian-cm12-c01': 'vod.aliyuncs.com',
            'cn-hangzhou': 'vod.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'vod.aliyuncs.com',
            'cn-hangzhou-finance': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'vod.aliyuncs.com',
            'cn-hangzhou-test-306': 'vod.aliyuncs.com',
            'cn-hongkong': 'vod.aliyuncs.com',
            'cn-hongkong-finance-pop': 'vod.aliyuncs.com',
            'cn-huhehaote': 'vod.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'vod.aliyuncs.com',
            'cn-qingdao': 'vod.aliyuncs.com',
            'cn-qingdao-nebula': 'vod.aliyuncs.com',
            'cn-shanghai-et15-b01': 'vod.aliyuncs.com',
            'cn-shanghai-et2-b01': 'vod.aliyuncs.com',
            'cn-shanghai-finance-1': 'vod.aliyuncs.com',
            'cn-shanghai-inner': 'vod.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'vod.aliyuncs.com',
            'cn-shenzhen-finance-1': 'vod.aliyuncs.com',
            'cn-shenzhen-inner': 'vod.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'vod.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'vod.aliyuncs.com',
            'cn-wuhan': 'vod.aliyuncs.com',
            'cn-wulanchabu': 'vod.aliyuncs.com',
            'cn-yushanfang': 'vod.aliyuncs.com',
            'cn-zhangbei': 'vod.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'vod.aliyuncs.com',
            'cn-zhangjiakou': 'vod.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'vod.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'vod.aliyuncs.com',
            'eu-west-1': 'vod.aliyuncs.com',
            'eu-west-1-oxs': 'vod.aliyuncs.com',
            'me-east-1': 'vod.aliyuncs.com',
            'rus-west-1-pop': 'vod.aliyuncs.com',
            'us-east-1': 'vod.aliyuncs.com',
            'us-west-1': 'vod.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('vod', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_aitemplate_with_options(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddAITemplateResponse(),
            self.do_rpcrequest('AddAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddAITemplateResponse(),
            await self.do_rpcrequest_async('AddAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_aitemplate(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
    ) -> vod_20170321_models.AddAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    async def add_aitemplate_async(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
    ) -> vod_20170321_models.AddAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_aitemplate_with_options_async(request, runtime)

    def add_category_with_options(
        self,
        request: vod_20170321_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddCategoryResponse(),
            self.do_rpcrequest('AddCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: vod_20170321_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddCategoryResponse(),
            await self.do_rpcrequest_async('AddCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_category(
        self,
        request: vod_20170321_models.AddCategoryRequest,
    ) -> vod_20170321_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    async def add_category_async(
        self,
        request: vod_20170321_models.AddCategoryRequest,
    ) -> vod_20170321_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_category_with_options_async(request, runtime)

    def add_editing_project_with_options(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddEditingProjectResponse(),
            self.do_rpcrequest('AddEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_editing_project_with_options_async(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddEditingProjectResponse(),
            await self.do_rpcrequest_async('AddEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_editing_project(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_with_options(request, runtime)

    async def add_editing_project_async(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_editing_project_with_options_async(request, runtime)

    def add_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('AddTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('AddTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_transcode_template_group(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    async def add_transcode_template_group_async(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_transcode_template_group_with_options_async(request, runtime)

    def add_vod_domain_with_options(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodDomainResponse(),
            self.do_rpcrequest('AddVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodDomainResponse(),
            await self.do_rpcrequest_async('AddVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vod_domain(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
    ) -> vod_20170321_models.AddVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    async def add_vod_domain_async(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
    ) -> vod_20170321_models.AddVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vod_domain_with_options_async(request, runtime)

    def add_vod_template_with_options(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodTemplateResponse(),
            self.do_rpcrequest('AddVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vod_template_with_options_async(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodTemplateResponse(),
            await self.do_rpcrequest_async('AddVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vod_template(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    async def add_vod_template_async(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vod_template_with_options_async(request, runtime)

    def add_watermark_with_options(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddWatermarkResponse(),
            self.do_rpcrequest('AddWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_watermark_with_options_async(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AddWatermarkResponse(),
            await self.do_rpcrequest_async('AddWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_watermark(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
    ) -> vod_20170321_models.AddWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    async def add_watermark_async(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
    ) -> vod_20170321_models.AddWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_watermark_with_options_async(request, runtime)

    def attach_app_policy_to_identity_with_options(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AttachAppPolicyToIdentityResponse(),
            self.do_rpcrequest('AttachAppPolicyToIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_app_policy_to_identity_with_options_async(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.AttachAppPolicyToIdentityResponse(),
            await self.do_rpcrequest_async('AttachAppPolicyToIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_app_policy_to_identity(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    async def attach_app_policy_to_identity_async(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_app_policy_to_identity_with_options_async(request, runtime)

    def batch_set_vod_domain_configs_with_options(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchSetVodDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_vod_domain_configs_with_options_async(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchSetVodDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchSetVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_vod_domain_configs(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    async def batch_set_vod_domain_configs_async(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_vod_domain_configs_with_options_async(request, runtime)

    def batch_start_vod_domain_with_options(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStartVodDomainResponse(),
            self.do_rpcrequest('BatchStartVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_start_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStartVodDomainResponse(),
            await self.do_rpcrequest_async('BatchStartVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_vod_domain(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    async def batch_start_vod_domain_async(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_vod_domain_with_options_async(request, runtime)

    def batch_stop_vod_domain_with_options(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStopVodDomainResponse(),
            self.do_rpcrequest('BatchStopVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStopVodDomainResponse(),
            await self.do_rpcrequest_async('BatchStopVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_vod_domain(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    async def batch_stop_vod_domain_async(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_vod_domain_with_options_async(request, runtime)

    def cancel_url_upload_jobs_with_options(
        self,
        request: vod_20170321_models.CancelUrlUploadJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CancelUrlUploadJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CancelUrlUploadJobsResponse(),
            self.do_rpcrequest('CancelUrlUploadJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_url_upload_jobs_with_options_async(
        self,
        request: vod_20170321_models.CancelUrlUploadJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CancelUrlUploadJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CancelUrlUploadJobsResponse(),
            await self.do_rpcrequest_async('CancelUrlUploadJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_url_upload_jobs(
        self,
        request: vod_20170321_models.CancelUrlUploadJobsRequest,
    ) -> vod_20170321_models.CancelUrlUploadJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_url_upload_jobs_with_options(request, runtime)

    async def cancel_url_upload_jobs_async(
        self,
        request: vod_20170321_models.CancelUrlUploadJobsRequest,
    ) -> vod_20170321_models.CancelUrlUploadJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_url_upload_jobs_with_options_async(request, runtime)

    def create_app_info_with_options(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAppInfoResponse(),
            self.do_rpcrequest('CreateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_info_with_options_async(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAppInfoResponse(),
            await self.do_rpcrequest_async('CreateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_info(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_info_with_options(request, runtime)

    async def create_app_info_async(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_info_with_options_async(request, runtime)

    def create_audit_with_options(
        self,
        request: vod_20170321_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAuditResponse(),
            self.do_rpcrequest('CreateAudit', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_audit_with_options_async(
        self,
        request: vod_20170321_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAuditResponse(),
            await self.do_rpcrequest_async('CreateAudit', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_audit(
        self,
        request: vod_20170321_models.CreateAuditRequest,
    ) -> vod_20170321_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    async def create_audit_async(
        self,
        request: vod_20170321_models.CreateAuditRequest,
    ) -> vod_20170321_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_audit_with_options_async(request, runtime)

    def create_detection_template_with_options(
        self,
        request: vod_20170321_models.CreateDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateDetectionTemplateResponse(),
            self.do_rpcrequest('CreateDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_detection_template_with_options_async(
        self,
        request: vod_20170321_models.CreateDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateDetectionTemplateResponse(),
            await self.do_rpcrequest_async('CreateDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_detection_template(
        self,
        request: vod_20170321_models.CreateDetectionTemplateRequest,
    ) -> vod_20170321_models.CreateDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_detection_template_with_options(request, runtime)

    async def create_detection_template_async(
        self,
        request: vod_20170321_models.CreateDetectionTemplateRequest,
    ) -> vod_20170321_models.CreateDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_detection_template_with_options_async(request, runtime)

    def create_upload_attached_media_with_options(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadAttachedMediaResponse(),
            self.do_rpcrequest('CreateUploadAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_attached_media_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadAttachedMediaResponse(),
            await self.do_rpcrequest_async('CreateUploadAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_attached_media(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    async def create_upload_attached_media_async(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_attached_media_with_options_async(request, runtime)

    def create_upload_image_with_options(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadImageResponse(),
            self.do_rpcrequest('CreateUploadImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_image_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadImageResponse(),
            await self.do_rpcrequest_async('CreateUploadImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_image(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    async def create_upload_image_async(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_image_with_options_async(request, runtime)

    def create_upload_video_with_options(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadVideoResponse(),
            self.do_rpcrequest('CreateUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_video_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadVideoResponse(),
            await self.do_rpcrequest_async('CreateUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_video(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_video_with_options(request, runtime)

    async def create_upload_video_async(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_video_with_options_async(request, runtime)

    def create_vod_real_time_log_delivery_with_options(
        self,
        request: vod_20170321_models.CreateVodRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateVodRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateVodRealTimeLogDeliveryResponse(),
            self.do_rpcrequest('CreateVodRealTimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_vod_real_time_log_delivery_with_options_async(
        self,
        request: vod_20170321_models.CreateVodRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateVodRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateVodRealTimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('CreateVodRealTimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_vod_real_time_log_delivery(
        self,
        request: vod_20170321_models.CreateVodRealTimeLogDeliveryRequest,
    ) -> vod_20170321_models.CreateVodRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vod_real_time_log_delivery_with_options(request, runtime)

    async def create_vod_real_time_log_delivery_async(
        self,
        request: vod_20170321_models.CreateVodRealTimeLogDeliveryRequest,
    ) -> vod_20170321_models.CreateVodRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vod_real_time_log_delivery_with_options_async(request, runtime)

    def delete_aiimage_infos_with_options(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAIImageInfosResponse(),
            self.do_rpcrequest('DeleteAIImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aiimage_infos_with_options_async(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAIImageInfosResponse(),
            await self.do_rpcrequest_async('DeleteAIImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aiimage_infos(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    async def delete_aiimage_infos_async(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aiimage_infos_with_options_async(request, runtime)

    def delete_aitemplate_with_options(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAITemplateResponse(),
            self.do_rpcrequest('DeleteAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAITemplateResponse(),
            await self.do_rpcrequest_async('DeleteAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aitemplate(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    async def delete_aitemplate_async(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aitemplate_with_options_async(request, runtime)

    def delete_app_info_with_options(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAppInfoResponse(),
            self.do_rpcrequest('DeleteAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_info_with_options_async(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAppInfoResponse(),
            await self.do_rpcrequest_async('DeleteAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_info(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    async def delete_app_info_async(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_info_with_options_async(request, runtime)

    def delete_attached_media_with_options(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAttachedMediaResponse(),
            self.do_rpcrequest('DeleteAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_attached_media_with_options_async(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAttachedMediaResponse(),
            await self.do_rpcrequest_async('DeleteAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_attached_media(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    async def delete_attached_media_async(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_attached_media_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteCategoryResponse(),
            self.do_rpcrequest('DeleteCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteCategoryResponse(),
            await self.do_rpcrequest_async('DeleteCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_category(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_detection_template_with_options(
        self,
        request: vod_20170321_models.DeleteDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteDetectionTemplateResponse(),
            self.do_rpcrequest('DeleteDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_detection_template_with_options_async(
        self,
        request: vod_20170321_models.DeleteDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteDetectionTemplateResponse(),
            await self.do_rpcrequest_async('DeleteDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_detection_template(
        self,
        request: vod_20170321_models.DeleteDetectionTemplateRequest,
    ) -> vod_20170321_models.DeleteDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_detection_template_with_options(request, runtime)

    async def delete_detection_template_async(
        self,
        request: vod_20170321_models.DeleteDetectionTemplateRequest,
    ) -> vod_20170321_models.DeleteDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_detection_template_with_options_async(request, runtime)

    def delete_dynamic_image_with_options(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteDynamicImageResponse(),
            self.do_rpcrequest('DeleteDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dynamic_image_with_options_async(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteDynamicImageResponse(),
            await self.do_rpcrequest_async('DeleteDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dynamic_image(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_image_with_options(request, runtime)

    async def delete_dynamic_image_async(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dynamic_image_with_options_async(request, runtime)

    def delete_editing_project_with_options(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteEditingProjectResponse(),
            self.do_rpcrequest('DeleteEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_editing_project_with_options_async(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteEditingProjectResponse(),
            await self.do_rpcrequest_async('DeleteEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_editing_project(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_with_options(request, runtime)

    async def delete_editing_project_async(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_project_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: vod_20170321_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteImageResponse(),
            self.do_rpcrequest('DeleteImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: vod_20170321_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteImageResponse(),
            await self.do_rpcrequest_async('DeleteImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image(
        self,
        request: vod_20170321_models.DeleteImageRequest,
    ) -> vod_20170321_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: vod_20170321_models.DeleteImageRequest,
    ) -> vod_20170321_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_message_callback_with_options(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMessageCallbackResponse(),
            self.do_rpcrequest('DeleteMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_message_callback_with_options_async(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMessageCallbackResponse(),
            await self.do_rpcrequest_async('DeleteMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_message_callback(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    async def delete_message_callback_async(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_callback_with_options_async(request, runtime)

    def delete_mezzanines_with_options(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMezzaninesResponse(),
            self.do_rpcrequest('DeleteMezzanines', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mezzanines_with_options_async(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMezzaninesResponse(),
            await self.do_rpcrequest_async('DeleteMezzanines', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mezzanines(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    async def delete_mezzanines_async(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mezzanines_with_options_async(request, runtime)

    def delete_multipart_upload_with_options(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMultipartUploadResponse(),
            self.do_rpcrequest('DeleteMultipartUpload', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_multipart_upload_with_options_async(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMultipartUploadResponse(),
            await self.do_rpcrequest_async('DeleteMultipartUpload', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_multipart_upload(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_multipart_upload_with_options(request, runtime)

    async def delete_multipart_upload_async(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_multipart_upload_with_options_async(request, runtime)

    def delete_stream_with_options(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteStreamResponse(),
            self.do_rpcrequest('DeleteStream', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stream_with_options_async(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteStreamResponse(),
            await self.do_rpcrequest_async('DeleteStream', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stream(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
    ) -> vod_20170321_models.DeleteStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_with_options(request, runtime)

    async def delete_stream_async(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
    ) -> vod_20170321_models.DeleteStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stream_with_options_async(request, runtime)

    def delete_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('DeleteTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('DeleteTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_transcode_template_group(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    async def delete_transcode_template_group_async(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transcode_template_group_with_options_async(request, runtime)

    def delete_video_with_options(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVideoResponse(),
            self.do_rpcrequest('DeleteVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_video_with_options_async(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVideoResponse(),
            await self.do_rpcrequest_async('DeleteVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_video(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
    ) -> vod_20170321_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    async def delete_video_async(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
    ) -> vod_20170321_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_video_with_options_async(request, runtime)

    def delete_vod_domain_with_options(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodDomainResponse(),
            self.do_rpcrequest('DeleteVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodDomainResponse(),
            await self.do_rpcrequest_async('DeleteVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_domain(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    async def delete_vod_domain_async(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_domain_with_options_async(request, runtime)

    def delete_vod_realtime_log_delivery_with_options(
        self,
        request: vod_20170321_models.DeleteVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DeleteVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_vod_realtime_log_delivery_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DeleteVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_vod_realtime_log_delivery(
        self,
        request: vod_20170321_models.DeleteVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_realtime_log_delivery_with_options(request, runtime)

    async def delete_vod_realtime_log_delivery_async(
        self,
        request: vod_20170321_models.DeleteVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DeleteVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_realtime_log_delivery_with_options_async(request, runtime)

    def delete_vod_specific_config_with_options(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodSpecificConfigResponse(),
            self.do_rpcrequest('DeleteVodSpecificConfig', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_specific_config_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodSpecificConfigResponse(),
            await self.do_rpcrequest_async('DeleteVodSpecificConfig', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_specific_config(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_specific_config_with_options(request, runtime)

    async def delete_vod_specific_config_async(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_specific_config_with_options_async(request, runtime)

    def delete_vod_template_with_options(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodTemplateResponse(),
            self.do_rpcrequest('DeleteVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_template_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodTemplateResponse(),
            await self.do_rpcrequest_async('DeleteVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_template(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_template_with_options(request, runtime)

    async def delete_vod_template_async(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_template_with_options_async(request, runtime)

    def delete_watermark_with_options(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteWatermarkResponse(),
            self.do_rpcrequest('DeleteWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_watermark_with_options_async(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteWatermarkResponse(),
            await self.do_rpcrequest_async('DeleteWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_watermark(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    async def delete_watermark_async(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_watermark_with_options_async(request, runtime)

    def describe_play_top_videos_with_options(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayTopVideosResponse(),
            self.do_rpcrequest('DescribePlayTopVideos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_top_videos_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayTopVideosResponse(),
            await self.do_rpcrequest_async('DescribePlayTopVideos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_top_videos(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    async def describe_play_top_videos_async(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_top_videos_with_options_async(request, runtime)

    def describe_play_user_avg_with_options(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserAvgResponse(),
            self.do_rpcrequest('DescribePlayUserAvg', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_user_avg_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserAvgResponse(),
            await self.do_rpcrequest_async('DescribePlayUserAvg', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_user_avg(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    async def describe_play_user_avg_async(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_user_avg_with_options_async(request, runtime)

    def describe_play_user_total_with_options(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserTotalResponse(),
            self.do_rpcrequest('DescribePlayUserTotal', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_user_total_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserTotalResponse(),
            await self.do_rpcrequest_async('DescribePlayUserTotal', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_user_total(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    async def describe_play_user_total_async(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_user_total_with_options_async(request, runtime)

    def describe_play_video_statis_with_options(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayVideoStatisResponse(),
            self.do_rpcrequest('DescribePlayVideoStatis', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_video_statis_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayVideoStatisResponse(),
            await self.do_rpcrequest_async('DescribePlayVideoStatis', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_video_statis(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_video_statis_with_options(request, runtime)

    async def describe_play_video_statis_async(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_video_statis_with_options_async(request, runtime)

    def describe_vod_aidata_with_options(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodAIDataResponse(),
            self.do_rpcrequest('DescribeVodAIData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_aidata_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodAIDataResponse(),
            await self.do_rpcrequest_async('DescribeVodAIData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_aidata(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_aidata_with_options(request, runtime)

    async def describe_vod_aidata_async(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_aidata_with_options_async(request, runtime)

    def describe_vod_certificate_list_with_options(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodCertificateListResponse(),
            self.do_rpcrequest('DescribeVodCertificateList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_certificate_list_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodCertificateListResponse(),
            await self.do_rpcrequest_async('DescribeVodCertificateList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_certificate_list(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    async def describe_vod_certificate_list_async(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_certificate_list_with_options_async(request, runtime)

    def describe_vod_domain_bps_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainBpsDataResponse(),
            self.do_rpcrequest('DescribeVodDomainBpsData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_bps_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainBpsData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_bps_data(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_bps_data_with_options(request, runtime)

    async def describe_vod_domain_bps_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_bps_data_with_options_async(request, runtime)

    def describe_vod_domain_certificate_info_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainCertificateInfoResponse(),
            self.do_rpcrequest('DescribeVodDomainCertificateInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_certificate_info_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainCertificateInfoResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainCertificateInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_certificate_info(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_certificate_info_with_options(request, runtime)

    async def describe_vod_domain_certificate_info_async(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_certificate_info_with_options_async(request, runtime)

    def describe_vod_domain_configs_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainConfigsResponse(),
            self.do_rpcrequest('DescribeVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_configs_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainConfigsResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_configs(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    async def describe_vod_domain_configs_async(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_configs_with_options_async(request, runtime)

    def describe_vod_domain_detail_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainDetailResponse(),
            self.do_rpcrequest('DescribeVodDomainDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_detail_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainDetailResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_detail(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    async def describe_vod_domain_detail_async(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_detail_with_options_async(request, runtime)

    def describe_vod_domain_log_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainLogResponse(),
            self.do_rpcrequest('DescribeVodDomainLog', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_log_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainLogResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainLog', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_log(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    async def describe_vod_domain_log_async(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_log_with_options_async(request, runtime)

    def describe_vod_domain_realtime_log_delivery_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DescribeVodDomainRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_realtime_log_delivery_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_realtime_log_delivery(
        self,
        request: vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_realtime_log_delivery_with_options(request, runtime)

    async def describe_vod_domain_realtime_log_delivery_async(
        self,
        request: vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DescribeVodDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_realtime_log_delivery_with_options_async(request, runtime)

    def describe_vod_domain_traffic_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainTrafficDataResponse(),
            self.do_rpcrequest('DescribeVodDomainTrafficData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_traffic_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainTrafficData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_traffic_data(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_traffic_data_with_options(request, runtime)

    async def describe_vod_domain_traffic_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_traffic_data_with_options_async(request, runtime)

    def describe_vod_domain_usage_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainUsageDataResponse(),
            self.do_rpcrequest('DescribeVodDomainUsageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_usage_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainUsageDataResponse(),
            await self.do_rpcrequest_async('DescribeVodDomainUsageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_usage_data(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    async def describe_vod_domain_usage_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_usage_data_with_options_async(request, runtime)

    def describe_vod_refresh_quota_with_options(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshQuotaResponse(),
            self.do_rpcrequest('DescribeVodRefreshQuota', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_refresh_quota_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshQuotaResponse(),
            await self.do_rpcrequest_async('DescribeVodRefreshQuota', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_refresh_quota(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_quota_with_options(request, runtime)

    async def describe_vod_refresh_quota_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_refresh_quota_with_options_async(request, runtime)

    def describe_vod_refresh_tasks_with_options(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshTasksResponse(),
            self.do_rpcrequest('DescribeVodRefreshTasks', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_refresh_tasks_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshTasksResponse(),
            await self.do_rpcrequest_async('DescribeVodRefreshTasks', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_refresh_tasks(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_tasks_with_options(request, runtime)

    async def describe_vod_refresh_tasks_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_refresh_tasks_with_options_async(request, runtime)

    def describe_vod_storage_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodStorageDataResponse(),
            self.do_rpcrequest('DescribeVodStorageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_storage_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodStorageDataResponse(),
            await self.do_rpcrequest_async('DescribeVodStorageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_storage_data(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_storage_data_with_options(request, runtime)

    async def describe_vod_storage_data_async(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_storage_data_with_options_async(request, runtime)

    def describe_vod_tag_resources_with_options(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodTagResourcesResponse(),
            self.do_rpcrequest('DescribeVodTagResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_tag_resources_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodTagResourcesResponse(),
            await self.do_rpcrequest_async('DescribeVodTagResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_tag_resources(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_tag_resources_with_options(request, runtime)

    async def describe_vod_tag_resources_async(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_tag_resources_with_options_async(request, runtime)

    def describe_vod_transcode_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodTranscodeDataResponse(),
            self.do_rpcrequest('DescribeVodTranscodeData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_transcode_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodTranscodeDataResponse(),
            await self.do_rpcrequest_async('DescribeVodTranscodeData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_transcode_data(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_transcode_data_with_options(request, runtime)

    async def describe_vod_transcode_data_async(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_transcode_data_with_options_async(request, runtime)

    def describe_vod_user_domains_with_options(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodUserDomainsResponse(),
            self.do_rpcrequest('DescribeVodUserDomains', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_user_domains_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodUserDomainsResponse(),
            await self.do_rpcrequest_async('DescribeVodUserDomains', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_user_domains(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_user_domains_with_options(request, runtime)

    async def describe_vod_user_domains_async(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_user_domains_with_options_async(request, runtime)

    def describe_vod_user_tags_with_options(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodUserTagsResponse(),
            self.do_rpcrequest('DescribeVodUserTags', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_user_tags_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodUserTagsResponse(),
            await self.do_rpcrequest_async('DescribeVodUserTags', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_user_tags(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_user_tags_with_options(request, runtime)

    async def describe_vod_user_tags_async(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_user_tags_with_options_async(request, runtime)

    def describe_vod_verify_content_with_options(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodVerifyContentResponse(),
            self.do_rpcrequest('DescribeVodVerifyContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_verify_content_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodVerifyContentResponse(),
            await self.do_rpcrequest_async('DescribeVodVerifyContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_verify_content(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_verify_content_with_options(request, runtime)

    async def describe_vod_verify_content_async(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_verify_content_with_options_async(request, runtime)

    def detach_app_policy_from_identity_with_options(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DetachAppPolicyFromIdentityResponse(),
            self.do_rpcrequest('DetachAppPolicyFromIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_app_policy_from_identity_with_options_async(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.DetachAppPolicyFromIdentityResponse(),
            await self.do_rpcrequest_async('DetachAppPolicyFromIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_app_policy_from_identity(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_app_policy_from_identity_with_options(request, runtime)

    async def detach_app_policy_from_identity_async(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_app_policy_from_identity_with_options_async(request, runtime)

    def disable_vod_realtime_log_delivery_with_options(
        self,
        request: vod_20170321_models.DisableVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DisableVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DisableVodRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DisableVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def disable_vod_realtime_log_delivery_with_options_async(
        self,
        request: vod_20170321_models.DisableVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DisableVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.DisableVodRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DisableVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def disable_vod_realtime_log_delivery(
        self,
        request: vod_20170321_models.DisableVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DisableVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_vod_realtime_log_delivery_with_options(request, runtime)

    async def disable_vod_realtime_log_delivery_async(
        self,
        request: vod_20170321_models.DisableVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.DisableVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_vod_realtime_log_delivery_with_options_async(request, runtime)

    def enable_vod_realtime_log_delivery_with_options(
        self,
        request: vod_20170321_models.EnableVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.EnableVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.EnableVodRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('EnableVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def enable_vod_realtime_log_delivery_with_options_async(
        self,
        request: vod_20170321_models.EnableVodRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.EnableVodRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.EnableVodRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('EnableVodRealtimeLogDelivery', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def enable_vod_realtime_log_delivery(
        self,
        request: vod_20170321_models.EnableVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.EnableVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_vod_realtime_log_delivery_with_options(request, runtime)

    async def enable_vod_realtime_log_delivery_async(
        self,
        request: vod_20170321_models.EnableVodRealtimeLogDeliveryRequest,
    ) -> vod_20170321_models.EnableVodRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_vod_realtime_log_delivery_with_options_async(request, runtime)

    def get_aicaption_extraction_jobs_with_options(
        self,
        request: vod_20170321_models.GetAICaptionExtractionJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAICaptionExtractionJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAICaptionExtractionJobsResponse(),
            self.do_rpcrequest('GetAICaptionExtractionJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aicaption_extraction_jobs_with_options_async(
        self,
        request: vod_20170321_models.GetAICaptionExtractionJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAICaptionExtractionJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAICaptionExtractionJobsResponse(),
            await self.do_rpcrequest_async('GetAICaptionExtractionJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aicaption_extraction_jobs(
        self,
        request: vod_20170321_models.GetAICaptionExtractionJobsRequest,
    ) -> vod_20170321_models.GetAICaptionExtractionJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aicaption_extraction_jobs_with_options(request, runtime)

    async def get_aicaption_extraction_jobs_async(
        self,
        request: vod_20170321_models.GetAICaptionExtractionJobsRequest,
    ) -> vod_20170321_models.GetAICaptionExtractionJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aicaption_extraction_jobs_with_options_async(request, runtime)

    def get_aiimage_jobs_with_options(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIImageJobsResponse(),
            self.do_rpcrequest('GetAIImageJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiimage_jobs_with_options_async(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIImageJobsResponse(),
            await self.do_rpcrequest_async('GetAIImageJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiimage_jobs(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    async def get_aiimage_jobs_async(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiimage_jobs_with_options_async(request, runtime)

    def get_aimedia_audit_job_with_options(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIMediaAuditJobResponse(),
            self.do_rpcrequest('GetAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aimedia_audit_job_with_options_async(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIMediaAuditJobResponse(),
            await self.do_rpcrequest_async('GetAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aimedia_audit_job(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    async def get_aimedia_audit_job_async(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aimedia_audit_job_with_options_async(request, runtime)

    def get_aitemplate_with_options(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAITemplateResponse(),
            self.do_rpcrequest('GetAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAITemplateResponse(),
            await self.do_rpcrequest_async('GetAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aitemplate(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
    ) -> vod_20170321_models.GetAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    async def get_aitemplate_async(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
    ) -> vod_20170321_models.GetAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aitemplate_with_options_async(request, runtime)

    def get_aivideo_tag_result_with_options(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIVideoTagResultResponse(),
            self.do_rpcrequest('GetAIVideoTagResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aivideo_tag_result_with_options_async(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIVideoTagResultResponse(),
            await self.do_rpcrequest_async('GetAIVideoTagResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aivideo_tag_result(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    async def get_aivideo_tag_result_async(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aivideo_tag_result_with_options_async(request, runtime)

    def get_app_infos_with_options(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAppInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAppInfosResponse(),
            self.do_rpcrequest('GetAppInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_infos_with_options_async(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAppInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAppInfosResponse(),
            await self.do_rpcrequest_async('GetAppInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_infos(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
    ) -> vod_20170321_models.GetAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_infos_with_options(request, runtime)

    async def get_app_infos_async(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
    ) -> vod_20170321_models.GetAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_infos_with_options_async(request, runtime)

    def get_attached_media_info_with_options(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAttachedMediaInfoResponse(),
            self.do_rpcrequest('GetAttachedMediaInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_attached_media_info_with_options_async(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAttachedMediaInfoResponse(),
            await self.do_rpcrequest_async('GetAttachedMediaInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_attached_media_info(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_attached_media_info_with_options(request, runtime)

    async def get_attached_media_info_async(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_attached_media_info_with_options_async(request, runtime)

    def get_audit_history_with_options(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAuditHistoryResponse(),
            self.do_rpcrequest('GetAuditHistory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audit_history_with_options_async(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAuditHistoryResponse(),
            await self.do_rpcrequest_async('GetAuditHistory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_history(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_history_with_options(request, runtime)

    async def get_audit_history_async(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_history_with_options_async(request, runtime)

    def get_categories_with_options(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetCategoriesResponse(),
            self.do_rpcrequest('GetCategories', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_categories_with_options_async(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetCategoriesResponse(),
            await self.do_rpcrequest_async('GetCategories', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_categories(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
    ) -> vod_20170321_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    async def get_categories_async(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
    ) -> vod_20170321_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_categories_with_options_async(request, runtime)

    def get_default_aitemplate_with_options(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDefaultAITemplateResponse(),
            self.do_rpcrequest('GetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDefaultAITemplateResponse(),
            await self.do_rpcrequest_async('GetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_aitemplate(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_aitemplate_with_options(request, runtime)

    async def get_default_aitemplate_async(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_aitemplate_with_options_async(request, runtime)

    def get_detection_job_with_options(
        self,
        request: vod_20170321_models.GetDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionJobResponse(),
            self.do_rpcrequest('GetDetectionJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_detection_job_with_options_async(
        self,
        request: vod_20170321_models.GetDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionJobResponse(),
            await self.do_rpcrequest_async('GetDetectionJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_detection_job(
        self,
        request: vod_20170321_models.GetDetectionJobRequest,
    ) -> vod_20170321_models.GetDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_job_with_options(request, runtime)

    async def get_detection_job_async(
        self,
        request: vod_20170321_models.GetDetectionJobRequest,
    ) -> vod_20170321_models.GetDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_job_with_options_async(request, runtime)

    def get_detection_result_with_options(
        self,
        request: vod_20170321_models.GetDetectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionResultResponse(),
            self.do_rpcrequest('GetDetectionResult', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_detection_result_with_options_async(
        self,
        request: vod_20170321_models.GetDetectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionResultResponse(),
            await self.do_rpcrequest_async('GetDetectionResult', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_detection_result(
        self,
        request: vod_20170321_models.GetDetectionResultRequest,
    ) -> vod_20170321_models.GetDetectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_result_with_options(request, runtime)

    async def get_detection_result_async(
        self,
        request: vod_20170321_models.GetDetectionResultRequest,
    ) -> vod_20170321_models.GetDetectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_result_with_options_async(request, runtime)

    def get_detection_template_with_options(
        self,
        request: vod_20170321_models.GetDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionTemplateResponse(),
            self.do_rpcrequest('GetDetectionTemplate', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_detection_template_with_options_async(
        self,
        request: vod_20170321_models.GetDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDetectionTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDetectionTemplateResponse(),
            await self.do_rpcrequest_async('GetDetectionTemplate', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_detection_template(
        self,
        request: vod_20170321_models.GetDetectionTemplateRequest,
    ) -> vod_20170321_models.GetDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_template_with_options(request, runtime)

    async def get_detection_template_async(
        self,
        request: vod_20170321_models.GetDetectionTemplateRequest,
    ) -> vod_20170321_models.GetDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_template_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectResponse(),
            self.do_rpcrequest('GetEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_with_options_async(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectResponse(),
            await self.do_rpcrequest_async('GetEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_editing_project(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    async def get_editing_project_async(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_with_options_async(request, runtime)

    def get_editing_project_materials_with_options(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectMaterialsResponse(),
            self.do_rpcrequest('GetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_materials_with_options_async(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectMaterialsResponse(),
            await self.do_rpcrequest_async('GetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_editing_project_materials(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    async def get_editing_project_materials_async(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_materials_with_options_async(request, runtime)

    def get_image_info_with_options(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetImageInfoResponse(),
            self.do_rpcrequest('GetImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_info_with_options_async(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetImageInfoResponse(),
            await self.do_rpcrequest_async('GetImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_info(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
    ) -> vod_20170321_models.GetImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_info_with_options(request, runtime)

    async def get_image_info_async(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
    ) -> vod_20170321_models.GetImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_info_with_options_async(request, runtime)

    def get_media_audit_audio_result_detail_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditAudioResultDetailResponse(),
            self.do_rpcrequest('GetMediaAuditAudioResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_audio_result_detail_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditAudioResultDetailResponse(),
            await self.do_rpcrequest_async('GetMediaAuditAudioResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_audio_result_detail(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_audio_result_detail_with_options(request, runtime)

    async def get_media_audit_audio_result_detail_async(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_audio_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultResponse(),
            self.do_rpcrequest('GetMediaAuditResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultResponse(),
            await self.do_rpcrequest_async('GetMediaAuditResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_with_options(request, runtime)

    async def get_media_audit_result_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_with_options_async(request, runtime)

    def get_media_audit_result_detail_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultDetailResponse(),
            self.do_rpcrequest('GetMediaAuditResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_detail_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultDetailResponse(),
            await self.do_rpcrequest_async('GetMediaAuditResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result_detail(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_detail_with_options(request, runtime)

    async def get_media_audit_result_detail_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_timeline_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultTimelineResponse(),
            self.do_rpcrequest('GetMediaAuditResultTimeline', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_timeline_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultTimelineResponse(),
            await self.do_rpcrequest_async('GetMediaAuditResultTimeline', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result_timeline(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_timeline_with_options(request, runtime)

    async def get_media_audit_result_timeline_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_timeline_with_options_async(request, runtime)

    def get_media_dnaresult_with_options(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaDNAResultResponse(),
            self.do_rpcrequest('GetMediaDNAResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_dnaresult_with_options_async(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaDNAResultResponse(),
            await self.do_rpcrequest_async('GetMediaDNAResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_dnaresult(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_dnaresult_with_options(request, runtime)

    async def get_media_dnaresult_async(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_dnaresult_with_options_async(request, runtime)

    def get_message_callback_with_options(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMessageCallbackResponse(),
            self.do_rpcrequest('GetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_message_callback_with_options_async(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMessageCallbackResponse(),
            await self.do_rpcrequest_async('GetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_message_callback(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    async def get_message_callback_async(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_callback_with_options_async(request, runtime)

    def get_mezzanine_info_with_options(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMezzanineInfoResponse(),
            self.do_rpcrequest('GetMezzanineInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mezzanine_info_with_options_async(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMezzanineInfoResponse(),
            await self.do_rpcrequest_async('GetMezzanineInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mezzanine_info(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    async def get_mezzanine_info_async(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mezzanine_info_with_options_async(request, runtime)

    def get_play_info_with_options(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetPlayInfoResponse(),
            self.do_rpcrequest('GetPlayInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_play_info_with_options_async(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetPlayInfoResponse(),
            await self.do_rpcrequest_async('GetPlayInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_play_info(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    async def get_play_info_async(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_play_info_with_options_async(request, runtime)

    def get_transcode_summary_with_options(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeSummaryResponse(),
            self.do_rpcrequest('GetTranscodeSummary', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_summary_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeSummaryResponse(),
            await self.do_rpcrequest_async('GetTranscodeSummary', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_summary(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_summary_with_options(request, runtime)

    async def get_transcode_summary_async(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_summary_with_options_async(request, runtime)

    def get_transcode_task_with_options(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTaskResponse(),
            self.do_rpcrequest('GetTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_task_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTaskResponse(),
            await self.do_rpcrequest_async('GetTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_task(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    async def get_transcode_task_async(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_task_with_options_async(request, runtime)

    def get_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('GetTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('GetTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_template_group(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    async def get_transcode_template_group_async(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_template_group_with_options_async(request, runtime)

    def get_urlupload_infos_with_options(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetURLUploadInfosResponse(),
            self.do_rpcrequest('GetURLUploadInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_urlupload_infos_with_options_async(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetURLUploadInfosResponse(),
            await self.do_rpcrequest_async('GetURLUploadInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_urlupload_infos(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    async def get_urlupload_infos_async(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_urlupload_infos_with_options_async(request, runtime)

    def get_upload_details_with_options(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetUploadDetailsResponse(),
            self.do_rpcrequest('GetUploadDetails', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_upload_details_with_options_async(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetUploadDetailsResponse(),
            await self.do_rpcrequest_async('GetUploadDetails', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_upload_details(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    async def get_upload_details_async(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_details_with_options_async(request, runtime)

    def get_video_info_with_options(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfoResponse(),
            self.do_rpcrequest('GetVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_info_with_options_async(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfoResponse(),
            await self.do_rpcrequest_async('GetVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_info(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    async def get_video_info_async(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_info_with_options_async(request, runtime)

    def get_video_infos_with_options(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfosResponse(),
            self.do_rpcrequest('GetVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_infos_with_options_async(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfosResponse(),
            await self.do_rpcrequest_async('GetVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_infos(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_infos_with_options(request, runtime)

    async def get_video_infos_async(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_infos_with_options_async(request, runtime)

    def get_video_list_with_options(
        self,
        request: vod_20170321_models.GetVideoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoListResponse(),
            self.do_rpcrequest('GetVideoList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_list_with_options_async(
        self,
        request: vod_20170321_models.GetVideoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoListResponse(),
            await self.do_rpcrequest_async('GetVideoList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_list(
        self,
        request: vod_20170321_models.GetVideoListRequest,
    ) -> vod_20170321_models.GetVideoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    async def get_video_list_async(
        self,
        request: vod_20170321_models.GetVideoListRequest,
    ) -> vod_20170321_models.GetVideoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_list_with_options_async(request, runtime)

    def get_video_play_auth_with_options(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoPlayAuthResponse(),
            self.do_rpcrequest('GetVideoPlayAuth', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_play_auth_with_options_async(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoPlayAuthResponse(),
            await self.do_rpcrequest_async('GetVideoPlayAuth', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_play_auth(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_play_auth_with_options(request, runtime)

    async def get_video_play_auth_async(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_play_auth_with_options_async(request, runtime)

    def get_vod_template_with_options(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVodTemplateResponse(),
            self.do_rpcrequest('GetVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_vod_template_with_options_async(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVodTemplateResponse(),
            await self.do_rpcrequest_async('GetVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_vod_template(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vod_template_with_options(request, runtime)

    async def get_vod_template_async(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vod_template_with_options_async(request, runtime)

    def get_watermark_with_options(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetWatermarkResponse(),
            self.do_rpcrequest('GetWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_watermark_with_options_async(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.GetWatermarkResponse(),
            await self.do_rpcrequest_async('GetWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_watermark(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
    ) -> vod_20170321_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_watermark_with_options(request, runtime)

    async def get_watermark_async(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
    ) -> vod_20170321_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_watermark_with_options_async(request, runtime)

    def list_aiimage_info_with_options(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIImageInfoResponse(),
            self.do_rpcrequest('ListAIImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aiimage_info_with_options_async(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIImageInfoResponse(),
            await self.do_rpcrequest_async('ListAIImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aiimage_info(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    async def list_aiimage_info_async(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aiimage_info_with_options_async(request, runtime)

    def list_aijob_with_options(
        self,
        request: vod_20170321_models.ListAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIJobResponse(),
            self.do_rpcrequest('ListAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aijob_with_options_async(
        self,
        request: vod_20170321_models.ListAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIJobResponse(),
            await self.do_rpcrequest_async('ListAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aijob(
        self,
        request: vod_20170321_models.ListAIJobRequest,
    ) -> vod_20170321_models.ListAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    async def list_aijob_async(
        self,
        request: vod_20170321_models.ListAIJobRequest,
    ) -> vod_20170321_models.ListAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aijob_with_options_async(request, runtime)

    def list_aitemplate_with_options(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAITemplateResponse(),
            self.do_rpcrequest('ListAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAITemplateResponse(),
            await self.do_rpcrequest_async('ListAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aitemplate(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
    ) -> vod_20170321_models.ListAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    async def list_aitemplate_async(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
    ) -> vod_20170321_models.ListAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aitemplate_with_options_async(request, runtime)

    def list_app_info_with_options(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppInfoResponse(),
            self.do_rpcrequest('ListAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_info_with_options_async(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppInfoResponse(),
            await self.do_rpcrequest_async('ListAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_info(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
    ) -> vod_20170321_models.ListAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    async def list_app_info_async(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
    ) -> vod_20170321_models.ListAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_info_with_options_async(request, runtime)

    def list_app_policies_for_identity_with_options(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppPoliciesForIdentityResponse(),
            self.do_rpcrequest('ListAppPoliciesForIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_policies_for_identity_with_options_async(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppPoliciesForIdentityResponse(),
            await self.do_rpcrequest_async('ListAppPoliciesForIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_policies_for_identity(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_policies_for_identity_with_options(request, runtime)

    async def list_app_policies_for_identity_async(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_policies_for_identity_with_options_async(request, runtime)

    def list_audit_security_ip_with_options(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAuditSecurityIpResponse(),
            self.do_rpcrequest('ListAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_audit_security_ip_with_options_async(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAuditSecurityIpResponse(),
            await self.do_rpcrequest_async('ListAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_audit_security_ip(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_audit_security_ip_with_options(request, runtime)

    async def list_audit_security_ip_async(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_audit_security_ip_with_options_async(request, runtime)

    def list_detection_job_with_options(
        self,
        request: vod_20170321_models.ListDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDetectionJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDetectionJobResponse(),
            self.do_rpcrequest('ListDetectionJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_detection_job_with_options_async(
        self,
        request: vod_20170321_models.ListDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDetectionJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDetectionJobResponse(),
            await self.do_rpcrequest_async('ListDetectionJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_detection_job(
        self,
        request: vod_20170321_models.ListDetectionJobRequest,
    ) -> vod_20170321_models.ListDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detection_job_with_options(request, runtime)

    async def list_detection_job_async(
        self,
        request: vod_20170321_models.ListDetectionJobRequest,
    ) -> vod_20170321_models.ListDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detection_job_with_options_async(request, runtime)

    def list_detection_template_with_options(
        self,
        request: vod_20170321_models.ListDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDetectionTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDetectionTemplateResponse(),
            self.do_rpcrequest('ListDetectionTemplate', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_detection_template_with_options_async(
        self,
        request: vod_20170321_models.ListDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDetectionTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDetectionTemplateResponse(),
            await self.do_rpcrequest_async('ListDetectionTemplate', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_detection_template(
        self,
        request: vod_20170321_models.ListDetectionTemplateRequest,
    ) -> vod_20170321_models.ListDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detection_template_with_options(request, runtime)

    async def list_detection_template_async(
        self,
        request: vod_20170321_models.ListDetectionTemplateRequest,
    ) -> vod_20170321_models.ListDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detection_template_with_options_async(request, runtime)

    def list_dynamic_image_with_options(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDynamicImageResponse(),
            self.do_rpcrequest('ListDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dynamic_image_with_options_async(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDynamicImageResponse(),
            await self.do_rpcrequest_async('ListDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dynamic_image(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_image_with_options(request, runtime)

    async def list_dynamic_image_async(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_image_with_options_async(request, runtime)

    def list_letter_send_job_with_options(
        self,
        request: vod_20170321_models.ListLetterSendJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLetterSendJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListLetterSendJobResponse(),
            self.do_rpcrequest('ListLetterSendJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_letter_send_job_with_options_async(
        self,
        request: vod_20170321_models.ListLetterSendJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLetterSendJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListLetterSendJobResponse(),
            await self.do_rpcrequest_async('ListLetterSendJob', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_letter_send_job(
        self,
        request: vod_20170321_models.ListLetterSendJobRequest,
    ) -> vod_20170321_models.ListLetterSendJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_letter_send_job_with_options(request, runtime)

    async def list_letter_send_job_async(
        self,
        request: vod_20170321_models.ListLetterSendJobRequest,
    ) -> vod_20170321_models.ListLetterSendJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_letter_send_job_with_options_async(request, runtime)

    def list_live_record_video_with_options(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListLiveRecordVideoResponse(),
            self.do_rpcrequest('ListLiveRecordVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_live_record_video_with_options_async(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListLiveRecordVideoResponse(),
            await self.do_rpcrequest_async('ListLiveRecordVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_live_record_video(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    async def list_live_record_video_async(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_video_with_options_async(request, runtime)

    def list_media_dnadelete_job_with_options(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListMediaDNADeleteJobResponse(),
            self.do_rpcrequest('ListMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_dnadelete_job_with_options_async(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListMediaDNADeleteJobResponse(),
            await self.do_rpcrequest_async('ListMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_dnadelete_job(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_dnadelete_job_with_options(request, runtime)

    async def list_media_dnadelete_job_async(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_dnadelete_job_with_options_async(request, runtime)

    def list_snapshots_with_options(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListSnapshotsResponse(),
            self.do_rpcrequest('ListSnapshots', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListSnapshotsResponse(),
            await self.do_rpcrequest_async('ListSnapshots', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_snapshots(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def list_transcode_task_with_options(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTaskResponse(),
            self.do_rpcrequest('ListTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_transcode_task_with_options_async(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTaskResponse(),
            await self.do_rpcrequest_async('ListTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transcode_task(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    async def list_transcode_task_async(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transcode_task_with_options_async(request, runtime)

    def list_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('ListTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('ListTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transcode_template_group(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_template_group_with_options(request, runtime)

    async def list_transcode_template_group_async(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transcode_template_group_with_options_async(request, runtime)

    def list_vod_realtime_log_delivery_domains_with_options(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse(),
            self.do_rpcrequest('ListVodRealtimeLogDeliveryDomains', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_vod_realtime_log_delivery_domains_with_options_async(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse(),
            await self.do_rpcrequest_async('ListVodRealtimeLogDeliveryDomains', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_vod_realtime_log_delivery_domains(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryDomainsRequest,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vod_realtime_log_delivery_domains_with_options(request, runtime)

    async def list_vod_realtime_log_delivery_domains_async(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryDomainsRequest,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vod_realtime_log_delivery_domains_with_options_async(request, runtime)

    def list_vod_realtime_log_delivery_infos_with_options(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse(),
            self.do_rpcrequest('ListVodRealtimeLogDeliveryInfos', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_vod_realtime_log_delivery_infos_with_options_async(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse(),
            await self.do_rpcrequest_async('ListVodRealtimeLogDeliveryInfos', '2017-03-21', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_vod_realtime_log_delivery_infos(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryInfosRequest,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vod_realtime_log_delivery_infos_with_options(request, runtime)

    async def list_vod_realtime_log_delivery_infos_async(
        self,
        request: vod_20170321_models.ListVodRealtimeLogDeliveryInfosRequest,
    ) -> vod_20170321_models.ListVodRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vod_realtime_log_delivery_infos_with_options_async(request, runtime)

    def list_vod_template_with_options(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodTemplateResponse(),
            self.do_rpcrequest('ListVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vod_template_with_options_async(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodTemplateResponse(),
            await self.do_rpcrequest_async('ListVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vod_template(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vod_template_with_options(request, runtime)

    async def list_vod_template_async(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vod_template_with_options_async(request, runtime)

    def list_watermark_with_options(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListWatermarkResponse(),
            self.do_rpcrequest('ListWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_watermark_with_options_async(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ListWatermarkResponse(),
            await self.do_rpcrequest_async('ListWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_watermark(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
    ) -> vod_20170321_models.ListWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_watermark_with_options(request, runtime)

    async def list_watermark_async(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
    ) -> vod_20170321_models.ListWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_watermark_with_options_async(request, runtime)

    def move_app_resource_with_options(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.MoveAppResourceResponse(),
            self.do_rpcrequest('MoveAppResource', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_app_resource_with_options_async(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.MoveAppResourceResponse(),
            await self.do_rpcrequest_async('MoveAppResource', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_app_resource(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_app_resource_with_options(request, runtime)

    async def move_app_resource_async(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_app_resource_with_options_async(request, runtime)

    def preload_vod_object_caches_with_options(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.PreloadVodObjectCachesResponse(),
            self.do_rpcrequest('PreloadVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preload_vod_object_caches_with_options_async(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.PreloadVodObjectCachesResponse(),
            await self.do_rpcrequest_async('PreloadVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preload_vod_object_caches(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    async def preload_vod_object_caches_async(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_vod_object_caches_with_options_async(request, runtime)

    def produce_editing_project_video_with_options(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ProduceEditingProjectVideoResponse(),
            self.do_rpcrequest('ProduceEditingProjectVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def produce_editing_project_video_with_options_async(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.ProduceEditingProjectVideoResponse(),
            await self.do_rpcrequest_async('ProduceEditingProjectVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def produce_editing_project_video(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    async def produce_editing_project_video_async(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.produce_editing_project_video_with_options_async(request, runtime)

    def refresh_upload_video_with_options(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshUploadVideoResponse(),
            self.do_rpcrequest('RefreshUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_upload_video_with_options_async(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshUploadVideoResponse(),
            await self.do_rpcrequest_async('RefreshUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_upload_video(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    async def refresh_upload_video_async(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_upload_video_with_options_async(request, runtime)

    def refresh_vod_object_caches_with_options(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshVodObjectCachesResponse(),
            self.do_rpcrequest('RefreshVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_vod_object_caches_with_options_async(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshVodObjectCachesResponse(),
            await self.do_rpcrequest_async('RefreshVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_vod_object_caches(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    async def refresh_vod_object_caches_async(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_vod_object_caches_with_options_async(request, runtime)

    def register_media_with_options(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RegisterMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RegisterMediaResponse(),
            self.do_rpcrequest('RegisterMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_media_with_options_async(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RegisterMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.RegisterMediaResponse(),
            await self.do_rpcrequest_async('RegisterMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
    ) -> vod_20170321_models.RegisterMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_with_options(request, runtime)

    async def register_media_async(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
    ) -> vod_20170321_models.RegisterMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchEditingProjectResponse(),
            self.do_rpcrequest('SearchEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_editing_project_with_options_async(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchEditingProjectResponse(),
            await self.do_rpcrequest_async('SearchEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_editing_project(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    async def search_editing_project_async(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_editing_project_with_options_async(request, runtime)

    def search_media_with_options(
        self,
        request: vod_20170321_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchMediaResponse(),
            self.do_rpcrequest('SearchMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: vod_20170321_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchMediaResponse(),
            await self.do_rpcrequest_async('SearchMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_media(
        self,
        request: vod_20170321_models.SearchMediaRequest,
    ) -> vod_20170321_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: vod_20170321_models.SearchMediaRequest,
    ) -> vod_20170321_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def set_audit_security_ip_with_options(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetAuditSecurityIpResponse(),
            self.do_rpcrequest('SetAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_audit_security_ip_with_options_async(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetAuditSecurityIpResponse(),
            await self.do_rpcrequest_async('SetAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_audit_security_ip(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    async def set_audit_security_ip_async(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_audit_security_ip_with_options_async(request, runtime)

    def set_crossdomain_content_with_options(
        self,
        request: vod_20170321_models.SetCrossdomainContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetCrossdomainContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetCrossdomainContentResponse(),
            self.do_rpcrequest('SetCrossdomainContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_crossdomain_content_with_options_async(
        self,
        request: vod_20170321_models.SetCrossdomainContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetCrossdomainContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetCrossdomainContentResponse(),
            await self.do_rpcrequest_async('SetCrossdomainContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_crossdomain_content(
        self,
        request: vod_20170321_models.SetCrossdomainContentRequest,
    ) -> vod_20170321_models.SetCrossdomainContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_crossdomain_content_with_options(request, runtime)

    async def set_crossdomain_content_async(
        self,
        request: vod_20170321_models.SetCrossdomainContentRequest,
    ) -> vod_20170321_models.SetCrossdomainContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_crossdomain_content_with_options_async(request, runtime)

    def set_default_aitemplate_with_options(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultAITemplateResponse(),
            self.do_rpcrequest('SetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultAITemplateResponse(),
            await self.do_rpcrequest_async('SetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_aitemplate(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_aitemplate_with_options(request, runtime)

    async def set_default_aitemplate_async(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_aitemplate_with_options_async(request, runtime)

    def set_default_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('SetDefaultTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('SetDefaultTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_transcode_template_group(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_transcode_template_group_with_options(request, runtime)

    async def set_default_transcode_template_group_async(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_transcode_template_group_with_options_async(request, runtime)

    def set_default_watermark_with_options(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultWatermarkResponse(),
            self.do_rpcrequest('SetDefaultWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_watermark_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultWatermarkResponse(),
            await self.do_rpcrequest_async('SetDefaultWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_watermark(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_watermark_with_options(request, runtime)

    async def set_default_watermark_async(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_watermark_with_options_async(request, runtime)

    def set_editing_project_materials_with_options(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetEditingProjectMaterialsResponse(),
            self.do_rpcrequest('SetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_editing_project_materials_with_options_async(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetEditingProjectMaterialsResponse(),
            await self.do_rpcrequest_async('SetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_editing_project_materials(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_editing_project_materials_with_options(request, runtime)

    async def set_editing_project_materials_async(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_editing_project_materials_with_options_async(request, runtime)

    def set_message_callback_with_options(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetMessageCallbackResponse(),
            self.do_rpcrequest('SetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_message_callback_with_options_async(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetMessageCallbackResponse(),
            await self.do_rpcrequest_async('SetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_callback(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_message_callback_with_options(request, runtime)

    async def set_message_callback_async(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_message_callback_with_options_async(request, runtime)

    def set_vod_domain_certificate_with_options(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetVodDomainCertificateResponse(),
            self.do_rpcrequest('SetVodDomainCertificate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_vod_domain_certificate_with_options_async(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SetVodDomainCertificateResponse(),
            await self.do_rpcrequest_async('SetVodDomainCertificate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vod_domain_certificate(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_vod_domain_certificate_with_options(request, runtime)

    async def set_vod_domain_certificate_async(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_vod_domain_certificate_with_options_async(request, runtime)

    def submit_aicaption_extraction_job_with_options(
        self,
        request: vod_20170321_models.SubmitAICaptionExtractionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAICaptionExtractionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAICaptionExtractionJobResponse(),
            self.do_rpcrequest('SubmitAICaptionExtractionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aicaption_extraction_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAICaptionExtractionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAICaptionExtractionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAICaptionExtractionJobResponse(),
            await self.do_rpcrequest_async('SubmitAICaptionExtractionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aicaption_extraction_job(
        self,
        request: vod_20170321_models.SubmitAICaptionExtractionJobRequest,
    ) -> vod_20170321_models.SubmitAICaptionExtractionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aicaption_extraction_job_with_options(request, runtime)

    async def submit_aicaption_extraction_job_async(
        self,
        request: vod_20170321_models.SubmitAICaptionExtractionJobRequest,
    ) -> vod_20170321_models.SubmitAICaptionExtractionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aicaption_extraction_job_with_options_async(request, runtime)

    def submit_aiimage_audit_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageAuditJobResponse(),
            self.do_rpcrequest('SubmitAIImageAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aiimage_audit_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageAuditJobResponse(),
            await self.do_rpcrequest_async('SubmitAIImageAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aiimage_audit_job(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_audit_job_with_options(request, runtime)

    async def submit_aiimage_audit_job_async(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aiimage_audit_job_with_options_async(request, runtime)

    def submit_aiimage_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageJobResponse(),
            self.do_rpcrequest('SubmitAIImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aiimage_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageJobResponse(),
            await self.do_rpcrequest_async('SubmitAIImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aiimage_job(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    async def submit_aiimage_job_async(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aiimage_job_with_options_async(request, runtime)

    def submit_aijob_with_options(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIJobResponse(),
            self.do_rpcrequest('SubmitAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aijob_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIJobResponse(),
            await self.do_rpcrequest_async('SubmitAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aijob(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aijob_with_options(request, runtime)

    async def submit_aijob_async(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aijob_with_options_async(request, runtime)

    def submit_aimedia_audit_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIMediaAuditJobResponse(),
            self.do_rpcrequest('SubmitAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aimedia_audit_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIMediaAuditJobResponse(),
            await self.do_rpcrequest_async('SubmitAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aimedia_audit_job(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aimedia_audit_job_with_options(request, runtime)

    async def submit_aimedia_audit_job_async(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aimedia_audit_job_with_options_async(request, runtime)

    def submit_detection_job_with_options(
        self,
        request: vod_20170321_models.SubmitDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDetectionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDetectionJobResponse(),
            self.do_rpcrequest('SubmitDetectionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_detection_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDetectionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDetectionJobResponse(),
            await self.do_rpcrequest_async('SubmitDetectionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_detection_job(
        self,
        request: vod_20170321_models.SubmitDetectionJobRequest,
    ) -> vod_20170321_models.SubmitDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_detection_job_with_options(request, runtime)

    async def submit_detection_job_async(
        self,
        request: vod_20170321_models.SubmitDetectionJobRequest,
    ) -> vod_20170321_models.SubmitDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_detection_job_with_options_async(request, runtime)

    def submit_dynamic_image_job_with_options(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDynamicImageJobResponse(),
            self.do_rpcrequest('SubmitDynamicImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_dynamic_image_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDynamicImageJobResponse(),
            await self.do_rpcrequest_async('SubmitDynamicImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_dynamic_image_job(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    async def submit_dynamic_image_job_async(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_dynamic_image_job_with_options_async(request, runtime)

    def submit_live_editing_with_options(
        self,
        request: vod_20170321_models.SubmitLiveEditingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitLiveEditingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitLiveEditingResponse(),
            self.do_rpcrequest('SubmitLiveEditing', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_live_editing_with_options_async(
        self,
        request: vod_20170321_models.SubmitLiveEditingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitLiveEditingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitLiveEditingResponse(),
            await self.do_rpcrequest_async('SubmitLiveEditing', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_live_editing(
        self,
        request: vod_20170321_models.SubmitLiveEditingRequest,
    ) -> vod_20170321_models.SubmitLiveEditingResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_live_editing_with_options(request, runtime)

    async def submit_live_editing_async(
        self,
        request: vod_20170321_models.SubmitLiveEditingRequest,
    ) -> vod_20170321_models.SubmitLiveEditingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_live_editing_with_options_async(request, runtime)

    def submit_media_dnadelete_job_with_options(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitMediaDNADeleteJobResponse(),
            self.do_rpcrequest('SubmitMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_dnadelete_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitMediaDNADeleteJobResponse(),
            await self.do_rpcrequest_async('SubmitMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_dnadelete_job(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    async def submit_media_dnadelete_job_async(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_dnadelete_job_with_options_async(request, runtime)

    def submit_preprocess_jobs_with_options(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitPreprocessJobsResponse(),
            self.do_rpcrequest('SubmitPreprocessJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_preprocess_jobs_with_options_async(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitPreprocessJobsResponse(),
            await self.do_rpcrequest_async('SubmitPreprocessJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_preprocess_jobs(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    async def submit_preprocess_jobs_async(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_preprocess_jobs_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitSnapshotJobResponse(),
            self.do_rpcrequest('SubmitSnapshotJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitSnapshotJobResponse(),
            await self.do_rpcrequest_async('SubmitSnapshotJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_transcode_jobs_with_options(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitTranscodeJobsResponse(),
            self.do_rpcrequest('SubmitTranscodeJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_transcode_jobs_with_options_async(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitTranscodeJobsResponse(),
            await self.do_rpcrequest_async('SubmitTranscodeJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_transcode_jobs(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_transcode_jobs_with_options(request, runtime)

    async def submit_transcode_jobs_async(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_transcode_jobs_with_options_async(request, runtime)

    def submit_workflow_job_with_options(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitWorkflowJobResponse(),
            self.do_rpcrequest('SubmitWorkflowJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_workflow_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitWorkflowJobResponse(),
            await self.do_rpcrequest_async('SubmitWorkflowJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_workflow_job(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_workflow_job_with_options(request, runtime)

    async def submit_workflow_job_async(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_workflow_job_with_options_async(request, runtime)

    def tag_vod_resources_with_options(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.TagVodResourcesResponse(),
            self.do_rpcrequest('TagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_vod_resources_with_options_async(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.TagVodResourcesResponse(),
            await self.do_rpcrequest_async('TagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_vod_resources(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_vod_resources_with_options(request, runtime)

    async def tag_vod_resources_async(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_vod_resources_with_options_async(request, runtime)

    def un_tag_vod_resources_with_options(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UnTagVodResourcesResponse(),
            self.do_rpcrequest('UnTagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_vod_resources_with_options_async(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UnTagVodResourcesResponse(),
            await self.do_rpcrequest_async('UnTagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_tag_vod_resources(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_vod_resources_with_options(request, runtime)

    async def un_tag_vod_resources_async(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_vod_resources_with_options_async(request, runtime)

    def update_aitemplate_with_options(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAITemplateResponse(),
            self.do_rpcrequest('UpdateAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAITemplateResponse(),
            await self.do_rpcrequest_async('UpdateAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_aitemplate(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    async def update_aitemplate_async(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aitemplate_with_options_async(request, runtime)

    def update_app_info_with_options(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAppInfoResponse(),
            self.do_rpcrequest('UpdateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_info_with_options_async(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAppInfoResponse(),
            await self.do_rpcrequest_async('UpdateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_info(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    async def update_app_info_async(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_info_with_options_async(request, runtime)

    def update_attached_media_infos_with_options(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAttachedMediaInfosResponse(),
            self.do_rpcrequest('UpdateAttachedMediaInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_attached_media_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAttachedMediaInfosResponse(),
            await self.do_rpcrequest_async('UpdateAttachedMediaInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_attached_media_infos(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_attached_media_infos_with_options(request, runtime)

    async def update_attached_media_infos_async(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_attached_media_infos_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateCategoryResponse(),
            self.do_rpcrequest('UpdateCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateCategoryResponse(),
            await self.do_rpcrequest_async('UpdateCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_category(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_detection_job_with_options(
        self,
        request: vod_20170321_models.UpdateDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateDetectionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateDetectionJobResponse(),
            self.do_rpcrequest('UpdateDetectionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_detection_job_with_options_async(
        self,
        request: vod_20170321_models.UpdateDetectionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateDetectionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateDetectionJobResponse(),
            await self.do_rpcrequest_async('UpdateDetectionJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_detection_job(
        self,
        request: vod_20170321_models.UpdateDetectionJobRequest,
    ) -> vod_20170321_models.UpdateDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_detection_job_with_options(request, runtime)

    async def update_detection_job_async(
        self,
        request: vod_20170321_models.UpdateDetectionJobRequest,
    ) -> vod_20170321_models.UpdateDetectionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_detection_job_with_options_async(request, runtime)

    def update_detection_template_with_options(
        self,
        request: vod_20170321_models.UpdateDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateDetectionTemplateResponse(),
            self.do_rpcrequest('UpdateDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_detection_template_with_options_async(
        self,
        request: vod_20170321_models.UpdateDetectionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateDetectionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateDetectionTemplateResponse(),
            await self.do_rpcrequest_async('UpdateDetectionTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_detection_template(
        self,
        request: vod_20170321_models.UpdateDetectionTemplateRequest,
    ) -> vod_20170321_models.UpdateDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_detection_template_with_options(request, runtime)

    async def update_detection_template_async(
        self,
        request: vod_20170321_models.UpdateDetectionTemplateRequest,
    ) -> vod_20170321_models.UpdateDetectionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_detection_template_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateEditingProjectResponse(),
            self.do_rpcrequest('UpdateEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_editing_project_with_options_async(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateEditingProjectResponse(),
            await self.do_rpcrequest_async('UpdateEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_editing_project(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    async def update_editing_project_async(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_editing_project_with_options_async(request, runtime)

    def update_image_infos_with_options(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateImageInfosResponse(),
            self.do_rpcrequest('UpdateImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_image_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateImageInfosResponse(),
            await self.do_rpcrequest_async('UpdateImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_image_infos(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_image_infos_with_options(request, runtime)

    async def update_image_infos_async(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_image_infos_with_options_async(request, runtime)

    def update_stream_info_with_options(
        self,
        request: vod_20170321_models.UpdateStreamInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateStreamInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateStreamInfoResponse(),
            self.do_rpcrequest('UpdateStreamInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_stream_info_with_options_async(
        self,
        request: vod_20170321_models.UpdateStreamInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateStreamInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateStreamInfoResponse(),
            await self.do_rpcrequest_async('UpdateStreamInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stream_info(
        self,
        request: vod_20170321_models.UpdateStreamInfoRequest,
    ) -> vod_20170321_models.UpdateStreamInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stream_info_with_options(request, runtime)

    async def update_stream_info_async(
        self,
        request: vod_20170321_models.UpdateStreamInfoRequest,
    ) -> vod_20170321_models.UpdateStreamInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stream_info_with_options_async(request, runtime)

    def update_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateTranscodeTemplateGroupResponse(),
            self.do_rpcrequest('UpdateTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateTranscodeTemplateGroupResponse(),
            await self.do_rpcrequest_async('UpdateTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_transcode_template_group(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    async def update_transcode_template_group_async(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transcode_template_group_with_options_async(request, runtime)

    def update_video_info_with_options(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfoResponse(),
            self.do_rpcrequest('UpdateVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_video_info_with_options_async(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfoResponse(),
            await self.do_rpcrequest_async('UpdateVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_video_info(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    async def update_video_info_async(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_video_info_with_options_async(request, runtime)

    def update_video_infos_with_options(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfosResponse(),
            self.do_rpcrequest('UpdateVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_video_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfosResponse(),
            await self.do_rpcrequest_async('UpdateVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_video_infos(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_video_infos_with_options(request, runtime)

    async def update_video_infos_async(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_video_infos_with_options_async(request, runtime)

    def update_vod_domain_with_options(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodDomainResponse(),
            self.do_rpcrequest('UpdateVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodDomainResponse(),
            await self.do_rpcrequest_async('UpdateVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vod_domain(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vod_domain_with_options(request, runtime)

    async def update_vod_domain_async(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vod_domain_with_options_async(request, runtime)

    def update_vod_template_with_options(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodTemplateResponse(),
            self.do_rpcrequest('UpdateVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_vod_template_with_options_async(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodTemplateResponse(),
            await self.do_rpcrequest_async('UpdateVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vod_template(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vod_template_with_options(request, runtime)

    async def update_vod_template_async(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vod_template_with_options_async(request, runtime)

    def update_watermark_with_options(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateWatermarkResponse(),
            self.do_rpcrequest('UpdateWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_watermark_with_options_async(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateWatermarkResponse(),
            await self.do_rpcrequest_async('UpdateWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_watermark(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    async def update_watermark_async(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_watermark_with_options_async(request, runtime)

    def upload_media_by_urlwith_options(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadMediaByURLResponse(),
            self.do_rpcrequest('UploadMediaByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_media_by_urlwith_options_async(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadMediaByURLResponse(),
            await self.do_rpcrequest_async('UploadMediaByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_media_by_url(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    async def upload_media_by_url_async(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_media_by_urlwith_options_async(request, runtime)

    def upload_stream_by_urlwith_options(
        self,
        request: vod_20170321_models.UploadStreamByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadStreamByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadStreamByURLResponse(),
            self.do_rpcrequest('UploadStreamByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_stream_by_urlwith_options_async(
        self,
        request: vod_20170321_models.UploadStreamByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadStreamByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadStreamByURLResponse(),
            await self.do_rpcrequest_async('UploadStreamByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_stream_by_url(
        self,
        request: vod_20170321_models.UploadStreamByURLRequest,
    ) -> vod_20170321_models.UploadStreamByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_stream_by_urlwith_options(request, runtime)

    async def upload_stream_by_url_async(
        self,
        request: vod_20170321_models.UploadStreamByURLRequest,
    ) -> vod_20170321_models.UploadStreamByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_stream_by_urlwith_options_async(request, runtime)

    def verify_vod_domain_owner_with_options(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.VerifyVodDomainOwnerResponse(),
            self.do_rpcrequest('VerifyVodDomainOwner', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_vod_domain_owner_with_options_async(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vod_20170321_models.VerifyVodDomainOwnerResponse(),
            await self.do_rpcrequest_async('VerifyVodDomainOwner', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_vod_domain_owner(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_vod_domain_owner_with_options(request, runtime)

    async def verify_vod_domain_owner_async(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_vod_domain_owner_with_options_async(request, runtime)
