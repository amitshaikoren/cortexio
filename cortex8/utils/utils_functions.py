import inspect
import importlib.util
import datetime
from cortex8 import PROJECT_NAME


# TODO: change project name
LAST = -1


def load_drivers(drivers_to_load):
    # TODO: implement security measures
    #       function not safe if user is able to use it, can return any class from any module

    drivers = dict()

    # Get calling modules' absolute pure path
    calling_module_frame = inspect.stack()[1]
    calling_module = inspect.getmodule(calling_module_frame[0])
    calling_module_path = calling_module.__file__

    # Given calling modules' absolute pure path, get pythonic path of parent directory relative to project
    # For example if abosulte path is /home/user/PycharmProjects/cortex8/cortex8/frontend/network/client/utils/reader.py
    # then we will generate cortex8.frontend.network.client.utils
    calling_module_path_components = calling_module_path.split('/')

    #getting the last time PROJECT_NAME was found in the path
    project_name_index = len(calling_module_path_components) - 1 - calling_module_path_components[::-1].index(PROJECT_NAME)

    calling_module_pythonic_path = ".".join(calling_module_path_components[project_name_index:LAST])

    module_to_import = calling_module_pythonic_path + "." + drivers_to_load

    mod = importlib.import_module(module_to_import)
    # TODO: handle exception better

    # create dictionary of {class_scheme:class} key,value pairs (looks at __init__ file)
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj):
            drivers[obj.scheme] = obj
    return drivers


def epoch_to_datetime(time_passed, date_format="%d/%m/%Y, %H:%M:%S:%f", milisecs=False):
    seconds = time_passed / 1000 if milisecs else time_passed
    date = datetime.datetime.fromtimestamp(seconds).strftime(date_format)

    return date
