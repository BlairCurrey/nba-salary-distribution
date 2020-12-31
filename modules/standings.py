from nba_api.stats.endpoints import leaguestandings
from time import sleep
import os
import json
from modules.helpers import Helpers
from modules.winpercentages import WinPercentages

class Standings:
    def __init__(self, nbaSalaryData):
        self.nbaSalaryData = nbaSalaryData #not sure if ill use this
        self.seasons = [Helpers.toShortYear(k) for k in nbaSalaryData.keys()]
        self.data = {"resourceSets": []}
        self.path = "data/raw"
        self.file = "standings.json"
        self.__init()
        self.winPercentages = WinPercentages(self.data, self.nbaSalaryData)
        self.winPercentages.save()
    
    def __init(self):
        """Requests and saves data if empty"""
        self.load()
        if self.isEmpty():
            print("Standing data not found locally. Requesting.")
            self.request()
            self.save()
        else:
            print("Local standings data found")
        
    def isEmpty(self):
        return len(self.data["resourceSets"]) == 0
    
    def request(self):
        print(f'Requesting data starting in {self.seasons[0]} and ending in {self.seasons[-1]}')
        for s in self.seasons:
            print(f'Requesting data for {s}')
            standing = json.loads(leaguestandings.LeagueStandings(season=s).get_json())
            self.data["resourceSets"].append(standing)
            sleep(0.6)
    
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
    
    def load(self):
        if os.path.isfile(f'{self.path}/{self.file}'):
            with open(f'{self.path}/{self.file}', 'r') as fp:
                self.data = json.load(fp)