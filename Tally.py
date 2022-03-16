from clr_loader import get_coreclr 
import pythonnet # to use dll in python
import sys # to add dll directory to path

path = r"./net6.0"
sys.path.append(path)

rt = get_coreclr("TallyConnector.json") #Json we created earlier
pythonnet.set_runtime(rt)
pythonnet.load()

import clr
clr.AddReference("TallyConnector") # Load Assembly


from TallyConnector import Tally
from TallyConnector.Models import Company,MastersMapping,BasicTallyObject
from System.Collections.Generic import List


tally = Tally()
IsTallyRunning = tally.Check().Result #Check Tally is running on given url and port
print(IsTallyRunning)

companyName = tally.GetActiveTallyCompany().Result
print(f'Active Company in Tally - {companyName}')

companies = tally.GetCompaniesList().Result
company:Company
if IsTallyRunning:
    for company in companies:
        print(f'Name - {company.Name:<20} Starting From - {company.StartingFrom} Country - { company.Country}')

        companyName = company.Name
        tally.ChangeCompany(companyName)
        tally.FetchAllTallyData().Wait() #this will save All basic master data in tally.Masters Variable

        #Groups = tally.GetMasters(TallyObjectType.Groups)
        mastertype:MastersMapping
        for mastertype in MastersMapping.MastersMappings:
            Masters:List[BasicTallyObject] = tally.GetMasters(mastertype.MasterType)
            #Masters contains list of basicTallyObject that has properties GUID,TallyId
            t = f'{mastertype.MasterType.ToString():<15} in Company'
            #Printing Number of masters by type
            print(f'Number of  {t:<25} - {companyName:<10} = {Masters.Count}')
