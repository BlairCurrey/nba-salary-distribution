class Helpers:
    
    @staticmethod
    def toShortYear(season):
        '''converts from format like 2019-2020 to format like 2019-20'''
        return f'{season[:5]}{season[7:]}'
    
    @staticmethod
    def toLongYear(shortYear):
        '''converts from format like 2019/20 to format like 2019-2020'''
        longYear = shortYear.replace("/","-")

        firstTwo = shortYear[:2] #20 from 2019
        lastTwo = shortYear[2:4] #19 from 2019

        indexToInsert = longYear.find("-") + 1

        if lastTwo != '99':
            longYear = longYear[:indexToInsert] + firstTwo  + longYear[indexToInsert:]
        else:
            newFirstTwo = str(int(firstTwo) + 1)
            longYear = longYear[:indexToInsert] + newFirstTwo  + longYear[indexToInsert:]

        return longYear