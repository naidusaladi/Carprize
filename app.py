import streamlit as st
import pickle
import math
from PIL import Image


st.title("Car Prize Prediction")


image = Image.open("th.jpg")
st.image(image)

reg=pickle.load(open("linearreg.sav",'rb'))

col1, col2, = st.columns(2)

col3,col4 =st.columns(2)

col5,col6=st.columns(2)

col7,col8=st.columns(2)

with col1:
    year = st.number_input(label="Year",min_value=1997, max_value=2018)
   

with col2:
    mileage = st.number_input(label="Mileage",min_value=5, max_value=2457832)

with col3:
    State = st.selectbox(
        
        'State',
        (' AK', ' AL', ' AR', ' AZ', ' CA', ' CO', ' CT', ' DC', ' DE', ' FL', ' GA', ' HI', ' IA', ' ID', ' IL', ' IN', ' KS', ' KY', ' LA', ' MA', ' MD', ' ME', ' MI', ' MN', ' MO', ' MS', ' MT', ' NC', ' ND', ' NE', ' NH', ' NJ', ' NM', ' NV', ' NY', ' OH', ' OK', ' OR', ' PA', ' RI', ' SC', ' SD', ' TN', ' TX', ' UT', ' VA', ' VT', ' WA', ' WI', ' WV', ' WY'))
    
with col4:
   make = st.selectbox(
       
       'Make',
       ('Acura', 'Audi', 'BMW', 'Bentley', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'FIAT', 'Ford', 'Freightliner', 'GMC', 'Honda', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia', 'Land', 'Lexus', 'Lincoln', 'MINI', 'Mazda', 'Mercedes-Benz', 'Mercury', 'Mitsubishi', 'Nissan', 'Pontiac', 'Porsche', 'Ram', 'Scion', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo')) 
