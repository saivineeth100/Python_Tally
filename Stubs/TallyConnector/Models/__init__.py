# encoding: utf-8
# module TallyConnector.Models calls itself Models
# from TallyConnector, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Action(Enum, IComparable, IFormattable, IConvertible):
    """ enum Action, values: Alter (1), Cancel (3), Create (0), Delete (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Alter = None
    Cancel = None
    Create = None
    Delete = None
    value__ = None


class AdAllocType(Enum, IComparable, IFormattable, IConvertible):
    """ enum AdAllocType, values: AppropriateByQty (1), AppropriateByValue (2), None (0), NotApplicable (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AppropriateByQty = None
    AppropriateByValue = None
    None = None
    NotApplicable = None
    value__ = None


class TallyBaseObject(object):
    """ TallyBaseObject() """
    OtherAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OtherAttributes(self: TallyBaseObject) -> Array[XmlAttribute]

Set: OtherAttributes(self: TallyBaseObject) = value
"""

    OtherFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OtherFields(self: TallyBaseObject) -> Array[XmlElement]

Set: OtherFields(self: TallyBaseObject) = value
"""



class InventoryAllocations(TallyBaseObject):
    """ InventoryAllocations() """
    ActualQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualQuantity(self: InventoryAllocations) -> str

Set: ActualQuantity(self: InventoryAllocations) = value
"""

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: InventoryAllocations) -> str

Set: Amount(self: InventoryAllocations) = value
"""

    BatchAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchAllocations(self: InventoryAllocations) -> List[BatchAllocations]

Set: BatchAllocations(self: InventoryAllocations) = value
"""

    BilledQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BilledQuantity(self: InventoryAllocations) -> str

Set: BilledQuantity(self: InventoryAllocations) = value
"""

    BOMName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BOMName(self: InventoryAllocations) -> str

Set: BOMName(self: InventoryAllocations) = value
"""

    CostCategoryAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CostCategoryAllocations(self: InventoryAllocations) -> List[CostCategoryAllocations]

Set: CostCategoryAllocations(self: InventoryAllocations) = value
"""

    DeemedPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeemedPositive(self: InventoryAllocations) -> str

Set: DeemedPositive(self: InventoryAllocations) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: InventoryAllocations) -> str

Set: ForexAmount(self: InventoryAllocations) = value
"""

    IsScrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsScrap(self: InventoryAllocations) -> str

Set: IsScrap(self: InventoryAllocations) = value
"""

    Rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rate(self: InventoryAllocations) -> str

Set: Rate(self: InventoryAllocations) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: InventoryAllocations) -> str

Set: RateofExchange(self: InventoryAllocations) = value
"""

    StockItemName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockItemName(self: InventoryAllocations) -> str

Set: StockItemName(self: InventoryAllocations) = value
"""



class AllInventoryAllocations(InventoryAllocations):
    """ AllInventoryAllocations() """

class AttendanceEntry(object):
    """ AttendanceEntry() """
    AttdType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttdType(self: AttendanceEntry) -> str

Set: AttdType(self: AttendanceEntry) = value
"""

    AttdTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttdTypeId(self: AttendanceEntry) -> str

Set: AttdTypeId(self: AttendanceEntry) = value
"""

    AttdTypeTimeValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttdTypeTimeValue(self: AttendanceEntry) -> str

Set: AttdTypeTimeValue(self: AttendanceEntry) = value
"""

    AttdTypeValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttdTypeValue(self: AttendanceEntry) -> str

Set: AttdTypeValue(self: AttendanceEntry) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AttendanceEntry) -> str

Set: Name(self: AttendanceEntry) = value
"""



class TallyXmlJson(TallyBaseObject):
    """ TallyXmlJson() """
    def GetJson(self, Indented):
        """ GetJson(self: TallyXmlJson, Indented: bool) -> str """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: TallyXmlJson, attrOverrides: XmlAttributeOverrides) -> str """
        pass


class BasicTallyObject(TallyXmlJson, ITallyObject, IBasicTallyObject):
    """ BasicTallyObject() """
    def PrepareForExport(self):
        """ PrepareForExport(self: BasicTallyObject) """
        pass

    def ToString(self):
        """ ToString(self: BasicTallyObject) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: BasicTallyObject) -> str

Set: GUID(self: BasicTallyObject) = value
"""

    TallyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TallyId(self: BasicTallyObject) -> Nullable[int]

Set: TallyId(self: BasicTallyObject) = value
"""



class BatchAllocations(TallyBaseObject):
    """ BatchAllocations() """
    ActualQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualQuantity(self: BatchAllocations) -> str

Set: ActualQuantity(self: BatchAllocations) = value
"""

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: BatchAllocations) -> str

Set: Amount(self: BatchAllocations) = value
"""

    BatchName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchName(self: BatchAllocations) -> str

Set: BatchName(self: BatchAllocations) = value
"""

    BilledQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BilledQuantity(self: BatchAllocations) -> str

Set: BilledQuantity(self: BatchAllocations) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: BatchAllocations) -> str

Set: ForexAmount(self: BatchAllocations) = value
"""

    GodownName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GodownName(self: BatchAllocations) -> str

Set: GodownName(self: BatchAllocations) = value
"""

    OrderNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNo(self: BatchAllocations) -> str

Set: OrderNo(self: BatchAllocations) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: BatchAllocations) -> str

Set: RateofExchange(self: BatchAllocations) = value
"""

    TrackingNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrackingNo(self: BatchAllocations) -> str

Set: TrackingNo(self: BatchAllocations) = value
"""



class BillAllocations(TallyBaseObject):
    """ BillAllocations() """
    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: BillAllocations) -> str

Set: Amount(self: BillAllocations) = value
"""

    BillCP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillCP(self: BillAllocations) -> BillCP

Set: BillCP(self: BillAllocations) = value
"""

    BillCreditPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillCreditPeriod(self: BillAllocations) -> str

Set: BillCreditPeriod(self: BillAllocations) = value
"""

    BillType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillType(self: BillAllocations) -> str

Set: BillType(self: BillAllocations) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: BillAllocations) -> str

Set: ForexAmount(self: BillAllocations) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BillAllocations) -> str

Set: Name(self: BillAllocations) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: BillAllocations) -> str

Set: RateofExchange(self: BillAllocations) = value
"""



class BillCP(object):
    """ BillCP() """
    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Days(self: BillCP) -> str

Set: Days(self: BillCP) = value
"""

    JD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JD(self: BillCP) -> str

Set: JD(self: BillCP) = value
"""

    TextValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextValue(self: BillCP) -> str

Set: TextValue(self: BillCP) = value
"""



class Body(object):
    """ Body[T]() """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: Body[T]) -> Data[T]

Set: Data(self: Body[T]) = value
"""

    Desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Desc(self: Body[T]) -> Description

Set: Desc(self: Body[T]) = value
"""



class DCollection(object):
    """ DCollection() """
    def SetAttributes(self, ismodify, isFixed, isInitialize, isOption, isInternal):
        """ SetAttributes(self: DCollection, ismodify: YesNo, isFixed: YesNo, isInitialize: YesNo, isOption: YesNo, isInternal: YesNo) """
        pass

    IsFixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixed(self: DCollection) -> YesNo

Set: IsFixed(self: DCollection) = value
"""

    IsInitialize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInitialize(self: DCollection) -> YesNo

Set: IsInitialize(self: DCollection) = value
"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: DCollection) -> YesNo

Set: IsInternal(self: DCollection) = value
"""

    IsModify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsModify(self: DCollection) -> YesNo

Set: IsModify(self: DCollection) = value
"""

    IsOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOption(self: DCollection) -> YesNo

Set: IsOption(self: DCollection) = value
"""



class Collection(DCollection):
    """
    Collection(colName: str, colType: str, childOf: str, nativeFields: List[str], filters: List[str], Isintialize: YesNo)
    Collection()
    Collection(objcollectionName: str, objects: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, colName: str, colType: str, childOf: str, nativeFields: List[str], filters: List[str], Isintialize: YesNo)
        __new__(cls: type)
        __new__(cls: type, objcollectionName: str, objects: str)
        """
        pass

    Childof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Childof(self: Collection) -> str

