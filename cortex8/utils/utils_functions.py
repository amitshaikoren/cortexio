import inspect


LAST = -1

def load_drivers(drivers_path):
    # TODO: implement security measures
    # function not safe if user is able to use it, can return any class from any module
    drivers = dict()

    module_name = drivers_path.split('/')[LAST]
    mod = __import__(module_name)
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj):
            drivers[obj.scheme] = obj

    return drivers
