from datetime import datetime

def time_stamp():
    return str(datetime.now().strftime("%Y%m%d_"))

