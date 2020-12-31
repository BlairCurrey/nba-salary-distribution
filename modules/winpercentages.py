import os
import json
import pandas as pd
from modules.normalize import Normalize
from modules.helpers import Helpers

class WinPercentages:
    def __init__(self, standingsData, nbaSalaryData):
        self.standingsData = standingsData
        self.nbaSalaryData = nbaSalaryData
        self.path = "data/raw"
        self.file = "winPercentages.json"
        self.data = {}
        self.parseStandingsData()
        
    def save(self):
        fileLoc = f'{self.path}/{self.file}'
        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            with open(fileLoc, 'w') as fp:
                json.dump(self.data, fp, indent=4)
        except:
            print("Win percentage save failed")
        else:
            print("Win percentages saved to f'{fileLoc}'")
    
    def parseStandingsData(self):
        iCity = self.standingsData["resourceSets"][0]["resultSets"][0]["headers"].index("TeamCity")
        iName = self.standingsData["resourceSets"][0]["resultSets"][0]["headers"].index("TeamName")
        iWinPct = self.standingsData["resourceSets"][0]["resultSets"][0]["headers"].index("WinPCT")

        for year in self.standingsData["resourceSets"]:
            y = Helpers.toLongYear(year["parameters"]["SeasonYear"])
            self.data[y] = {}
            for team in year["resultSets"][0]["rowSet"]:
                t = Normalize.city(team[iCity], team[iName])
                self.data[y][t] = team[iWinPct]        
    
    def dataFrame(self):
        if not bool(self.data): 
            raise Exception("No win percentage data found")
        return pd.read_json(json.dumps(self.data), orient="index")