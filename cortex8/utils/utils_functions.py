import inspect
import os
import pathlib
import cortex8.backend.protocols.protocol_drivers.protobuf
import importlib.util



LAST = -1

def load_drivers(drivers_path):
    # TODO: implement security measures
    #       function not safe if user is able to use it, can return any class from any module

    # TODO: Implement it so that user only has to insert relative path, currently we get the current
    #       Working directory's path, we want the callers' path
    drivers = dict()
    calling_module_frame = inspect.stack()[1]
    calling_module = inspect.getmodule(calling_module_frame[0])
    calling_module_path = calling_module.__file__
    calling_module_name = calling_module.__name__

    full_path = pathlib.Path(calling_module_path) / drivers_path / "__init__.py"

    spec = importlib.util.spec_from_file_location(calling_module_name, full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj):
            drivers[obj.scheme] = obj

    return drivers
