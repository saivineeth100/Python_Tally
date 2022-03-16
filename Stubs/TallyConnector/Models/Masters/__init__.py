# encoding: utf-8
# module TallyConnector.Models.Masters calls itself Masters
# from TallyConnector, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ClosingBalances(object):
    """ ClosingBalances() """
    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Amount(self: ClosingBalances) -> str

Set: Amount(self: ClosingBalances) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: ClosingBalances) -> str

Set: Date(self: ClosingBalances) = value
"""



class Currency(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ Currency() """
    def PrepareForExport(self):
        """ PrepareForExport(self: Currency) """
        pass

    def ToString(self):
        """ ToString(self: Currency) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: Currency) -> str

Set: Action(self: Currency) = value
"""

    DecimalPlaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimalPlaces(self: Currency) -> int

Set: DecimalPlaces(self: Currency) = value
"""

    DecimalPlaces_Print = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimalPlaces_Print(self: Currency) -> int

Set: DecimalPlaces_Print(self: Currency) = value
"""

    DecimalSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimalSymbol(self: Currency) -> str

Set: DecimalSymbol(self: Currency) = value
"""

    ExpandedSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpandedSymbol(self: Currency) -> str

Set: ExpandedSymbol(self: Currency) = value
"""

    HasSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSpace(self: Currency) -> str

Set: HasSpace(self: Currency) = value
"""

    InMilllions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InMilllions(self: Currency) -> str

Set: InMilllions(self: Currency) = value
"""

    IsSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSuffix(self: Currency) -> str

Set: IsSuffix(self: Currency) = value
"""

    MailingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailingName(self: Currency) -> str

Set: MailingName(self: Currency) = value
"""

    OriginalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalName(self: Currency) -> str

Set: OriginalName(self: Currency) = value
"""



class Group(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ Group() """
    def CreateNamesList(self):
        """ CreateNamesList(self: Group) """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: Group, attrOverrides: XmlAttributeOverrides) -> str """
        pass

    def PrepareForExport(self):
        """ PrepareForExport(self: Group) """
        pass

    def ToString(self):
        """ ToString(self: Group) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: Group) -> Action

Set: Action(self: Group) = value
"""

    AddLAllocType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddLAllocType(self: Group) -> AdAllocType

Set: AddLAllocType(self: Group) = value
"""

    AffectGrossProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AffectGrossProfit(self: Group) -> YesNo

Set: AffectGrossProfit(self: Group) = value
"""

    Alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alias(self: Group) -> str

Set: Alias(self: Group) = value
"""

    CanDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanDelete(self: Group) -> YesNo

Set: CanDelete(self: Group) = value
"""

    IsAddable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAddable(self: Group) -> YesNo

Set: IsAddable(self: Group) = value
"""

    IsCalculable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCalculable(self: Group) -> YesNo

Set: IsCalculable(self: Group) = value
"""

    IsRevenue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRevenue(self: Group) -> YesNo

Set: IsRevenue(self: Group) = value
"""

    IsSubledger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSubledger(self: Group) -> YesNo

Set: IsSubledger(self: Group) = value
"""

    LanguageNameList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageNameList(self: Group) -> List[LanguageNameList]

Set: LanguageNameList(self: Group) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Group) -> str

Set: Name(self: Group) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: Group) -> str

Set: OldName(self: Group) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: Group) -> str

Set: Parent(self: Group) = value
"""



class InterestList(object):
    """ InterestList() """
    FromDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromDate(self: InterestList) -> str

Set: FromDate(self: InterestList) = value
"""

    Interestappliedfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interestappliedfrom(self: InterestList) -> Nullable[float]

Set: Interestappliedfrom(self: InterestList) = value
"""

    Interestappliedon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interestappliedon(self: InterestList) -> InterestAppliedOn

Set: Interestappliedon(self: InterestList) = value
"""

    InterestBalancetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestBalancetype(self: InterestList) -> InterestBalanceType

Set: InterestBalancetype(self: InterestList) = value
"""

    Interestfromtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interestfromtype(self: InterestList) -> InterestFromType

