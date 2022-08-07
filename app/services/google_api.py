from datetime import datetime, timedelta
from typing import List, Tuple

from aiogoogle import Aiogoogle

from app.core.config import Drive, Sheets, settings
from app.models import CharityProject


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(Sheets.DT_FORMAT)
    service = await wrapper_services.discover(
        'sheets',
        Sheets.VERSION
    )

    spreadsheet_body = {
        'properties': {
            'title': f'Отчет от {now_date_time}',
            'locale': Sheets.LOCALE
        },
        'sheets': [
            {
                'properties': {
                    'sheetType': Sheets.TYPE,
                    'sheetId': Sheets.ID,
                    'title': Sheets.TITLE,
                    'gridProperties': {
                        'rowCount': Sheets.ROW_COUNT,
                        'columnCount': Sheets.COLUMN_COUNT
                    }
                }
            }
        ]
    }

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )

    return response['spreadsheetId']


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }

    service = await wrapper_services.discover('drive', Drive.VERSION)

    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    projects: List[Tuple[CharityProject, timedelta]],
    wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(Sheets.DT_FORMAT)
    service = await wrapper_services.discover(
        'sheets',
        Sheets.VERSION
    )

    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]

    table_values.extend(
        [
            [project.name, str(completion), project.description]
            for project, completion in projects
        ]
    )

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=Sheets.UPDATE_RANGE,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
