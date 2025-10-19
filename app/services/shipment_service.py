from app.database.models import ShipmentEvent
from app.services.base import BaseService


class ShipmentEventService(BaseService):
    def __init__(self,session):
        super().__init__(ShipmentEvent,session)

    async def add(
            self,
            shipment:Shipment
            
    )