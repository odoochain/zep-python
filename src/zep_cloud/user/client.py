# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.session import Session
from ..types.success_response import SuccessResponse
from ..types.user import User
from ..types.user_list_response import UserListResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Add a user.

        Parameters
        ----------
        email : typing.Optional[str]
            The email address of the user.

        first_name : typing.Optional[str]
            The first name of the user.

        last_name : typing.Optional[str]
            The last name of the user.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata associated with the user.

        user_id : typing.Optional[str]
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was added.

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.add()
        """
        _request: typing.Dict[str, typing.Any] = {}
        if email is not OMIT:
            _request["email"] = email
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if user_id is not OMIT:
            _request["user_id"] = user_id
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def list_ordered(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserListResponse:
        """
        List all users with pagination.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Page number for pagination, starting from 1

        page_size : typing.Optional[int]
            Number of users to retrieve per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserListResponse
            Successfully retrieved list of users

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.list_ordered()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users-ordered"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "pageNumber": page_number,
                        "pageSize": page_size,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was retrieved.

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.get(
            user_id="userId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        delete user by id

        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            OK

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.delete(
            user_id="userId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        user_id: str,
        *,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update a user.

        Parameters
        ----------
        user_id : str
            User ID

        email : typing.Optional[str]
            The email address of the user.

        first_name : typing.Optional[str]
            The first name of the user.

        last_name : typing.Optional[str]
            The last name of the user.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata to update

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was updated.

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.update(
            user_id="userId",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if email is not OMIT:
            _request["email"] = email
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_sessions(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Session]:
        """
        list all sessions for a user by user id

        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            OK

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.user.get_sessions(
            user_id="userId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/sessions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Session], _response.json())  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Add a user.

        Parameters
        ----------
        email : typing.Optional[str]
            The email address of the user.

        first_name : typing.Optional[str]
            The first name of the user.

        last_name : typing.Optional[str]
            The last name of the user.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata associated with the user.

        user_id : typing.Optional[str]
            The unique identifier of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was added.

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.add()
        """
        _request: typing.Dict[str, typing.Any] = {}
        if email is not OMIT:
            _request["email"] = email
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if user_id is not OMIT:
            _request["user_id"] = user_id
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def list_ordered(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserListResponse:
        """
        List all users with pagination.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Page number for pagination, starting from 1

        page_size : typing.Optional[int]
            Number of users to retrieve per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserListResponse
            Successfully retrieved list of users

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.list_ordered()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "users-ordered"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "pageNumber": page_number,
                        "pageSize": page_size,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UserListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was retrieved.

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.get(
            user_id="userId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        delete user by id

        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            OK

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.delete(
            user_id="userId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        user_id: str,
        *,
        email: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update a user.

        Parameters
        ----------
        user_id : str
            User ID

        email : typing.Optional[str]
            The email address of the user.

        first_name : typing.Optional[str]
            The first name of the user.

        last_name : typing.Optional[str]
            The last name of the user.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata to update

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user that was updated.

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.update(
            user_id="userId",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if email is not OMIT:
            _request["email"] = email
        if first_name is not OMIT:
            _request["first_name"] = first_name
        if last_name is not OMIT:
            _request["last_name"] = last_name
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(User, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_sessions(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Session]:
        """
        list all sessions for a user by user id

        Parameters
        ----------
        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            OK

        Examples
        --------
        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.user.get_sessions(
            user_id="userId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/sessions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Session], _response.json())  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
