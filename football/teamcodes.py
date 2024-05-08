import enum

class Teams(enum.Enum):
    Bayern = 5
    Augsburg = 16
    Leverkusen = 3
    Dortmund = 4
    # M_gladbach = 15
    # Wolfsburg = 31
    # Frankfurt = 12
    # Sheffield_United = 6
    # PSV = 4
    Roma = 100
    Juventus = 109
    # Genoa = 19
    # Sassuolo = 10
    Napoli = 113
    Lazio = 110
    Inter = 108
    # Torino = 545
    Fiorentina = 99
    # Heidenheim = 356
    # Bochum = 674
    # Porto = 100
    Union_Berlin = 28
    Man_United = 66
    Tottenham = 73
    # Bournemouth = 471
    Aston_Villa = 58
    # Everton = 110
    # Watford = 108
    Leicester_City = 338
    West_Ham = 563
    # Stoke = 98
    Liverpool = 64
    # West_Brom = 13
    Man_City = 65
    # Galatasaray = 46
    # Lille = 17
    PSG = 524
    # Marseille = 30
    # Nice = 721
    # Monaco = 21
    # Nantes = 32
    # Montpellier = 44
    # Stade_Rennais = 26
    # Stade_de_Reims = 29
    # Toulouse = 36
    # Olympique_Lyon = 503
    # Lorient = 28
    # Almería = 24
    # Real_Sociedad = 66
    # Getafe = 73
    # Valencia = 1044
    Sevilla_FC = 559
    # Athletic = 62
    Barça = 81
    Real_Madrid = 86
    # Celta = 71
    # Real_Betis = 68
    # Villarreal = 354
    # Granada = 61
    # Sporting_CP = 72

class Leagues(enum.Enum):
    BSA = 2013    #Brazilian First Division
    BL = 2002     #Bundesliga
    FL = 2015    #Ligue 1
    PL = 2021     #Premier League
    ECL = 2016    #English Championship
    LL = 2014   #La Liga 
    SA = 2019    #Serie A
    PPL = 2017    #Portugese First Dvision
    ERD = 2003    #Eredivisie [Dutch]
    CL = 2001 

class Seasons(enum.Enum):
    Season_2001_2002 = 2001
    Season_2002_2003 = 2002
    Season_2003_2004 = 2003
    Season_2004_2005 = 2004
    Season_2005_2006 = 2005
    Season_2006_2007 = 2006
    Season_2007_2008 = 2007
    Season_2008_2009 = 2008
    Season_2009_2010 = 2009
    Season_2010_2011 = 2010
    Season_2011_2012 = 2011
    Season_2012_2013 = 2012
    Season_2013_2014 = 2013
    Season_2014_2015 = 2014
    Season_2015_2016 = 2015
    Season_2016_2017 = 2016
    Season_2017_2018 = 2017
    Season_2018_2019 = 2018
    Season_2019_2020 = 2019
    Season_2020_2021 = 2020
    Season_2021_2022 = 2021
    Season_2022_2023 = 2022
    Current_Season = 2023