Set: Interestfromtype(self: InterestList) = value
"""

    InterestRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestRate(self: InterestList) -> Nullable[float]

Set: InterestRate(self: InterestList) = value
"""

    InterestStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestStyle(self: InterestList) -> InterestStyle

Set: InterestStyle(self: InterestList) = value
"""

    RoundLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundLimit(self: InterestList) -> Nullable[float]

Set: RoundLimit(self: InterestList) = value
"""

    RoundType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundType(self: InterestList) -> RoundType

Set: RoundType(self: InterestList) = value
"""

    ToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToDate(self: InterestList) -> str

Set: ToDate(self: InterestList) = value
"""



class Ledger(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ Ledger() """
    def CreateNamesList(self):
        """ CreateNamesList(self: Ledger) """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: Ledger, attrOverrides: XmlAttributeOverrides) -> str """
        pass

    def PrepareForExport(self):
        """ PrepareForExport(self: Ledger) """
        pass

    def ToString(self):
        """ ToString(self: Ledger) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: Ledger) -> Action

Set: Action(self: Ledger) = value
"""

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: Ledger) -> str

Set: Address(self: Ledger) = value
"""

    AffectStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AffectStock(self: Ledger) -> YesNo

Set: AffectStock(self: Ledger) = value
"""

    Alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alias(self: Ledger) -> str

Set: Alias(self: Ledger) = value
"""

    CanDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanDelete(self: Ledger) -> YesNo

Set: CanDelete(self: Ledger) = value
"""

    CleanedClosingBal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CleanedClosingBal(self: Ledger) -> Nullable[float]

Set: CleanedClosingBal(self: Ledger) = value
"""

    CleanedOpeningBal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CleanedOpeningBal(self: Ledger) -> Nullable[float]

Set: CleanedOpeningBal(self: Ledger) = value
"""

    ClosingBal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosingBal(self: Ledger) -> str

Set: ClosingBal(self: Ledger) = value
"""

    ClosingBalances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosingBalances(self: Ledger) -> List[ClosingBalances]

Set: ClosingBalances(self: Ledger) = value
"""

    ClosingForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosingForexAmount(self: Ledger) -> str

Set: ClosingForexAmount(self: Ledger) = value
"""

    ClosingRateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosingRateofExchange(self: Ledger) -> str

Set: ClosingRateofExchange(self: Ledger) = value
"""

    ContactPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContactPerson(self: Ledger) -> str

Set: ContactPerson(self: Ledger) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Country(self: Ledger) -> str

Set: Country(self: Ledger) = value
"""

    CreditLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreditLimit(self: Ledger) -> str

Set: CreditLimit(self: Ledger) = value
"""

    CreditPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreditPeriod(self: Ledger) -> str

Set: CreditPeriod(self: Ledger) = value
"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Currency(self: Ledger) -> str

Set: Currency(self: Ledger) = value
"""

    DeemedExport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeemedExport(self: Ledger) -> YesNo

Set: DeemedExport(self: Ledger) = value
"""

    DeemedPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeemedPositive(self: Ledger) -> YesNo

Set: DeemedPositive(self: Ledger) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Ledger) -> str

Set: Description(self: Ledger) = value
"""

    Email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Email(self: Ledger) -> str

Set: Email(self: Ledger) = value
"""

    Emailcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Emailcc(self: Ledger) -> str

Set: Emailcc(self: Ledger) = value
"""

    FAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FAddress(self: Ledger) -> HAddress

Set: FAddress(self: Ledger) = value
"""

    FaxNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaxNo(self: Ledger) -> str

Set: FaxNo(self: Ledger) = value
"""

    ForexAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForexAmount(self: Ledger) -> str

Set: ForexAmount(self: Ledger) = value
"""

    Forpayroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Forpayroll(self: Ledger) -> YesNo

