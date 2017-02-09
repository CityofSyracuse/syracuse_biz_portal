INSPECTION_TYPE_CHOICES = {'85': 'Codes Inspection (Electrical)',
                           '84': 'Codes Inspection (Building)',
                           '83': 'Fire Prevention Inspection',
                           '82': 'Zoning Inspection'
                           }

INSPECTION_DEPARTMENT_CHOICES = {'85': 'Codes',
                                 '84': 'Codes',
                                 '83': 'Fire'
                                 }

INSPECTION_STATUS_CHOICES = {'1': 'Pass',
                             '2': 'Fail',
                             '3': 'N/A',
                             '4': 'In Progress',
                             '5': 'No Progress',
                             '6': 'No Work Started'
                             }

PERMIT_TYPE_CHOICES = {'100': 'FPB Private Pump - FPB Private Pump',
                       '101': 'FPB Propane - FPB Propane',
                       '102': 'FPB Tanker Truck - FPB Tanker Truck',
                       '103': 'FPB Tent - FPB Tent',
                       '106': ('Electric (Meter Set) - Meter Set Permit'
                               '(to turn power on)'),
                       '112': 'Res. Remodel/Chg Occ - Residentail Remodel',
                       '113': ('Com. Reno/Rem/Chg Occ - Commercial'
                               'Renovation Remodel'),
                       '114': ('Loading Zone (Business) - Loading Zone'
                               'Permit for businesses w/ non-commercial'
                               'license plates'),
                       '115': ('Loading Zone (Res) - Loading Zone'
                               'permit for residential use of LZ'),
                       '116': 'Public Assembly - ',
                       '117': ('Encroach (Deminimus) - Small encroachment,'
                               'usually associated with real estate trx.'),
                       '118': ('Encroachment (Converted) - For AS400 zoning'
                               'records where major v minor could not'
                               'be distinguished'),
                       '119': 'Res. Sidewalk Replace - ',
                       '45': 'Com. New Building - New Commercial Construction',
                       '46': 'Res. New 1-2 Family - New 1-2 Family Home',
                       '48': 'Pool / Hot Tub - New Pool / Hot Tub',
                       '58': 'Demolition - ',
                       '59': 'Electric - Electric',
                       '61': 'Banner - Banner',
                       '62': 'Fire Alarm - Fire Alarm',
                       '63': 'Security Alarm - Security Alarm',
                       '64': 'Elevator - Elevator',
                       '65': ('Site Work - Paving/Excavating/Grading/'
                              'Laying Stone'),
                       '70': 'Antenna / Dish - Antenna / Dish',
                       '72': 'Tank - Tank',
                       '73': 'HVAC/Mechanical - Mechanical',
                       '74': 'Misc.(deck, fence,ramp) - Miscellaneous',
                       '75': 'Sprinkler - Sprinkler',
                       '76': 'Sign - Sign',
                       '77': 'Footing / Foundation - Footing / Foundation',
                       '83': ('Encroach (Major) - ROW Encroachment'
                              '(Major / Permanent)'),
                       '84': ('Encroach (Minor) - ROW Encroachment'
                              '(Minor / Temporary)'),
                       '85': 'Curb Cut - ROW Curb Cut',
                       '86': 'Liability Waiver - ROW Liability Waiver',
                       '87': ('Non-Com Loading Zone - ROW Non-Commercial'
                              'Loading Zone'),
                       '88': 'Non-Food Vendor - ROW Non-Food Vendor',
                       '89': 'Parking Meter Rental - ROW Parking Meter Rental',
                       '91': 'Road Cut - ROW Road Cut',
                       '92': 'Sidewalk Cafe - ROW Sidewalk Cafe',
                       '93': 'Sidewalk Replace - ROW Sidewalk Replacement',
                       '94': ('Block Party (Business) - Block Party'
                              '(Business District Street Closing)'),
                       '95': ('Block Party (Residential) - Block Party'
                              '(Residential Street Closing)'),
                       '96': 'Coin Laundry - Coin Laundry',
                       '97': 'FPB Welding / Cutting - FPB Welding / Cutting',
                       '98': 'FPB Fireworks - FPB Fireworks',
                       '99': ('FPB Hazardous Chemicals - FPB'
                              'Hazardous Chemicals')}

PERMIT_DEPARTMENT_CHOICES = {'1': 'Board of Zoning Appeals',
                               '10': 'DPW - Sidewalk Inspector',
                               '11': 'DPW - Street Repair - Permits',
                               '12': 'DPW - Traffic Control',
                               '13': 'DPW - Transportation Planner',
                               '14': 'Engineering - City Engineer',
                               '15': 'Engineering - Design & Construction',
                               '16': 'Engineering - Mapping',
                               '17': 'Engineering - Public Buildings',
                               '18': 'Engineering - Sewers',
                               '19': 'Engineering - Stormwater (SWPPP)',
                               '20': 'Fire Prevention Bureau',
                               '21': "Mayor's Office - Constituent Services",
                               '22': 'NBD - Commissioner',
                               '23': 'NBD - Division of Business Development',
                               '24': 'NYS DOT',
                               '25': 'Onondaga Co Department of Health',
                               '26': 'Onondaga Co Planning Board',
                               '27': 'Onondaga Co Plumbing Control',
                               '3': 'Landmark Preservation Board',
                               '30': 'Outside Architect Review',
                               '31': 'Parks - Special Events',
                               '32': 'Central Permit Office',
                               '33': 'Permit Desk/Codes',
                               '34': 'City Planning - SOCPA',
                               '35': 'Police Department - Community Policing',
                               '36': 'Police Department - Special Events',
                               '37': 'Water Commissioner',
                               '38': 'Water Engineering',
                               '39': 'Zoning Planner',
                               '4': 'Pre-Dev Review',
                               '40': 'Parks - Forestry',
                               '41': 'Certificate of Appropriateness',
                               '47': 'Law - Housing Judgments',
                               '48': 'Parking Violations',
                               '49': 'Water Billing',
                               '5': 'Assessment - Commissioner',
                               '50': 'Tax Billing',
                               '51': 'Zoning - Licensing',
                               '54': 'Law - Stormwater Agreements',
                               '55': 'Eng - SW Agreements - Tech',
                               '56': 'Eng - SW Agreements - Filed',
                               '58': 'Planning Commission',
                               '59': 'Common Council',
                               '6': 'Corporation Counsel',
                               '60': 'District Councilor',
                               '61': 'National Grid',
                               '62': 'Verizon',
                               '63': 'CENTRO',
                               '64': 'Parking Violations - LZ',
                               '66': 'Zoning Administrator',
                               '67': 'DPW Street Repair - Zoning',
                               '68': 'SOCPA 911',
                               '7': 'DPW - Commissioner',
                               '70': 'DPW Commissioner - Zoning',
                               '71': 'NBD - Neighborhood Planning',
                               '72': 'Code Enforcement',
                               '73': 'Treasury',
                               '74': 'DPW Sewers - Zoning',
                               '75': 'DPW Sidewalks - Zoning',
                               '76': 'Eng. Design & Cons. - Zoning',
                               '77': 'City Engineer - Zoning',
                               '78': 'Eng. Mapping - Zoning',
                               '79': 'Water Engineering - Zoning',
                               '8': 'DPW - Insurance',
                               '80': 'City Planning - Zoning',
                               '81': 'Fire Prevention - Zoning',
                               '82': 'DPW Traffic Control- Zoning',
                               '83': 'Eng Sewers- Zoning',
                               '84': 'Eng Stormwater (SWPPP)- Zoning',
                               '9': 'DPW - Sanitation & Sewers'}
