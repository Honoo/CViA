import abc

class Filter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, resume_attribute, query_attribute):
        raise NotImplementedError('The run method takes in a resume and \
                                   a dictionary of attribute scores.')