Set: Childof(self: Collection) = value
"""

    Filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filters(self: Collection) -> List[str]

Set: Filters(self: Collection) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Collection) -> str

Set: Name(self: Collection) = value
"""

    NativeFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NativeFields(self: Collection) -> List[str]

Set: NativeFields(self: Collection) = value
"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: Collection) -> str

Set: Objects(self: Collection) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Collection) -> str

Set: Type(self: Collection) = value
"""



class Colllection(object):
    """ Colllection[T]() """
    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: Colllection[T]) -> List[T]

Set: Objects(self: Colllection[T]) = value
"""



class Company(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ Company() """
    def ToString(self):
        """ ToString(self: Company) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: Company) -> str

Set: Address(self: Company) = value
"""

    BooksFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BooksFrom(self: Company) -> str

Set: BooksFrom(self: Company) = value
"""

    CompNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompNum(self: Company) -> str

Set: CompNum(self: Company) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Country(self: Company) -> str

Set: Country(self: Company) = value
"""

    Email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Email(self: Company) -> str

Set: Email(self: Company) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: Company) -> str

Set: EndDate(self: Company) = value
"""

    FaxNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaxNumber(self: Company) -> str

Set: FaxNumber(self: Company) = value
"""

    IntegrateAccountswithInventory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntegrateAccountswithInventory(self: Company) -> str

Set: IntegrateAccountswithInventory(self: Company) = value
"""

    IsBillWiseOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBillWiseOn(self: Company) -> str

Set: IsBillWiseOn(self: Company) = value
"""

    IsCostCentersOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCostCentersOn(self: Company) -> str

Set: IsCostCentersOn(self: Company) = value
"""

    IsGSTon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGSTon(self: Company) -> str

Set: IsGSTon(self: Company) = value
"""

    Isintereston = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Isintereston(self: Company) -> str

Set: Isintereston(self: Company) = value
"""

    IsInventoryOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInventoryOn(self: Company) -> str

Set: IsInventoryOn(self: Company) = value
"""

    IsPayrollOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPayrollOn(self: Company) -> str

Set: IsPayrollOn(self: Company) = value
"""

    IsTCSon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTCSon(self: Company) -> str

Set: IsTCSon(self: Company) = value
"""

    IsTDSon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTDSon(self: Company) -> str

Set: IsTDSon(self: Company) = value
"""

    MailingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailingName(self: Company) -> str

Set: MailingName(self: Company) = value
"""

    MobileNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MobileNumber(self: Company) -> str

Set: MobileNumber(self: Company) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Company) -> str

Set: Name(self: Company) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: Company) -> str

Set: PhoneNumber(self: Company) = value
"""

    PinCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PinCode(self: Company) -> str

Set: PinCode(self: Company) = value
"""

    StartingFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartingFrom(self: Company) -> str

Set: StartingFrom(self: Company) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: Company) -> str

Set: State(self: Company) = value
"""

    TANNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TANNumber(self: Company) -> str

Set: TANNumber(self: Company) = value
"""

    TANRegNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TANRegNumber(self: Company) -> str

Set: TANRegNumber(self: Company) = value
"""

    TDSDeductorBranch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TDSDeductorBranch(self: Company) -> str

Set: TDSDeductorBranch(self: Company) = value
"""

    TDSDeductorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TDSDeductorType(self: Company) -> str

Set: TDSDeductorType(self: Company) = value
"""

    Website = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Website(self: Company) -> str

Set: Website(self: Company) = value
"""



class CompanyOnDisk(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ CompanyOnDisk() """
    def ToString(self):
        """ ToString(self: CompanyOnDisk) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompNum(self: CompanyOnDisk) -> str

Set: CompNum(self: CompanyOnDisk) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: CompanyOnDisk) -> str

Set: EndDate(self: CompanyOnDisk) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CompanyOnDisk) -> str

Set: Name(self: CompanyOnDisk) = value
"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDate(self: CompanyOnDisk) -> str

Set: StartDate(self: CompanyOnDisk) = value
"""



class ComponentsItem(object):
    """ ComponentsItem() """
    ActualQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualQuantity(self: ComponentsItem) -> str

Set: ActualQuantity(self: ComponentsItem) = value
"""

    CostAllocPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CostAllocPercentage(self: ComponentsItem) -> str

Set: CostAllocPercentage(self: ComponentsItem) = value
"""

    Godown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Godown(self: ComponentsItem) -> str

Set: Godown(self: ComponentsItem) = value
"""

    NatureOfItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NatureOfItem(self: ComponentsItem) -> ComponentType

Set: NatureOfItem(self: ComponentsItem) = value
"""

    StockItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockItem(self: ComponentsItem) -> str

Set: StockItem(self: ComponentsItem) = value
"""



class ComponentsList(object):
    """ ComponentsList() """
    BasicQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicQuantity(self: ComponentsList) -> str

Set: BasicQuantity(self: ComponentsList) = value
"""

    ComponentsItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentsItems(self: ComponentsList) -> List[ComponentsItem]

Set: ComponentsItems(self: ComponentsList) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ComponentsList) -> str

Set: Name(self: ComponentsList) = value
"""



class ComponentType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ComponentType, values: ByProduct (2), Component (0), CoProduct (3), Scrap (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ByProduct = None
    Component = None
    CoProduct = None
    Scrap = None
    value__ = None


class CostCategoryAllocations(TallyBaseObject):
    """ CostCategoryAllocations() """
    CostCategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CostCategoryName(self: CostCategoryAllocations) -> str

Set: CostCategoryName(self: CostCategoryAllocations) = value
"""

    CostCenterAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CostCenterAllocations(self: CostCategoryAllocations) -> List[CostCenterAllocations]

Set: CostCenterAllocations(self: CostCategoryAllocations) = value
"""



class CostCenterAllocations(TallyBaseObject):
    """ CostCenterAllocations() """
    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: CostCenterAllocations) -> str

Set: Amount(self: CostCenterAllocations) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: CostCenterAllocations) -> str

Set: ForexAmount(self: CostCenterAllocations) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CostCenterAllocations) -> str

Set: Name(self: CostCenterAllocations) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: CostCenterAllocations) -> str

Set: RateofExchange(self: CostCenterAllocations) = value
"""



class Data(object):
    """ Data[T]() """
    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collection(self: Data[T]) -> Colllection[T]

Set: Collection(self: Data[T]) = value
"""

    FuncResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FuncResult(self: Data[T]) -> FunctionResult

Set: FuncResult(self: Data[T]) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: Data[T]) -> Message[T]

Set: Message(self: Data[T]) = value
"""



class DeliveryNotes(object):
    """ DeliveryNotes() """
    DeliveryNote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryNote(self: DeliveryNotes) -> str

Set: DeliveryNote(self: DeliveryNotes) = value
"""

    ShippingDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShippingDate(self: DeliveryNotes) -> str

Set: ShippingDate(self: DeliveryNotes) = value
"""



class Description(object):
    """ Description() """
    StaticVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticVariables(self: Description) -> StaticVariables

Set: StaticVariables(self: Description) = value
"""



class DocumentType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DocumentType, values: BillofEntry (3), BillofSupply (2), Challan (4), CreditNote (6), DeliveryChallan (5), None (0), Others (7), TaxInvoice (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BillofEntry = None
    BillofSupply = None
    Challan = None
    CreditNote = None
    DeliveryChallan = None
    None = None
    Others = None
    TaxInvoice = None
    value__ = None


class Envelope(TallyXmlJson):
    """
    Envelope[T]()
    Envelope[T](ObjecttoExport: T, staticVariables: StaticVariables)
    Envelope[T](ObjectstoExport: List[T], staticVariables: StaticVariables)
    """
    def GetXML(self, attrOverrides):
        """ GetXML(self: Envelope[T], attrOverrides: XmlAttributeOverrides) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, ObjecttoExport: T, staticVariables: StaticVariables)
        __new__(cls: type, ObjectstoExport: List[T], staticVariables: StaticVariables)
        """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: Envelope[T]) -> Body[T]

Set: Body(self: Envelope[T]) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: Envelope[T]) -> Header

Set: Header(self: Envelope[T]) = value
"""



class VoucherLedger(TallyBaseObject):
    """ VoucherLedger() """
    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: VoucherLedger) -> str

Set: Amount(self: VoucherLedger) = value
"""

    BillAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillAllocations(self: VoucherLedger) -> List[BillAllocations]

Set: BillAllocations(self: VoucherLedger) = value
"""

    CleanedAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CleanedAmount(self: VoucherLedger) -> Nullable[float]

