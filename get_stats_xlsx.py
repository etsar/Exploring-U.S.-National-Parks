# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:52:25 2023

@author: entsa
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.common.exceptions import StaleElementReferenceException


parks = [{"Text":"Abraham Lincoln Birthplace NHP (ABLI)","Value":"ABLI"},{"Text":"Acadia NP (ACAD)","Value":"ACAD"},{"Text":"Adams NHP (ADAM)","Value":"ADAM"},{"Text":"African Burial Ground NM (AFBG)","Value":"AFBG"},{"Text":"Agate Fossil Beds NM (AGFO)","Value":"AGFO"},{"Text":"Alagnak Wild River (ALAG)","Value":"ALAG"},{"Text":"Alibates Flint Quarries NM (ALFL)","Value":"ALFL"},{"Text":"Allegheny Portage Railroad NHS (ALPO)","Value":"ALPO"},{"Text":"Amistad NRA (AMIS)","Value":"AMIS"},{"Text":"Andersonville NHS (ANDE)","Value":"ANDE"},{"Text":"Andrew Johnson NHS (ANJO)","Value":"ANJO"},{"Text":"Aniakchak NM & PRES (ANIA)","Value":"ANIA"},{"Text":"Antietam NB (ANTI)","Value":"ANTI"},{"Text":"Apostle Islands NL (APIS)","Value":"APIS"},{"Text":"Appomattox Court House NHP (APCO)","Value":"APCO"},{"Text":"Arches NP (ARCH)","Value":"ARCH"},{"Text":"Arkansas Post NMEM (ARPO)","Value":"ARPO"},{"Text":"Arlington House The R.E. Lee MEM (ARHO)","Value":"ARHO"},{"Text":"Assateague Island NS (ASIS)","Value":"ASIS"},{"Text":"Aztec Ruins NM (AZRU)","Value":"AZRU"},{"Text":"Badlands NP (BADL)","Value":"BADL"},{"Text":"Bandelier NM (BAND)","Value":"BAND"},{"Text":"Belmont-Paul Women's Equality NM (BEPA)","Value":"BEPA"},{"Text":"Bent's Old Fort NHS (BEOL)","Value":"BEOL"},{"Text":"Bering Land Bridge NPRES (BELA)","Value":"BELA"},{"Text":"Big Bend NP (BIBE)","Value":"BIBE"},{"Text":"Big Cypress NPRES (BICY)","Value":"BICY"},{"Text":"Big Hole NB (BIHO)","Value":"BIHO"},{"Text":"Big South Fork NRRA (BISO)","Value":"BISO"},{"Text":"Big Thicket NPRES (BITH)","Value":"BITH"},{"Text":"Bighorn Canyon NRA (BICA)","Value":"BICA"},{"Text":"Birmingham Civil Rights NM (BICR)","Value":"BICR"},{"Text":"Biscayne NP (BISC)","Value":"BISC"},{"Text":"Black Canyon of the Gunnison NP (BLCA)","Value":"BLCA"},{"Text":"Blackstone River Valley NHP (BLRV)","Value":"BLRV"},{"Text":"Blue Ridge PKWY (BLRI)","Value":"BLRI"},{"Text":"Bluestone NSR (BLUE)","Value":"BLUE"},{"Text":"Booker T. Washington NM (BOWA)","Value":"BOWA"},{"Text":"Boston African American NHS (BOAF)","Value":"BOAF"},{"Text":"Boston Harbor Islands NRA (BOHA)","Value":"BOHA"},{"Text":"Boston NHP (BOST)","Value":"BOST"},{"Text":"Brices Cross Roads (BRCR)","Value":"BRCR"},{"Text":"Brown v. Board of Education NHP (BRVB)","Value":"BRVB"},{"Text":"Bryce Canyon NP (BRCA)","Value":"BRCA"},{"Text":"Buck Island Reef NM (BUIS)","Value":"BUIS"},{"Text":"Buffalo NR (BUFF)","Value":"BUFF"},{"Text":"Cabrillo NM (CABR)","Value":"CABR"},{"Text":"Camp Nelson NM (CANE)","Value":"CANE"},{"Text":"Canaveral NS (CANA)","Value":"CANA"},{"Text":"Cane River Creole NHP (CARI)","Value":"CARI"},{"Text":"Canyon de Chelly NM (CACH)","Value":"CACH"},{"Text":"Canyonlands NP (CANY)","Value":"CANY"},{"Text":"Cape Cod NS (CACO)","Value":"CACO"},{"Text":"Cape Hatteras NS (CAHA)","Value":"CAHA"},{"Text":"Cape Krusenstern NM (CAKR)","Value":"CAKR"},{"Text":"Cape Lookout NS (CALO)","Value":"CALO"},{"Text":"Capitol Reef NP (CARE)","Value":"CARE"},{"Text":"Capulin Volcano NM (CAVO)","Value":"CAVO"},{"Text":"Carl Sandburg Home NHS (CARL)","Value":"CARL"},{"Text":"Carlsbad Caverns NP (CAVE)","Value":"CAVE"},{"Text":"Carter G. Woodson Home NHS (CAWO)","Value":"CAWO"},{"Text":"Casa Grande Ruins NM (CAGR)","Value":"CAGR"},{"Text":"Castillo de San Marcos NM (CASA)","Value":"CASA"},{"Text":"Castle Clinton NM (CACL)","Value":"CACL"},{"Text":"Castle Mountains NM (CAMO)","Value":"CAMO"},{"Text":"Catoctin Mountain Park (CATO)","Value":"CATO"},{"Text":"Cedar Breaks NM (CEBR)","Value":"CEBR"},{"Text":"Cedar Creek and Belle Grove (CEBE)","Value":"CEBE"},{"Text":"Cesar E. Chavez NM (CECH)","Value":"CECH"},{"Text":"Chaco Culture NHP (CHCU)","Value":"CHCU"},{"Text":"Chamizal NMEM (CHAM)","Value":"CHAM"},{"Text":"Channel Islands NP (CHIS)","Value":"CHIS"},{"Text":"Charles Pinckney NHS (CHPI)","Value":"CHPI"},{"Text":"Charles Young Buffalo Soldiers NM (CHYO)","Value":"CHYO"},{"Text":"Chattahoochee River NRA (CHAT)","Value":"CHAT"},{"Text":"Chesapeake & Ohio Canal NHP (CHOH)","Value":"CHOH"},{"Text":"Chickamauga & Chattanooga NMP (CHCH)","Value":"CHCH"},{"Text":"Chickasaw NRA (CHIC)","Value":"CHIC"},{"Text":"Chiricahua NM (CHIR)","Value":"CHIR"},{"Text":"Christiansted NHS (CHRI)","Value":"CHRI"},{"Text":"City of Rocks NRES (CIRO)","Value":"CIRO"},{"Text":"Clara Barton NHS (CLBA)","Value":"CLBA"},{"Text":"Colonial NHP (COLO)","Value":"COLO"},{"Text":"Colorado NM (COLM)","Value":"COLM"},{"Text":"Congaree NP (CONG)","Value":"CONG"},{"Text":"Coronado NMEM (CORO)","Value":"CORO"},{"Text":"Cowpens NB (COWP)","Value":"COWP"},{"Text":"Crater Lake NP (CRLA)","Value":"CRLA"},{"Text":"Craters of the Moon NM & PRES (CRMO)","Value":"CRMO"},{"Text":"Cumberland Gap NHP (CUGA)","Value":"CUGA"},{"Text":"Cumberland Island NS (CUIS)","Value":"CUIS"},{"Text":"Curecanti NRA (CURE)","Value":"CURE"},{"Text":"Cuyahoga Valley NP (CUVA)","Value":"CUVA"},{"Text":"Dayton Aviation Heritage NHP (DAAV)","Value":"DAAV"},{"Text":"De Soto NMEM (DESO)","Value":"DESO"},{"Text":"Death Valley NP (DEVA)","Value":"DEVA"},{"Text":"Delaware Water Gap NRA (DEWA)","Value":"DEWA"},{"Text":"Denali NP & PRES (DENA)","Value":"DENA"},{"Text":"Devils Postpile NM (DEPO)","Value":"DEPO"},{"Text":"Devils Tower NM (DETO)","Value":"DETO"},{"Text":"Dinosaur NM (DINO)","Value":"DINO"},{"Text":"Dry Tortugas NP (DRTO)","Value":"DRTO"},{"Text":"Dwight D. Eisenhower MEM (DDEM)","Value":"DDEM"},{"Text":"Ebey's Landing (EBLA)","Value":"EBLA"},{"Text":"Edgar Allan Poe NHS (EDAL)","Value":"EDAL"},{"Text":"Effigy Mounds NM (EFMO)","Value":"EFMO"},{"Text":"Eisenhower NHS (EISE)","Value":"EISE"},{"Text":"El Malpais NM (ELMA)","Value":"ELMA"},{"Text":"El Morro NM (ELMO)","Value":"ELMO"},{"Text":"Eleanor Roosevelt NHS (ELRO)","Value":"ELRO"},{"Text":"Emmett Till and Mamie Till-Mobley NM (TILL)","Value":"TILL"},{"Text":"Eugene O'Neill NHS (EUON)","Value":"EUON"},{"Text":"Everglades NP (EVER)","Value":"EVER"},{"Text":"Federal Hall NMEM (FEHA)","Value":"FEHA"},{"Text":"Fire Island NS (FIIS)","Value":"FIIS"},{"Text":"First Ladies NHS (FILA)","Value":"FILA"},{"Text":"First State NHP (FRST)","Value":"FRST"},{"Text":"Flight 93 NMEM (FLNI)","Value":"FLNI"},{"Text":"Florissant Fossil Beds NM (FLFO)","Value":"FLFO"},{"Text":"Ford's Theatre NHS (FOTH)","Value":"FOTH"},{"Text":"Fort Bowie NHS (FOBO)","Value":"FOBO"},{"Text":"Fort Caroline NMEM (FOCA)","Value":"FOCA"},{"Text":"Fort Davis NHS (FODA)","Value":"FODA"},{"Text":"Fort Donelson NB (FODO)","Value":"FODO"},{"Text":"Fort Frederica NM (FOFR)","Value":"FOFR"},{"Text":"Fort Laramie NHS (FOLA)","Value":"FOLA"},{"Text":"Fort Larned NHS (FOLS)","Value":"FOLS"},{"Text":"Fort Matanzas NM (FOMA)","Value":"FOMA"},{"Text":"Fort McHenry NM & HS (FOMC)","Value":"FOMC"},{"Text":"Fort Monroe NM (FOMR)","Value":"FOMR"},{"Text":"Fort Necessity NB (FONE)","Value":"FONE"},{"Text":"Fort Point NHS (FOPO)","Value":"FOPO"},{"Text":"Fort Pulaski NM (FOPU)","Value":"FOPU"},{"Text":"Fort Raleigh NHS (FORA)","Value":"FORA"},{"Text":"Fort Scott NHS (FOSC)","Value":"FOSC"},{"Text":"Fort Smith NHS (FOSM)","Value":"FOSM"},{"Text":"Fort Stanwix NM (FOST)","Value":"FOST"},{"Text":"Fort Sumter and Fort Moultrie NHP (FOSU)","Value":"FOSU"},{"Text":"Fort Union NM (FOUN)","Value":"FOUN"},{"Text":"Fort Union Trading Post NHS (FOUS)","Value":"FOUS"},{"Text":"Fort Vancouver NHS (FOVA)","Value":"FOVA"},{"Text":"Fort Washington Park (FOWA)","Value":"FOWA"},{"Text":"Fossil Butte NM (FOBU)","Value":"FOBU"},{"Text":"Franklin Delano Roosevelt MEM (FRDE)","Value":"FRDE"},{"Text":"Frederick Douglass NHS (FRDO)","Value":"FRDO"},{"Text":"Frederick Law Olmsted NHS (FRLA)","Value":"FRLA"},{"Text":"Fredericksburg & Spotsylvania NMP (FRSP)","Value":"FRSP"},{"Text":"Freedom Riders NM (FRRI)","Value":"FRRI"},{"Text":"Friendship Hill NHS (FRHI)","Value":"FRHI"},{"Text":"Gates of the Arctic NP & PRES (GAAR)","Value":"GAAR"},{"Text":"Gateway Arch NP (JEFF)","Value":"JEFF"},{"Text":"Gateway NRA (GATE)","Value":"GATE"},{"Text":"Gauley River NRA (GARI)","Value":"GARI"},{"Text":"General Grant NMEM (GEGR)","Value":"GEGR"},{"Text":"George Rogers Clark NHP (GERO)","Value":"GERO"},{"Text":"George Washington Birthplace NM (GEWA)","Value":"GEWA"},{"Text":"George Washington Carver NM (GWCA)","Value":"GWCA"},{"Text":"George Washington MEM PKWY (GWMP)","Value":"GWMP"},{"Text":"Gettysburg NMP (GETT)","Value":"GETT"},{"Text":"Gila Cliff Dwellings NM (GICL)","Value":"GICL"},{"Text":"Glacier Bay NP & PRES (GLBA)","Value":"GLBA"},{"Text":"Glacier NP (GLAC)","Value":"GLAC"},{"Text":"Glen Canyon NRA (GLCA)","Value":"GLCA"},{"Text":"Golden Gate NRA (GOGA)","Value":"GOGA"},{"Text":"Golden Spike NHP (GOSP)","Value":"GOSP"},{"Text":"Governors Island NM (GOIS)","Value":"GOIS"},{"Text":"Grand Canyon NP (GRCA)","Value":"GRCA"},{"Text":"Grand Portage NM (GRPO)","Value":"GRPO"},{"Text":"Grand Teton NP (GRTE)","Value":"GRTE"},{"Text":"Grant-Kohrs Ranch NHS (GRKO)","Value":"GRKO"},{"Text":"Great Basin NP (GRBA)","Value":"GRBA"},{"Text":"Great Sand Dunes NP & PRES (GRSA)","Value":"GRSA"},{"Text":"Great Smoky Mountains NP (GRSM)","Value":"GRSM"},{"Text":"Greenbelt Park (GREE)","Value":"GREE"},{"Text":"Guadalupe Mountains NP (GUMO)","Value":"GUMO"},{"Text":"Guilford Courthouse NMP (GUCO)","Value":"GUCO"},{"Text":"Gulf Islands NS (GUIS)","Value":"GUIS"},{"Text":"Hagerman Fossil Beds NM (HAFO)","Value":"HAFO"},{"Text":"Haleakala NP (HALE)","Value":"HALE"},{"Text":"Hamilton Grange NMEM (HAGR)","Value":"HAGR"},{"Text":"Hampton NHS (HAMP)","Value":"HAMP"},{"Text":"Harpers Ferry NHP (HAFE)","Value":"HAFE"},{"Text":"Harriet Tubman NHP (HART)","Value":"HART"},{"Text":"Harriet Tubman Underground Railroad NHP (HATU)","Value":"HATU"},{"Text":"Harry S Truman NHS (HSTR)","Value":"HSTR"},{"Text":"Hawaii Volcanoes NP (HAVO)","Value":"HAVO"},{"Text":"Herbert Hoover NHS (HEHO)","Value":"HEHO"},{"Text":"Home of Franklin D. Roosevelt NHS (HOFR)","Value":"HOFR"},{"Text":"Homestead NHP (HOME)","Value":"HOME"},{"Text":"Honouliuli NHS (HONO)","Value":"HONO"},{"Text":"Hopewell Culture NHP (HOCU)","Value":"HOCU"},{"Text":"Hopewell Furnace NHS (HOFU)","Value":"HOFU"},{"Text":"Horseshoe Bend NMP (HOBE)","Value":"HOBE"},{"Text":"Hot Springs NP (HOSP)","Value":"HOSP"},{"Text":"Hovenweep NM (HOVE)","Value":"HOVE"},{"Text":"Hubbell Trading Post NHS (HUTR)","Value":"HUTR"},{"Text":"Independence NHP (INDE)","Value":"INDE"},{"Text":"Indiana Dunes NP (INDU)","Value":"INDU"},{"Text":"Isle Royale NP (ISRO)","Value":"ISRO"},{"Text":"James A. Garfield NHS (JAGA)","Value":"JAGA"},{"Text":"Jean Lafitte NHP & PRES (JELA)","Value":"JELA"},{"Text":"Jewel Cave NM (JECA)","Value":"JECA"},{"Text":"Jimmy Carter NHP (JICA)","Value":"JICA"},{"Text":"John D. Rockefeller, Jr. MEM PKWY (JODR)","Value":"JODR"},{"Text":"John Day Fossil Beds NM (JODA)","Value":"JODA"},{"Text":"John F. Kennedy Center For Pa (JOFK)","Value":"JOFK"},{"Text":"John F. Kennedy NHS (JOFI)","Value":"JOFI"},{"Text":"John Muir NHS (JOMU)","Value":"JOMU"},{"Text":"Johnstown Flood NMEM (JOFL)","Value":"JOFL"},{"Text":"Joshua Tree NP (JOTR)","Value":"JOTR"},{"Text":"Kalaupapa NHP (KALA)","Value":"KALA"},{"Text":"Kaloko Honokohau NHP (KAHO)","Value":"KAHO"},{"Text":"Katahdin Woods and Waters NM (KAWW)","Value":"KAWW"},{"Text":"Katmai NP & PRES (KATM)","Value":"KATM"},{"Text":"Kenai Fjords NP (KEFJ)","Value":"KEFJ"},{"Text":"Kennesaw Mountain NBP (KEMO)","Value":"KEMO"},{"Text":"Keweenaw NHP (KEWE)","Value":"KEWE"},{"Text":"Kings Canyon NP (KICA)","Value":"KICA"},{"Text":"Kings Mountain NMP (KIMO)","Value":"KIMO"},{"Text":"Klondike Gold Rush NHP Alaska (KLGO)","Value":"KLGO"},{"Text":"Klondike Gold Rush NHP Seattle (KLSE)","Value":"KLSE"},{"Text":"Knife River Indian Villages NHS (KNRI)","Value":"KNRI"},{"Text":"Kobuk Valley NP (KOVA)","Value":"KOVA"},{"Text":"Korean War Veterans Memorial (KOWA)","Value":"KOWA"},{"Text":"Lake Chelan NRA (LACH)","Value":"LACH"},{"Text":"Lake Clark NP & PRES (LACL)","Value":"LACL"},{"Text":"Lake Mead NRA (LAKE)","Value":"LAKE"},{"Text":"Lake Meredith NRA (LAMR)","Value":"LAMR"},{"Text":"Lake Roosevelt NRA (LARO)","Value":"LARO"},{"Text":"Lassen Volcanic NP (LAVO)","Value":"LAVO"},{"Text":"Lava Beds NM (LABE)","Value":"LABE"},{"Text":"LBJ Memorial Grove on the Potomac (LYBA)","Value":"LYBA"},{"Text":"Lewis & Clark NHP (LEWI)","Value":"LEWI"},{"Text":"Lincoln Boyhood NMEM (LIBO)","Value":"LIBO"},{"Text":"Lincoln Home NHS (LIHO)","Value":"LIHO"},{"Text":"Lincoln Memorial (LINC)","Value":"LINC"},{"Text":"Little Bighorn Battlefield NM (LIBI)","Value":"LIBI"},{"Text":"Little River Canyon NPRES (LIRI)","Value":"LIRI"},{"Text":"Little Rock Central High School NHS (CHSC)","Value":"CHSC"},{"Text":"Longfellow House Washington's HQ NHS (LONG)","Value":"LONG"},{"Text":"Lowell NHP (LOWE)","Value":"LOWE"},{"Text":"Lyndon B. Johnson NHP (LYJO)","Value":"LYJO"},{"Text":"Maggie L. Walker NHS (MAWA)","Value":"MAWA"},{"Text":"Mammoth Cave NP (MACA)","Value":"MACA"},{"Text":"Manassas NBP (MANA)","Value":"MANA"},{"Text":"Manhattan Project NHP (MAPR)","Value":"MAPR"},{"Text":"Manzanar NHS (MANZ)","Value":"MANZ"},{"Text":"Marsh-Billings-Rockefeller NHP (MABI)","Value":"MABI"},{"Text":"Martin Luther King, Jr. Memorial (MLKM)","Value":"MLKM"},{"Text":"Martin Luther King, Jr. NHP (MALU)","Value":"MALU"},{"Text":"Martin Van Buren NHS (MAVA)","Value":"MAVA"},{"Text":"Mary McLeod Bethune Council House NHS (MABE)","Value":"MABE"},{"Text":"Medgar and Myrlie Evers Home NM (MEMY)","Value":"MEMY"},{"Text":"Mesa Verde NP (MEVE)","Value":"MEVE"},{"Text":"Mill Springs Battlefield NM (MISP)","Value":"MISP"},{"Text":"Minidoka NHS (MIIN)","Value":"MIIN"},{"Text":"Minute Man NHP (MIMA)","Value":"MIMA"},{"Text":"Minuteman Missile NHS (MIMI)","Value":"MIMI"},{"Text":"Mississippi NRRA (MISS)","Value":"MISS"},{"Text":"Missouri NRR (MNRR)","Value":"MNRR"},{"Text":"Mojave NPRES (MOJA)","Value":"MOJA"},{"Text":"Monocacy NB (MONO)","Value":"MONO"},{"Text":"Montezuma Castle NM (MOCA)","Value":"MOCA"},{"Text":"Moores Creek NB (MOCR)","Value":"MOCR"},{"Text":"Morristown NHP (MORR)","Value":"MORR"},{"Text":"Mount Rainier NP (MORA)","Value":"MORA"},{"Text":"Mount Rushmore NMEM (MORU)","Value":"MORU"},{"Text":"Muir Woods NM (MUWO)","Value":"MUWO"},{"Text":"Natchez NHP (NATC)","Value":"NATC"},{"Text":"Natchez Trace PKWY (NATR)","Value":"NATR"},{"Text":"National Capital Parks Central (NCPC)","Value":"NCPC"},{"Text":"National Capital Parks Combined (NACA)","Value":"NACA"},{"Text":"National Capital Parks East (NCPE)","Value":"NCPE"},{"Text":"National Park of American Samoa (NPSA)","Value":"NPSA"},{"Text":"National Visitor Center (NAVC)","Value":"NAVC"},{"Text":"Natural Bridges NM (NABR)","Value":"NABR"},{"Text":"Navajo NM (NAVA)","Value":"NAVA"},{"Text":"New Bedford Whaling NHP (NEBE)","Value":"NEBE"},{"Text":"New Orleans Jazz NHP (JAZZ)","Value":"JAZZ"},{"Text":"New Philadelphia NHS (NEPH)","Value":"NEPH"},{"Text":"New River Gorge NP & PRES (NERI)","Value":"NERI"},{"Text":"Nez Perce NHP (NEPE)","Value":"NEPE"},{"Text":"Nicodemus NHS (NICO)","Value":"NICO"},{"Text":"Ninety Six NHS (NISI)","Value":"NISI"},{"Text":"Niobrara NSR (NIOB)","Value":"NIOB"},{"Text":"Noatak NPRES (NOAT)","Value":"NOAT"},{"Text":"North Cascades NP (NOCA)","Value":"NOCA"},{"Text":"Obed W&SR (OBRI)","Value":"OBRI"},{"Text":"Ocmulgee Mounds NHP (OCMU)","Value":"OCMU"},{"Text":"Oklahoma City NMEM (OKCI)","Value":"OKCI"},{"Text":"Olympic NP (OLYM)","Value":"OLYM"},{"Text":"Oregon Caves NM & PRES (ORCA)","Value":"ORCA"},{"Text":"Organ Pipe Cactus NM (ORPI)","Value":"ORPI"},{"Text":"Ozark NSR (OZAR)","Value":"OZAR"},{"Text":"Padre Island NS (PAIS)","Value":"PAIS"},{"Text":"Palo Alto Battlefield NHP (PAAL)","Value":"PAAL"},{"Text":"Paterson Great Falls NHP (PAGR)","Value":"PAGR"},{"Text":"Pea Ridge NMP (PERI)","Value":"PERI"},{"Text":"Pearl Harbor NMEM (PERL)","Value":"PERL"},{"Text":"Pecos NHP (PECO)","Value":"PECO"},{"Text":"Pennsylvania Avenue NHS (PAAV)","Value":"PAAV"},{"Text":"Perry's Victory & Intl. Peace MEM (PEVI)","Value":"PEVI"},{"Text":"Petersburg NB (PETE)","Value":"PETE"},{"Text":"Petrified Forest NP (PEFO)","Value":"PEFO"},{"Text":"Petroglyph NM (PETR)","Value":"PETR"},{"Text":"Pictured Rocks NL (PIRO)","Value":"PIRO"},{"Text":"Pinnacles NP (PINN)","Value":"PINN"},{"Text":"Pipe Spring NM (PISP)","Value":"PISP"},{"Text":"Pipestone NM (PIPE)","Value":"PIPE"},{"Text":"Piscataway Park (PISC)","Value":"PISC"},{"Text":"Point Reyes NS (PORE)","Value":"PORE"},{"Text":"Port Chicago Naval Magazine NMEM (POCH)","Value":"POCH"},{"Text":"President W.J. Clinton Birthplace Home NHS (WICL)","Value":"WICL"},{"Text":"President's Park (PRPA)","Value":"PRPA"},{"Text":"Prince William Forest Park (PRWI)","Value":"PRWI"},{"Text":"Pullman NHP (PULL)","Value":"PULL"},{"Text":"Pu'uhonua o Honaunau NHP (PUHO)","Value":"PUHO"},{"Text":"Pu'ukohola Heiau NHS (PUHE)","Value":"PUHE"},{"Text":"Rainbow Bridge NM (RABR)","Value":"RABR"},{"Text":"Reconstruction Era NHP (REER)","Value":"REER"},{"Text":"Redwood NP (REDW)","Value":"REDW"},{"Text":"Richmond NBP (RICH)","Value":"RICH"},{"Text":"Rio Grande W&SR (RIGR)","Value":"RIGR"},{"Text":"River Raisin NBP (RIRA)","Value":"RIRA"},{"Text":"Rock Creek Park (ROCR)","Value":"ROCR"},{"Text":"Rocky Mountain NP (ROMO)","Value":"ROMO"},{"Text":"Roger Williams NMEM (ROWI)","Value":"ROWI"},{"Text":"Rosie The Riveter WWII Home Front NHP (RORI)","Value":"RORI"},{"Text":"Ross Lake NRA (ROLA)","Value":"ROLA"},{"Text":"Russell Cave NM (RUCA)","Value":"RUCA"},{"Text":"Sagamore Hill NHS (SAHI)","Value":"SAHI"},{"Text":"Saguaro NP (SAGU)","Value":"SAGU"},{"Text":"Saint Croix Island IHS (SACR)","Value":"SACR"},{"Text":"Saint Croix NSR (SACN)","Value":"SACN"},{"Text":"Saint Paul's Church NHS (SAPA)","Value":"SAPA"},{"Text":"Saint-Gaudens NHP (SAGA)","Value":"SAGA"},{"Text":"Salem Maritime NHS (SAMA)","Value":"SAMA"},{"Text":"Salinas Pueblo Missions NM (SAPU)","Value":"SAPU"},{"Text":"Salt River Bay NHP & Ecological Pres (SARI)","Value":"SARI"},{"Text":"San Antonio Missions NHP (SAAN)","Value":"SAAN"},{"Text":"San Francisco Maritime NHP (SAFR)","Value":"SAFR"},{"Text":"San Juan Island NHP (SAJH)","Value":"SAJH"},{"Text":"San Juan NHS (SAJU)","Value":"SAJU"},{"Text":"Sand Creek Massacre NHS (SAND)","Value":"SAND"},{"Text":"Santa Monica Mountains NRA (SAMO)","Value":"SAMO"},{"Text":"Saratoga NHP (SARA)","Value":"SARA"},{"Text":"Saugus Iron Works NHS (SAIR)","Value":"SAIR"},{"Text":"Scotts Bluff NM (SCBL)","Value":"SCBL"},{"Text":"Sequoia NP (SEQU)","Value":"SEQU"},{"Text":"Shenandoah NP (SHEN)","Value":"SHEN"},{"Text":"Shiloh NMP (SHIL)","Value":"SHIL"},{"Text":"Sitka NHP (SITK)","Value":"SITK"},{"Text":"Sleeping Bear Dunes NL (SLBE)","Value":"SLBE"},{"Text":"Springfield Armory NHS (SPAR)","Value":"SPAR"},{"Text":"Statue of Liberty NM (STLI)","Value":"STLI"},{"Text":"Ste. Genevieve NHP (STGE)","Value":"STGE"},{"Text":"Steamtown NHS (STEA)","Value":"STEA"},{"Text":"Stones River NB (STRI)","Value":"STRI"},{"Text":"Stonewall NM (STON)","Value":"STON"},{"Text":"Sunset Crater Volcano NM (SUCR)","Value":"SUCR"},{"Text":"Tallgrass Prairie NPRES (TAPR)","Value":"TAPR"},{"Text":"Thaddeus Kosciuszko NMEM (THKO)","Value":"THKO"},{"Text":"Theodore Roosevelt Birthplace NHS (THRB)","Value":"THRB"},{"Text":"Theodore Roosevelt Inaugural NHS (THRI)","Value":"THRI"},{"Text":"Theodore Roosevelt Island (THIS)","Value":"THIS"},{"Text":"Theodore Roosevelt NP (THRO)","Value":"THRO"},{"Text":"Thomas Edison NHP (EDIS)","Value":"EDIS"},{"Text":"Thomas Jefferson MEM (JEFM)","Value":"JEFM"},{"Text":"Thomas Stone NHS (THST)","Value":"THST"},{"Text":"Timpanogos Cave NM (TICA)","Value":"TICA"},{"Text":"Timucuan EHP (TIMU)","Value":"TIMU"},{"Text":"Tonto NM (TONT)","Value":"TONT"},{"Text":"Tule Lake NM (TULE)","Value":"TULE"},{"Text":"Tule Springs Fossil Beds NM (TUSK)","Value":"TUSK"},{"Text":"Tumacacori NHP (TUMA)","Value":"TUMA"},{"Text":"Tupelo NBS (TUPE)","Value":"TUPE"},{"Text":"Tuskegee Airmen NHS (TUAI)","Value":"TUAI"},{"Text":"Tuskegee Institute NHS (TUIN)","Value":"TUIN"},{"Text":"Tuzigoot NM (TUZI)","Value":"TUZI"},{"Text":"Ulysses S. Grant NHS (ULSG)","Value":"ULSG"},{"Text":"Upper Delaware S&RR (UPDE)","Value":"UPDE"},{"Text":"Valles Caldera NPRES (VALL)","Value":"VALL"},{"Text":"Valley Forge NHP (VAFO)","Value":"VAFO"},{"Text":"Vanderbilt Mansion NHS (VAMA)","Value":"VAMA"},{"Text":"Vicksburg NMP (VICK)","Value":"VICK"},{"Text":"Vietnam Veterans MEM (VIVE)","Value":"VIVE"},{"Text":"Virgin Islands NP (VIIS)","Value":"VIIS"},{"Text":"Voyageurs NP (VOYA)","Value":"VOYA"},{"Text":"Waco Mammoth NM (WACO)","Value":"WACO"},{"Text":"Walnut Canyon NM (WACA)","Value":"WACA"},{"Text":"War in the Pacific NHP (WAPA)","Value":"WAPA"},{"Text":"Washington Monument (WAMO)","Value":"WAMO"},{"Text":"Washita Battlefield NHS (WABA)","Value":"WABA"},{"Text":"Weir Farm NHP (WEFA)","Value":"WEFA"},{"Text":"Whiskeytown NRA (WHIS)","Value":"WHIS"},{"Text":"White House (WHHO)","Value":"WHHO"},{"Text":"White Sands NP (WHSA)","Value":"WHSA"},{"Text":"Whitman Mission NHS (WHMI)","Value":"WHMI"},{"Text":"William Howard Taft NHS (WIHO)","Value":"WIHO"},{"Text":"Wilson's Creek NB (WICR)","Value":"WICR"},{"Text":"Wind Cave NP (WICA)","Value":"WICA"},{"Text":"Wolf Trap NP for the Performing Arts (WOTR)","Value":"WOTR"},{"Text":"Women's Rights NHP (WORI)","Value":"WORI"},{"Text":"World War I Memorial (WWIM)","Value":"WWIM"},{"Text":"World War II Memorial (WWII)","Value":"WWII"},{"Text":"Wrangell-St. Elias NP & PRES (WRST)","Value":"WRST"},{"Text":"Wright Brothers NMEM (WRBR)","Value":"WRBR"},{"Text":"Wupatki NM (WUPA)","Value":"WUPA"},{"Text":"Yellowstone NP (YELL)","Value":"YELL"},{"Text":"Yosemite NP (YOSE)","Value":"YOSE"},{"Text":"Yukon-Charley Rivers NPRES (YUCH)","Value":"YUCH"},{"Text":"Zion NP (ZION)","Value":"ZION"}]
selected_parks = [park for park in parks if 'NP' in park["Text"] and "NPRES" not in park["Text"] and "Performing" not in park["Text"]]
# last_downloaded_park_key = "DRTO"
national_parks = {}
for park in selected_parks:
    national_parks[park['Text']] = park['Value']
    
