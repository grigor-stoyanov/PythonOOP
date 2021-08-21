import structlog

logger = structlog.get_logger()
logger.error('test')


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class Base:
    pass


@singleton
class A(Base):
    pass


a1 = A()
a2 = A()
# same id
print(id(a1))
print(id(a2))