Set: CleanedAmount(self: VoucherLedger) = value
"""

    CostCategoryAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CostCategoryAllocations(self: VoucherLedger) -> List[CostCategoryAllocations]

Set: CostCategoryAllocations(self: VoucherLedger) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: VoucherLedger) -> str

Set: ForexAmount(self: VoucherLedger) = value
"""

    InventoryAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InventoryAllocations(self: VoucherLedger) -> List[InventoryAllocations]

Set: InventoryAllocations(self: VoucherLedger) = value
"""

    IsDeemedPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeemedPositive(self: VoucherLedger) -> str

Set: IsDeemedPositive(self: VoucherLedger) = value
"""

    LedgerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LedgerName(self: VoucherLedger) -> str

Set: LedgerName(self: VoucherLedger) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: VoucherLedger) -> str

Set: RateofExchange(self: VoucherLedger) = value
"""



class EVoucherLedger(VoucherLedger):
    """ EVoucherLedger() """

class EwayBillDetail(TallyBaseObject):
    """ EwayBillDetail() """
    BillDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillDate(self: EwayBillDetail) -> str

Set: BillDate(self: EwayBillDetail) = value
"""

    BillNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillNumber(self: EwayBillDetail) -> str

Set: BillNumber(self: EwayBillDetail) = value
"""

    ConsolidatedBillDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsolidatedBillDate(self: EwayBillDetail) -> str

Set: ConsolidatedBillDate(self: EwayBillDetail) = value
"""

    ConsolidatedBillNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsolidatedBillNumber(self: EwayBillDetail) -> str

Set: ConsolidatedBillNumber(self: EwayBillDetail) = value
"""

    DispatchFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchFrom(self: EwayBillDetail) -> str

Set: DispatchFrom(self: EwayBillDetail) = value
"""

    DispatchTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchTo(self: EwayBillDetail) -> str

Set: DispatchTo(self: EwayBillDetail) = value
"""

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentType(self: EwayBillDetail) -> DocumentType

Set: DocumentType(self: EwayBillDetail) = value
"""

    IsCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancelled(self: EwayBillDetail) -> str

Set: IsCancelled(self: EwayBillDetail) = value
"""

    IsCancelledPending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancelledPending(self: EwayBillDetail) -> str

Set: IsCancelledPending(self: EwayBillDetail) = value
"""

    SubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubType(self: EwayBillDetail) -> SubSupplyType

Set: SubType(self: EwayBillDetail) = value
"""

    TransporterDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransporterDetails(self: EwayBillDetail) -> List[TransporterDetail]

Set: TransporterDetails(self: EwayBillDetail) = value
"""



class ExciseJurisdiction(object):
    """ ExciseJurisdiction() """
    ApplicableFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicableFrom(self: ExciseJurisdiction) -> str

Set: ApplicableFrom(self: ExciseJurisdiction) = value
"""

    Commissionerate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Commissionerate(self: ExciseJurisdiction) -> str

Set: Commissionerate(self: ExciseJurisdiction) = value
"""

    Division = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Division(self: ExciseJurisdiction) -> str

Set: Division(self: ExciseJurisdiction) = value
"""

    Range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Range(self: ExciseJurisdiction) -> str

Set: Range(self: ExciseJurisdiction) = value
"""



class ExciseNatureOfPurchase(Enum, IComparable, IFormattable, IConvertible):
    """ enum ExciseNatureOfPurchase, values: Any (1), Importer (2), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Any = None
    Importer = None
    None = None
    value__ = None


class FailureResponse(object):
    """ FailureResponse() """

class FetchList(object):
    """
    FetchList()
    FetchList(FList: List[str])
    """
    @staticmethod # known case of __new__
    def __new__(self, FList=None):
        """
        __new__(cls: type)
        __new__(cls: type, FList: List[str])
        """
        pass

    LFetch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LFetch(self: FetchList) -> List[str]

Set: LFetch(self: FetchList) = value
"""



class Field(DCollection):
    """
    Field(name: str, xMLTag: str)
    Field(fields: List[str], repeatFields: Dictionary[str, str], fieldName: str, xmlTag: str)
    Field(fields: List[str], fieldName: str, xmltag: str)
    Field()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, xMLTag: str)
        __new__(cls: type, fields: List[str], repeatFields: Dictionary[str, str], fieldName: str, xmlTag: str)
        __new__(cls: type, fields: List[str], fieldName: str, xmltag: str)
        __new__(cls: type)
        """
        pass

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: Field) -> str

Set: Fields(self: Field) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Field) -> str

Set: Name(self: Field) = value
"""

    Option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Option(self: Field) -> List[str]

Set: Option(self: Field) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: Field) -> str

Set: Repeat(self: Field) = value
"""

    Scrolled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scrolled(self: Field) -> str

Set: Scrolled(self: Field) = value
"""

    Set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Set(self: Field) -> str

Set: Set(self: Field) = value
"""

    XMLAttr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XMLAttr(self: Field) -> str

Set: XMLAttr(self: Field) = value
"""

    XMLTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XMLTag(self: Field) -> str

Set: XMLTag(self: Field) = value
"""



class Filter(object):
    """
    Filter()
    Filter(filterName: str, filterFormulae: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, filterName=None, filterFormulae=None):
        """
        __new__(cls: type)
        __new__(cls: type, filterName: str, filterFormulae: str)
        """
        pass

    FilterFormulae = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterFormulae(self: Filter) -> str

Set: FilterFormulae(self: Filter) = value
"""

    FilterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterName(self: Filter) -> str

Set: FilterName(self: Filter) = value
"""



class Form(DCollection):
    """
    Form()
    Form(formName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, formName=None):
        """
        __new__(cls: type)
        __new__(cls: type, formName: str)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Form) -> str

Set: Name(self: Form) = value
"""

    PartName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartName(self: Form) -> str

Set: PartName(self: Form) = value
"""

    Parts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parts(self: Form) -> List[str]

Set: Parts(self: Form) = value
"""

    ReportTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReportTag(self: Form) -> str

Set: ReportTag(self: Form) = value
"""

    Set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Set(self: Form) -> List[str]

Set: Set(self: Form) = value
"""

    Use = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Use(self: Form) -> List[str]

Set: Use(self: Form) = value
"""



class FunctionParam(object):
    """
    FunctionParam()
    FunctionParam(param: List[str])
    """
    @staticmethod # known case of __new__
    def __new__(self, param=None):
        """
        __new__(cls: type)
        __new__(cls: type, param: List[str])
        """
        pass

    Param = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Param(self: FunctionParam) -> List[str]

Set: Param(self: FunctionParam) = value
"""



class FunctionResult(object):
    """ FunctionResult() """
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: FunctionResult) -> str

Set: Result(self: FunctionResult) = value
"""



class GSTDetail(TallyBaseObject):
    """ GSTDetail() """
    ApplicableFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicableFrom(self: GSTDetail) -> str

Set: ApplicableFrom(self: GSTDetail) = value
"""

    CalculationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculationType(self: GSTDetail) -> str

Set: CalculationType(self: GSTDetail) = value
"""

    HSNCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HSNCode(self: GSTDetail) -> str

Set: HSNCode(self: GSTDetail) = value
"""

    HSNDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HSNDescription(self: GSTDetail) -> str

Set: HSNDescription(self: GSTDetail) = value
"""

    HSNMasterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HSNMasterName(self: GSTDetail) -> str

Set: HSNMasterName(self: GSTDetail) = value
"""

    IcludeExpForSlabCalc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IcludeExpForSlabCalc(self: GSTDetail) -> YesNo

Set: IcludeExpForSlabCalc(self: GSTDetail) = value
"""

    IsInEligibleforITC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInEligibleforITC(self: GSTDetail) -> YesNo

Set: IsInEligibleforITC(self: GSTDetail) = value
"""

    IsNonGSTGoods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNonGSTGoods(self: GSTDetail) -> YesNo

Set: IsNonGSTGoods(self: GSTDetail) = value
"""

    IsReverseChargeApplicable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReverseChargeApplicable(self: GSTDetail) -> YesNo

Set: IsReverseChargeApplicable(self: GSTDetail) = value
"""

    StateWiseDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateWiseDetails(self: GSTDetail) -> List[StateWiseDetail]

