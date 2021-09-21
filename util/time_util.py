import time

def convert_time_to_XX(time):
    output = str(time)
    if(time < 10):
        output = "0" + output
    return output

def get_current_time() -> str:
    lt = time.localtime()
    return std_format_time.format(
        SS=convert_time_to_XX(lt[3]),
        MM=convert_time_to_XX(lt[4]),
        HH=convert_time_to_XX(lt[5]))

def get_current_date() -> str:
    lt = time.localtime()
    return std_format_date.format(
        DD=convert_time_to_XX(lt[2]),
        MM=convert_time_to_XX(lt[1]),
        YYYY=lt[0])

def get_current_time_and_date() -> str:
    return get_current_time() + " | " + get_current_date()

std_format_date = "{DD}.{MM}.{YYYY}"
std_format_time = "{SS}:{MM}:{HH}"