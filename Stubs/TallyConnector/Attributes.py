# encoding: utf-8
# module TallyConnector.Attributes calls itself Attributes
# from TallyConnector, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TallyCategoryAttribute(CategoryAttribute, _Attribute):
    """ TallyCategoryAttribute(category: str) """
    def GetLocalizedString(self, *args): #cannot find CLR method
        """
        GetLocalizedString(self: CategoryAttribute, value: str) -> str
        
            Looks up the localized name of the specified category.
        
            value: The identifer for the category to look up.
            Returns: The localized name of the category, or ll if a localized name does not exist.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, category):
        """ __new__(cls: type, category: str) """
        pass


class TDLCollectionAttribute(Attribute, _Attribute):
    """
    TDLCollectionAttribute()
    TDLCollectionAttribute(collectionName: str, type: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, collectionName=None, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, collectionName: str, type: str)
        """
        pass

    CollectionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectionName(self: TDLCollectionAttribute) -> str

Set: CollectionName(self: TDLCollectionAttribute) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: TDLCollectionAttribute) -> str

Set: Type(self: TDLCollectionAttribute) = value
"""



