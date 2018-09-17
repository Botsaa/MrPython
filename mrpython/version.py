
MRPYTHON_VERSION_MAJOR = 1
MRPYTHON_VERSION_MINOR = 0
MRPYTHON_VERSION_PATCH = 0
MRPYTHON_VERSION_TAG = "legacy"


def version_string():
    return "{}.{}.{}{}".format(MRPYTHON_VERSION_MAJOR,
                               MRPYTHON_VERSION_MINOR,
                               MRPYTHON_VERSION_PATCH,
                               "" if MRPYTHON_VERSION_TAG == "" else ("-" + MRPYTHON_VERSION_TAG))

