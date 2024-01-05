# Natural Language Toolkit: SVM-based classifier

"""
nltk.classify.svm was deprecated. For classification based
on support vector machines SVMs use nltk.classify.scikitlearn
(or `scikit-learn <http://scikit-learn.org>`_ directly).
"""


class SvmClassifier(object):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(__doc__)