Set: StateWiseDetails(self: GSTDetail) = value
"""

    Taxability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Taxability(self: GSTDetail) -> GSTTaxabilityType

Set: Taxability(self: GSTDetail) = value
"""



class GSTPartyType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GSTPartyType, values: DeemedExport (1), Embassy_UN_Body (2), No (4), None (0), NotApplicable (0), SEZ (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DeemedExport = None
    Embassy_UN_Body = None
    No = None
    None = None
    NotApplicable = None
    SEZ = None
    value__ = None


class GSTRateDetail(object):
    """ GSTRateDetail() """
    DutyHead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DutyHead(self: GSTRateDetail) -> str

Set: DutyHead(self: GSTRateDetail) = value
"""

    GSTRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTRate(self: GSTRateDetail) -> float

Set: GSTRate(self: GSTRateDetail) = value
"""

    ValuationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValuationType(self: GSTRateDetail) -> str

Set: ValuationType(self: GSTRateDetail) = value
"""



class GSTRegistrationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GSTRegistrationType, values: Composition (1), Consumer (2), None (0), Regular (3), Unknown (0), Unregistered (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Composition = None
    Consumer = None
    None = None
    Regular = None
    Unknown = None
    Unregistered = None
    value__ = None


class GSTTaxabilityType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GSTTaxabilityType, values: Exempt (2), NilRated (3), None (0), Taxable (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Exempt = None
    NilRated = None
    None = None
    Taxable = None
    value__ = None


class GSTTaxType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GSTTaxType, values: CentralTax (1), Cess (2), IntegratedTax (3), None (0), StateTax (5), UTTax (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CentralTax = None
    Cess = None
    IntegratedTax = None
    None = None
    StateTax = None
    UTTax = None
    value__ = None


class HAddress(object):
    """ HAddress() """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: HAddress) -> List[str]

Set: Address(self: HAddress) = value
"""

    FullAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullAddress(self: HAddress) -> str

Set: FullAddress(self: HAddress) = value
"""



class Header(object):
    """
    Header(Request: RequestTye, Type: HType, ID: str)
    Header()
    """
    @staticmethod # known case of __new__
    def __new__(self, Request=None, Type=None, ID=None):
        """
        __new__(cls: type, Request: RequestTye, Type: HType, ID: str)
        __new__(cls: type)
        """
        pass

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ID(self: Header) -> str

Set: ID(self: Header) = value
"""

    Request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Request(self: Header) -> RequestTye

Set: Request(self: Header) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Header) -> HType

Set: Type(self: Header) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: Header) -> int

Set: Version(self: Header) = value
"""



class HType(Enum, IComparable, IFormattable, IConvertible):
    """ enum HType, values: Collection (1), Data (2), Function (3), Object (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Collection = None
    Data = None
    Function = None
    Object = None
    value__ = None


class IBasicTallyObject:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: IBasicTallyObject) -> str

Set: GUID(self: IBasicTallyObject) = value
"""

    TallyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TallyId(self: IBasicTallyObject) -> Nullable[int]

Set: TallyId(self: IBasicTallyObject) = value
"""



class ID(object):
    """ ID() """
    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: ID) -> str

Set: Text(self: ID) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ID) -> str

Set: Type(self: ID) = value
"""



class ImportResult(object):
    """ ImportResult() """
    Altered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Altered(self: ImportResult) -> Nullable[int]

Set: Altered(self: ImportResult) = value
"""

    Cacelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cacelled(self: ImportResult) -> Nullable[int]

Set: Cacelled(self: ImportResult) = value
"""

    Combined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Combined(self: ImportResult) -> Nullable[int]

Set: Combined(self: ImportResult) = value
"""

    Created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Created(self: ImportResult) -> Nullable[int]

Set: Created(self: ImportResult) = value
"""

    Deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Deleted(self: ImportResult) -> Nullable[int]

Set: Deleted(self: ImportResult) = value
"""

    Errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Errors(self: ImportResult) -> Nullable[int]

Set: Errors(self: ImportResult) = value
"""

    Ignored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ignored(self: ImportResult) -> Nullable[int]

Set: Ignored(self: ImportResult) = value
"""

    LastMID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastMID(self: ImportResult) -> Nullable[int]

Set: LastMID(self: ImportResult) = value
"""

    LastVchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastVchId(self: ImportResult) -> Nullable[int]

Set: LastVchId(self: ImportResult) = value
"""



class InterestAppliedOn(Enum, IComparable, IFormattable, IConvertible):
    """ enum InterestAppliedOn, values: Always (1), None (0), PastDueDate (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Always = None
    None = None
    PastDueDate = None
    value__ = None


class InterestBalanceType(Enum, IComparable, IFormattable, IConvertible):
    """ enum InterestBalanceType, values: AllBalances (1), None (0), OnCreditBalances (2), OnDebitBalances (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllBalances = None
    None = None
    OnCreditBalances = None
    OnDebitBalances = None
    value__ = None


class InterestFromType(Enum, IComparable, IFormattable, IConvertible):
    """ enum InterestFromType, values: DateOfApplicability (1), DateSpecifiedDuringEntry (2), DueDateOfInvoice (3), EffectiveDateOfTransaction (4), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DateOfApplicability = None
    DateSpecifiedDuringEntry = None
    DueDateOfInvoice = None
    EffectiveDateOfTransaction = None
    None = None
    value__ = None


class InterestStyle(Enum, IComparable, IFormattable, IConvertible):
    """ enum InterestStyle, values: CalendarMonth (3), CalendarYear (4), Month_30Day (1), None (0), Year_365Day (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalendarMonth = None
    CalendarYear = None
    Month_30Day = None
    None = None
    value__ = None
    Year_365Day = None


class InventoryEntries(AllInventoryAllocations):
    """ InventoryEntries() """

class InventoryinAllocations(InventoryAllocations):
    """ InventoryinAllocations() """

class InventoryoutAllocations(InventoryAllocations):
    """ InventoryoutAllocations() """

class ITallyObject:
    # no doc
    def PrepareForExport(self):
        """ PrepareForExport(self: ITallyObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: ITallyObject) -> str

Set: GUID(self: ITallyObject) = value
"""

    TallyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TallyId(self: ITallyObject) -> Nullable[int]

Set: TallyId(self: ITallyObject) = value
"""



class LanguageNameList(object):
    """ LanguageNameList() """
    LanguageAlias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageAlias(self: LanguageNameList) -> str

Set: LanguageAlias(self: LanguageNameList) = value
"""

    NameList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameList(self: LanguageNameList) -> Names

Set: NameList(self: LanguageNameList) = value
"""



class LicenseInfo(TallyXmlJson):
    """ LicenseInfo() """
    AccountId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AccountId(self: LicenseInfo) -> str

Set: AccountId(self: LicenseInfo) = value
"""

    AdminMailId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdminMailId(self: LicenseInfo) -> str

Set: AdminMailId(self: LicenseInfo) = value
"""

    ApplicationPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationPath(self: LicenseInfo) -> str

Set: ApplicationPath(self: LicenseInfo) = value
"""

    DataPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataPath(self: LicenseInfo) -> str

Set: DataPath(self: LicenseInfo) = value
"""

    IsAdmin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAdmin(self: LicenseInfo) -> str

Set: IsAdmin(self: LicenseInfo) = value
"""

    IsEducationalMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEducationalMode(self: LicenseInfo) -> str

Set: IsEducationalMode(self: LicenseInfo) = value
"""

    IsGold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGold(self: LicenseInfo) -> str

Set: IsGold(self: LicenseInfo) = value
"""

    IsIndian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIndian(self: LicenseInfo) -> str

Set: IsIndian(self: LicenseInfo) = value
"""

    IsLicenseClientMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLicenseClientMode(self: LicenseInfo) -> str

Set: IsLicenseClientMode(self: LicenseInfo) = value
"""

    IsRemoteAccessMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRemoteAccessMode(self: LicenseInfo) -> str

Set: IsRemoteAccessMode(self: LicenseInfo) = value
"""

    IsSilver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSilver(self: LicenseInfo) -> str

Set: IsSilver(self: LicenseInfo) = value
"""

    PlanName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanName(self: LicenseInfo) -> str

Set: PlanName(self: LicenseInfo) = value
"""

    RemoteSerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemoteSerialNumber(self: LicenseInfo) -> str

Set: RemoteSerialNumber(self: LicenseInfo) = value
"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumber(self: LicenseInfo) -> str

Set: SerialNumber(self: LicenseInfo) = value
"""

    UserLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserLevel(self: LicenseInfo) -> str

Set: UserLevel(self: LicenseInfo) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: LicenseInfo) -> str

Set: UserName(self: LicenseInfo) = value
"""



class LicInfoBody(object):
    """ LicInfoBody() """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: LicInfoBody) -> LicInfoData

Set: Data(self: LicInfoBody) = value
"""

    Desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Desc(self: LicInfoBody) -> Description

Set: Desc(self: LicInfoBody) = value
"""



class LicInfoColloction(object):
    """ LicInfoColloction() """
    LicenseInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseInfo(self: LicInfoColloction) -> LicenseInfo

Set: LicenseInfo(self: LicInfoColloction) = value
"""



class LicInfoData(object):
    """ LicInfoData() """
    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collection(self: LicInfoData) -> LicInfoColloction

Set: Collection(self: LicInfoData) = value
"""



class LicInfoEnvelope(TallyXmlJson):
    """ LicInfoEnvelope() """
    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: LicInfoEnvelope) -> LicInfoBody

Set: Body(self: LicInfoEnvelope) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: LicInfoEnvelope) -> Header

Set: Header(self: LicInfoEnvelope) = value
"""



class Line(DCollection):
    """
    Line(lineName: str, fields: List[str], xmlTag: str)
    Line(lineName: str, CollectionName: str)
    Line()
    """
    @staticmethod # known case of __new__
    def __new__(self, lineName=None, *__args):
        """
        __new__(cls: type, lineName: str, fields: List[str], xmlTag: str)
        __new__(cls: type, lineName: str, CollectionName: str)
        __new__(cls: type)
        """
        pass

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: Line) -> List[str]

