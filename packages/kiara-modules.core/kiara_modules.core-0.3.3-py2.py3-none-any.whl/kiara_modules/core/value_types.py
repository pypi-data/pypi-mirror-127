# -*- coding: utf-8 -*-

"""This module contains the value type classes that are used in the ``kiara_modules.core`` package.
"""

import datetime
import json
import pprint
import typing

from kiara import KiaraEntryPointItem
from kiara.data.types import ValueType
from kiara.utils.class_loading import find_value_types_under
from kiara.utils.output import pretty_print_arrow_table
from rich.console import ConsoleRenderable, RichCast

from kiara_modules.core.metadata_schemas import KiaraFile, KiaraFileBundle

if typing.TYPE_CHECKING:
    from kiara.data.values import Value

value_types: KiaraEntryPointItem = (
    find_value_types_under,
    ["kiara_modules.core.value_types"],
)


class BytesType(ValueType):
    """An array of bytes."""

    _value_type_name = "bytes"

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
        return str(hash(value))

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data: bytes = value.get_value_data()
        return [data.decode()]

    # @classmethod
    # def get_operations(
    #     cls,
    # ) -> typing.Mapping[str, typing.Mapping[str, typing.Mapping[str, typing.Any]]]:
    #
    #     return {
    #         "save_value": {
    #             "default": {
    #                 "module_type": "bytes.save",
    #                 "input_name": "bytes",
    #             }
    #         }
    #     }


class StringType(ValueType):
    """A string."""

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
        return str(hash(value))

    def validate(cls, value: typing.Any) -> None:

        if not isinstance(value, str):
            raise ValueError(f"Invalid type '{type(value)}': string required")

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [data]


class BooleanType(ValueType):
    "A boolean."

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
        return str(hash(value))

    def validate(cls, value: typing.Any):
        if not isinstance(value, bool):
            # if isinstance(v, str):
            #     if v.lower() in ["true", "yes"]:
            #         v = True
            #     elif v.lower() in ["false", "no"]:
            #         v = False
            #     else:
            #         raise ValueError(f"Can't parse string into boolean: {v}")
            # else:
            raise ValueError(f"Invalid type '{type(value)}' for boolean: {value}")

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [str(data)]


class IntegerType(ValueType):
    """An integer."""

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
        return str(hash(value))

    def validate(cls, value: typing.Any) -> None:

        if not isinstance(value, int):
            #     if isinstance(v, str):
            #         try:
            #             v = int(v)
            #         except Exception:
            #             raise ValueError(f"Can't parse string into integer: {v}")
            # else:
            raise ValueError(f"Invalid type '{type(value)}' for integer: {value}")

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [str(data)]


class FloatType(ValueType):
    "A float."

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
        return str(hash(value))

    def validate(cls, value: typing.Any) -> typing.Any:

        if not isinstance(value, float):
            raise ValueError(f"Invalid type '{type(value)}' for float: {value}")

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [str(data)]


class DictType(ValueType):
    """A dict-like object."""

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:

        from deepdiff import DeepHash

        dh = DeepHash(value)
        return str(dh[value])

    def validate(cls, value: typing.Any) -> None:

        if not isinstance(value, typing.Mapping):
            raise ValueError(f"Invalid type '{type(value)}', not a mapping.")

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [pprint.pformat(data)]


class ListType(ValueType):
    """A list-like object."""

    @classmethod
    def calculate_value_hash(self, value: typing.Any, hash_type: str) -> str:

        from deepdiff import DeepHash

        dh = DeepHash(value)
        return str(dh[value])

    def validate(cls, value: typing.Any) -> None:

        assert isinstance(value, typing.Iterable)

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [pprint.pformat(data)]


class TableType(ValueType):
    """A table.

    Internally, this is backed by the [Apache Arrow](https://arrow.apache.org) [``Table``](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html) class.
    """

    @classmethod
    def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
        import pyarrow as pa

        return [pa.Table]

    @classmethod
    def check_data(cls, data: typing.Any) -> typing.Optional["ValueType"]:

        import pyarrow as pa

        if isinstance(data, pa.Table):
            return TableType()

        return None

    # @classmethod
    # def get_supported_hash_types(cls) -> typing.Iterable[str]:
    #
    #     return ["pandas_df_hash"]
    #
    # @classmethod
    # def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:
    #
    #     import pyarrow as pa
    #
    #     # this is only for testing, and will be replaced with a native arrow table hush function, once I figure out how to do that efficiently
    #     table: pa.Table = value
    #     from pandas.util import hash_pandas_object
    #
    #     hash_result = hash_pandas_object(table.to_pandas()).sum()
    #     return str(hash_result)

    def validate(cls, value: typing.Any) -> None:
        import pyarrow as pa

        if not isinstance(value, pa.Table):
            raise Exception(
                f"invalid type '{type(value).__name__}', must be '{pa.Table.__name__}'."
            )

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        max_rows = print_config.get("max_no_rows")
        max_row_height = print_config.get("max_row_height")
        max_cell_length = print_config.get("max_cell_length")

        half_lines: typing.Optional[int] = None
        if max_rows:
            half_lines = int(max_rows / 2)

        result = [
            pretty_print_arrow_table(
                value.get_value_data(),
                rows_head=half_lines,
                rows_tail=half_lines,
                max_row_height=max_row_height,
                max_cell_length=max_cell_length,
            )
        ]
        return result


class ArrayType(ValueType):
    """An Apache arrow array."""

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        max_rows = print_config.get("max_no_rows")
        max_row_height = print_config.get("max_row_height")
        max_cell_length = print_config.get("max_cell_length")

        half_lines: typing.Optional[int] = None
        if max_rows:
            half_lines = int(max_rows / 2)

        array = value.get_value_data()
        import pyarrow as pa

        temp_table = pa.Table.from_arrays(arrays=[array], names=["array"])
        result = [
            pretty_print_arrow_table(
                temp_table,
                rows_head=half_lines,
                rows_tail=half_lines,
                max_row_height=max_row_height,
                max_cell_length=max_cell_length,
            )
        ]
        return result


