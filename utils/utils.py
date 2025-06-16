from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.views import exception_handler
import json
import logging
import re
import unicodedata

# Get logger for current module using __name__
logger = logging.getLogger(__name__)


class PrettyJSONEncoder(json.JSONEncoder):
    def __init__(self, *args, indent, sort_keys, **kwargs):
        super().__init__(*args, indent=2, sort_keys=True, **kwargs)


class QueryParamFilterBackend(BaseFilterBackend):
    """
    Filters the queryset based on the provided filters dictionary.
    Supports both single values and multiple values for the same parameter.

    Args:
        queryset (QuerySet): The initial queryset to filter.
        request (Request): The HTTP request object containing query parameters.
        filters (dict): A mapping of query parameters to model field names.
                        Example: {"name": "name", "category": "category__name"}

    Returns:
        QuerySet: The filtered queryset.
    """

    def __init__(self, filters=None):
        self.filters = filters

    def filter_queryset(self, request, queryset, view):
        # Prefer filters from the instance, fallback to the view, else empty dict
        filters = (
            self.filters if self.filters is not None else getattr(view, "filters", {})
        )

        for query_param, model_field in filters.items():
            # Check for multiple values using getlist instead of get
            values = request.query_params.getlist(query_param)

            if values:  # Only filter if values are provided
                if len(values) == 1:
                    # Single value - maintain original behavior
                    queryset = queryset.filter(**{model_field: values[0]})
                else:
                    # Multiple values - use the __in lookup
                    queryset = queryset.filter(**{f"{model_field}__in": values})

        return queryset


class QueryParamSortBackend(BaseFilterBackend):
    """
    Sorts the queryset based on the provided sorting dictionary.

    The view should define a 'sorting' attribute that maps sort parameter values
    to queryset ordering fields.

    Example:
        class ProductView(APIView):
            sorting = {
                "price_asc": "price",
                "price_desc": "-price",
                "latest": "-created_at",
                "oldest": "created_at"
            }
            # Optional: override the default sort field
            default_sort = "-created_at"

    This will look for the 'sort' query parameter in the URL and apply
    the corresponding ordering to the queryset.
    """

    def filter_queryset(self, request, queryset, view):
        # Get the sorting attribute from the view class (if any) or use an empty dictionary
        sorting_mapping = getattr(view, "sorting", {})
        # Get the sort parameter from the request
        sort_param = request.query_params.get("sort")
        # Get default sort order from view
        default_sort = getattr(view, "default_sort", None)
        # If no sort parameter or not in mapping, apply default sort
        if not sort_param or sort_param not in sorting_mapping:
            if default_sort:
                return queryset.order_by(default_sort)
            # If no default sort is provided, return the queryset as is
            return queryset
        # Apply the sorting based on the mapping
        order_by_field = sorting_mapping[sort_param]
        return queryset.order_by(order_by_field)


def custom_exception_handler(exc, context):
    # Call the default exception handler first
    response = exception_handler(exc, context)
    if response is not None:
        # Modify the response data structure to wrap errors in "errors" key
        response.data = {"errors": response.data}

    return response


def handle_server_error(request, error, debug=False):
    if isinstance(error, ValidationError):
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"errors": error.detail},
        )
    if isinstance(error, NotFound):
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"errors": {"detail": "The requested resource was not found."}},
        )

    if debug:
        raise error

    logger.error("Server Error: %s", error, exc_info=True)
    return Response(
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        data={"errors": {"detail": "Internal server error. Please try again later."}},
    )


def slugify(value: str) -> str:
    """
    Convert a string to a slug suitable for URLs.

    - Lowercases the string
    - Removes non-alphanumeric characters (except hyphens)
    - Replaces spaces and underscores with hyphens
    - Removes leading/trailing hyphens
    """
    value = str(value)
    # Normalize unicode characters
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    # Lowercase
    value = value.lower()
    # Replace spaces and underscores with hyphens
    value = re.sub(r"[\s_]+", "-", value)
    # Remove non-alphanumeric and non-hyphen characters
    value = re.sub(r"[^a-z0-9-]", "", value)
    # Remove multiple hyphens
    value = re.sub(r"-{2,}", "-", value)
    # Remove leading/trailing hyphens
    value = value.strip("-")
    return value


def get_display_text(value):
    words = value.split("_")
    formatted_words = [word.capitalize() for word in words]
    return " ".join(formatted_words)