Set: Fields(self: Line) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Line) -> str

Set: Name(self: Line) = value
"""

    Option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Option(self: Line) -> List[str]

Set: Option(self: Line) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: Line) -> str

Set: Repeat(self: Line) = value
"""

    Scrolled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scrolled(self: Line) -> str

Set: Scrolled(self: Line) = value
"""

    XMLTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XMLTag(self: Line) -> str

Set: XMLTag(self: Line) = value
"""



class MasterLookupField(Enum, IComparable, IFormattable, IConvertible):
    """ enum MasterLookupField, values: AlterId (2), GUID (4), MasterId (1), Name (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlterId = None
    GUID = None
    MasterId = None
    Name = None
    value__ = None


class MastersBasicInfo(object):
    """ MastersBasicInfo[T](masterType: TallyObjectType, masters: List[T]) """
    @staticmethod # known case of __new__
    def __new__(self, masterType, masters):
        """ __new__(cls: type, masterType: TallyObjectType, masters: List[T]) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MastersBasicInfo[T]) -> int

"""

    Masters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Masters(self: MastersBasicInfo[T]) -> List[T]

Set: Masters(self: MastersBasicInfo[T]) = value
"""

    MasterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterType(self: MastersBasicInfo[T]) -> TallyObjectType

Set: MasterType(self: MastersBasicInfo[T]) = value
"""



class MastersMapping(object):
    """ MastersMapping(masterType: TallyObjectType, tallyMasterType: str, filters: List[Filter]) """
    @staticmethod # known case of __new__
    def __new__(self, masterType, tallyMasterType, filters):
        """ __new__(cls: type, masterType: TallyObjectType, tallyMasterType: str, filters: List[Filter]) """
        pass

    Filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filters(self: MastersMapping) -> List[Filter]

Set: Filters(self: MastersMapping) = value
"""

    MasterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterType(self: MastersMapping) -> TallyObjectType

Set: MasterType(self: MastersMapping) = value
"""

    TallyMasterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TallyMasterType(self: MastersMapping) -> str

Set: TallyMasterType(self: MastersMapping) = value
"""


    MastersMappings = None


class Message(object):
    """ Message[T]() """
    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: Message[T]) -> List[T]

Set: Objects(self: Message[T]) = value
"""



class MultiAddress(object):
    """ MultiAddress() """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: MultiAddress) -> str

Set: Address(self: MultiAddress) = value
"""

    ContactPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContactPerson(self: MultiAddress) -> str

Set: ContactPerson(self: MultiAddress) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Country(self: MultiAddress) -> str

Set: Country(self: MultiAddress) = value
"""

    CSTNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CSTNumber(self: MultiAddress) -> str

Set: CSTNumber(self: MultiAddress) = value
"""

    Email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Email(self: MultiAddress) -> str

Set: Email(self: MultiAddress) = value
"""

    ExciseImportRegistrationNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExciseImportRegistrationNo(self: MultiAddress) -> str

Set: ExciseImportRegistrationNo(self: MultiAddress) = value
"""

    ExciseJurisdictions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExciseJurisdictions(self: MultiAddress) -> List[ExciseJurisdiction]

Set: ExciseJurisdictions(self: MultiAddress) = value
"""

    ExciseNatureOfPurchase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExciseNatureOfPurchase(self: MultiAddress) -> ExciseNatureOfPurchase

Set: ExciseNatureOfPurchase(self: MultiAddress) = value
"""

    ExciseRegistrationNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExciseRegistrationNo(self: MultiAddress) -> str

Set: ExciseRegistrationNo(self: MultiAddress) = value
"""

    FaxNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaxNumber(self: MultiAddress) -> str

Set: FaxNumber(self: MultiAddress) = value
"""

    GSTDealerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTDealerType(self: MultiAddress) -> GSTRegistrationType

Set: GSTDealerType(self: MultiAddress) = value
"""

    GSTIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTIN(self: MultiAddress) -> str

Set: GSTIN(self: MultiAddress) = value
"""

    ImportExportCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportExportCode(self: MultiAddress) -> str

Set: ImportExportCode(self: MultiAddress) = value
"""

    IsOtherTerritoryAssessee = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOtherTerritoryAssessee(self: MultiAddress) -> YesNo

Set: IsOtherTerritoryAssessee(self: MultiAddress) = value
"""

    MobileNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MobileNo(self: MultiAddress) -> str

Set: MobileNo(self: MultiAddress) = value
"""

    PANNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PANNumber(self: MultiAddress) -> str

Set: PANNumber(self: MultiAddress) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: MultiAddress) -> str

Set: PhoneNumber(self: MultiAddress) = value
"""

    PinCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PinCode(self: MultiAddress) -> str

Set: PinCode(self: MultiAddress) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: MultiAddress) -> str

Set: State(self: MultiAddress) = value
"""

    VATNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VATNumber(self: MultiAddress) -> str

Set: VATNumber(self: MultiAddress) = value
"""


    FAddress = None


class Names(object):
    """ Names() """
    NAMES = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NAMES(self: Names) -> List[str]

Set: NAMES(self: Names) = value
"""



class ObjBody(object):
    """ ObjBody() """
    Desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Desc(self: ObjBody) -> ObjDescription

Set: Desc(self: ObjBody) = value
"""



class ObjDescription(object):
    """ ObjDescription() """
    FetchList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FetchList(self: ObjDescription) -> FetchList

Set: FetchList(self: ObjDescription) = value
"""

    StaticVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticVariables(self: ObjDescription) -> StaticVariables

Set: StaticVariables(self: ObjDescription) = value
"""



class ObjEnvelope(TallyXmlJson):
    """ ObjEnvelope() """
    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: ObjEnvelope) -> ObjBody

Set: Body(self: ObjEnvelope) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: ObjEnvelope) -> ObjHeader

Set: Header(self: ObjEnvelope) = value
"""



class ObjHeader(object):
    """
    ObjHeader(subtype: str, ObjID: str)
    ObjHeader()
    """
    @staticmethod # known case of __new__
    def __new__(self, subtype=None, ObjID=None):
        """
        __new__(cls: type, subtype: str, ObjID: str)
        __new__(cls: type)
        """
        pass

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ID(self: ObjHeader) -> ID

Set: ID(self: ObjHeader) = value
"""

    Request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Request(self: ObjHeader) -> str

