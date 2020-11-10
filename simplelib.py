import version_query


def simple_fun(x):
    return x * x


def get_version():
    return version_query.predict_version_str()