Set: Forpayroll(self: Ledger) = value
"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: Ledger) -> str

Set: Group(self: Ledger) = value
"""

    GSTIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTIN(self: Ledger) -> str

Set: GSTIN(self: Ledger) = value
"""

    GSTPartyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTPartyType(self: Ledger) -> GSTPartyType

Set: GSTPartyType(self: Ledger) = value
"""

    GSTRegistrationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTRegistrationType(self: Ledger) -> GSTRegistrationType

Set: GSTRegistrationType(self: Ledger) = value
"""

    GSTTaxType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GSTTaxType(self: Ledger) -> GSTTaxType

Set: GSTTaxType(self: Ledger) = value
"""

    InterestIncludeForAmountsAdded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestIncludeForAmountsAdded(self: Ledger) -> YesNo

Set: InterestIncludeForAmountsAdded(self: Ledger) = value
"""

    InterestIncludeForAmountsDeducted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestIncludeForAmountsDeducted(self: Ledger) -> YesNo

Set: InterestIncludeForAmountsDeducted(self: Ledger) = value
"""

    InterestList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterestList(self: Ledger) -> List[InterestList]

Set: InterestList(self: Ledger) = value
"""

    IsBillwise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBillwise(self: Ledger) -> YesNo

Set: IsBillwise(self: Ledger) = value
"""

    IsCostcenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCostcenter(self: Ledger) -> YesNo

Set: IsCostcenter(self: Ledger) = value
"""

    IsCreditCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCreditCheck(self: Ledger) -> YesNo

Set: IsCreditCheck(self: Ledger) = value
"""

    IsECommerceOperator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsECommerceOperator(self: Ledger) -> YesNo

Set: IsECommerceOperator(self: Ledger) = value
"""

    Isintereston = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Isintereston(self: Ledger) -> YesNo

Set: Isintereston(self: Ledger) = value
"""

    IsinterestonBillWise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsinterestonBillWise(self: Ledger) -> YesNo

Set: IsinterestonBillWise(self: Ledger) = value
"""

    IsOtherTerritoryAssessee = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOtherTerritoryAssessee(self: Ledger) -> YesNo

Set: IsOtherTerritoryAssessee(self: Ledger) = value
"""

    Isrevenue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Isrevenue(self: Ledger) -> YesNo

Set: Isrevenue(self: Ledger) = value
"""

    IsTransporter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTransporter(self: Ledger) -> YesNo

Set: IsTransporter(self: Ledger) = value
"""

    LandlineNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LandlineNo(self: Ledger) -> str

Set: LandlineNo(self: Ledger) = value
"""

    LanguageNameList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageNameList(self: Ledger) -> List[LanguageNameList]

Set: LanguageNameList(self: Ledger) = value
"""

    MailingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MailingName(self: Ledger) -> str

Set: MailingName(self: Ledger) = value
"""

    MobileNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MobileNo(self: Ledger) -> str

Set: MobileNo(self: Ledger) = value
"""

    MultipleAddresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultipleAddresses(self: Ledger) -> List[MultiAddress]

Set: MultipleAddresses(self: Ledger) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Ledger) -> str

Set: Name(self: Ledger) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: Ledger) -> str

Set: Notes(self: Ledger) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: Ledger) -> str

Set: OldName(self: Ledger) = value
"""

    OpeningBal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpeningBal(self: Ledger) -> str

Set: OpeningBal(self: Ledger) = value
"""

    OverrideAdvanceInterest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideAdvanceInterest(self: Ledger) -> YesNo

Set: OverrideAdvanceInterest(self: Ledger) = value
"""

    OverrideInterest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideInterest(self: Ledger) -> YesNo

Set: OverrideInterest(self: Ledger) = value
"""

    PANNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PANNumber(self: Ledger) -> str

Set: PANNumber(self: Ledger) = value
"""

    PinCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PinCode(self: Ledger) -> str

