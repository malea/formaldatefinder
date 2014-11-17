from formaldatefinder.models import Event, User

"""

python3 manage.py shell < populate_event.py

"""

valid_FIDs = ['1600658491', '1600658492', '1600658401', 
        '1600658405', '1600658417', '1600658420', '1600658423', 
        '1600658429', '1600658435', '1600658437']

event_id = eid = 4

e = Event.objects.get(id=eid)

for fid_ in valid_FIDs:

    try:
        exists = e.user_set.get(fid=fid_)
    except:
        u = User(fid=fid_)
        u.event = e
        u.save()

'''
for us in e.user_set.all():
    us.delete()
'''




