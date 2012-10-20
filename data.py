#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: data.py

# The Quiz of Country and Their Capital
# University of Djillali Liabes (UDL) - Sidi Bel Abbes
# Faculty of Sciences - Computer Science (LMD1) 2011/2012 
# Student: Boubakr NOUR <n.boubakr@gmail.com>

# License: Academic Free License (AFL)
# Source des capitales: http://www.newworldencyclopedia.org/entry/list_of_countries_by_continent

class Continent:
    """
    Class contains all the countries and their capitals and a help.
    """
    
    # Africa = 54 countries
    africa = [
      ['algeria', 'algiers'],
      ['angola', 'luanda'],
      ['benin', 'porto-novo', 'seat of government at cotonou'],
      ['botswana', 'gaborone'],
      ['burkina faso', 'ouagadougou'],
      ['burundi', 'bujumbura'],
      ['cameroon', 'yaounde'],
      ['cape verde', 'praia'],
      ['central african republic', 'bangui'],
      ['chad', "n'djamena"],
      ['comoros', 'moroni'],
      ['democratic republic of congo', 'kinshasa'],
      ['republic of congo', 'brazzaville'],
      ["cote d'ivoire", 'yamoussoukro', 'seat of government at abidjan'],
      ['djibouti', 'djibouti'],
      ['egypt', 'cairo'],
      ['equatorial guinea', 'malabo'],
      ['eritrea', 'asmara'],
      ['ethiopia', 'addis ababa'],
      ['gabon', 'libreville'],
      ['gambia', 'banjul'],
      ['ghana', 'accra'],
      ['guinea', 'conakry'],
      ['guinea-bissau', 'bissau'],
      ['kenya', 'nairobi'],
      ['lesotho', 'maseru'],
      ['liberia', 'monrovia'],
      ['libya', 'tripoli'],
      ['madagascar', 'antananarivo'],
      ['malawi', 'lilongwe'],
      ['mali', 'bamako'],
      ['mauritania', 'nouakchott'],
      ['mauritius', 'port louis'],
      ['morocco', 'rabat'],
      ['mozambique', 'maputo'],
      ['namibia', 'windhoek'],
      ['niger', 'niamey'],
      ['nigeria', 'abuja'],
      ['rwanda', 'kigali'],
      ['sao tome and principe', 'sao tome'],
      ['senegal', 'dakar'],
      ['seychelles', 'victoria'],
      ['sierra leone', 'freetown'],
      ['somalia', 'mogadishu'],
      ['south africa', 'pretoria', 'cape town (legislative), bloemfontein (judicial'],
      ['sudan', 'khartoum'],
      ['swaziland', 'mbabane', 'lobamba (royal and legislative)'],
      ['tanzania', 'dodoma', 'seat of government at dar es salaam'],
      ['togo', 'lome'],
      ['tunisia', 'tunis'],
      ['uganda', 'kampala'],
      ['western sahara', 'el aaiun'],
      ['zambia', 'lusaka'],
      ['zimbabwe', 'harare']
    ]
    
    # America = 35 countires
    america = [
      ['antigua and barbuda', "saint john's"],
      ['bahamas', 'nassau'],
      ['barbados', 'bridgetown'],
      ['belize', 'belmopan'],
      ['canada', 'ottawa'],
      ['costa rica', 'san jose'],
      ['cuba', 'havana'],
      ['dominica', 'roseau'],
      ['dominican republic', 'santo domingo'],
      ['el salvador', 'san salvador'],
      ['grenada', "saint george's"],
      ['guatemala', 'guatemala'],
      ['haiti', 'port-au-prince'],
      ['honduras', 'tegucigalpa'],
      ['jamaica', 'kingston'],
      ['mexico', 'mexico'],
      ['nicaragua', 'managua'],
      ['panama', 'panama'],
      ['saint kitts and nevis', 'basseterre'],
      ['saint lucia', 'castries'],
      ['saint vincent and the grenadines', 'kingstown'],
      ['trinidad and tobago', 'port of spain'],
      ['united states', 'washington'],
      ['argentina', 'buenos aires'],
      ['bolivia', 'sucre', 'seat of government at la paz'],
      ['brazil', 'brasilia'],
      ['chile', 'santiago'],
      ['colombia', 'bogota'],
      ['ecuador', 'quito'],
      ['guyana', 'georgetown'],
      ['paraguay', 'asuncion'],
      ['peru', 'lima'],
      ['suriname', 'paramaribo'],
      ['uruguay', 'montevideo'],
      ['venezuela', 'caracas']
    ]
    
    # Asia = 48 countries
    asia = [
      ['afghanistan', 'kabul'],
      ['armenia', 'yerevan'],
      ['azerbaijan', 'baku'],
      ['bahrain', 'manama'],
      ['bangladesh', 'dhaka'],
      ['bhutan', 'thimphu'],
      ['brunei', 'bandar seri begawan'],
      ['cambodia', 'phnom penh'],
      ['china', 'beijing'],
      ['taiwan', 'taipei'],
      ['cyprus', 'nicosia'],
      ['georgia', 'tbilisi'],
      ['india', 'new delhi'],
      ['indonesia', 'jakarta'],
      ['iran', 'tehran'],
      ['iraq', 'baghdad'],
      ['japan', 'tokyo'],
      ['jordan', 'amman'],
      ['kazakhstan', 'astana'],
      ['north korea', 'pyongyang'],
      ['south korea', 'seoul'],
      ['kuwait', 'kuwait'],
      ['kyrgyzstan', 'bishkek'],
      ['laos', 'vientiane'],
      ['lebanon', 'beirut'],
      ['malaysia', 'kuala lumpur'],
      ['maldives', 'male'],
      ['mongolia', 'ulaanbaatar'],
      ['myanmar (Burma)', 'naypyidaw'],
      ['nepal', 'kathmandu'],
      ['oman', 'muscat'],
      ['pakistan', 'islamabad'],
      ['palestine', 'quads'],
      ['philippines', 'manila'],
      ['qatar', 'doha'],
      ['saudi arabia', 'riyadh'],
      ['singapore', 'singapore'],
      ['sri lanka', 'sri jayewardenepura kotte'],
      ['syria', 'damascus'],
      ['tajikistan', 'dushanbe'],
      ['thailand', 'bangkok'],
      ['timor-leste (east timor)', 'dili'],
      ['turkey', 'ankara'],
      ['turkmenistan', 'ashgabat'],
      ['united arab emirates', 'abu dhabi'],
      ['uzbekistan', 'tashkent'],
      ['vietnam', 'hanoi'],
      [' yemen', "sana'a"]
    ]
    
    # Europe = 45 Countries
    europe = [
      ['albania', 'tirana'],
      ['andorra', 'andorra la vella'],
      ['austria', 'vienna'],
      ['belarus', 'minsk'],
      ['belgium', 'brussels'],
      ['bosnia and herzegovina', 'sarajevo'],
      ['bulgaria', 'sofia'],
      ['croatia', 'zagreb'],
      ['czech republic', 'prague'],
      ['denmark', 'copenhagen'],
      ['estonia', 'tallinn'],
      ['finland', 'helsinki'],
      ['france', 'paris'],
      ['germany', 'berlin'],
      ['greece', 'athens'],
      ['hungary', 'budapest'],
      ['iceland', 'reykjavík'],
      ['ireland', 'dublin'],
      ['italy', 'rome'],
      ['kosovo', 'pristina'],
      ['latvia', 'riga'],
      ['liechtenstein', 'vaduz'],
      ['lithuania', 'vilnius'],
      ['luxembourg', 'luxembourg'],
      ['former yugoslav republic of macedonia', 'skopje'],
      ['malta', 'valletta'],
      ['moldova', 'chisinau'],
      ['monaco', 'monaco'],
      ['montenegro', 'podgorica'],
      ['netherlands', 'amsterdam', 'seat of government at the hague'],
      ['norway', 'oslo'],
      ['poland', 'warsaw'],
      ['portugal', 'lisbon'],
      ['romania', 'bucharest'],
      ['russia', 'moscow'],
      ['san marino', 'san marino'],
      ['serbia', 'belgrade'],
      ['slovakia', 'bratislava'],
      ['slovenia', 'ljubljana'],
      ['spain', 'madrid'],
      ['sweden', 'stockholm'],
      ['switzerland', 'berne'],
      ['ukraine', 'kiev'],
      ['united kingdom', 'london'],
      ['vatican city', 'vatican']
    ]
    
    # Oceania = 15 countries
    oceania = [
      ['australia', 'canberra'],
      ['fiji', 'suva'],
      ['kiribati', 'south tarawa'],
      ['marshall islands', 'majuro'],
      ['micronesia', 'palikir'],
      ['nauru', 'yaren'],
      ['new zealand', 'wellington'],
      ['palau', 'melekeok'],
      ['papua new guinea', 'port moresby'],
      ['samoa', 'apia'],
      ['solomon islands', 'honiara'],
      ['tongo', "nuku'alofa"],
      ['tuvalu', 'funafuti'],
      ['vanuatu', 'port vila']
    ]
    
    world = []  # An empty list will extend all continents
    world.extend(africa)
    world.extend(america)
    world.extend(asia)
    world.extend(europe)
    world.extend(oceania)
# EOF