Set: PinCode(self: Ledger) = value
"""

    RateofExchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofExchange(self: Ledger) -> str

Set: RateofExchange(self: Ledger) = value
"""

    RateofTax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RateofTax(self: Ledger) -> Nullable[float]

Set: RateofTax(self: Ledger) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: Ledger) -> str

Set: State(self: Ledger) = value
"""

    TaxType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaxType(self: Ledger) -> TaxType

Set: TaxType(self: Ledger) = value
"""

    TransporterID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransporterID(self: Ledger) -> str

Set: TransporterID(self: Ledger) = value
"""

    Website = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Website(self: Ledger) -> str

Set: Website(self: Ledger) = value
"""



class VoucherType(BasicTallyObject, ITallyObject, IBasicTallyObject):
    """ VoucherType() """
    def CreateNamesList(self):
        """ CreateNamesList(self: VoucherType) """
        pass

    def GetXML(self, attrOverrides):
        """ GetXML(self: VoucherType, attrOverrides: XmlAttributeOverrides) -> str """
        pass

    def PrepareForExport(self):
        """ PrepareForExport(self: VoucherType) """
        pass

    def ToString(self):
        """ ToString(self: VoucherType) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: VoucherType) -> str

Set: Action(self: VoucherType) = value
"""

    Alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alias(self: VoucherType) -> str

Set: Alias(self: VoucherType) = value
"""

    AsMfgJrnl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsMfgJrnl(self: VoucherType) -> str

Set: AsMfgJrnl(self: VoucherType) = value
"""

    CanDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanDelete(self: VoucherType) -> str

Set: CanDelete(self: VoucherType) = value
"""

    CommonNarration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommonNarration(self: VoucherType) -> str

Set: CommonNarration(self: VoucherType) = value
"""

    EffectStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectStock(self: VoucherType) -> str

Set: EffectStock(self: VoucherType) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: VoucherType) -> str

Set: IsActive(self: VoucherType) = value
"""

    IsDefaultAllocationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultAllocationEnabled(self: VoucherType) -> str

Set: IsDefaultAllocationEnabled(self: VoucherType) = value
"""

    IsforJobworkIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsforJobworkIn(self: VoucherType) -> str

Set: IsforJobworkIn(self: VoucherType) = value
"""

    IsOptional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOptional(self: VoucherType) -> str

Set: IsOptional(self: VoucherType) = value
"""

    LanguageNameList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageNameList(self: VoucherType) -> List[LanguageNameList]

Set: LanguageNameList(self: VoucherType) = value
"""

    MultiNarration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiNarration(self: VoucherType) -> str

Set: MultiNarration(self: VoucherType) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: VoucherType) -> str

Set: Name(self: VoucherType) = value
"""

    NumberingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingMethod(self: VoucherType) -> str

Set: NumberingMethod(self: VoucherType) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: VoucherType) -> str

Set: OldName(self: VoucherType) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: VoucherType) -> str

Set: Parent(self: VoucherType) = value
"""

    PrintAfterSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintAfterSave(self: VoucherType) -> str

Set: PrintAfterSave(self: VoucherType) = value
"""

    UseforJobwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseforJobwork(self: VoucherType) -> str

Set: UseforJobwork(self: VoucherType) = value
"""

    UseforPOSInvoice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseforPOSInvoice(self: VoucherType) -> str

Set: UseforPOSInvoice(self: VoucherType) = value
"""

    UseZeroEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseZeroEntries(self: VoucherType) -> str

Set: UseZeroEntries(self: VoucherType) = value
"""

    VchPrintBankName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VchPrintBankName(self: VoucherType) -> str

Set: VchPrintBankName(self: VoucherType) = value
"""

    VchPrintJurisdiction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VchPrintJurisdiction(self: VoucherType) -> str

Set: VchPrintJurisdiction(self: VoucherType) = value
"""

    VchPrintTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VchPrintTitle(self: VoucherType) -> str

Set: VchPrintTitle(self: VoucherType) = value
"""



# variables with complex values

