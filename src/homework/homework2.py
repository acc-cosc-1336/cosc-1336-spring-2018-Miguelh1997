def get_time(hour, minutes, seconds, time_type, meridiem='AM'):

    if time_type != 12 and time_type != 24:
        return 'Invalid time_type(12 or 24 only)'

    if time_type == 24:
        if (hour < 0 or hour > 23):
            return 'Invalid hours(range 0-23)'
            
    if time_type == 12:
        
        if (hour < 1 or hour > 12):
            return 'Invalid hours(range 1-12)'
    
    if (minutes > 59 or minutes < 0):
        return 'Invalid minutes(range 0-59)'
    
    if (seconds > 59 or seconds < 0):
        return 'Invalid seconds(range 0-59)'

    if (hour < 10):
        hour = "0" + str(hour)
    else:
        hour = str(hour)

       
    if (minutes < 10):
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
       
    if (seconds < 10):
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    if time_type == 12:
            time = hour +":"+minutes+":"+seconds + " "+meridiem
    if time_type == 24:
            time = hour +":"+minutes+":"+seconds
        
    
    return  time

def time_from_utc(utc_offset, utc_zero_time):

    if utc_offset == -4:
        utc_ast = utc_zero_time + (-4)
        return utc_ast % 24
    elif utc_offset == -5:
        utc_est = utc_zero_time - 5
        return utc_est % 24
    elif utc_offset == -6:
        utc_cst = utc_zero_time - 6
        return utc_cst % 24
    elif utc_offset == -7:
        utc_mst = utc_zero_time - 7
        return utc_mst % 24
    elif utc_offset == (-8):
        utc_pst = utc_zero_time - 8
        return utc_pst % 24
    elif utc_offset == -9:
        utc_al = utc_zero_time - 9
        return utc_al % 24
    elif utc_offset == -10:
        utc_hst = utc_zero_time - 10
        return utc_hst % 24
    elif utc_offset == -11:
        utc_sst = utc_zero_time - 11
        return utc_sst % 24
    elif utc_offset == 1:
        utc_cet == utc_zero_time + 1
        return utc_cet % 24
    elif utc_offset == 2:
        utc_eet = utc_zero_time + 2
        return utc_eet % 24
    elif utc_offset == 3:
        utc_ct = utc_zero_time + 3
        return utc_ct % 24
    elif utc_offset == 4:
        utc_dt = utc_zero_time + 4
        return utc_dt % 24
    elif utc_offest == 8:
        utc_awst = utc_zero_time + 8
        return utc_awst % 24

    
    
