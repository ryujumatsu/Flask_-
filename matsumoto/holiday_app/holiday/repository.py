from typing import Optional

from holiday import db
from holiday.models.holiday import Holiday


def create_holiday(holi_date, holi_text) -> Holiday:
    holiday = Holiday(holi_date, holi_text)
    db.session.add(holiday)
    db.session.commit()
    return holiday


def get_holiday_by_date(holi_date) -> Optional[Holiday]:
    return db.session.query(Holiday).get(holi_date)


def get_all() -> list[Holiday]:
    return db.session.query(Holiday).all()


def update_holiday(holi_date, holi_text) -> Holiday:
    db.session.query(Holiday).filter(Holiday.holi_date == holi_date).\
        update({Holiday.holi_text: holi_text})


def delete_holiday(holi_date) -> Optional[str]:
    holiday = get_holiday_by_date(holi_date)
    if holiday:
        holi_text = holiday.holi_text
        db.session.query(Holiday).\
            filter(Holiday.holi_date == holi_date).delete()
        db.session.commit()
        return holi_text
    else:
        return None