with col5:
    model = st.selectbox(
        
        'Model',
        ('1', '15002WD', '15004WD', '1500Laramie', '1500Tradesman', '200LX', '200Limited', '200S', '200Touring', '25002WD', '25004WD', '3', '300300C', '300300S', '3004dr', '300Base', '300Limited', '300Touring', '35004WD', '350Z2dr', '4Runner2WD', '4Runner4WD', '4Runner4dr', '4RunnerLimited', '4RunnerRWD', '4RunnerSR5', '4RunnerTrail', '5', '500Pop', '6', '7', '911', '9112dr', 'A34dr', 'A44dr', 'A64dr', 'A8', 'AcadiaAWD', 'AcadiaFWD', 'Accent4dr', 'Accord', 'AccordEX', 'AccordEX-L', 'AccordLX', 'AccordLX-S', 'AccordSE', 'Altima4dr', 'Armada2WD', 'Armada4WD', 'Avalanche2WD', 'Avalanche4WD', 'Avalon4dr', 'AvalonLimited', 'AvalonTouring', 'AvalonXLE', 'Azera4dr', 'Boxster2dr', 'C-Class4dr', 'C-ClassC', 'C-ClassC300', 'C-ClassC350', 'C702dr', 'CC4dr', 'CR-V2WD', 'CR-V4WD', 'CR-VEX', 'CR-VEX-L', 'CR-VLX', 'CR-VSE', 'CR-ZEX', 'CT', 'CTCT', 'CTS', 'CTS-V', 'CTS4dr', 'CX-7FWD', 'CX-9AWD', 'CX-9FWD', 'CX-9Grand', 'CX-9Touring', 'Caliber4dr', 'Camaro2dr', 'CamaroConvertible', 'CamaroCoupe', 'Camry', 'Camry4dr', 'CamryBase', 'CamryL', 'CamryLE', 'CamrySE', 'CamryXLE', 'Canyon2WD', 'Canyon4WD', 'CanyonCrew', 'CanyonExtended', 'CayenneAWD', 'Cayman2dr', 'Challenger2dr', 'ChallengerR/T', 'Charger4dr', 'ChargerSE', 'ChargerSXT', 'CherokeeLimited', 'CherokeeSport', 'Civic', 'CivicEX', 'CivicEX-L', 'CivicLX', 'CivicSi', 'Cobalt2dr', 'Cobalt4dr', 'Colorado2WD', 'Colorado4WD', 'ColoradoCrew', 'ColoradoExtended', 'Compass4WD', 'CompassLatitude', 'CompassLimited', 'CompassSport', 'Continental', 'Cooper', 'Corolla4dr', 'CorollaL', 'CorollaLE', 'CorollaS', 'Corvette2dr', 'CorvetteConvertible', 'CorvetteCoupe', 'CruzeLT', 'CruzeSedan', 'DTS4dr', 'Dakota2WD', 'Dakota4WD', 'Durango2WD', 'Durango4dr', 'DurangoAWD', 'DurangoSXT', 'E-ClassE', 'E-ClassE320', 'E-ClassE350', 'ES', 'ESES', 'Eclipse3dr', 'Econoline', 'EdgeLimited', 'EdgeSE', 'EdgeSEL', 'EdgeSport', 'Elantra', 'Elantra4dr', 'ElantraLimited', 'Element2WD', 'Element4WD', 'EnclaveConvenience', 'EnclaveLeather', 'EnclavePremium', 'Eos2dr', 'EquinoxAWD', 'EquinoxFWD', 'Escalade', 'Escalade2WD', 'Escalade4dr', 'EscaladeAWD', 'Escape4WD', 'Escape4dr', 'EscapeFWD', 'EscapeLImited', 'EscapeLimited', 'EscapeS', 'EscapeSE', 'EscapeXLT', 'Excursion137"', 'Expedition', 'Expedition2WD', 'Expedition4WD', 'ExpeditionLimited', 'ExpeditionXLT', 'Explorer', 'Explorer4WD', 'Explorer4dr', 'ExplorerBase', 'ExplorerEddie', 'ExplorerFWD', 'ExplorerLimited', 'ExplorerXLT', 'Express', 'F-1502WD', 'F-1504WD', 'F-150FX2', 'F-150FX4', 'F-150King', 'F-150Lariat', 'F-150Limited', 'F-150Platinum', 'F-150STX', 'F-150SuperCrew', 'F-150XL', 'F-150XLT', 'F-250King', 'F-250Lariat', 'F-250XL', 'F-250XLT', 'F-350King', 'F-350Lariat', 'F-350XL', 'F-350XLT', 'FJ', 'FX35AWD', 'FiestaS', 'FiestaSE', 'FitSport', 'FlexLimited', 'FlexSE', 'FlexSEL', 'Focus4dr', 'Focus5dr', 'FocusS', 'FocusSE', 'FocusSEL', 'FocusST', 'FocusTitanium', 'Forester2.5X', 'Forester4dr', 'Forte', 'ForteEX', 'ForteLX', 'ForteSX', 'Frontier', 'Frontier2WD', 'Frontier4WD', 'Fusion4dr', 'FusionHybrid', 'FusionS', 'FusionSE', 'FusionSEL', 'G35', 'G37', 'G64dr', 'GLI4dr', 'GS', 'GSGS', 'GTI2dr', 'GTI4dr', 'GX', 'GXGX', 'Galant4dr', 'Genesis', 'Golf', 'Grand', 'Highlander', 'Highlander4WD', 'Highlander4dr', 'HighlanderBase', 'HighlanderFWD', 'HighlanderLimited', 'HighlanderSE', 'IS', 'ISIS', 'Impala4dr', 'ImpalaLS', 'ImpalaLT', 'Impreza', 'Impreza2.0i', 'ImprezaSport', 'Jetta', 'JourneyAWD', 'JourneyFWD', 'JourneySXT', 'LS', 'LSLS', 'LX', 'LXLX', 'LaCrosse4dr', 'LaCrosseAWD', 'LaCrosseFWD', 'Lancer4dr', 'Land', 'Legacy', 'Legacy2.5i', 'Legacy3.6R', 'Liberty4WD', 'LibertyLimited', 'LibertySport', 'Lucerne4dr', 'M-ClassML350', 'MDX4WD', 'MDXAWD', 'MKXAWD', 'MKXFWD', 'MKZ4dr', 'MX5', 'Malibu', 'Malibu1LT', 'Malibu4dr', 'MalibuLS', 'MalibuLT', 'Matrix5dr', 'Maxima4dr', 'Mazda34dr', 'Mazda35dr', 'Mazda64dr', 'Milan4dr', 'Model', 'Monte', 'Murano2WD', 'MuranoAWD', 'MuranoS', 'Mustang2dr', 'MustangBase', 'MustangDeluxe', 'MustangGT', 'MustangPremium', 'MustangShelby', 'Navigator', 'Navigator2WD', 'Navigator4WD', 'Navigator4dr', 'New', 'OdysseyEX', 'OdysseyEX-L', 'OdysseyLX', 'OdysseyTouring', 'Optima4dr', 'OptimaEX', 'OptimaLX', 'OptimaSX', 'Outback2.5i', 'Outback3.6R', 'Outlander', 'Outlander2WD', 'Outlander4WD', 'PT', 'PacificaLimited', 'PacificaTouring', 'Passat', 'Passat4dr', 'Pathfinder2WD', 'Pathfinder4WD', 'PathfinderS', 'PathfinderSE', 'Patriot4WD', 'PatriotLatitude', 'PatriotLimited', 'PatriotSport', 'Pilot2WD', 'Pilot4WD', 'PilotEX', 'PilotEX-L', 'PilotLX', 'PilotSE', 'PilotTouring', 'Prius', 'Prius5dr', 'PriusBase', 'PriusFive', 'PriusFour', 'PriusOne', 'PriusThree', 'PriusTwo', 'Q5quattro', 'Q7quattro', 'QX562WD', 'QX564WD', 'Quest4dr', 'RAV4', 'RAV44WD', 'RAV44dr', 'RAV4Base', 'RAV4FWD', 'RAV4LE', 'RAV4Limited', 'RAV4Sport', 'RAV4XLE', 'RDXAWD', 'RDXFWD', 'RX', 'RX-84dr', 'RXRX', 'Ram', 'Ranger2WD', 'Ranger4WD', 'RangerSuperCab', 'Regal4dr', 'RegalGS', 'RegalPremium', 'RegalTurbo', 'RidgelineRTL', 'RidgelineSport', 'RioLX', 'RogueFWD', 'Rover', 'S2000Manual', 'S44dr', 'S60T5', 'S804dr', 'SC', 'SL-ClassSL500', 'SLK-ClassSLK350', 'SRXLuxury', 'STS4dr', 'Santa', 'Savana', 'Sedona4dr', 'SedonaEX', 'SedonaLX', 'Sentra4dr', 'Sequoia4WD', 'Sequoia4dr', 'SequoiaLimited', 'SequoiaPlatinum', 'SequoiaSR5', 'Sienna5dr', 'SiennaLE', 'SiennaLimited', 'SiennaSE', 'SiennaXLE', 'Sierra', 'Silverado', 'Sonata4dr', 'SonataLimited', 'SonataSE', 'SonicHatch', 'SonicSedan', 'Sorento2WD', 'SorentoEX', 'SorentoLX', 'SorentoSX', 'Soul+', 'SoulBase', 'Sportage2WD', 'SportageAWD', 'SportageEX', 'SportageLX', 'SportageSX', 'Sprinter', 'Suburban2WD', 'Suburban4WD', 'Suburban4dr', 'Super', 'TL4dr', 'TLAutomatic', 'TSXAutomatic', 'TT2dr', 'Tacoma2WD', 'Tacoma4WD', 'TacomaBase', 'TacomaPreRunner', 'Tahoe2WD', 'Tahoe4WD', 'Tahoe4dr', 'TahoeLS', 'TahoeLT', 'Taurus4dr', 'TaurusLimited', 'TaurusSE', 'TaurusSEL', 'TaurusSHO', 'TerrainAWD', 'TerrainFWD', 'Tiguan2WD', 'TiguanS', 'TiguanSE', 'TiguanSEL', 'Titan', 'Titan2WD', 'Titan4WD', 'Touareg4dr', 'Town', 'Transit', 'TraverseAWD', 'TraverseFWD', 'TucsonAWD', 'TucsonFWD', 'TucsonLimited', 'Tundra', 'Tundra2WD', 'Tundra4WD', 'TundraBase', 'TundraLimited', 'TundraSR5', 'VeracruzAWD', 'VeracruzFWD', 'Versa4dr', 'Versa5dr', 'Vibe4dr', 'WRXBase', 'WRXLimited', 'WRXPremium', 'WRXSTI', 'Wrangler', 'Wrangler2dr', 'Wrangler4WD', 'WranglerRubicon', 'WranglerSahara', 'WranglerSport', 'WranglerX', 'X1xDrive28i', 'X3AWD', 'X3xDrive28i', 'X5AWD', 'X5xDrive35i', 'XC60AWD', 'XC60FWD', 'XC60T6', 'XC704dr', 'XC90AWD', 'XC90FWD', 'XC90T6', 'XF4dr', 'XJ4dr', 'XK2dr', 'Xterra2WD', 'Xterra4WD', 'Xterra4dr', 'Yaris', 'Yaris4dr', 'YarisBase', 'YarisLE', 'Yukon', 'Yukon2WD', 'Yukon4WD', 'Yukon4dr', 'tC2dr', 'xB5dr', 'xD5dr'))

