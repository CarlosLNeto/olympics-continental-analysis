"""
Mapeamento de Códigos NOC (National Olympic Committee) para Continentes

Baseado nos códigos oficiais do COI (Comitê Olímpico Internacional)
"""

NOC_TO_CONTINENT = {
    # ÁFRICA
    'ALG': 'África',  # Algeria
    'ANG': 'África',  # Angola
    'BEN': 'África',  # Benin
    'BOT': 'África',  # Botswana
    'BUR': 'África',  # Burkina Faso
    'BDI': 'África',  # Burundi
    'CMR': 'África',  # Cameroon
    'CPV': 'África',  # Cape Verde
    'CAF': 'África',  # Central African Republic
    'CHA': 'África',  # Chad
    'COM': 'África',  # Comoros
    'CGO': 'África',  # Congo
    'COD': 'África',  # Democratic Republic of Congo
    'CIV': 'África',  # Côte d'Ivoire
    'DJI': 'África',  # Djibouti
    'EGY': 'África',  # Egypt
    'GEQ': 'África',  # Equatorial Guinea
    'ERI': 'África',  # Eritrea
    'ETH': 'África',  # Ethiopia
    'GAB': 'África',  # Gabon
    'GAM': 'África',  # Gambia
    'GHA': 'África',  # Ghana
    'GUI': 'África',  # Guinea
    'GBS': 'África',  # Guinea-Bissau
    'KEN': 'África',  # Kenya
    'LES': 'África',  # Lesotho
    'LBR': 'África',  # Liberia
    'LBA': 'África',  # Libya
    'MAD': 'África',  # Madagascar
    'MAW': 'África',  # Malawi
    'MLI': 'África',  # Mali
    'MTN': 'África',  # Mauritania
    'MRI': 'África',  # Mauritius
    'MAR': 'África',  # Morocco
    'MOZ': 'África',  # Mozambique
    'NAM': 'África',  # Namibia
    'NIG': 'África',  # Niger
    'NGR': 'África',  # Nigeria
    'RWA': 'África',  # Rwanda
    'STP': 'África',  # São Tomé and Príncipe
    'SEN': 'África',  # Senegal
    'SEY': 'África',  # Seychelles
    'SLE': 'África',  # Sierra Leone
    'SOM': 'África',  # Somalia
    'RSA': 'África',  # South Africa
    'SSD': 'África',  # South Sudan
    'SUD': 'África',  # Sudan
    'SWZ': 'África',  # Eswatini (Swaziland)
    'TAN': 'África',  # Tanzania
    'TOG': 'África',  # Togo
    'TUN': 'África',  # Tunisia
    'UGA': 'África',  # Uganda
    'ZAM': 'África',  # Zambia
    'ZIM': 'África',  # Zimbabwe
    
    # AMÉRICAS
    'ARG': 'Américas',  # Argentina
    'ARU': 'Américas',  # Aruba
    'ANT': 'Américas',  # Antigua and Barbuda
    'BAH': 'Américas',  # Bahamas
    'BAR': 'Américas',  # Barbados
    'BIZ': 'Américas',  # Belize
    'BER': 'Américas',  # Bermuda
    'BOL': 'Américas',  # Bolivia
    'BRA': 'Américas',  # Brazil
    'IVB': 'Américas',  # British Virgin Islands
    'CAN': 'Américas',  # Canada
    'CAY': 'Américas',  # Cayman Islands
    'CHI': 'Américas',  # Chile
    'COL': 'Américas',  # Colombia
    'CRC': 'Américas',  # Costa Rica
    'CUB': 'Américas',  # Cuba
    'DMA': 'Américas',  # Dominica
    'DOM': 'Américas',  # Dominican Republic
    'ECU': 'Américas',  # Ecuador
    'ESA': 'Américas',  # El Salvador
    'GRN': 'Américas',  # Grenada
    'GUA': 'Américas',  # Guatemala
    'GUY': 'Américas',  # Guyana
    'HAI': 'Américas',  # Haiti
    'HON': 'Américas',  # Honduras
    'JAM': 'Américas',  # Jamaica
    'MEX': 'Américas',  # Mexico
    'NCA': 'Américas',  # Nicaragua
    'PAN': 'Américas',  # Panama
    'PAR': 'Américas',  # Paraguay
    'PER': 'Américas',  # Peru
    'PUR': 'Américas',  # Puerto Rico
    'SKN': 'Américas',  # Saint Kitts and Nevis
    'LCA': 'Américas',  # Saint Lucia
    'VIN': 'Américas',  # Saint Vincent and the Grenadines
    'SUR': 'Américas',  # Suriname
    'TTO': 'Américas',  # Trinidad and Tobago
    'USA': 'Américas',  # United States
    'URU': 'Américas',  # Uruguay
    'VEN': 'Américas',  # Venezuela
    'ISV': 'Américas',  # US Virgin Islands
    
    # ÁSIA
    'AFG': 'Ásia',  # Afghanistan
    'BRN': 'Ásia',  # Bahrain
    'BAN': 'Ásia',  # Bangladesh
    'BHU': 'Ásia',  # Bhutan
    'BRU': 'Ásia',  # Brunei
    'CAM': 'Ásia',  # Cambodia
    'CHN': 'Ásia',  # China
    'TPE': 'Ásia',  # Chinese Taipei (Taiwan)
    'HKG': 'Ásia',  # Hong Kong
    'IND': 'Ásia',  # India
    'INA': 'Ásia',  # Indonesia
    'IRI': 'Ásia',  # Iran
    'IRQ': 'Ásia',  # Iraq
    'JPN': 'Ásia',  # Japan
    'JOR': 'Ásia',  # Jordan
    'KAZ': 'Ásia',  # Kazakhstan
    'KUW': 'Ásia',  # Kuwait
    'KGZ': 'Ásia',  # Kyrgyzstan
    'LAO': 'Ásia',  # Laos
    'LBN': 'Ásia',  # Lebanon
    'MAS': 'Ásia',  # Malaysia
    'MDV': 'Ásia',  # Maldives
    'MGL': 'Ásia',  # Mongolia
    'MYA': 'Ásia',  # Myanmar
    'NEP': 'Ásia',  # Nepal
    'PRK': 'Ásia',  # North Korea
    'OMA': 'Ásia',  # Oman
    'PAK': 'Ásia',  # Pakistan
    'PLE': 'Ásia',  # Palestine
    'PHI': 'Ásia',  # Philippines
    'QAT': 'Ásia',  # Qatar
    'KSA': 'Ásia',  # Saudi Arabia
    'SGP': 'Ásia',  # Singapore
    'KOR': 'Ásia',  # South Korea
    'SRI': 'Ásia',  # Sri Lanka
    'SYR': 'Ásia',  # Syria
    'TJK': 'Ásia',  # Tajikistan
    'THA': 'Ásia',  # Thailand
    'TLS': 'Ásia',  # Timor-Leste
    'TKM': 'Ásia',  # Turkmenistan
    'UAE': 'Ásia',  # United Arab Emirates
    'UZB': 'Ásia',  # Uzbekistan
    'VIE': 'Ásia',  # Vietnam
    'YEM': 'Ásia',  # Yemen
    
    # EUROPA
    'ALB': 'Europa',  # Albania
    'AND': 'Europa',  # Andorra
    'ARM': 'Europa',  # Armenia
    'AUT': 'Europa',  # Austria
    'AZE': 'Europa',  # Azerbaijan
    'BLR': 'Europa',  # Belarus
    'BEL': 'Europa',  # Belgium
    'BIH': 'Europa',  # Bosnia and Herzegovina
    'BUL': 'Europa',  # Bulgaria
    'CRO': 'Europa',  # Croatia
    'CYP': 'Europa',  # Cyprus
    'CZE': 'Europa',  # Czech Republic
    'DEN': 'Europa',  # Denmark
    'EST': 'Europa',  # Estonia
    'FIN': 'Europa',  # Finland
    'FRA': 'Europa',  # France
    'GEO': 'Europa',  # Georgia
    'GER': 'Europa',  # Germany
    'GRE': 'Europa',  # Greece
    'HUN': 'Europa',  # Hungary
    'ISL': 'Europa',  # Iceland
    'IRL': 'Europa',  # Ireland
    'ISR': 'Europa',  # Israel
    'ITA': 'Europa',  # Italy
    'KOS': 'Europa',  # Kosovo
    'LAT': 'Europa',  # Latvia
    'LIE': 'Europa',  # Liechtenstein
    'LTU': 'Europa',  # Lithuania
    'LUX': 'Europa',  # Luxembourg
    'MKD': 'Europa',  # North Macedonia
    'MLT': 'Europa',  # Malta
    'MDA': 'Europa',  # Moldova
    'MON': 'Europa',  # Monaco
    'MNE': 'Europa',  # Montenegro
    'NED': 'Europa',  # Netherlands
    'NOR': 'Europa',  # Norway
    'POL': 'Europa',  # Poland
    'POR': 'Europa',  # Portugal
    'ROU': 'Europa',  # Romania
    'RUS': 'Europa',  # Russia
    'SMR': 'Europa',  # San Marino
    'SRB': 'Europa',  # Serbia
    'SVK': 'Europa',  # Slovakia
    'SLO': 'Europa',  # Slovenia
    'ESP': 'Europa',  # Spain
    'SWE': 'Europa',  # Sweden
    'SUI': 'Europa',  # Switzerland
    'TUR': 'Europa',  # Turkey
    'UKR': 'Europa',  # Ukraine
    'GBR': 'Europa',  # Great Britain
    'ROC': 'Europa',  # Russian Olympic Committee
    'AIN': 'Europa',  # Individual Neutral Athletes
    
    # OCEANIA
    'ASA': 'Oceania',  # American Samoa
    'AUS': 'Oceania',  # Australia
    'COK': 'Oceania',  # Cook Islands
    'FIJ': 'Oceania',  # Fiji
    'GUM': 'Oceania',  # Guam
    'KIR': 'Oceania',  # Kiribati
    'MHL': 'Oceania',  # Marshall Islands
    'FSM': 'Oceania',  # Micronesia
    'NRU': 'Oceania',  # Nauru
    'NZL': 'Oceania',  # New Zealand
    'PLW': 'Oceania',  # Palau
    'PNG': 'Oceania',  # Papua New Guinea
    'SAM': 'Oceania',  # Samoa
    'SOL': 'Oceania',  # Solomon Islands
    'TGA': 'Oceania',  # Tonga
    'TUV': 'Oceania',  # Tuvalu
    'VAN': 'Oceania',  # Vanuatu
    
    # CÓDIGOS HISTÓRICOS E ESPECIAIS
    'URS': 'Europa',  # USSR (União Soviética)
    'EUN': 'Europa',  # Unified Team (1992)
    'TCH': 'Europa',  # Czechoslovakia
    'YUG': 'Europa',  # Yugoslavia
    'FRG': 'Europa',  # West Germany
    'GDR': 'Europa',  # East Germany
    'SCG': 'Europa',  # Serbia and Montenegro
    'ANZ': 'Oceania',  # Australasia (Australia + New Zealand)
    'BOH': 'Europa',  # Bohemia
    'ZZX': 'Diversos',  # Mixed teams
    'IOA': 'Diversos',  # Independent Olympic Athletes
    'IOP': 'Diversos',  # Independent Olympic Participants
    'AHO': 'Américas',  # Netherlands Antilles
}

def get_continent(noc_code):
    """
    Retorna o continente para um código NOC
    
    Args:
        noc_code (str): Código NOC do país
        
    Returns:
        str: Nome do continente ou 'Desconhecido'
    """
    return NOC_TO_CONTINENT.get(noc_code, 'Desconhecido')

def get_continents_summary():
    """
    Retorna resumo dos continentes
    
    Returns:
        dict: Dicionário com contagem por continente
    """
    from collections import Counter
    return dict(Counter(NOC_TO_CONTINENT.values()))

if __name__ == '__main__':
    summary = get_continents_summary()
    print("Resumo de países por continente:")
    for continent, count in sorted(summary.items()):
        print(f"  {continent}: {count} países")
    print(f"\nTotal: {sum(summary.values())} códigos NOC mapeados")
