import requests
import json



"""
19.05.04 by HyunHo
description : https://developer.riotgames.com/api-methods/
Tournament-stub, Tournament -> cannot use

"""


class ChampionMasteryInfo:

    """
    description : https://developer.riotgames.com/api-methods/
    """

    def __init__(self, region, api_key):

        self.region = region
        self.api_key = api_key


    def getAllChampsInfo_byEncryptedSummonerId(self, encryptedId):
        """
        :param encryptedId: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        :return: Get all champion mastery entries sorted by number of champion points descending,
        """
        url = 'https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}' \
            .format(self.region, encryptedId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getChampInfo_byEncryptedSummonerId_and_championId(self, encryptedId, championId):
        """
        :param encryptedId: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        :param championId:
        :return: Get a champion mastery by player ID and champion ID.
        """

        url = 'https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}' \
              '/by-champion/{}?api_key={}'.format(self.region, encryptedId, championId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getChampScores_byEncryptedSummonerId(self, encryptedId):
        """
        :param encryptedId: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        :return: Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
        """
        url = 'https://{}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{}?api_key={}' \
            .format(self.region, encryptedId, self.api_key)

        response = requests.get(url)
        totalScore = json.loads(response.text)
        return totalScore


class ChampionRotation:

    """
    description : https://developer.riotgames.com/api-methods/
    """


    def __init__(self, region, api_key):

        self.region = region
        self.api_key = api_key

    def getRotationInfo(self):
        """
        :return: Get League of Legends status for the given shard.
        """
        url = 'https://{}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={}'

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict


class LeagueInfo:

    """
    description : https://developer.riotgames.com/api-methods/#league-v4/GET_getAllLeaguePositionsForSummoner
    """

    def __init__(self, region, api_key):

        self.region = region
        self.api_key = api_key

    def getChallegerInfo_byQueue(self, queue):
        """
        :param queue:
        :return: Get the challenger league for given queue.
        """

        url = 'https://{}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{}?api_key={}'\
            .format(self.region, queue, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getSummonerInfo_byEncryptedSummonerId(self, encryptedId):
        """
        :param encryptedId: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        :return: Get league entries in all queues for a given summoner ID.
        """

        url = 'https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}' \
            .format(self.region, encryptedId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getLeagueEntriesInfo(self, queue, tier, division):
        """
        :param queue:
        :param tier:
        :param division:
        :return: Get all the league entries.
        """
        url = 'https://{}.api.riotgames.com/lol/league/v4/entries/{}/{}/{}?api_key={}'\
            .format(self.region, queue, tier, division, self.api_key)
        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getGrandMasterInfo_byQueue(self, queue):
        """
        :param queue:
        :return: Get the grandmaster league for given queue.
        """

        url = 'https://{}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{}?api_key={}'\
            .format(self.region, queue, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getLeagueInfo_byLeagueId(self, leagueId):
        """
        :param leagueId:
        :return: Get league with given ID, including inactive entries.
        """
        url ='https://{}.api.riotgames.com/lol/league/v4/leagues/{}?api_key={}'\
            .format(self.region, leagueId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getMasterInfo_byQueue(self, queue):
        """
        :param queue:
        :return: Get the master league for given queue.
        """
        url = 'https://{}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{}?api_key={}'\
            .format(self.region, queue, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

class Status:
    """
    description : https://developer.riotgames.com/api-methods/#lol-status-v3/GET_getShardData
    """

    def __init__(self, region, api_key):
        self.region = region
        self.api_key = api_key

    def getStatusInfo(self):
        """
        :return: Get League of Legends status for the given shard.
        """

        url = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}' \
            .format(self.region, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict


class MatchInfo:

    """
    description : https://developer.riotgames.com/api-methods/#match-v4
    """

    def __init__(self, region, api_key):
        self.region = region
        self.api_key = api_key

    def getMatchIDs_byTournamentCode(self, tournamentCode):
        """
        :param tournamentCode: Get match IDs by tournament code.
        :return:
        """
        url = 'https://{}.api.riotgames.com/lol/match/v4/matches/by-tournament-code/{}/ids?api_key={}' \
            .format(self.region, tournamentCode, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getMatch_byMatchId(self, matchId):
        """
        :param matchId:
        :return: Get match by match ID.
        """
        url = 'https://{}.api.riotgames.com/lol/match/v4/matches/{}?api_key={}' \
            .format(self.region, matchId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getMatch_byMatchId_and_tournamentCode(self, matchId, tournamentCode):
        """
        :param matchId:
        :param tournamentCode:
        :return: Get match by match ID and tournament code.
        """
        url = 'https://{}.api.riotgames.com/lol/match/v4/matches/{}/by-tournament-code/{}/ids?api_key={}' \
            .format(self.region, matchId, tournamentCode, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getMatchlists_byEncryptedId(self, encryptedAccountId):
        """
        :param encryptedAccountId: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        :return: Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any.
        """

        url = 'https://{}.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?api_key={}' \
            .format(self.region, encryptedAccountId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getTimelines_byMatchId(self, matchId):
        """
        :param matchId:
        :return: Get match timeline by match ID.
        """
        url = 'https://{}.api.riotgames.com/lol/match/v4/timelines/by-match/{}?api_key={}' \
            .format(self.region, matchId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict


class SpectatorInfo:

    """
    description : https://developer.riotgames.com/api-methods/#spectator-v4
    """

    def __init__(self, region, api_key):
        self.region = region
        self.api_key = api_key

    def getActiveGamesInfo_byEncryptedSummonerId(self, encryptedId):
        """
        :param encryptedID: SummonerInfo 클래스의 getInfo_bySummonerName 메서드 통해 얻을 수 있음
        """
        url = 'https://{}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{}?api_key={}' \
            .format(self.region, encryptedId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getFeatured_gamesInfo(self):

        url = 'https://{}.api.riotgames.com/lol/spectator/v4/featured-games?api_key={}'\
            .format(self.region, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

class SummonerInfo:

    """
    description : https://developer.riotgames.com/api-methods/#summoner-v4
    """

    def __init__(self, region, api_key):

        self.region = region
        self.api_key = api_key

    def getInfo_byEncryptedAccountId(self, encryptedAccountId):
        """
        :param encryptedAccountId: getInfo_bySummonerName 함수의 결과에서 얻을 수 있음
        """
        url = 'https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{}?api_key={}'\
            .format(self.region, encryptedAccountId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getInfo_bySummonerName(self, summonerName):

        url = 'https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'\
            .format(self.region, summonerName, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict



    def getInfo_byPuuid(self, encryptedPUUID):
        url = 'https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{}?api_key={}' \
            .format(self.region, encryptedPUUID, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

    def getInfo_byEncryptedSummonerId(self, encryptedSummonerId):
        url = 'https://{}.api.riotgames.com/lol/summoner/v4/summoners/{}?api_key={}' \
            .format(self.region, encryptedSummonerId, self.api_key)

        response = requests.get(url)
        info_dict = json.loads(response.text)
        return info_dict

class ThirdPartyCodeInfo:

    """
    description : https://developer.riotgames.com/api-methods/#third-party-code-v4
    """

    def __init__(self, region, api_key):
        self.region = region
        self.api_key = api_key

    def getThirdPartyInfo(self, encryptedSummonerId):
        """
        :param encryptedAccountId: getInfo_bySummonerName 함수의 결과에서 얻을 수 있음
        """
        url = 'https://{}.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/{}?api_key={}' \
            .format(self.region, encryptedSummonerId, self.api_key)

        response = requests.get(url)
        return response.content

