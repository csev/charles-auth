import os
import hashlib
from datetime import datetime
from dateutil import relativedelta

secret = os.getenv('CHARLES_AUTH_SECRET')

def getexpire(date) :

    strdate = str(date)

    # 2005
    expire = strdate[2:4] + strdate[5:7]
    return int(expire)

def makepw(user, secret):

    # 2020-05-03 20:07:19.778803
    date = datetime.now()
    date = date + relativedelta(months=+3)

    expire = getexpire(date)

    # user_2005
    index = user + '_' + str(expire)

    # user_2005_asecret
    base = index + '_' + secret

    m = hashlib.sha256()
    m.update(base.encode())
    sig = m.hexdigest()

    # 2005_7cce7423
    pw = str(expire) + '_' + sig[0:8]
    return pw

def checkpw(user, pw, secret) :
    # 2020-05-03 20:07:19.778803
    date = datetime.now()
    expire = getexpire(date)

    pieces = pw.split('_')
    if len(pieces) != 2 : return False

    try:
        check = int(pieces[0])
    except:
        return False

    if expire > check:
        return False

    # user_2005_asecret
    base = user + '_' + str(check) + '_' + secret

    m = hashlib.sha256()
    m.update(base.encode())
    sig = m.hexdigest()

    # user_2005_asecret
    return sig.startswith(pieces[1])
