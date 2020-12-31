class Normalize:
    cityChange = {
        "New Jersey": "Brooklyn",
        "Vancouver": "Memphis",
        "New Orleans/Oklahoma City": "New Orleans",
        "Seattle": "Oklahoma City",
        "LA": "Los Angeles"
    }
    
    @staticmethod
    def city(originalCity, teamName=None):
        c = originalCity
        if c in Normalize.cityChange:
            c = Normalize.cityChange[originalCity]
        if c == "Los Angeles":
            c = Normalize.whichLA(teamName)
        return c
            
    @staticmethod
    def whichLA(teamName):
        if teamName == "Lakers":
            return "LA Lakers"
        elif teamName == "Clippers":
            return "LA Clippers"
        else:
            raise Exception('teamName did not match expected values')
    
    @staticmethod
    def validateTeams(winPercentagesData, nbaSalaryData):
        teams = set()

        for year in list(winPercentagesData.keys()):
            list1 = list(nbaSalaryData[year].keys())
            list2 = list(winPercentagesData[year].keys())
            diff = list(set(list1) - set(list2))
            for d in diff:
                teams.add(d)

        if len(teams)>0:
            print(f"{len(teams)} team(s) in requested data but not in nbaSalaryData:")
            print(teams)
        else:
            print("No teams in requested data that don't exist in nbaSalaryData")

if __name__ == "__main__":
    print(Normalize.cityChange)