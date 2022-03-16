# encoding: utf-8
# module TallyConnector
# from TallyConnector, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CLogger(object):
    """ CLogger(logger: ILogger) """
    def SetupLog(self, *__args):
        """ SetupLog(self: CLogger, company: str, fromDate: str, toDate: str)SetupLog(self: CLogger, baseURL: str, port: int, company: str, fromDate: str, toDate: str) """
        pass

    def TallyCheck(self, fullURL):
        """ TallyCheck(self: CLogger, fullURL: str) """
        pass

    def TallyError(self, fullURL, message):
        """ TallyError(self: CLogger, fullURL: str, message: str) """
        pass

    def TallyNotRunning(self, fullURL):
        """ TallyNotRunning(self: CLogger, fullURL: str) """
        pass

    def TallyRunning(self, fullURL):
        """ TallyRunning(self: CLogger, fullURL: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger):
        """ __new__(cls: type, logger: ILogger) """
        pass


class Tally(object, IDisposable):
    """
    Tally(baseURL: str, port: int, Logger: ILogger[Tally], Timeoutseconds: int)
    Tally(Logger: ILogger[Tally], Timeoutseconds: int)
    """
    @staticmethod
    def Basetoderieved(Derieved, Base):
        """ Basetoderieved(Derieved: object, Base: object) """
        pass

    def ChangeCompany(self, company, fromDate, toDate):
        """ ChangeCompany(self: Tally, company: str, fromDate: str, toDate: str) """
        pass

    def Check(self):
        """ Check(self: Tally) -> Task[bool] """
        pass

    def Dispose(self):
        """ Dispose(self: Tally) """
        pass

    def FetchAllTallyData(self):
        """ FetchAllTallyData(self: Tally) -> Task """
        pass

    def GetActiveTallyCompany(self):
        """ GetActiveTallyCompany(self: Tally) -> Task[str] """
        pass

    def GetAttendanceType(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetAttendanceType[AttendnceType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[AttendanceType] """
        pass

    def GetCompaniesList(self):
        """ GetCompaniesList(self: Tally) -> Task[List[Company]] """
        pass

    def GetCompaniesListinPath(self):
        """ GetCompaniesListinPath(self: Tally) -> Task[List[CompanyOnDisk]] """
        pass

    def GetCostCategory(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetCostCategory[CostCategoryType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[CostCategory] """
        pass

    def GetCostCenter(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetCostCenter[CostCenterType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[CostCenter] """
        pass

    def GetCurrency(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetCurrency[CurrencyType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[Currency] """
        pass

    def GetEmployee(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetEmployee[EmployeeType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[Employee] """
        pass

    def GetEmployeeGroup(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetEmployeeGroup[EmployeeGroupType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[EmployeeGroup] """
        pass

    def GetGodown(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetGodown[GodownType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[Godown] """
        pass

    def GetGroup(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetGroup[GroupType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[GroupType] """
        pass

    def GetLedger(self, LookupValue, LookupField, company, fetchList):
        """ GetLedger[LedgerType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fetchList: List[str]) -> Task[LedgerType] """
        pass

    def GetLedgerDynamic(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetLedgerDynamic[LedgerType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[LedgerType] """
        pass

    def GetLicenseInfo(self):
        """ GetLicenseInfo(self: Tally) -> Task[LicenseInfo] """
        pass

    def GetMasters(self, masterType):
        """ GetMasters(self: Tally, masterType: TallyObjectType) -> List[BasicTallyObject] """
        pass

    def GetNativeCollectionXML(self, Sv, ColType, childof, NativeFields, filters, isInitialize, TallyType, xmlAttributeOverrides):
        """ GetNativeCollectionXML[ReturnObject](self: Tally, Sv: StaticVariables, ColType: str, childof: str, NativeFields: List[str], filters: List[Filter], isInitialize: YesNo, TallyType: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[List[ReturnObject]] """
        pass

    def GetObjectfromTally(self, LookupValue, LookupField, *__args):
        """
        GetObjectfromTally[ReturnType](self: Tally, LookupValue: str, LookupField: VoucherLookupField, Isinventory: bool, company: str, fromDate: str, toDate: str, fetchList: List[str], xmlAttributeOverrides: XmlAttributeOverrides) -> Task[ReturnType]
        GetObjectfromTally[ReturnType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str], xmlAttributeOverrides: XmlAttributeOverrides) -> Task[ReturnType]
        """
        pass

    def GetObjectfromTallyBasedonClass(self):
        """ GetObjectfromTallyBasedonClass(self: Tally) """
        pass

    def GetObjectsfromTally(self, company, ColType, childof, fetchList, filters, isInitialize, xmlAttributeOverrides):
        """ GetObjectsfromTally[ReturnObjectType](self: Tally, company: str, ColType: str, childof: str, fetchList: List[str], filters: List[Filter], isInitialize: YesNo, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[List[ReturnObjectType]] """
        pass

    def GetObjFromTally(self, ObjName, ObjType, company, fromDate, toDate, fetchList, viewname):
        """ GetObjFromTally[T](self: Tally, ObjName: str, ObjType: str, company: str, fromDate: str, toDate: str, fetchList: List[str], viewname: VoucherViewType) -> Task[T] """
        pass

    def GetObjfromXml(self, Xml, attrOverrides):
        """ GetObjfromXml[T](self: Tally, Xml: str, attrOverrides: XmlAttributeOverrides) -> T """
        pass

    def GetPropertyInfo(self, type):
        """ GetPropertyInfo(self: Tally, type: Type) -> Array[PropertyInfo] """
        pass

    def GetReportXML(self, reportname, Sv):
        """ GetReportXML(self: Tally, reportname: str, Sv: StaticVariables) -> Task[str] """
        pass

    def GetStockCategory(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetStockCategory[StockCategoryType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[StockCategory] """
        pass

    def GetStockGroup(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetStockGroup[StockGroupType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[StockGroup] """
        pass

    def GetStockItem(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetStockItem[StockItemType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[StockItem] """
        pass

    def GetUnit(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetUnit[UnitType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[Unit] """
        pass

    def GetVoucher(self, LookupValue, LookupField, company, fetchList, viewName):
        """ GetVoucher[VchType](self: Tally, LookupValue: str, LookupField: VoucherLookupField, company: str, fetchList: List[str], viewName: VoucherViewType) -> Task[Voucher] """
        pass

    def GetVoucherByVoucherNumber(self, VoucherNumber, Date, company, fetchList):
        """ GetVoucherByVoucherNumber(self: Tally, VoucherNumber: str, Date: str, company: str, fetchList: List[str]) -> Task[Voucher] """
        pass

    def GetVoucherType(self, LookupValue, LookupField, company, fromDate, toDate, fetchList):
        """ GetVoucherType[VchrType](self: Tally, LookupValue: str, LookupField: MasterLookupField, company: str, fromDate: str, toDate: str, fetchList: List[str]) -> Task[VoucherType] """
        pass

    def ParseResponse(self, RespXml):
        """ ParseResponse(self: Tally, RespXml: str) -> PResult """
        pass

    def PostAttendanceType(self, AttendanceType, company, xmlAttributeOverrides):
        """ PostAttendanceType[AttendanceTypType](self: Tally, AttendanceType: AttendanceType, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostCostCategory(self, CostCategory, company, xmlAttributeOverrides):
        """ PostCostCategory[CostCategoryType](self: Tally, CostCategory: CostCategory, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostCostCenter(self, costCenter, company, xmlAttributeOverrides):
        """ PostCostCenter[CostCenterType](self: Tally, costCenter: CostCenter, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostCurrency(self, currency, company, xmlAttributeOverrides):
        """ PostCurrency[CurrencyType](self: Tally, currency: Currency, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostEmployee(self, Employee, company, xmlAttributeOverrides):
        """ PostEmployee[EmployeeType](self: Tally, Employee: Employee, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostEmployeeGroup(self, EmployeeGroup, company, xmlAttributeOverrides):
        """ PostEmployeeGroup[EmployeeGroupType](self: Tally, EmployeeGroup: EmployeeGroup, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostGodown(self, godown, company, xmlAttributeOverrides):
        """ PostGodown[GodownType](self: Tally, godown: Godown, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostGroup(self, group, company, xmlAttributeOverrides):
        """ PostGroup[GroupType](self: Tally, group: GroupType, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostLedger(self, ledger, company, xmlAttributeOverrides):
        """ PostLedger[LedgerType](self: Tally, ledger: LedgerType, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostObjectToTally(self, Object, company, xmlAttributeOverrides):
        """ PostObjectToTally[ObjectType](self: Tally, Object: ObjectType, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostStockCategory(self, stockCategory, company, xmlAttributeOverrides):
        """ PostStockCategory[StockCategoryType](self: Tally, stockCategory: StockCategory, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostStockGroup(self, stockGroup, company, xmlAttributeOverrides):
        """ PostStockGroup[StockGroupType](self: Tally, stockGroup: StockGroup, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostStockItem(self, stockItem, company, xmlAttributeOverrides):
        """ PostStockItem[StockItemType](self: Tally, stockItem: StockItem, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostUnit(self, unit, company, xmlAttributeOverrides):
        """ PostUnit[UnitType](self: Tally, unit: Unit, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostVoucher(self, voucher, company, xmlAttributeOverrides):
        """ PostVoucher[TVoucher](self: Tally, voucher: Voucher, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    def PostVoucherType(self, voucherType, company, xmlAttributeOverrides):
        """ PostVoucherType[VoucherTypType](self: Tally, voucherType: VoucherType, company: str, xmlAttributeOverrides: XmlAttributeOverrides) -> Task[PResult] """
        pass

    @staticmethod
    def ReplaceXML(strText):
        """ ReplaceXML(strText: str) -> str """
        pass

    @staticmethod
    def ReplaceXMLText(strXmlText):
        """ ReplaceXMLText(strXmlText: str) -> str """
        pass

    def SendRequest(self, SXml):
        """ SendRequest(self: Tally, SXml: str) -> Task[str] """
        pass

    def Setup(self, baseURL, port, company, fromDate, toDate):
        """ Setup(self: Tally, baseURL: str, port: int, company: str, fromDate: str, toDate: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, baseURL: str, port: int, Logger: ILogger[Tally], Timeoutseconds: int)
        __new__(cls: type, Logger: ILogger[Tally], Timeoutseconds: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CompaniesList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompaniesList(self: Tally) -> List[Company]

"""

    Company = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Company(self: Tally) -> str

"""

    FromDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromDate(self: Tally) -> str

"""

    LicenseInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseInfo(self: Tally) -> LicenseInfo

"""

    Masters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Masters(self: Tally) -> List[MastersBasicInfo[BasicTallyObject]]

"""

    ReqStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReqStatus(self: Tally) -> str

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: Tally) -> str

"""

    ToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToDate(self: Tally) -> str

"""



# variables with complex values

