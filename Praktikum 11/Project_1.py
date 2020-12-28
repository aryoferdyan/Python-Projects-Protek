
import datetime 

def diffDate(x): 
    now = datetime.datetime.now()
    nx = x.split('-')

    # (thn, tgl, bln) 
    a = datetime.datetime(now.year, now.month, now.day) 
    b = datetime.datetime(int(nx[0]), int(nx[1]), int(nx[2])) 
     
    selisih = a-b  
    if selisih.days < 0:
        selisih = selisih * -1
    
    return selisih.days


