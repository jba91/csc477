# CSC477 

Our dataset came from data.gov:

https://catalog.data.gov/dataset/crime-data-from-2010-to-present

This dataset contains crimes that occurred in the City of Los Angeles dating back to 2010.
Our goal was to predict the location (AreaID) of crimes based on this data.

The dataset has 26 fields but we only wanted to use (5) fields as we were interested in
crimes that had a human victim. We did not want to consider crimes involving property etc.

The fields we were interested were:

AreaID : CrimeID : Age : Gender : Race

AreadID is an integer from 1 to 21 representing the 21 police departments located in Los Angeles, CA.
CrimeID is a code used to indicate the type of crime committed - integer.
Age refers to the age of the victim of the crime - integer.
Gender: a character - M (Male) or F (Female)
Race: a character code - W for white, etc

We wrote `make_data_file.py` to parse the original csv file from data.gov and select only the fields we were interested in. We also converted all 5 fields to floating point values. The original csv has data such as:

```
DR Number,Date Reported,Date Occurred,Time Occurred,Area ID,Area Name,Reporting District,Crime Code,Crime Code Description,MO Codes,Victim Age,Victim Sex,Victim Descent,Premise Code,Premise Description,Weapon Used Code,Weapon Description,Status Code,Status Description,Crime Code 1,Crime Code 2,Crime Code 3,Crime Code 4,Address,Cross Street,Location 
001208575,03/14/2013,03/11/2013,1800,12,77th Street,1241,626,INTIMATE PARTNER - SIMPLE ASSAULT,0416 0446 1243 2000,30,F,W,502,"MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)",400,"STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)",AO,Adult Other,626,,,,6300    BRYNHURST                    AV,,"(33.9829, -118.3338)"
102005556,01/25/2010,01/22/2010,2300,20,Olympic,2071,510,VEHICLE - STOLEN,,,,,101,STREET,,,IC,Invest Cont,510,,,,VAN NESS,15TH,"(34.0454, -118.3157)"
0418,03/19/2013,03/18/2013,2030,18,Southeast,1823,510,VEHICLE - STOLEN,,12,,,101,STREET,,,IC,Invest Cont,510,,,,200 E  104TH                        ST,,"(33.942, -118.2717)"
101822289,11/11/2010,11/10/2010,1800,18,Southeast,1803,510,VEHICLE - STOLEN,,,,,101,STREET,,,IC,Invest Cont,510,,,,88TH,WALL,"(33.9572, -118.2717)"
042104479,01/11/2014,01/04/2014,2300,21,Topanga,2133,745,VANDALISM - MISDEAMEANOR ($399 OR UNDER),0329,84,M,W,501,SINGLE FAMILY DWELLING,,,IC,Invest Cont,745,,,,7200    CIRRUS                       WY,,"(34.2009, -118.6369)"
120125367,01/08/2013,01/08/2013,1400,01,Central,0111,110,CRIMINAL HOMICIDE,1243 2000 1813 1814 2002 0416 0400,49,F,W,501,SINGLE FAMILY DWELLING,400,"STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)",AA,Adult Arrest,110,,,,600 N  HILL                         ST,,"(34.0591, -118.2412)"
101105609,01/28/2010,01/27/2010,2230,11,Northeast,1125,510,VEHICLE - STOLEN,,,,,108,PARKING LOT,,,IC,Invest Cont,510,,,,YORK,AVENUE 51,"(34.1211, -118.2048)"
101620051,11/11/2010,11/07/2010,1600,16,Foothill,1641,510,VEHICLE - STOLEN,,,,,101,STREET,,,IC,Invest Cont,510,,,,EL DORADO,TRUESDALE,"(34.241, -118.3987)"
101910498,04/07/2010,04/07/2010,1600,19,Mission,1902,510,VEHICLE - STOLEN,,,,,101,STREET,,,IC,Invest Cont,510,,,,GLENOAKS,DRELL,"(34.3147, -118.4589)"
```

our Python program converts the above to the following:

```
AreaID,CrimeID,Age,Gender,Race
1.0,110.0,49.0,1.0,17.0
1.0,110.0,58.0,0.0,2.0
1.0,121.0,15.0,1.0,17.0
1.0,121.0,25.0,1.0,17.0
1.0,121.0,28.0,1.0,2.0
1.0,121.0,40.0,1.0,7.0
```

Note all the numerical values in the new file are floating point numbers.





