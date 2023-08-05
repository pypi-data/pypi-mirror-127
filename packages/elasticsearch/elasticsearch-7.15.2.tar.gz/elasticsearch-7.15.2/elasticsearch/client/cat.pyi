#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Any, Collection, Dict, MutableMapping, Optional, Tuple, Union

from .utils import NamespacedClient

class CatClient(NamespacedClient):
    def aliases(
        self,
        *,
        name: Optional[Any] = ...,
        expand_wildcards: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def allocation(
        self,
        *,
        node_id: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def count(
        self,
        *,
        index: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def health(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        ts: Optional[bool] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def help(
        self,
        *,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> str: ...
    def indices(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        expand_wildcards: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        health: Optional[Any] = ...,
        help: Optional[bool] = ...,
        include_unloaded_segments: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        pri: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def master(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def nodes(
        self,
        *,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        full_id: Optional[bool] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        include_unloaded_segments: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def recovery(
        self,
        *,
        index: Optional[Any] = ...,
        active_only: Optional[bool] = ...,
        bytes: Optional[Any] = ...,
        detailed: Optional[bool] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def shards(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def segments(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def pending_tasks(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def thread_pool(
        self,
        *,
        thread_pool_patterns: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        size: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def fielddata(
        self,
        *,
        fields: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def plugins(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        include_bootstrap: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def nodeattrs(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def repositories(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def snapshots(
        self,
        *,
        repository: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        ignore_unavailable: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def tasks(
        self,
        *,
        actions: Optional[Any] = ...,
        detailed: Optional[bool] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        nodes: Optional[Any] = ...,
        parent_task_id: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def templates(
        self,
        *,
        name: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        local: Optional[bool] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def ml_data_frame_analytics(
        self,
        *,
        id: Optional[Any] = ...,
        allow_no_match: Optional[bool] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def ml_datafeeds(
        self,
        *,
        datafeed_id: Optional[Any] = ...,
        allow_no_datafeeds: Optional[bool] = ...,
        allow_no_match: Optional[bool] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def ml_jobs(
        self,
        *,
        job_id: Optional[Any] = ...,
        allow_no_jobs: Optional[bool] = ...,
        allow_no_match: Optional[bool] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def ml_trained_models(
        self,
        *,
        model_id: Optional[Any] = ...,
        allow_no_match: Optional[bool] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        from_: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        size: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
    def transforms(
        self,
        *,
        transform_id: Optional[Any] = ...,
        allow_no_match: Optional[bool] = ...,
        format: Optional[Any] = ...,
        from_: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[bool] = ...,
        s: Optional[Any] = ...,
        size: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[bool] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Union[Dict[str, Any], str]: ...
