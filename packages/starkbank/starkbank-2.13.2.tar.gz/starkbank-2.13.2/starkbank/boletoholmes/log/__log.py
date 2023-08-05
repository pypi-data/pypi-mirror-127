from ...utils import rest
from ...utils.api import from_api_json
from ...utils.checks import check_datetime, check_date
from ...utils.resource import Resource
from ..__boletoholmes import _resource as _holmes_resource


class Log(Resource):
    """# boletoholmes.Log object
    Every time a BoletoHolmes entity is modified, a corresponding boletoholmes.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the BoletoHolmes.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - holmes [BoletoHolmes]: BoletoHolmes entity to which the log refers to.
    - type [string]: type of the BoletoHolmes event which triggered the log creation. ex: "solving" or "solved"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, holmes):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.holmes = from_api_json(_holmes_resource, holmes)


_resource = {"class": Log, "name": "BoletoHolmesLog"}


def get(id, user=None):
    """# Retrieve a specific boletoHolmes.Log
    Receive a single boletoHolmes.Log object previously created by the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - boletoholmes.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, holmes_ids=None, user=None):
    """# Retrieve boletoholmes.Logs
    Receive a generator of boletoholmes.Log objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by event type. ex: ["solving", "solved"]
    - holmes_ids [list of strings, default None]: list of BoletoHolmes ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of boletoholmes.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        holmes_ids=holmes_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, holmes_ids=None, user=None):
    """# Retrieve paged boletoholmes.Logs
    Receive a list of up to 100 boletoholmes.Log objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by event type. ex: ["solving", "solved"]
    - holmes_ids [list of strings, default None]: list of boletoholmes.Log ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of boletoholmes.Log objects with updated attributes
    - cursor to retrieve the next page of boletoholmes.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        holmes_ids=holmes_ids,
        user=user,
    )
