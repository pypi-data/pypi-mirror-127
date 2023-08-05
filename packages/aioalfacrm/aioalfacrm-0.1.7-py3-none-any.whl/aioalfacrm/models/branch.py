from typing import Optional, List

from .. import fields
from ..core import AlfaObject


class Branch(AlfaObject):
    id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    is_active: Optional[bool] = fields.Bool()
    subject_ids: Optional[List[int]] = fields.ListField(base=fields.Integer())
    weight: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            name: Optional[str] = '',
            is_active: Optional[bool] = True,
            subject_ids: Optional[List[int]] = None,
            weight: Optional[int] = None,
            **kwargs,
    ):
        super(Branch, self).__init__(
            id=id_,
            name=name,
            is_active=is_active,
            subject_ids=subject_ids,
            weight=weight,
            **kwargs
        )