class DateType(ValueType):
    """A date.

    Internally, this will always be represented as a Python ``datetime`` object. Iff provided as input, it can also
    be as string, in which case the [``dateutils.parser.parse``](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse) method will be used to parse the string into a datetime object.
    """

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_typpe: str) -> str:

        return str(hash(value))

    def parse_value(self, v: typing.Any) -> typing.Any:

        from dateutil import parser

        if isinstance(v, str):
            d = parser.parse(v)
            return d
        elif isinstance(v, datetime.date):
            _d = datetime.datetime(year=v.year, month=v.month, day=v.day)
            return _d

        return None

    def validate(cls, value: typing.Any):
        assert isinstance(value, datetime.datetime)

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data = value.get_value_data()
        return [str(data)]


# class FilePathType(ValueType):
#     """Represents a path to a local file."""
#
#     @classmethod
#     def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
#         return [str]
#
#     def validate(cls, value: typing.Any) -> None:
#
#         if isinstance(value, Path):
#             value = value.as_posix()
#
#         value = os.path.abspath(os.path.expanduser(value))
#         assert isinstance(value, str)
#
#         if not os.path.exists(value):
#             raise Exception(
#                 f"Invalid file path value: no file exists for path '{value}'."
#             )
#         if not os.path.isfile(os.path.realpath(value)):
#             raise Exception(
#                 f"Invalid file path value: path '{value}' exists but does not point to a file."
#             )
#
#     def pretty_print_as_renderables(
#         self, value: "Value", print_config: typing.Mapping[str, typing.Any]
#     ) -> typing.Any:
#
#         data: str = value.get_value_data()
#         return [data]


# class FolderPathType(ValueType):
#     """Represents a path to a local folder."""
#
#     @classmethod
#     def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
#         return [str]
#
#     def pretty_print_as_renderables(
#         self, value: "Value", print_config: typing.Mapping[str, typing.Any]
#     ) -> typing.Any:
#
#         data: str = value.get_value_data()
#         return [data]
#
#     def validate(cls, value: typing.Any) -> None:
#
#         if isinstance(value, Path):
#             value = value.as_posix()
#
#         value = os.path.abspath(os.path.expanduser(value))
#         assert isinstance(value, str)
#
#         if not os.path.exists(value):
#             raise Exception(
#                 f"Invalid folder path value: no folder exists for path '{value}'."
#             )
#         if not os.path.isdir(os.path.realpath(value)):
#             raise Exception(
#                 f"Invalid file path value: path '{value}' exists but does not point to a file."
#             )


class FileType(ValueType):
    """A representation of a file.

    It is recommended to 'onboard' files before working with them, otherwise metadata consistency can not be guaranteed.
    """

    @classmethod
    def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
        return [FileType]

    @classmethod
    def get_supported_hash_types(cls) -> typing.Iterable[str]:
        return ["sha3_256"]

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:

        assert hash_type == "sha3_256"
        assert isinstance(value, KiaraFile)
        return value.file_hash

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        data: KiaraFile = value.get_value_data()
        max_lines = print_config.get("max_lines", 34)
        try:
            lines = []
            with open(data.path, "r") as f:
                for idx, l in enumerate(f):
                    if idx > max_lines:
                        lines.append("...\n")
                        lines.append("...")
                        break
                    lines.append(l)

            # TODO: syntax highlighting
            return ["".join(lines)]
        except UnicodeDecodeError:
            # found non-text data
            return [
                "Binary file or non-utf8 enconding, not printing content...",
                "",
                "[b]File metadata:[/b]",
                "",
                data.json(indent=2),
            ]


class FileBundleType(ValueType):
    """A representation of a set of files (folder, archive, etc.).

    It is recommended to 'onboard' files before working with them, otherwise metadata consistency can not be guaranteed.
    """

    @classmethod
    def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
        return [FileBundleType]

    @classmethod
    def get_supported_hash_types(cls) -> typing.Iterable[str]:
        return ["sha3_256"]

    @classmethod
    def calculate_value_hash(cls, value: typing.Any, hash_type: str) -> str:

        assert hash_type == "sha3_256"

        assert isinstance(value, KiaraFileBundle)
        return value.file_bundle_hash

    def pretty_print_as_renderables(
        self, value: "Value", print_config: typing.Mapping[str, typing.Any]
    ) -> typing.Any:

        max_no_included_files = print_config.get("max_no_files", 40)

        data: KiaraFileBundle = value.get_value_data()
        pretty = data.dict(exclude={"included_files"})
        files = list(data.included_files.keys())
        if max_no_included_files >= 0:
            if len(files) > max_no_included_files:
                half = int((max_no_included_files - 1) / 2)
                head = files[0:half]
                tail = files[-1 * half :]  # noqa
                files = (
                    head
                    + ["..... output skipped .....", "..... output skipped ....."]
                    + tail
                )
        pretty["included_files"] = files
        return [json.dumps(pretty, indent=2)]
        # return [data.json(indent=2)]


class RenderablesType(ValueType):
    """A list of renderable objects, used in the 'rich' Python library, to print to the terminal or in Jupyter.

    Internally, the result list items can be either a string, a 'rich.console.ConsoleRenderable', or a 'rich.console.RichCast'.
    """

    @classmethod
    def candidate_python_types(cls) -> typing.Optional[typing.Iterable[typing.Type]]:
        return [str, ConsoleRenderable, RichCast]
