import uuid

class TripCreator:
    def __init__(self, trip_repository, emails_reposiory) -> None:
        self.__trip_repository = trip_repository
        self.__emails_reposiory = emails_reposiory


    def create(self, body: dict) -> dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {  **body, "id": trip_id }

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_reposiory.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })

            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request","message": str(exception) },
                "status_code": 400
            }