# encoding: utf-8
# module TallyConnector.Models.Masters.Payroll calls itself Payroll
# from TallyConnector, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AttendanceType(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ AttendanceType() """
    def CreateNamesList(self):
        """ CreateNamesList(self: AttendanceType) """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: AttendanceType, attrOverrides: XmlAttributeOverrides) -> str """
        pass

    def PrepareForExport(self):
        """ PrepareForExport(self: AttendanceType) """
        pass

    def ToString(self):
        """ ToString(self: AttendanceType) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: AttendanceType) -> str

Set: Action(self: AttendanceType) = value
"""

    Alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alias(self: AttendanceType) -> str

Set: Alias(self: AttendanceType) = value
"""

    BaseUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseUnit(self: AttendanceType) -> str

Set: BaseUnit(self: AttendanceType) = value
"""

    CanDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanDelete(self: AttendanceType) -> str

Set: CanDelete(self: AttendanceType) = value
"""

    LanguageNameList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageNameList(self: AttendanceType) -> List[LanguageNameList]

Set: LanguageNameList(self: AttendanceType) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AttendanceType) -> str

Set: Name(self: AttendanceType) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: AttendanceType) -> str

Set: OldName(self: AttendanceType) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AttendanceType) -> str

Set: Parent(self: AttendanceType) = value
"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Period(self: AttendanceType) -> str

Set: Period(self: AttendanceType) = value
"""

    ProductionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProductionType(self: AttendanceType) -> str

Set: ProductionType(self: AttendanceType) = value
"""



class Employee(CostCenter, ITallyObject, IBasicTallyObject):
    """ Employee() """
    def CleanForExport(self):
        """ CleanForExport(self: Employee) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AadhaarNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AadhaarNumber(self: Employee) -> str

Set: AadhaarNumber(self: Employee) = value
"""

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: Employee) -> str

Set: Address(self: Employee) = value
"""

    BankAccountNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BankAccountNo(self: Employee) -> str

Set: BankAccountNo(self: Employee) = value
"""

    BankBranch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BankBranch(self: Employee) -> str

Set: BankBranch(self: Employee) = value
"""

    BankName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BankName(self: Employee) -> str

Set: BankName(self: Employee) = value
"""

    BloodGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BloodGroup(self: Employee) -> str

Set: BloodGroup(self: Employee) = value
"""

    Contract_ExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contract_ExpiryDate(self: Employee) -> str

Set: Contract_ExpiryDate(self: Employee) = value
"""

    Contract_StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contract_StartDate(self: Employee) -> str

Set: Contract_StartDate(self: Employee) = value
"""

    CountryofIssue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryofIssue(self: Employee) -> str

Set: CountryofIssue(self: Employee) = value
"""

    DateOfBirth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOfBirth(self: Employee) -> str

Set: DateOfBirth(self: Employee) = value
"""

    Designation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Designation(self: Employee) -> str

Set: Designation(self: Employee) = value
"""

    EPSAccountNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EPSAccountNumber(self: Employee) -> str

Set: EPSAccountNumber(self: Employee) = value
"""

    ESIDispensaryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ESIDispensaryName(self: Employee) -> str

Set: ESIDispensaryName(self: Employee) = value
"""

    ESINumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ESINumber(self: Employee) -> str

Set: ESINumber(self: Employee) = value
"""

    FAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FAddress(self: Employee) -> HAddress

Set: FAddress(self: Employee) = value
"""

    FatherName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FatherName(self: Employee) -> str

Set: FatherName(self: Employee) = value
"""

    ForPayroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForPayroll(self: Employee) -> str

Set: ForPayroll(self: Employee) = value
"""

    Function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Function(self: Employee) -> str

Set: Function(self: Employee) = value
"""

    Gender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gender(self: Employee) -> str

Set: Gender(self: Employee) = value
"""

    IFSC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFSC(self: Employee) -> str

Set: IFSC(self: Employee) = value
"""

    IsEmployeeGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmployeeGroup(self: Employee) -> str

Set: IsEmployeeGroup(self: Employee) = value
"""

    JoiningDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JoiningDate(self: Employee) -> str

Set: JoiningDate(self: Employee) = value
"""

    JoiningDate_PF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JoiningDate_PF(self: Employee) -> str

Set: JoiningDate_PF(self: Employee) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Employee) -> str

Set: Location(self: Employee) = value
"""

    Narration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Narration(self: Employee) -> str

Set: Narration(self: Employee) = value
"""

    PANNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PANNumber(self: Employee) -> str

Set: PANNumber(self: Employee) = value
"""

    PassportExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassportExpiryDate(self: Employee) -> str

Set: PassportExpiryDate(self: Employee) = value
"""

    PassportNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassportNumber(self: Employee) -> str

Set: PassportNumber(self: Employee) = value
"""

    PaymentDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaymentDetails(self: Employee) -> List[PaymentDetails]

Set: PaymentDetails(self: Employee) = value
"""

    PFAccountNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PFAccountNumber(self: Employee) -> str

Set: PFAccountNumber(self: Employee) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: Employee) -> str

Set: PhoneNumber(self: Employee) = value
"""

    PRAccountNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PRAccountNumber(self: Employee) -> str

Set: PRAccountNumber(self: Employee) = value
"""

    RelievingDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelievingDate(self: Employee) -> str

Set: RelievingDate(self: Employee) = value
"""

    RelievingDate_PF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelievingDate_PF(self: Employee) -> str

Set: RelievingDate_PF(self: Employee) = value
"""

    RelievingReason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelievingReason(self: Employee) -> str

Set: RelievingReason(self: Employee) = value
"""

    SpouseName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpouseName(self: Employee) -> str

Set: SpouseName(self: Employee) = value
"""

    TaxRegimeDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaxRegimeDetails(self: Employee) -> List[TaxRegimeDetails]

Set: TaxRegimeDetails(self: Employee) = value
"""

    UAN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UAN(self: Employee) -> str

Set: UAN(self: Employee) = value
"""

    VisaExpiryDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisaExpiryDate(self: Employee) -> str

Set: VisaExpiryDate(self: Employee) = value
"""

    VisaNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisaNumber(self: Employee) -> str

Set: VisaNumber(self: Employee) = value
"""

    WorkPermitNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorkPermitNumber(self: Employee) -> str

Set: WorkPermitNumber(self: Employee) = value
"""



class EmployeeGroup(CostCenter, ITallyObject, IBasicTallyObject):
    """ EmployeeGroup() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ForPayroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForPayroll(self: EmployeeGroup) -> str

Set: ForPayroll(self: EmployeeGroup) = value
"""

    IsEmployeeGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmployeeGroup(self: EmployeeGroup) -> str

Set: IsEmployeeGroup(self: EmployeeGroup) = value
"""



class TaxRegimeDetails(object):
    """ TaxRegimeDetails() """
    ApplicableFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicableFrom(self: TaxRegimeDetails) -> str

Set: ApplicableFrom(self: TaxRegimeDetails) = value
"""

    TaxRegime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaxRegime(self: TaxRegimeDetails) -> str

Set: TaxRegime(self: TaxRegimeDetails) = value
"""



