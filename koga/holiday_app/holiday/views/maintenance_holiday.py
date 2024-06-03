from holiday.models.mst_holiday import Holiday
from holiday import db

def judge_input(date,text):
    get_date = db.session.query(Holiday).filter(Holiday.holi_date==date).all()
    get_text = db.session.query(Holiday).filter(Holiday.holi_text==text).all()
    if (len(get_date) != 0):
        if (len(get_text) != 0):
            return 0
            #祝日被りエラー
        else:
            return 1
            #祝日のテキスト情報更新
    else:
        return 2
        #祝日の新規登録


# filter と filter_byの違い
# filter(Holiday.holi_text==text).first()
# filter_by(holi_text==text).first()