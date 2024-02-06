from sqlalchemy.event import listens_for, listen

from Service.tables.web.ocd import WebOcdArtbase


# @listens_for(WebOcdArtbase, "set", named=True)
# def on_web_ocd_artbase_set(**kwargs):
#     # target: ArticleItem = kwargs["target"]
#     # session: Session = Session.by_id(target.session_id)
#     # session.edit_date = datetime.now()
#     # db.session.commit()
#     print("on_web_ocd_artbase_set......", kwargs)
#

