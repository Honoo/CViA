import abc

class DataSource(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(cls, filepath):
        raise NotImplementedError('The load method takes in a filepath and \
                                  returns data.')