Set: Request(self: ObjHeader) = value
"""

    SubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubType(self: ObjHeader) -> str

Set: SubType(self: ObjHeader) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ObjHeader) -> str

Set: Type(self: ObjHeader) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: ObjHeader) -> int

Set: Version(self: ObjHeader) = value
"""



class Part(DCollection):
    """
    Part(topPartName: str, colName: str, lineName: str)
    Part()
    Part(rootTag: str, collectionName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, topPartName: str, colName: str, lineName: str)
        __new__(cls: type)
        __new__(cls: type, rootTag: str, collectionName: str)
        """
        pass

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: Part) -> List[str]

Set: Lines(self: Part) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Part) -> str

Set: Name(self: Part) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: Part) -> str

Set: Repeat(self: Part) = value
"""

    Scrolled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scrolled(self: Part) -> str

Set: Scrolled(self: Part) = value
"""



class PaymentDetails(object):
    """ PaymentDetails() """
    BankAccountNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BankAccountNo(self: PaymentDetails) -> str

Set: BankAccountNo(self: PaymentDetails) = value
"""

    BankBranch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BankBranch(self: PaymentDetails) -> str

Set: BankBranch(self: PaymentDetails) = value
"""

    ChequeCrossComment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChequeCrossComment(self: PaymentDetails) -> str

Set: ChequeCrossComment(self: PaymentDetails) = value
"""

    DefaultTransactionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultTransactionType(self: PaymentDetails) -> str

Set: DefaultTransactionType(self: PaymentDetails) = value
"""

    IFSC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFSC(self: PaymentDetails) -> str

Set: IFSC(self: PaymentDetails) = value
"""

    InFavour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InFavour(self: PaymentDetails) -> str

Set: InFavour(self: PaymentDetails) = value
"""

    SetasDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetasDefault(self: PaymentDetails) -> str

Set: SetasDefault(self: PaymentDetails) = value
"""

    TransactionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransactionName(self: PaymentDetails) -> str

Set: TransactionName(self: PaymentDetails) = value
"""



class PResult(object):
    """ PResult() """
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PResult) -> str

Set: Result(self: PResult) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PResult) -> RespStatus

Set: Status(self: PResult) = value
"""

    VoucherMasterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VoucherMasterId(self: PResult) -> str

Set: VoucherMasterId(self: PResult) = value
"""



class RBody(object):
    """ RBody() """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: RBody) -> Rdata

Set: Data(self: RBody) = value
"""



class Rdata(object):
    """ Rdata() """
    ImportResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportResult(self: Rdata) -> ImportResult

Set: ImportResult(self: Rdata) = value
"""

    LineError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineError(self: Rdata) -> str

Set: LineError(self: Rdata) = value
"""



class Report(DCollection):
    """
    Report()
    Report(rName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, rName=None):
        """
        __new__(cls: type)
        __new__(cls: type, rName: str)
        """
        pass

    AttrName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttrName(self: Report) -> str

Set: AttrName(self: Report) = value
"""

    FormName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormName(self: Report) -> str

Set: FormName(self: Report) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: Report) -> List[str]

Set: Repeat(self: Report) = value
"""

    Set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Set(self: Report) -> List[str]

Set: Set(self: Report) = value
"""

    Use = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Use(self: Report) -> List[str]

Set: Use(self: Report) = value
"""

    Variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Variable(self: Report) -> List[str]

Set: Variable(self: Report) = value
"""



class ReportField(object):
    """
    ReportField(XmlTag: str)
    ReportField(XmlTag: str, subFields: List[ReportField])
    ReportField(XmlTag: str, colName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, XmlTag, *__args):
        """
        __new__(cls: type, XmlTag: str)
        __new__(cls: type, XmlTag: str, subFields: List[ReportField])
        __new__(cls: type, XmlTag: str, colName: str)
        """
        pass

    Atrributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Atrributes(self: ReportField) -> List[str]

Set: Atrributes(self: ReportField) = value
"""

    CollectionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectionName(self: ReportField) -> str

Set: CollectionName(self: ReportField) = value
"""

    FieldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldName(self: ReportField) -> str

Set: FieldName(self: ReportField) = value
"""

    SubFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubFields(self: ReportField) -> List[ReportField]

Set: SubFields(self: ReportField) = value
"""

    XMLTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XMLTag(self: ReportField) -> str

Set: XMLTag(self: ReportField) = value
"""



class ReqDescription(object):
    """ ReqDescription() """
    FunctionParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FunctionParams(self: ReqDescription) -> FunctionParam

Set: FunctionParams(self: ReqDescription) = value
"""

    StaticVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticVariables(self: ReqDescription) -> StaticVariables

Set: StaticVariables(self: ReqDescription) = value
"""

    TDL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TDL(self: ReqDescription) -> ReqTDL

Set: TDL(self: ReqDescription) = value
"""



class ReqTDL(object):
    """ ReqTDL() """
    TDLMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TDLMessage(self: ReqTDL) -> TDLMessage

Set: TDLMessage(self: ReqTDL) = value
"""



class RequestBody(object):
    """ RequestBody() """
    Desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Desc(self: RequestBody) -> ReqDescription

Set: Desc(self: RequestBody) = value
"""



class RequestEnvelope(TallyXmlJson):
    """
    RequestEnvelope()
    RequestEnvelope(Type: HType, iD: str)
    RequestEnvelope(Type: HType, iD: str, sv: StaticVariables)
    RequestEnvelope(Type: HType, iD: str, sv: StaticVariables, rootreportfield: ReportField)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type=None, iD=None, sv=None, rootreportfield=None):
        """
        __new__(cls: type)
        __new__(cls: type, Type: HType, iD: str)
        __new__(cls: type, Type: HType, iD: str, sv: StaticVariables)
        __new__(cls: type, Type: HType, iD: str, sv: StaticVariables, rootreportfield: ReportField)
        """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: RequestEnvelope) -> RequestBody

Set: Body(self: RequestEnvelope) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: RequestEnvelope) -> Header

Set: Header(self: RequestEnvelope) = value
"""



class RequestTye(Enum, IComparable, IFormattable, IConvertible):
    """ enum RequestTye, values: Export (0), Import (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Export = None
    Import = None
    value__ = None


class ResponseEnvelope(object):
    """ ResponseEnvelope() """
    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: ResponseEnvelope) -> RBody

Set: Body(self: ResponseEnvelope) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: ResponseEnvelope) -> RHeader

Set: Header(self: ResponseEnvelope) = value
"""



class RespStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RespStatus, values: Failure (1), Sucess (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Failure = None
    Sucess = None
    value__ = None


class RHeader(object):
    """ RHeader() """
    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: RHeader) -> int

Set: Status(self: RHeader) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: RHeader) -> int

Set: Version(self: RHeader) = value
"""



class RoundType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RoundType, values: Dowward (1), None (0), Normal (2), NotApplicable (0), Upward (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Dowward = None
    None = None
    Normal = None
    NotApplicable = None
    Upward = None
    value__ = None


class StateWiseDetail(object):
    """ StateWiseDetail() """
    GSTRateDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTRateDetails(self: StateWiseDetail) -> List[GSTRateDetail]

Set: GSTRateDetails(self: StateWiseDetail) = value
"""

    StateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateName(self: StateWiseDetail) -> str

Set: StateName(self: StateWiseDetail) = value
"""



class StaticVariables(TallyBaseObject):
    """ StaticVariables() """
    ExplodeFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExplodeFlag(self: StaticVariables) -> str

Set: ExplodeFlag(self: StaticVariables) = value
"""

    SVCompany = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVCompany(self: StaticVariables) -> str

Set: SVCompany(self: StaticVariables) = value
"""

    SVExportFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVExportFormat(self: StaticVariables) -> str

Set: SVExportFormat(self: StaticVariables) = value
"""

    SVFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVFrom(self: StaticVariables) -> SVFrom

Set: SVFrom(self: StaticVariables) = value
"""

    SVFromDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVFromDate(self: StaticVariables) -> str

Set: SVFromDate(self: StaticVariables) = value
"""

    SVTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVTo(self: StaticVariables) -> SVTo

Set: SVTo(self: StaticVariables) = value
"""

    SVToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SVToDate(self: StaticVariables) -> str

Set: SVToDate(self: StaticVariables) = value
"""

    ViewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewName(self: StaticVariables) -> VoucherViewType

