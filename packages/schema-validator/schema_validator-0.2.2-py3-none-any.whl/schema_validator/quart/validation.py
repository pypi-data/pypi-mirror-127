from dataclasses import asdict, is_dataclass
from functools import wraps
from typing import (Any, Callable, Dict, Iterable, List, Optional, Union, cast)

from pydantic import BaseModel, ValidationError
from pydantic.dataclasses import is_builtin_dataclass
from quart import Response, current_app, g, jsonify, request
from werkzeug.datastructures import Headers
from werkzeug.exceptions import BadRequest

from schema_validator.constants import (
    SCHEMA_QUERYSTRING_ATTRIBUTE, SCHEMA_REQUEST_ATTRIBUTE,
    SCHEMA_RESPONSE_ATTRIBUTE, SCHEMA_TAG_ATTRIBUTE
)
from schema_validator.types import PydanticModel
from schema_validator.utils import DataSource, check_body_schema, \
    check_query_string_schema, check_response_schema


async def check_response(result, response_model: Dict[int, PydanticModel]):
    status_or_headers: Union[None, int, str, Dict, List] = None
    headers: Optional[Headers] = None

    if isinstance(result, tuple):
        value, status_or_headers, headers = result + (None,) * (
            3 - len(result))
    else:
        value = result

    if isinstance(value, Response):
        value = await value.get_json()

    status = 200
    if status_or_headers is not None and not isinstance(
        status_or_headers, (Headers, dict, list)
    ) and str(status_or_headers).isdigit():
        status = int(status_or_headers)

    bad_status = BadRequest.code

    for status_code, model_cls in response_model.items():
        if status_code != status:
            continue
        if isinstance(value, dict):
            try:
                model_value = model_cls(**value)
            except (TypeError, ValidationError) as ve:
                return jsonify(validation_error=str(ve)), bad_status
        elif type(value) == model_cls:
            model_value = value
        elif is_builtin_dataclass(value):
            model_value = model_cls(**asdict(value))
        else:
            return jsonify(validation_error="invalid response"), bad_status
        if is_dataclass(model_value):
            return asdict(model_value), status_or_headers, headers
        else:
            model_value = cast(BaseModel, model_value)
            return model_value.dict(), status_or_headers, headers
    return result


def validate(
    query_string: Optional[PydanticModel] = None,
    body: Optional[PydanticModel] = None,
    source: DataSource = DataSource.JSON,
    validate_path_args: bool = False,
    responses: Union[PydanticModel, Dict[int, PydanticModel], None] = None,
    headers: Optional[PydanticModel] = None,
    tags: Optional[Iterable[str]] = None
) -> Callable:
    """
    params:
        query_string:
            the params in query
        body:
            json body or form
        source:
            the body source
        response:
            response model define

    from dataclasses import dataclass
    from datetime import datetime
    from typing import Optional
    from pydantic import BaseModel

    from flask import Flask
    from schema_validator import FlaskSchema, validate

    app = Flask(__name__)

    FlaskSchema(app)
    OR

    schema = FlaskSchema()
    schema.init_app(app)

    @dataclass
    class Todo:
        task: str
        due: Optional[datetime]

    class TodoResponse(BaseModel):
        id: int
        name: str

    @app.post("/")
    @validate(body=Todo, responses=TodoResponse)
    def create_todo():
        ... # Do something with data, e.g. save to the DB
        return dict(id=1, name="2")

    @app.put("/")
    @validate(
        body=Todo,
        responses={200: TodoResponse, 400: TodoResponse},
        tags=["SOME-TAG"]
    )
    def update_todo():
        ... # Do something with data, e.g. save to the DB
        return TodoResponse(id=1, name="123")

    @tags("SOME-TAG", "OTHER-TAG")
    class View(MethodView):
        @validate(...)
        def get(self):
            return {}
    """

    # TODO
    if validate_path_args:
        pass
    # TODO
    if headers is not None:
        pass

    if query_string is not None:
        query_string = check_query_string_schema(query_string)

    if body is not None:
        body = check_body_schema(body, source)

    if responses is not None:
        responses = check_response_schema(responses)

    def decorator(func: Callable) -> Callable:

        if query_string:
            setattr(func, SCHEMA_QUERYSTRING_ATTRIBUTE, query_string)
        if body:
            setattr(func, SCHEMA_REQUEST_ATTRIBUTE, (body, source))
        if responses:
            setattr(func, SCHEMA_RESPONSE_ATTRIBUTE, responses)
        if tags:
            setattr(func, SCHEMA_TAG_ATTRIBUTE, list(set(tags)))

        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            err = {}
            if body:
                if source == DataSource.JSON:
                    data = await request.get_json()
                else:
                    data = await request.form

                try:
                    body_model = body(**data)
                except (TypeError, ValidationError) as ve:
                    err["body_params"] = str(ve)
                else:
                    g.body_params = body_model

            if query_string:
                try:
                    query_params = query_string(**request.args)
                except (TypeError, ValidationError) as ve:
                    err["query_params"] = str(ve)
                else:
                    g.query_params = query_params

            if err:
                return jsonify(validation_error=err), BadRequest.code

            result = await current_app.ensure_async(func)(*args, **kwargs)

            if responses:
                return await check_response(result, responses)
            return result

        return wrapper

    return decorator