# national_parks = {'Acadia NP (ACAD)': 'ACAD', 'Arches NP (ARCH)': 'ARCH', 'Badlands NP (BADL)': 'BADL'}

def retry_until_clickable(driver, by, value, max_retries=5):
    for retry in range(max_retries):
        try:
            element = driver.find_element(by, value)
            if element.is_displayed() and element.is_enabled():
                element.click()
                return
        except StaleElementReferenceException:
            pass

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

for park_key in national_parks.values():
    # if park_key <= last_downloaded_park_key:
    #     continue
    print(f"Park key: {park_key}")
    url = f"https://irma.nps.gov/Stats/SSRSReports/Park%20Specific%20Reports/Summary%20of%20Visitor%20Use%20By%20Month%20and%20Year%20(1979%20-%20Last%20Calendar%20Year)?Park={park_key}"
    driver.get(url)
    
    # Switch to the iframe
    frame = driver.find_element(By.XPATH, '/html/body/iframe')
    driver.switch_to.frame(frame)
    
    # Find and click Select year(s) dropdown menu
    e = driver.find_element(By.XPATH, '//*[@id="ReportViewer_ctl04_ctl05_ddDropDownButton"]')
    time.sleep(.5)
    e.click()
    
    # Select all years
    e = driver.find_element(By.XPATH, '//*[@id="ReportViewer_ctl04_ctl05_divDropDown_ctl00"]')
    time.sleep(.5)
    e.click()
    
    # Find and click View Report (to refresh the table)
    e = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportViewer_ctl04_ctl00"]')))
    time.sleep(.5)
    e.click()
    
    # Wait for the Export dropdown menu to be clickable and click it
    export_dropdown_xpath = '//*[@id="ReportViewer_ctl05_ctl04_ctl00"]'
    retry_until_clickable(driver, By.XPATH, export_dropdown_xpath)    
    time.sleep(2)
    e = driver.find_element(By.XPATH, export_dropdown_xpath)
    e.click()
    
    # Find and click Excel
    e = driver.find_element(By.XPATH, "//a[@title='Excel']")
    time.sleep(.5)
    e.click()
    time.sleep(10)
    
    # Rename the downloaded file to use the park code as the file name
    old_filename = "C:\\Users\entsa\Downloads\Summary of Visitor Use By Month and Year (1979 - Last Calendar Year).xlsx"
    new_filename = f"C:\\Users\entsa\Downloads\{park_key}.xlsx"
    if os.path.exists(old_filename):
        # Rename the downloaded file to use the park code as the file name
        try:
            os.rename(old_filename, new_filename)
        except FileExistsError:
            pass  # Handle if a file with the same name already exists


driver.quit()