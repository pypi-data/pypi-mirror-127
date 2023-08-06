import logging
from typing import Any, Callable, Tuple, Type

from django.test import Client
from django.urls import resolve, reverse
from django.views import View

from django_helper.code import Code

logger = logging.getLogger(__name__)


def groups_test(keys: str, resp_data: dict):
    assert_key(keys, resp_data)
    got_groups = resp_data.get(keys)
    assert_instance(got_groups, list)
    return got_groups


def details_test(got_details: dict) -> dict:
    # test format
    assert_response_format(got_details)
    details_data = got_details.get("data")

    # test groups keys
    assert_key("dataList", details_data)
    keys = ("supplier_abbreviation", "tableData", "supplier_name")

    supplier_info = details_data.get("dataList")[0]
    assert_instance(supplier_info, dict)
    assert_keys(keys, supplier_info)

    indicator_info = supplier_info.get("tableData")[0]
    assert_instance(indicator_info, dict)

    keys = ("label", "state", "se_factory", "indicator")
    alert_info = supplier_info.get("tableData")[1]
    assert_keys(keys, alert_info)
    return got_details


def assert_instance(data: Any, types: Type):
    assert isinstance(data, types), f"type is {type(data)}"


def assert_key(key: Any, data: dict):
    if key not in data.keys():
        raise AssertionError(f"{key} not in {data.keys()}")


def assert_attr(objects: Any, keys: Tuple[str, ...]):
    for key in keys:
        assert hasattr(objects, key), f"{objects} not has {key}"


def assert_export_file_type(resp):
    got = resp["Content-Type"]
    want = "application/octet-stream"
    assert_equal(got, want)


def assert_export_file_details(resp, filename: str):
    got = resp.get("Content-Disposition")
    want = f"attachment; filename={filename}"
    assert_equal(got, want)


def assert_response_get(client: Client, urls: str):
    resp = client.get(urls)
    assert resp.status_code == 200

    assert_response_format(resp.json())
    return resp


def assert_keys(keys: Tuple[str, ...], data: dict):
    for key in keys:
        if key not in data.keys():
            raise AssertionError(f"{key} not in {data.keys()}")


def assert_equal(got: Any, want: Any):
    if want != got:
        assert False, f"{got} != {want}"


def assert_view(urls: str, view_func: Callable):
    got = resolve(urls).func
    assert_equal(got, view_func)


def assert_urls(urls: str, view_name: str):
    got = reverse(view_name)
    want = urls
    assert_equal(got, want)


def assert_class_view(urls: str, view: Type[View]):
    got = resolve(urls).func
    want = view.as_view()
    assert_equal(got.view_class, want.view_class)


def assert_response(client: Client, urls: str, data: dict = None):
    resp = client.post(urls, data=data)
    assert resp.status_code == 200

    assert_response_format(resp.json())
    return resp


def assert_key_value_types(
    data: dict, keys: Tuple[str, ...], value_types: Tuple[Any, ...]
):
    for key, value_type in zip(keys, value_types):
        assert key in data.keys(), (key, data)
        assert isinstance(data[key], value_type), (key, value_type)


def assert_response_format(resp_json: dict):
    # test response structure
    keys = ("code", "msg", "data")
    assert_keys(keys, resp_json)


def assert_code(resp_json: dict, code: Code):
    if Code(resp_json.get("code")) != code:
        raise AssertionError(f"code: {code} != code in {resp_json}")