Set: ViewName(self: StaticVariables) = value
"""



class SubSupplyType(Enum, IComparable, IFormattable, IConvertible):
    """ enum SubSupplyType, values: ExhibitionorFairs (12), Export (3), ForOwnUse (5), Import (2), JobWork (4), JobWorkReturns (6), LinesSales (10), None (0), Others (8), RecipientNotKnown (11), SalesReturn (7), SKD_CKD_Lots (9), Supply (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ExhibitionorFairs = None
    Export = None
    ForOwnUse = None
    Import = None
    JobWork = None
    JobWorkReturns = None
    LinesSales = None
    None = None
    Others = None
    RecipientNotKnown = None
    SalesReturn = None
    SKD_CKD_Lots = None
    Supply = None
    value__ = None


class SVFrom(object):
    """ SVFrom() """
    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: SVFrom) -> str

Set: Text(self: SVFrom) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SVFrom) -> str

Set: Type(self: SVFrom) = value
"""



class SVTo(object):
    """ SVTo() """
    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: SVTo) -> str

Set: Text(self: SVTo) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SVTo) -> str

Set: Type(self: SVTo) = value
"""



class System(object):
    """
    System()
    System(name: str, text: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None, text=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, text: str)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: System) -> str

Set: Name(self: System) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: System) -> str

Set: Text(self: System) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: System) -> str

Set: Type(self: System) = value
"""



class TallyCustomObject(DCollection):
    """
    TallyCustomObject()
    TallyCustomObject(name: str, formulas: List[str])
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None, formulas=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, formulas: List[str])
        """
        pass

    LocalFormulas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalFormulas(self: TallyCustomObject) -> List[str]

Set: LocalFormulas(self: TallyCustomObject) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: TallyCustomObject) -> str

Set: Name(self: TallyCustomObject) = value
"""



class TallyObjectType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TallyObjectType, values: AttendanceTypes (10), CostCategories (3), CostCenters (4), Currencies (0), EmployeeGroups (11), Employees (12), Godowns (5), Groups (1), Ledgers (2), StockCategories (6), StockGroups (7), StockItems (8), Units (9), Vouchers (14), VoucherTypes (13) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AttendanceTypes = None
    CostCategories = None
    CostCenters = None
    Currencies = None
    EmployeeGroups = None
    Employees = None
    Godowns = None
    Groups = None
    Ledgers = None
    StockCategories = None
    StockGroups = None
    StockItems = None
    Units = None
    value__ = None
    Vouchers = None
    VoucherTypes = None


class TaxType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TaxType, values: CENVAT (10), CST (9), Default (8), Excise (4), FBT (5), GST (1), KrishiKalyanCess (11), Others (0), ServiceTax (6), SwachhBharatCess (12), TCS (2), TDS (3), VAT (7) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CENVAT = None
    CST = None
    Default = None
    Excise = None
    FBT = None
    GST = None
    KrishiKalyanCess = None
    Others = None
    ServiceTax = None
    SwachhBharatCess = None
    TCS = None
    TDS = None
    value__ = None
    VAT = None


class TDLMessage(object):
    """
    TDLMessage()
    TDLMessage(colName: str, colType: str, childof: str, nativeFields: List[str], filters: List[Filter], isInitialize: YesNo)
    TDLMessage(tallyCustomObjects: List[TallyCustomObject], objCollectionName: str, ObjNames: str)
    TDLMessage(rootreportField: ReportField)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, colName: str, colType: str, childof: str, nativeFields: List[str], filters: List[Filter], isInitialize: YesNo)
        __new__(cls: type, tallyCustomObjects: List[TallyCustomObject], objCollectionName: str, ObjNames: str)
        __new__(cls: type, rootreportField: ReportField)
        """
        pass

    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collection(self: TDLMessage) -> List[Collection]

Set: Collection(self: TDLMessage) = value
"""

    Field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Field(self: TDLMessage) -> List[Field]

Set: Field(self: TDLMessage) = value
"""

    Form = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Form(self: TDLMessage) -> List[Form]

Set: Form(self: TDLMessage) = value
"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Line(self: TDLMessage) -> List[Line]

Set: Line(self: TDLMessage) = value
"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: TDLMessage) -> List[TallyCustomObject]

Set: Object(self: TDLMessage) = value
"""

    Part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Part(self: TDLMessage) -> List[Part]

Set: Part(self: TDLMessage) = value
"""

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Report(self: TDLMessage) -> List[Report]

Set: Report(self: TDLMessage) = value
"""

    System = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: System(self: TDLMessage) -> List[System]

Set: System(self: TDLMessage) = value
"""



class TransporterDetail(TallyBaseObject):
    """ TransporterDetail() """
    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: TransporterDetail) -> str

Set: Distance(self: TransporterDetail) = value
"""

    DocumentDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentDate(self: TransporterDetail) -> str

Set: DocumentDate(self: TransporterDetail) = value
"""

    DocumentNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentNumber(self: TransporterDetail) -> str

Set: DocumentNumber(self: TransporterDetail) = value
"""

    TransporterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransporterId(self: TransporterDetail) -> str

Set: TransporterId(self: TransporterDetail) = value
"""

    TransporterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransporterName(self: TransporterDetail) -> str

Set: TransporterName(self: TransporterDetail) = value
"""

    TransportMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportMode(self: TransporterDetail) -> TransportMode

Set: TransportMode(self: TransporterDetail) = value
"""

    VehicleNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VehicleNumber(self: TransporterDetail) -> str

Set: VehicleNumber(self: TransporterDetail) = value
"""

    VehicleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VehicleType(self: TransporterDetail) -> VehicleType

Set: VehicleType(self: TransporterDetail) = value
"""



class TransportMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum TransportMode, values: Air (3), None (0), Rail (2), Road (1), Ship (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Air = None
    None = None
    Rail = None
    Road = None
    Ship = None
    value__ = None


class VBody(object):
    """ VBody() """
    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: VBody) -> VData

Set: Data(self: VBody) = value
"""

    Desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Desc(self: VBody) -> Description

Set: Desc(self: VBody) = value
"""



class VData(object):
    """ VData() """
    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collection(self: VData) -> VouchColl

Set: Collection(self: VData) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: VData) -> VoucherMessage

Set: Message(self: VData) = value
"""



class VehicleType(Enum, IComparable, IFormattable, IConvertible):
    """ enum VehicleType, values: None (0), OverDimensionalCargo (2), Regular (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    OverDimensionalCargo = None
    Regular = None
    value__ = None


class VouchColl(object):
    """ VouchColl() """
    Vouchers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vouchers(self: VouchColl) -> List[Voucher]

Set: Vouchers(self: VouchColl) = value
"""



class Voucher(TallyXmlJson, ITallyObject):
    """ Voucher() """
    def GetJson(self, Indented):
        """ GetJson(self: Voucher, Indented: bool) -> str """
        pass

    def GetJulianday(self):
        """ GetJulianday(self: Voucher) """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: Voucher, attrOverrides: XmlAttributeOverrides) -> str """
        pass

    def OrderLedgers(self):
        """ OrderLedgers(self: Voucher) """
        pass

    def PrepareForExport(self):
        """ PrepareForExport(self: Voucher) """
        pass

    def ToString(self):
        """ ToString(self: Voucher) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: Voucher) -> Action

Set: Action(self: Voucher) = value
"""

    AlterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlterId(self: Voucher) -> Nullable[int]

Set: AlterId(self: Voucher) = value
"""

    AttendanceEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttendanceEntries(self: Voucher) -> List[AttendanceEntry]

Set: AttendanceEntries(self: Voucher) = value
"""

    BasicDueDateofPayment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicDueDateofPayment(self: Voucher) -> str

Set: BasicDueDateofPayment(self: Voucher) = value
"""

    BasicShippedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicShippedBy(self: Voucher) -> str

Set: BasicShippedBy(self: Voucher) = value
"""

    BillofLandingDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillofLandingDate(self: Voucher) -> str

Set: BillofLandingDate(self: Voucher) = value
"""

    BillofLandingNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillofLandingNo(self: Voucher) -> str

Set: BillofLandingNo(self: Voucher) = value
"""

    BillToPlace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BillToPlace(self: Voucher) -> str

Set: BillToPlace(self: Voucher) = value
"""

    CarrierName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CarrierName(self: Voucher) -> str

