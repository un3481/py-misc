
##########################################################################################################################

# Check If Object Is a Caller
def iscaller(obj: object):
    return (hasattr(obj, '__callable__') and
        callable(obj.__callable__))

# Check If Object Is a True Caller
def istruecaller(obj: object):
    return (callable(obj) and iscaller(obj))

# Get Callable of Object
def getcallable(obj: object, bypass: bool = False):
    caller = [obj]
    while (iscaller(caller[-1]) and ((caller[-1].__pass__
        if hasattr(caller[-1], '__pass__') else False) or bypass)):
        caller.append(caller[-1].__callable__)
    return caller[-1]

# Check If Object Is a Resolvable
def isresolvable(obj: object):
    return (iscaller(obj) and
        all(hasattr(obj, attr) for attr in
        ['__resolve__', 'value', 'resolved',
        '__reject__', 'error', 'rejected',
        '__reset__', 'resolution']))

# Check If Object Is a Waitable
def iswaitable(obj: object):
    return (isresolvable(obj) and
        all(hasattr(obj, attr) for attr in
        ['wait', 'then', 'catch',
        '__thread__', '__trigger__']))

##########################################################################################################################

# Get Reference Object
def proxy_reference(obj):
    reference = [obj]
    while hasattr(reference[-1], '__proxy__'):
        reference.append(reference[-1].__proxy__)
    return reference[-1]

# Get Location of Object in Script
def locale(obj):
    reference = proxy_reference(obj)
    module = reference.__module__ if hasattr(reference, '__module__') else '__main__'
    module = module if module.startswith('__main__') else '::'.join(('__main__', module))
    qual = reference.__qualname__ if hasattr(reference, '__qualname__') else '__?__'
    locale = '::'.join((module, qual))
    locale = locale.replace('.<locals>.', '::')
    return locale

##########################################################################################################################
