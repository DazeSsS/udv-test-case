from fastapi import status


class AppException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class NotFoundException(AppException):
    def __init__(self, entity_name: str, entity_id: str | int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{entity_name} with ID {entity_id} does not exist'
        )
