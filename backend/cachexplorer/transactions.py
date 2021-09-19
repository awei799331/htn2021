from Cachexplorer.models import Authentication, UserInfo, CurrentTaskInfo
import datetime
import uuid


#Stuff to do when a new user must be added
def add_user_txn(session, new_username, new_password):

    new_userid = str(uuid.uuid4())
    a = authentication(username=new_username,
                       password=new_password,
                       userid=new_userid)
    session.add(a)
    ui = userinfo(cum_id=str(uuid.uuid4()),
                  goldstars=0,
                  totaldistance=0,
                  true_id=new_userid )
    session.add(ui)
    ct = currenttaskinfo(curr_id=str(uuid.uuid4()),
                         recentstartpoint="",
                         length=0,
                         target="",
                         true_id=new_userid )
    session.add(ct)

#Transaction to get Userid based on Username
def get_userid_txn(session, username):
    u = session.query(authentication).filter(authentication.username == username).first()
    if u:
        userid_oi = u.userid
        session.expunge(u)
    return userid_oi

#Transaction to update Current Task
def update_task_txn(session, user_id, new_startpoint, new_length, new_target):

        ct = session.query(currenttaskinfo).filter(currentaskinfo.true_id == user_id).first()
        ct.recentstartpoint=new_startpoint
        ct.length = new_length
        ct.target = new_target
        session.add(ct)


#Transaction to Update Cumulative Info
def update_cumulative_txn(session, user_id, new_goldstar, new_distance):

        ui = session.query(userinfo).filter(userinfo.true_id == user_id).first()
        totalgoldstars= ui.goldstars + new_goldstar
        ui.goldstars=totalgoldstars
        finaldistance = ui.totaldistance + new_distance
        ui.totaldistance = finaldistance
        session.add(ui)