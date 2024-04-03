import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo Registro em Banco de Dados")
def test_insert_attendees():
    event_id = "meu-uuid-e-nois2"
    attendee = {
        "uuid": "meu-uuid-do-attendee2",
        "name": "Leonardo2",
        "email": "leonardo@email.com2",
        "event_id": event_id,
    }
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee)
    print(response)

@pytest.mark.skip(reason="Não Necessita")    
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-do-attendee2"
    attendees_respository = AttendeesRepository()
    attendee = attendees_respository.get_attendee_badge_by_id(attendee_id)
    print(attendee)