Set: CarrierName(self: Voucher) = value
"""

    ConsigneeCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneeCountry(self: Voucher) -> str

Set: ConsigneeCountry(self: Voucher) = value
"""

    ConsigneeGSTIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneeGSTIN(self: Voucher) -> str

Set: ConsigneeGSTIN(self: Voucher) = value
"""

    ConsigneeMailingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneeMailingName(self: Voucher) -> str

Set: ConsigneeMailingName(self: Voucher) = value
"""

    ConsigneeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneeName(self: Voucher) -> str

Set: ConsigneeName(self: Voucher) = value
"""

    ConsigneePinCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneePinCode(self: Voucher) -> str

Set: ConsigneePinCode(self: Voucher) = value
"""

    ConsigneeState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConsigneeState(self: Voucher) -> str

Set: ConsigneeState(self: Voucher) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Country(self: Voucher) -> str

Set: Country(self: Voucher) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: Voucher) -> str

Set: Date(self: Voucher) = value
"""

    DeliveryNoteNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryNoteNo(self: Voucher) -> str

Set: DeliveryNoteNo(self: Voucher) = value
"""

    DeliveryNotes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryNotes(self: Voucher) -> DeliveryNotes

Set: DeliveryNotes(self: Voucher) = value
"""

    DesktinationCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesktinationCountry(self: Voucher) -> str

Set: DesktinationCountry(self: Voucher) = value
"""

    Destination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Destination(self: Voucher) -> str

Set: Destination(self: Voucher) = value
"""

    DischargePort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DischargePort(self: Voucher) -> str

Set: DischargePort(self: Voucher) = value
"""

    DispatchDocNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchDocNo(self: Voucher) -> str

Set: DispatchDocNo(self: Voucher) = value
"""

    DispatchFromName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchFromName(self: Voucher) -> str

Set: DispatchFromName(self: Voucher) = value
"""

    DispatchFromPinCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchFromPinCode(self: Voucher) -> str

Set: DispatchFromPinCode(self: Voucher) = value
"""

    DispatchFromPlace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchFromPlace(self: Voucher) -> str

Set: DispatchFromPlace(self: Voucher) = value
"""

    DispatchFromStateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispatchFromStateName(self: Voucher) -> str

Set: DispatchFromStateName(self: Voucher) = value
"""

    Dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dt(self: Voucher) -> str

Set: Dt(self: Voucher) = value
"""

    EffectiveDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveDate(self: Voucher) -> str

Set: EffectiveDate(self: Voucher) = value
"""

    EWayBillDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EWayBillDetails(self: Voucher) -> List[EwayBillDetail]

Set: EWayBillDetails(self: Voucher) = value
"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: Voucher) -> str

Set: GUID(self: Voucher) = value
"""

    InventoriesIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InventoriesIn(self: Voucher) -> List[InventoryinAllocations]

Set: InventoriesIn(self: Voucher) = value
"""

    InventoriesOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InventoriesOut(self: Voucher) -> List[InventoryoutAllocations]

Set: InventoriesOut(self: Voucher) = value
"""

    InventoryAllocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InventoryAllocations(self: Voucher) -> List[AllInventoryAllocations]

Set: InventoryAllocations(self: Voucher) = value
"""

    IRN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IRN(self: Voucher) -> str

Set: IRN(self: Voucher) = value
"""

    IRNAckDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IRNAckDate(self: Voucher) -> str

Set: IRNAckDate(self: Voucher) = value
"""

    IRNAckNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IRNAckNo(self: Voucher) -> str

Set: IRNAckNo(self: Voucher) = value
"""

    IsCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancelled(self: Voucher) -> str

Set: IsCancelled(self: Voucher) = value
"""

    IsOptional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOptional(self: Voucher) -> str

Set: IsOptional(self: Voucher) = value
"""

    LandingPort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LandingPort(self: Voucher) -> str

Set: LandingPort(self: Voucher) = value
"""

    Ledgers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ledgers(self: Voucher) -> List[VoucherLedger]

Set: Ledgers(self: Voucher) = value
"""

    Narration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Narration(self: Voucher) -> str

Set: Narration(self: Voucher) = value
"""

    OrderReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderReference(self: Voucher) -> str

Set: OrderReference(self: Voucher) = value
"""

    OverrideEWayBillApplicability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideEWayBillApplicability(self: Voucher) -> YesNo

Set: OverrideEWayBillApplicability(self: Voucher) = value
"""

    PartyGSTIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartyGSTIN(self: Voucher) -> str

Set: PartyGSTIN(self: Voucher) = value
"""

    PartyLedgerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartyLedgerName(self: Voucher) -> str

Set: PartyLedgerName(self: Voucher) = value
"""

    PartyMailingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartyMailingName(self: Voucher) -> str

Set: PartyMailingName(self: Voucher) = value
"""

    PartyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartyName(self: Voucher) -> str

Set: PartyName(self: Voucher) = value
"""

    PINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PINCode(self: Voucher) -> str

Set: PINCode(self: Voucher) = value
"""

    PlaceOfReceipt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaceOfReceipt(self: Voucher) -> str

Set: PlaceOfReceipt(self: Voucher) = value
"""

    PlaceOfSupply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaceOfSupply(self: Voucher) -> str

Set: PlaceOfSupply(self: Voucher) = value
"""

    PortCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PortCode(self: Voucher) -> str

Set: PortCode(self: Voucher) = value
"""

    PriceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PriceLevel(self: Voucher) -> str

Set: PriceLevel(self: Voucher) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: Voucher) -> str

Set: Reference(self: Voucher) = value
"""

    ReferenceDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceDate(self: Voucher) -> str

Set: ReferenceDate(self: Voucher) = value
"""

    RegistrationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegistrationType(self: Voucher) -> str

Set: RegistrationType(self: Voucher) = value
"""

    ShipOrFlightNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShipOrFlightNo(self: Voucher) -> str

Set: ShipOrFlightNo(self: Voucher) = value
"""

    ShippingBillDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShippingBillDate(self: Voucher) -> str

Set: ShippingBillDate(self: Voucher) = value
"""

    ShippingBillNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShippingBillNo(self: Voucher) -> str

Set: ShippingBillNo(self: Voucher) = value
"""

    ShippingDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShippingDate(self: Voucher) -> str

Set: ShippingDate(self: Voucher) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: Voucher) -> str

Set: State(self: Voucher) = value
"""

    TallyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TallyId(self: Voucher) -> Nullable[int]

Set: TallyId(self: Voucher) = value
"""

    VchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VchType(self: Voucher) -> str

Set: VchType(self: Voucher) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: Voucher) -> VoucherViewType

Set: View(self: Voucher) = value
"""

    VoucherNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VoucherNumber(self: Voucher) -> str

Set: VoucherNumber(self: Voucher) = value
"""

    VoucherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VoucherType(self: Voucher) -> str

Set: VoucherType(self: Voucher) = value
"""



class VoucherEnvelope(TallyXmlJson):
    """ VoucherEnvelope() """
    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: VoucherEnvelope) -> VBody

Set: Body(self: VoucherEnvelope) = value
"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: VoucherEnvelope) -> Header

Set: Header(self: VoucherEnvelope) = value
"""



class VoucherLookupField(Enum, IComparable, IFormattable, IConvertible):
    """ enum VoucherLookupField, values: AlterId (2), GUID (4), MasterId (1), VoucherNumber (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlterId = None
    GUID = None
    MasterId = None
    value__ = None
    VoucherNumber = None


class VoucherMessage(object):
    """ VoucherMessage() """
    Voucher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Voucher(self: VoucherMessage) -> Voucher

Set: Voucher(self: VoucherMessage) = value
"""



class VoucherViewType(Enum, IComparable, IFormattable, IConvertible):
    """ enum VoucherViewType, values: AccountingVoucherView (1), ConsumptionVoucherView (5), InvoiceVoucherView (2), MultiConsumptionVoucherView (4), None (0), PaySlipVoucherView (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AccountingVoucherView = None
    ConsumptionVoucherView = None
    InvoiceVoucherView = None
    MultiConsumptionVoucherView = None
    None = None
    PaySlipVoucherView = None
    value__ = None


class YesNo(Enum, IComparable, IFormattable, IConvertible):
    """ enum YesNo, values: No (2), None (0), Yes (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    No = None
    None = None
    value__ = None
    Yes = None


# variables with complex values