state_arr=[' AK', ' AL', ' AR', ' AZ', ' CA', ' CO', ' CT', ' DC', ' DE', ' FL', ' GA', ' HI', ' IA', ' ID', ' IL', ' IN', ' KS', ' KY', ' LA', ' MA', ' MD', ' ME', ' MI', ' MN', ' MO', ' MS', ' MT', ' NC', ' ND', ' NE', ' NH', ' NJ', ' NM', ' NV', ' NY', ' OH', ' OK', ' OR', ' PA', ' RI', ' SC', ' SD', ' TN', ' TX', ' UT', ' VA', ' VT', ' WA', ' WI', ' WV', ' WY']
make_arr=['Acura', 'Audi', 'BMW', 'Bentley', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'FIAT', 'Ford', 'Freightliner', 'GMC', 'Honda', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia', 'Land', 'Lexus', 'Lincoln', 'MINI', 'Mazda', 'Mercedes-Benz', 'Mercury', 'Mitsubishi', 'Nissan', 'Pontiac', 'Porsche', 'Ram', 'Scion', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']
model_arr=['1', '15002WD', '15004WD', '1500Laramie', '1500Tradesman', '200LX', '200Limited', '200S', '200Touring', '25002WD', '25004WD', '3', '300300C', '300300S', '3004dr', '300Base', '300Limited', '300Touring', '35004WD', '350Z2dr', '4Runner2WD', '4Runner4WD', '4Runner4dr', '4RunnerLimited', '4RunnerRWD', '4RunnerSR5', '4RunnerTrail', '5', '500Pop', '6', '7', '911', '9112dr', 'A34dr', 'A44dr', 'A64dr', 'A8', 'AcadiaAWD', 'AcadiaFWD', 'Accent4dr', 'Accord', 'AccordEX', 'AccordEX-L', 'AccordLX', 'AccordLX-S', 'AccordSE', 'Altima4dr', 'Armada2WD', 'Armada4WD', 'Avalanche2WD', 'Avalanche4WD', 'Avalon4dr', 'AvalonLimited', 'AvalonTouring', 'AvalonXLE', 'Azera4dr', 'Boxster2dr', 'C-Class4dr', 'C-ClassC', 'C-ClassC300', 'C-ClassC350', 'C702dr', 'CC4dr', 'CR-V2WD', 'CR-V4WD', 'CR-VEX', 'CR-VEX-L', 'CR-VLX', 'CR-VSE', 'CR-ZEX', 'CT', 'CTCT', 'CTS', 'CTS-V', 'CTS4dr', 'CX-7FWD', 'CX-9AWD', 'CX-9FWD', 'CX-9Grand', 'CX-9Touring', 'Caliber4dr', 'Camaro2dr', 'CamaroConvertible', 'CamaroCoupe', 'Camry', 'Camry4dr', 'CamryBase', 'CamryL', 'CamryLE', 'CamrySE', 'CamryXLE', 'Canyon2WD', 'Canyon4WD', 'CanyonCrew', 'CanyonExtended', 'CayenneAWD', 'Cayman2dr', 'Challenger2dr', 'ChallengerR/T', 'Charger4dr', 'ChargerSE', 'ChargerSXT', 'CherokeeLimited', 'CherokeeSport', 'Civic', 'CivicEX', 'CivicEX-L', 'CivicLX', 'CivicSi', 'Cobalt2dr', 'Cobalt4dr', 'Colorado2WD', 'Colorado4WD', 'ColoradoCrew', 'ColoradoExtended', 'Compass4WD', 'CompassLatitude', 'CompassLimited', 'CompassSport', 'Continental', 'Cooper', 'Corolla4dr', 'CorollaL', 'CorollaLE', 'CorollaS', 'Corvette2dr', 'CorvetteConvertible', 'CorvetteCoupe', 'CruzeLT', 'CruzeSedan', 'DTS4dr', 'Dakota2WD', 'Dakota4WD', 'Durango2WD', 'Durango4dr', 'DurangoAWD', 'DurangoSXT', 'E-ClassE', 'E-ClassE320', 'E-ClassE350', 'ES', 'ESES', 'Eclipse3dr', 'Econoline', 'EdgeLimited', 'EdgeSE', 'EdgeSEL', 'EdgeSport', 'Elantra', 'Elantra4dr', 'ElantraLimited', 'Element2WD', 'Element4WD', 'EnclaveConvenience', 'EnclaveLeather', 'EnclavePremium', 'Eos2dr', 'EquinoxAWD', 'EquinoxFWD', 'Escalade', 'Escalade2WD', 'Escalade4dr', 'EscaladeAWD', 'Escape4WD', 'Escape4dr', 'EscapeFWD', 'EscapeLImited', 'EscapeLimited', 'EscapeS', 'EscapeSE', 'EscapeXLT', 'Excursion137"', 'Expedition', 'Expedition2WD', 'Expedition4WD', 'ExpeditionLimited', 'ExpeditionXLT', 'Explorer', 'Explorer4WD', 'Explorer4dr', 'ExplorerBase', 'ExplorerEddie', 'ExplorerFWD', 'ExplorerLimited', 'ExplorerXLT', 'Express', 'F-1502WD', 'F-1504WD', 'F-150FX2', 'F-150FX4', 'F-150King', 'F-150Lariat', 'F-150Limited', 'F-150Platinum', 'F-150STX', 'F-150SuperCrew', 'F-150XL', 'F-150XLT', 'F-250King', 'F-250Lariat', 'F-250XL', 'F-250XLT', 'F-350King', 'F-350Lariat', 'F-350XL', 'F-350XLT', 'FJ', 'FX35AWD', 'FiestaS', 'FiestaSE', 'FitSport', 'FlexLimited', 'FlexSE', 'FlexSEL', 'Focus4dr', 'Focus5dr', 'FocusS', 'FocusSE', 'FocusSEL', 'FocusST', 'FocusTitanium', 'Forester2.5X', 'Forester4dr', 'Forte', 'ForteEX', 'ForteLX', 'ForteSX', 'Frontier', 'Frontier2WD', 'Frontier4WD', 'Fusion4dr', 'FusionHybrid', 'FusionS', 'FusionSE', 'FusionSEL', 'G35', 'G37', 'G64dr', 'GLI4dr', 'GS', 'GSGS', 'GTI2dr', 'GTI4dr', 'GX', 'GXGX', 'Galant4dr', 'Genesis', 'Golf', 'Grand', 'Highlander', 'Highlander4WD', 'Highlander4dr', 'HighlanderBase', 'HighlanderFWD', 'HighlanderLimited', 'HighlanderSE', 'IS', 'ISIS', 'Impala4dr', 'ImpalaLS', 'ImpalaLT', 'Impreza', 'Impreza2.0i', 'ImprezaSport', 'Jetta', 'JourneyAWD', 'JourneyFWD', 'JourneySXT', 'LS', 'LSLS', 'LX', 'LXLX', 'LaCrosse4dr', 'LaCrosseAWD', 'LaCrosseFWD', 'Lancer4dr', 'Land', 'Legacy', 'Legacy2.5i', 'Legacy3.6R', 'Liberty4WD', 'LibertyLimited', 'LibertySport', 'Lucerne4dr', 'M-ClassML350', 'MDX4WD', 'MDXAWD', 'MKXAWD', 'MKXFWD', 'MKZ4dr', 'MX5', 'Malibu', 'Malibu1LT', 'Malibu4dr', 'MalibuLS', 'MalibuLT', 'Matrix5dr', 'Maxima4dr', 'Mazda34dr', 'Mazda35dr', 'Mazda64dr', 'Milan4dr', 'Model', 'Monte', 'Murano2WD', 'MuranoAWD', 'MuranoS', 'Mustang2dr', 'MustangBase', 'MustangDeluxe', 'MustangGT', 'MustangPremium', 'MustangShelby', 'Navigator', 'Navigator2WD', 'Navigator4WD', 'Navigator4dr', 'New', 'OdysseyEX', 'OdysseyEX-L', 'OdysseyLX', 'OdysseyTouring', 'Optima4dr', 'OptimaEX', 'OptimaLX', 'OptimaSX', 'Outback2.5i', 'Outback3.6R', 'Outlander', 'Outlander2WD', 'Outlander4WD', 'PT', 'PacificaLimited', 'PacificaTouring', 'Passat', 'Passat4dr', 'Pathfinder2WD', 'Pathfinder4WD', 'PathfinderS', 'PathfinderSE', 'Patriot4WD', 'PatriotLatitude', 'PatriotLimited', 'PatriotSport', 'Pilot2WD', 'Pilot4WD', 'PilotEX', 'PilotEX-L', 'PilotLX', 'PilotSE', 'PilotTouring', 'Prius', 'Prius5dr', 'PriusBase', 'PriusFive', 'PriusFour', 'PriusOne', 'PriusThree', 'PriusTwo', 'Q5quattro', 'Q7quattro', 'QX562WD', 'QX564WD', 'Quest4dr', 'RAV4', 'RAV44WD', 'RAV44dr', 'RAV4Base', 'RAV4FWD', 'RAV4LE', 'RAV4Limited', 'RAV4Sport', 'RAV4XLE', 'RDXAWD', 'RDXFWD', 'RX', 'RX-84dr', 'RXRX', 'Ram', 'Ranger2WD', 'Ranger4WD', 'RangerSuperCab', 'Regal4dr', 'RegalGS', 'RegalPremium', 'RegalTurbo', 'RidgelineRTL', 'RidgelineSport', 'RioLX', 'RogueFWD', 'Rover', 'S2000Manual', 'S44dr', 'S60T5', 'S804dr', 'SC', 'SL-ClassSL500', 'SLK-ClassSLK350', 'SRXLuxury', 'STS4dr', 'Santa', 'Savana', 'Sedona4dr', 'SedonaEX', 'SedonaLX', 'Sentra4dr', 'Sequoia4WD', 'Sequoia4dr', 'SequoiaLimited', 'SequoiaPlatinum', 'SequoiaSR5', 'Sienna5dr', 'SiennaLE', 'SiennaLimited', 'SiennaSE', 'SiennaXLE', 'Sierra', 'Silverado', 'Sonata4dr', 'SonataLimited', 'SonataSE', 'SonicHatch', 'SonicSedan', 'Sorento2WD', 'SorentoEX', 'SorentoLX', 'SorentoSX', 'Soul+', 'SoulBase', 'Sportage2WD', 'SportageAWD', 'SportageEX', 'SportageLX', 'SportageSX', 'Sprinter', 'Suburban2WD', 'Suburban4WD', 'Suburban4dr', 'Super', 'TL4dr', 'TLAutomatic', 'TSXAutomatic', 'TT2dr', 'Tacoma2WD', 'Tacoma4WD', 'TacomaBase', 'TacomaPreRunner', 'Tahoe2WD', 'Tahoe4WD', 'Tahoe4dr', 'TahoeLS', 'TahoeLT', 'Taurus4dr', 'TaurusLimited', 'TaurusSE', 'TaurusSEL', 'TaurusSHO', 'TerrainAWD', 'TerrainFWD', 'Tiguan2WD', 'TiguanS', 'TiguanSE', 'TiguanSEL', 'Titan', 'Titan2WD', 'Titan4WD', 'Touareg4dr', 'Town', 'Transit', 'TraverseAWD', 'TraverseFWD', 'TucsonAWD', 'TucsonFWD', 'TucsonLimited', 'Tundra', 'Tundra2WD', 'Tundra4WD', 'TundraBase', 'TundraLimited', 'TundraSR5', 'VeracruzAWD', 'VeracruzFWD', 'Versa4dr', 'Versa5dr', 'Vibe4dr', 'WRXBase', 'WRXLimited', 'WRXPremium', 'WRXSTI', 'Wrangler', 'Wrangler2dr', 'Wrangler4WD', 'WranglerRubicon', 'WranglerSahara', 'WranglerSport', 'WranglerX', 'X1xDrive28i', 'X3AWD', 'X3xDrive28i', 'X5AWD', 'X5xDrive35i', 'XC60AWD', 'XC60FWD', 'XC60T6', 'XC704dr', 'XC90AWD', 'XC90FWD', 'XC90T6', 'XF4dr', 'XJ4dr', 'XK2dr', 'Xterra2WD', 'Xterra4WD', 'Xterra4dr', 'Yaris', 'Yaris4dr', 'YarisBase', 'YarisLE', 'Yukon', 'Yukon2WD', 'Yukon4WD', 'Yukon4dr', 'tC2dr', 'xB5dr', 'xD5dr']



if(st.button('predict')):
    test_state=[0]*len(state_arr)
    test_make=[0]*len(make_arr)
    test_model=[0]*len(model_arr)
    
    state_index=state_arr.index(State)
    make_index=make_arr.index(make)
    model_index=model_arr.index(model)
    
    test_state[state_index]=1
    test_make[make_index]=1
    test_model[model_index]=1
    
    final_arr=[year,mileage]+test_state+test_make+test_model
    values=[final_arr]
    pred=reg.predict(values)
    if(pred>5000):
        st.success(math.floor(pred))
    else:
        st.error('Give Correct Values')
 
        
     

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
