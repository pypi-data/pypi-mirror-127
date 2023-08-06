from typing import Optional

from .. import fields
from ..core.model import AlfaObject


class Room(AlfaObject):
    id: Optional[int] = fields.Integer()
    branch_id: Optional[int] = fields.Integer()
    location_id: Optional[int] = fields.Integer()
    streaming_id: Optional[int] = fields.Integer()
    color_id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    note: Optional[str] = fields.String()
    is_enabled: Optional[bool] = fields.Bool()
    weight: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            branch_id: Optional[int] = None,
            location_id: Optional[int] = None,
            streaming_id: Optional[int] = None,
            color_id: Optional[int] = None,
            name: Optional[str] = None,
            note: Optional[str] = None,
            is_enabled: Optional[bool] = None,
            weight: Optional[int] = None,
            **kwargs
    ):
        super().__init__(
            id=id_,
            branch_id=branch_id,
            location_id=location_id,
            streaming_id=streaming_id,
            color_id=color_id,
            name=name,
            note=note,
            is_enabled=is_enabled,
            weight=weight,
            **kwargs
        )
