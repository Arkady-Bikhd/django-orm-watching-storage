from django.utils.timezone import localtime


def get_duration(visit):

    duration = 0    
    if visit.leaved_at:
        duration = localtime(visit.leaved_at) - localtime(visit.entered_at)
    else:
        time_at = localtime(visit.entered_at)
        duration = localtime() - time_at 
    return calc_parts_duration(duration)


def calc_parts_duration(duration):

    time_visit = {            
            'hours': 0,
            'minutes': 0
        }
    if duration:
        all_seconds = duration.total_seconds()        
        time_visit = {            
            'hours': int(all_seconds / 3600),
            'minutes': (all_seconds % 3600) // 60
        }
    return time_visit

def format_duration(duration):
    
    display_time = f"{duration['hours']} ч., {duration['minutes']} мин." 
        
    return display_time


def is_visit_long(time_visit):

    return (time_visit['hours'] >= 1)
