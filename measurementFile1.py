# includes everything relevant, ignoring dipoles, scalars, tensors, and CP violation

####################
# Branching Ratios #
####################

# B+ -> K+ mu+ mu- branching ratio

measurements_BR_BKmumu = [
    'CDF B+->Kmumu BR July 2012',
    'LHCb B+->Kmumu BR March 2014',
    'Belle B+->Kmumu BR September 2020'
]

measurements_BR_BKmumu_only_LHCb = [
    'LHCb B+->Kmumu BR March 2014'
]


# B0 -> K0 mu+ mu- branching ratio

measurements_BR_B0Kmumu = [
    'CDF B0->Kmumu BR July 2012',
    'LHCb B0->Kmumu BR March 2014',
    'Belle B0->Kmumu BR September 2020'
]

measurements_BR_B0Kmumu_only_LHCb = [
    'LHCb B0->Kmumu BR March 2014'
]


# B0 -> K*0 mu+ mu- branching ratio

measurements_BR_BKstarmumu = [
    'CDF B0->K*mumu BR July 2012',
    'CMS B0->K*mumu BR November 2013',
    'CMS B0->K*mumu BR December 2015',
    'LHCb B0->K*mumu BR April 2017'
]

measurements_BR_BKstarmumu_only_LHCb = [
    'LHCb B0->K*mumu BR April 2017'
]


# B+ -> K*+ mu+ mu- branching ratio

measurements_BR_BplusKstarmumu = [
    'CDF B+->K*mumu BR July 2012',
    'LHCb B+->K*mumu BR March 2014'
]

measurements_BR_BplusKstarmumu_only_LHCb = [
    'LHCb B+->K*mumu BR March 2014'
]


# Bs -> phi mu+ mu- branching ratio

measurements_BR_Bsphimumu = [
    'CDF Bs->phimumu BR July 2012',
    'LHCb Bs->phimumu BR May 2021'
]

measurements_BR_Bsphimumu_only_LHCb = [
    'LHCb Bs->phimumu BR May 2021'
]


# B -> Xs mu+ mu- branching ratio

measurements_BR_BXsmumu = [
    'Belle B->Xsmumu BR December 2013'
]


# Lambdab -> Lambda mu+ mu- branching ratio

measurements_BR_LambdabLambdamumu = [
    'CDF Lambdab->Lambdamumu BR July 2012',
    'LHCb Lambdab->Lambdamumu BR March 2015'
]

measurements_BR_LambdabLambdamumu_only_LHCb = [
    'LHCb Lambdab->Lambdamumu BR March 2015'
]


# All semi-leptonic branching ratios

all_measurements_BR = measurements_BR_BKmumu + measurements_BR_B0Kmumu + measurements_BR_BKstarmumu + measurements_BR_BplusKstarmumu + measurements_BR_Bsphimumu + measurements_BR_BXsmumu + measurements_BR_LambdabLambdamumu

all_measurements_BR_meson = measurements_BR_BKmumu + measurements_BR_B0Kmumu + measurements_BR_BKstarmumu + measurements_BR_BplusKstarmumu + measurements_BR_Bsphimumu + measurements_BR_BXsmumu

all_measurements_BR_only_LHCb = measurements_BR_BKmumu_only_LHCb + measurements_BR_B0Kmumu_only_LHCb + measurements_BR_BKstarmumu_only_LHCb + measurements_BR_BplusKstarmumu_only_LHCb + measurements_BR_Bsphimumu_only_LHCb + measurements_BR_LambdabLambdamumu_only_LHCb

all_measurements_BR_meson_only_LHCb = measurements_BR_BKmumu_only_LHCb + measurements_BR_B0Kmumu_only_LHCb + measurements_BR_BKstarmumu_only_LHCb + measurements_BR_BplusKstarmumu_only_LHCb + measurements_BR_Bsphimumu_only_LHCb


#######################
# Angular Observables #
#######################

# B+ -> K+ mu+ mu- angular observables (only relevant for scalars or tensors)

#measurements_angular_BKmumu = [
#]


# B0 -> K0 mu+ mu- angular observables (only relevant for scalars or tensors)

#measurements_angular_B0Kmumu = [
#]


# B0 -> K*0 mu+ mu- angular observables

measurements_angular_BKstarmumu = [
    'CDF B0->K*mumu angular July 2012',
    'ATLAS B0->K*mumu angular April 2013',
    'CMS B0->K*mumu angular August 2013',
    'CMS B0->K*mumu angular December 2015',
    'CMS B0->K*mumu angular March 2017',
    'ATLAS B0->K*mumu angular 0.04-2 May 2018',
    'ATLAS B0->K*mumu angular 2-4 May 2018',
    'ATLAS B0->K*mumu angular 4-6 May 2018',
    'LHCb B0->K*mumu angular 0.1-0.98 March 2020',
    'LHCb B0->K*mumu angular 1.1-2.5 March 2020',
    'LHCb B0->K*mumu angular 2.5-4 March 2020',
    'LHCb B0->K*mumu angular 4-6 March 2020',
    'LHCb B0->K*mumu angular 15-19 March 2020'
]

measurements_angular_BKstarmumu_only_LHCb = [
    'LHCb B0->K*mumu angular 0.1-0.98 March 2020',
    'LHCb B0->K*mumu angular 1.1-2.5 March 2020',
    'LHCb B0->K*mumu angular 2.5-4 March 2020',
    'LHCb B0->K*mumu angular 4-6 March 2020',
    'LHCb B0->K*mumu angular 15-19 March 2020'
]


# B+ -> K*+ mu+ mu- angular observables

measurements_angular_BplusKstarmumu = [
    'LHCb B+->K*mumu angular 0.1-0.98 December 2020', 
    'LHCb B+->K*mumu angular 1.1-2.5 December 2020', 
    'LHCb B+->K*mumu angular 2.5-4 December 2020', 
    'LHCb B+->K*mumu angular 4-6 December 2020', 
    'LHCb B+->K*mumu angular 15-19 December 2020'
]


# Bs -> phi mu+ mu- angular observables

measurements_angular_Bsphimumu = [
    'LHCb Bs->phimumu angular 0.1-0.98 July 2021', 
    'LHCb Bs->phimumu angular 1.1-4 July 2021', 
    'LHCb Bs->phimumu angular 4-6 July 2021', 
    'LHCb Bs->phimumu angular 15-18.9 July 2021'
]


# Lambdab -> Lambda mu+ mu- angular observables

measurements_angular_LambdabLambdamumu = [
    'LHCb Lambdab->Lambdamumu angular August 2018'
]


# All angular observables

#all_measurements_angular = measurements_angular_BKmumu + measurements_angular_B0Kmumu + measurements_angular_BKstarmumu + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu + measurements_angular_LambdabLambdamumu

#all_measurements_angular_meson = measurements_angular_BKmumu + measurements_angular_B0Kmumu + measurements_angular_BKstarmumu + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu

all_measurements_angular = measurements_angular_BKstarmumu + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu + measurements_angular_LambdabLambdamumu

all_measurements_angular_meson = measurements_angular_BKstarmumu + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu

all_measurements_angular_only_LHCb = measurements_angular_BKstarmumu_only_LHCb + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu + measurements_angular_LambdabLambdamumu

all_measurements_angular_meson_only_LHCb = measurements_angular_BKstarmumu_only_LHCb + measurements_angular_BplusKstarmumu + measurements_angular_Bsphimumu


##############################
# Lepton Flavor Universality #
##############################

# LFU ratios

measurements_LFU_ratios = [
    'Belle RK September 2020',
    'Belle RK* September 2020',
    'LHCb RKS October 2021', 
    'LHCb RK*+ October 2021',
    'LHCb RK and RK* December 2022',
    'CMS RK January 2024'
]

measurements_LFU_ratios_only_LHCb = [
    'LHCb RKS October 2021', 
    'LHCb RK*+ October 2021',
    'LHCb RK and RK* December 2022'
]


# LFU angular observables 

measurements_LFU_angular = [
    'Belle B0->K*ll angular LFU December 2016'
]


# All LFU observables

all_measurements_LFU = measurements_LFU_ratios + measurements_LFU_angular

all_measurements_LFU_only_LHCb = measurements_LFU_ratios_only_LHCb



#############################
# Bs -> mu+ mu- Observables #
#############################

# Bs -> mu+ mu- branching ratio

measurements_Bsmumu_BR = [
    'HFLAV Bs->mumu BR average October 2022'
]

# Bs -> mu+ mu- effective lifetime (only relevant for scalars)

#measurements_Bsmumu_tau_eff = [
#]



###################
# All Observables #
###################

# All B -> K mu+ mu- observables 

#all_measurements_BKmumu = measurements_BR_B0Kmumu + measurements_angular_B0Kmumu + measurements_BR_BKmumu + measurements_angular_BKmumu


# All B -> K* mu+ mu- observables 

all_measurements_BKstarmumu = measurements_BR_BKstarmumu + measurements_angular_BKstarmumu + measurements_BR_BplusKstarmumu + measurements_angular_BplusKstarmumu

all_measurements_BKstarmumu_only_LHCb = measurements_BR_BKstarmumu_only_LHCb + measurements_angular_BKstarmumu_only_LHCb + measurements_BR_BplusKstarmumu_only_LHCb + measurements_angular_BplusKstarmumu



# All Bs -> phi mu+ mu- observables 

all_measurements_Bsphimumu = measurements_BR_Bsphimumu + measurements_angular_Bsphimumu

all_measurements_Bsphimumu_only_LHCb = measurements_BR_Bsphimumu_only_LHCb + measurements_angular_Bsphimumu


# All Lambdab -> Lambda mu+ mu- observables 

all_measurements_LambdabLambdamumu = measurements_BR_LambdabLambdamumu + measurements_angular_LambdabLambdamumu

all_measurements_LambdabLambdamumu_only_LHCb = measurements_BR_LambdabLambdamumu_only_LHCb + measurements_angular_LambdabLambdamumu


# All b->smumu observables 

#all_measurements_bsmumu = all_measurements_BKmumu + all_measurements_BKstarmumu + all_measurements_Bsphimumu + measurements_BR_BXsmumu + all_measurements_LambdabLambdamumu

#all_measurements_bsmumu_meson = all_measurements_BKmumu + all_measurements_BKstarmumu + all_measurements_Bsphimumu + measurements_BR_BXsmumu

all_measurements_bsmumu = measurements_BR_B0Kmumu + measurements_BR_BKmumu + all_measurements_BKstarmumu + all_measurements_Bsphimumu + measurements_BR_BXsmumu + all_measurements_LambdabLambdamumu

all_measurements_bsmumu_meson = measurements_BR_B0Kmumu + measurements_BR_BKmumu + all_measurements_BKstarmumu + all_measurements_Bsphimumu + measurements_BR_BXsmumu

all_measurements_bsmumu_only_LHCb = measurements_BR_B0Kmumu_only_LHCb + measurements_BR_BKmumu_only_LHCb + all_measurements_BKstarmumu_only_LHCb + all_measurements_Bsphimumu_only_LHCb + all_measurements_LambdabLambdamumu_only_LHCb

all_measurements_bsmumu_meson_only_LHCb = measurements_BR_B0Kmumu_only_LHCb + measurements_BR_BKmumu_only_LHCb + all_measurements_BKstarmumu_only_LHCb + all_measurements_Bsphimumu_only_LHCb


# All observables 

all_measurements = all_measurements_bsmumu + measurements_Bsmumu_BR + all_measurements_LFU

all_measurements_meson = all_measurements_bsmumu_meson + measurements_Bsmumu_BR + all_measurements_LFU

all_measurements_only_LHCb = all_measurements_bsmumu_only_LHCb + measurements_Bsmumu_BR + all_measurements_LFU_only_LHCb

all_measurements_meson_only_LHCb = all_measurements_bsmumu_meson_only_LHCb + measurements_Bsmumu_BR + all_measurements_LFU_only_LHCb


#2011

CDF_2011 = ['CDF Bs->mumu BR July 2011','CDF Lambdab->Lambdamumu BR July 2011','CDF B+->Kmu\
mu BR November 2011','CDF B0->Kmumu BR November 2011','CDF B0->K*mumu BR November 2011','CD\
F B+->K*mumu BR November 2011','CDF Bs->phimumu BR July 2011','CDF B0->K*mumu angular Augus\
t 2011','CDF B0->K*mumu CP August 2011','CDF B+->Kmumu angular August 2011']

Belle_2011 = []

ATLAS_2011 = []

CMS_2011 = ['CMS and LHCb Bs->mumu BR August 2011']

LHCb_2011 = ['LHCb B0->K*mumu BR August 2011','LHCb B0->K*mumu angular August 2011']

#2012

CDF_2012 = ['CDF Bs->mumu BR July 2011','CDF Lambdab->Lambdamumu BR July 2012','CDF B+->Kmumu BR July 2012','CDF B0->Kmumu BR July 2012','CDF B0->K*mumu BR July 2012','CDF B+->K*mumu BR July 2012','CDF Bs->phimumu BR July 2012','CDF B0->K*mumu angular July 2012','CDF B0->K*mumu CP July 2012','CDF B+->Kmumu angular July 2012']

Belle_2012 = []

ATLAS_2012 = ['ATLAS Bs->mumu BR April 2012']

CMS_2012 = ['CMS Bs->mumu BR March 2012']

LHCb_2012 = ['LHCb Bs->mumu BR March 2012','LHCb B0->Kmumu BR May 2012','LHCb B+->K*mumu BR May 2012','LHCb B0->K*mumu BR June 2012','LHCb B0->K*mumu angular June 2012','LHCb B+->Kmumu BR September 2012','LHCb B+->Kmumu angular September 2012']

#2013

CDF_2013 = CDF_2012

Belle_2013 = ['Belle B->Xsee BR December 2013','Belle B->Xsmumu BR December 2013']

ATLAS_2013 = ['ATLAS Bs->mumu BR April 2012','ATLAS B0->K*mumu angular April 2013']

CMS_2013 = ['CMS Bs->mumu BR July 2013','CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013']

LHCb_2013 = ['LHCb B0->Kmumu BR May 2012','LHCb B+->K*mumu BR May 2012','LHCb B+->Kmumu BR September 2012','LHCb B+->Kmumu angular September 2012','LHCb B0->K*mumu BR April 2013','LHCb B0->K*mumu angular Apri\
l 2013','LHCb B0->K*mumu CP April 2013','LHCb Bs->phimumu BR May 2013','LHCb Bs->phimumu angular May 2013','LHCb Bs->mumu BR July 2013','LHCb B0->K*mumu angular August 2013']

#2014

CDF_2014 = CDF_2012

Belle_2014 = Belle_2013

ATLAS_2014 = ATLAS_2013

CMS_2014 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS and LHCb Bs->mumu BR November 2014']

LHCb_2014 = ['LHCb B0->K*mumu BR April 2013','LHCb B0->K*mumu angular April 2013','LHCb B0->K*mumu CP April 2013','LHCb Bs->phimumu BR May 2013','LHCb Bs->phimumu angular May 2013','LHCb B0->K*mumu angular Au\
gust 2013','LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb RK June 2014']

#2015

CDF_2015 = CDF_2012

Belle_2015 = Belle_2013

ATLAS_2015 = ATLAS_2013

CMS_2015 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS and LHCb Bs->mumu BR November 2014','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015']

LHCb_2015 = ['LHCb B0->K*mumu BR April 2013','LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb RK June 2014','LHCb Lambdab\
->Lambdamumu BR March 2015','LHCb Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu angular 0.1-0.98 December 2015','LHCb B0->K*mum\
u angular 1.1-2.5 December 2015','LHCb B0->K*mumu angular 2.5-4 December 2015','LHCb B0->K*mumu angular 4-6 December 2015','LHCb B0->K*mumu angular 15-19 December 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2\
015','LHCb B0->K*mumu CP 1.1-2.5 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015']

#2016

CDF_2016 = CDF_2012

Belle_2016 = ['Belle B->Xsee BR December 2013','Belle B->Xsmumu BR December 2013','Belle B0->K*ll angular LFU December 2016']

ATLAS_2016 = ['ATLAS B0->K*mumu angular April 2013','ATLAS Bs->mumu BR April 2016']

CMS_2016 = CMS_2015

LHCb_2016 = ['LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb RK June 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHC\
b Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu angular 0.1-0.98 December 2015','LHCb B0->K*mumu angular 1.1-2.5 December 2015'\
,'LHCb B0->K*mumu angular 2.5-4 December 2015','LHCb B0->K*mumu angular 4-6 December 2015','LHCb B0->K*mumu angular 15-19 December 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5\
 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR June 2016']

#2017

CDF_2017 = CDF_2012

Belle_2017 = Belle_2016

ATLAS_2017 = ['ATLAS B0->K*mumu angular April 2013','ATLAS Bs->mumu BR April 2016','ATLAS B0->K*mumu angular April 2017']

CMS_2017 = ['CMS Bs->mumu BR July 2013','CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular \
March 2017']

LHCb_2017 = ['LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb RK June 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHC\
b Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu angular 0.1-0.98 December 2015','LHCb B0->K*mumu angular 1.1-2.5 December 2015'\
,'LHCb B0->K*mumu angular 2.5-4 December 2015','LHCb B0->K*mumu angular 4-6 December 2015','LHCb B0->K*mumu angular 15-19 December 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5\
 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb Bs->mumu BR March 2017','LHCb Bs-\
>mumu effective lifetime March 2017','LHCb RK* May 2017']

#2018

CDF_2018 = CDF_2012

Belle_2018 = Belle_2016

ATLAS_2018 = ['ATLAS B0->K*mumu angular April 2013','ATLAS B0->K*mumu angular 0.04-2 May 2018','ATLAS B0->K*mumu angular 2-4 May 2018','ATLAS B0->K*mumu angular 4-6 May 2018','ATLAS Bs->mumu BR December 2018']

CMS_2018 = CMS_2017

LHCb_2018 = ['LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb RK June 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHC\
b Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu angular 0.1-0.98 December 2015','LHCb B0->K*mumu angular 1.1-2.5 December 2015'\
,'LHCb B0->K*mumu angular 2.5-4 December 2015','LHCb B0->K*mumu angular 4-6 December 2015','LHCb B0->K*mumu angular 15-19 December 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5\
 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb Bs->mumu BR March 2017','LHCb Bs-\
>mumu effective lifetime March 2017','LHCb RK* May 2017','LHCb Lambdab->Lambdamumu angular August 2018']

#2019

CDF_2019 = CDF_2012

Belle_2019 = ['Belle B->Xsee BR December 2013','Belle B->Xsmumu BR December 2013','Belle B0->K*ll angular LFU December 2016','Belle RK* April 2019','Belle RK August 2019','Belle B+->Kmumu BR August 2019','Belle B0->Kmumu BR August 2019']

ATLAS_2019 = ATLAS_2018

CMS_2019 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular March 2017','CMS Bs->mumu BR October 2019','CMS Bs->mumu effective lifetime October 2019']

LHCb_2019 = ['LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHCb Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu angular 0.1-0.98 December 2015','LHCb B0->K*mumu angular 1.1-2.5 December 2015','LHCb B0->K*mumu angular 2.5-4 December 2015','LHCb B0->K*mumu angular 4-6 December 2015','LHCb B0->K*mumu angular 15-19 December 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb Bs->mumu BR March 2017','LHCb Bs->mumu effective lifetime March 2017','LHCb RK* May 2017','LHCb Lambdab->Lambdamumu angular August 2018','LHCb RK March 2019']

#2020

CDF_2020 = CDF_2012

Belle_2020 = ['Belle B->Xsee BR December 2013','Belle B->Xsmumu BR December 2013','Belle B0->K*ll angular LFU December 2016','Belle RK* September 2020','Belle RK September 2020','Belle B+->Kmumu BR September 2020','Belle B0->Kmumu BR September 2020']

ATLAS_2020 = ['ATLAS B0->K*mumu angular April 2013','ATLAS B0->K*mumu angular 0.04-2 May 2018','ATLAS B0->K*mumu angular 2-4 May 2018','ATLAS B0->K*mumu angular 4-6 May 2018']

CMS_2020 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular March 2017',]

LHCb_2020 = ['LHCb Bs->mumu BR July 2013','LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHCb Bs->phimumu BR June 2015','LHCb Bs->phimumu angular 1-6 June 2015','LHCb Bs->phimumu angular 15-19 June 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb RK* May 2017','LHCb Lambdab->Lambdamumu angular August 2018','LHCb RK March 2019','LHCb B0->K*mumu angular 0.1-0.98 March 2020','LHCb B0->K*mumu angular 1.1-2.5 March 2020','LHCb B0->K*mumu angular 2.5-4 March 2020','LHCb B0->K*mumu angular 4-6 March 2020','LHCb B0->K*mumu angular 15-19 March 2020','LHCb B+->K*mumu angular 0.1-0.98 December 2020','LHCb B+->K*mumu angular 1.1-2.5 December 2020','LHCb B+->K*mumu angular 2.5-4 December 2020','LHCb B+->K*mumu angular 4-6 December 2020','LHCb B+->K*mumu angular 15-19 December 2020','ATLAS CMS LHCb Bs->mumu BR August 2020','CMS LHCb Bs->mumu effective lifetime August 2020']

#2021

CDF_2021 = CDF_2012

Belle_2021 = Belle_2020

ATLAS_2021 = ['ATLAS B0->K*mumu angular April 2013','ATLAS B0->K*mumu angular 0.04-2 May 2018','ATLAS B0->K*mumu angular 2-4 May 2018','ATLAS B0->K*mumu angular 4-6 May 2018','ATLAS Bs->mumu BR December 2018']

CMS_2021 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular March 2017','CMS Bs->mumu BR May 2020','CMS Bs->mumu effective lifetime October 2019']

LHCb_2021 = ['LHCb Bs->mumu BR July 2013','LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb RK* May 2017','LHCb Lambdab->Lambdamumu angular August 2018','LHCb B0->K*mumu angular 0.1-0.98 March 2020','LHCb B0->K*mumu angular 1.1-2.5 March 2020','LHCb B0->K*mumu angular 2.5-4 March 2020','LHCb B0->K*mumu angular 4-6 March 2020','LHCb B0->K*mumu angular 15-19 March 2020','LHCb B+->K*mumu angular 0.1-0.98 December 2020','LHCb B+->K*mumu angular 1.1-2.5 December 2020','LHCb B+->K*mumu angular 2.5-4 December 2020','LHCb B+->K*mumu angular 4-6 December 2020','LHCb B+->K*mumu angular 15-19 December 2020','LHCb Bs->mumu BR August 2021','LHCb Bs->mumu effective lifetime August 2021','LHCb RK March 2021','LHCb Bs->phimumu BR May 2021','LHCb Bs->phimumu angular 0.1-0.98 July 2021','LHCb Bs->phimumu angular 1.1-4 July 2021','LHCb Bs->phimumu angular 4-6 July 2021','LHCb Bs->phimumu angular 15-18.9 July 2021','LHCb RKS October 2021','LHCb RK*+ October 2021']

#2022

CDF_2022 = CDF_2012

Belle_2022 = Belle_2020

ATLAS_2022 = ATLAS_2021

CMS_2022 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular March 2017','CMS Bs->mumu BR May 2020','CMS Bs->mumu effective lifetime October 2019','CMS Bs->mumu BR July 2022','CMS Bs->mumu effective lifetime July 2022']

LHCb_2022 = ['LHCb Bs->mumu BR July 2013','LHCb B+->Kmumu angular March 2014','LHCb B+->Kmumu BR March 2014','LHCb B0->Kmumu BR March 2014','LHCb B+->K*mumu BR March 2014','LHCb Lambdab->Lambdamumu BR March 2015','LHCb B0->K*mumu CP 0.1-0.98 December 2015','LHCb B0->K*mumu CP 1.1-2.5 December 2015','LHCb B0->K*mumu CP 2.5-4 December 2015','LHCb B0->K*mumu CP 4-6 December 2015','LHCb B0->K*mumu CP 15-19 December 2015','LHCb B0->K*mumu BR April 2017','LHCb Bs->mumu BR March 2017','LHCb Bs->mumu effective lifetime March 2017','LHCb Lambdab->Lambdamumu angular August 2018','LHCb B0->K*mumu angular 0.1-0.98 March 2020','LHCb B0->K*mumu angular 1.1-2.5 March 2020','LHCb B0->K*mumu angular 2.5-4 March 2020','LHCb B0->K*mumu angular 4-6 March 2020','LHCb B0->K*mumu angular 15-19 March 2020','LHCb B+->K*mumu angular 0.1-0.98 December 2020','LHCb B+->K*mumu angular 1.1-2.5 December 2020','LHCb B+->K*mumu angular 2.5-4 December 2020','LHCb B+->K*mumu angular 4-6 December 2020','LHCb B+->K*mumu angular 15-19 December 2020','LHCb Bs->mumu BR August 2021','LHCb Bs->mumu effective lifetime August 2021','LHCb Bs->phimumu BR May 2021','LHCb Bs->phimumu angular 0.1-0.98 July 2021','LHCb Bs->phimumu angular 1.1-4 July 2021','LHCb Bs->phimumu angular 4-6 July 2021','LHCb Bs->phimumu angular 15-18.9 July 2021','LHCb RKS October 2021','LHCb RK*+ October 2021','LHCb RK and RK* December 2022']

#2023

CDF_2023 = CDF_2012

Belle_2023 = Belle_2020

ATLAS_2023 = ATLAS_2021

CMS_2023 = CMS_2022

LHCb_2023 = LHCb_2022 

#2024

CDF_2024 = CDF_2012

Belle_2024 = Belle_2020

ATLAS_2024 = ATLAS_2021

#Sam's CMS additions (excluding values with 8<q2<14)
sams_additions = ['CMS B0->K*mumu q2 1.1-2 June 2024','CMS B0->K*mumu q2 2-4.3 June 2024','CMS B0->K*mumu q2 4.3-6 June 2024','CMS B0->K*mumu q2 14.18-16 June 2024','CMS B+->K+mumu July 2024','CMS B0->K*mumu q2 1.1-2 November 2024','CMS B0->K*mumu q2 2-4.3 November 2024','CMS B0->K*mumu q2 4.3-6 November 2024','CMS B0->K*mumu q2 6-8.68 November 2024','CMS B0->K*mumu q2 14.18-16 November 2024'] #+ ['CMS B0->K*mumu q2 6-8.68 June 2024','CMS B0->K*mumu q2 10.09-12.86 June 2024']

CMS_2024 = ['CMS B0->K*mumu BR November 2013','CMS B0->K*mumu angular August 2013','CMS B0->K*mumu BR December 2015','CMS B0->K*mumu angular December 2015','CMS B0->K*mumu angular March 2017','CMS Bs->mumu BR May 2020','CMS Bs->mumu effective lifetime October 2019','CMS Bs->mumu BR July 2022','CMS Bs->mumu effective lifetime July 2022','CMS RK January 2024'] + sams_additions

LHCb_2024 = LHCb_2022

#aggregate lists
list_2011 = CDF_2011 + Belle_2011 + ATLAS_2011 + CMS_2011 + LHCb_2011
list_2012 = CDF_2012 + Belle_2012 + ATLAS_2012 + CMS_2012 + LHCb_2012
list_2013 = CDF_2013 + Belle_2013 + ATLAS_2013 + CMS_2013 + LHCb_2013
list_2014 = CDF_2014 + Belle_2014 + ATLAS_2014 + CMS_2014 + LHCb_2014
list_2015 = CDF_2015 + Belle_2015 + ATLAS_2015 + CMS_2015 + LHCb_2015
list_2016 = CDF_2016 + Belle_2016 + ATLAS_2016 + CMS_2016 + LHCb_2016
list_2017 = CDF_2017 + Belle_2017 + ATLAS_2017 + CMS_2017 + LHCb_2017
list_2018 = CDF_2018 + Belle_2018 + ATLAS_2018 + CMS_2018 + LHCb_2018
list_2019 = CDF_2019 + Belle_2019 + ATLAS_2019 + CMS_2019 + LHCb_2019
list_2020 = CDF_2020 + Belle_2020 + ATLAS_2020 + CMS_2020 + LHCb_2020
list_2021 = CDF_2021 + Belle_2021 + ATLAS_2021 + CMS_2021 + LHCb_2021
list_2022 = CDF_2022 + Belle_2022 + ATLAS_2022 + CMS_2022 + LHCb_2022
list_2023 = CDF_2023 + Belle_2023 + ATLAS_2023 + CMS_2023 + LHCb_2023
list_2024 = CDF_2024 + Belle_2024 + ATLAS_2024 + CMS_2024 + LHCb_2024

#runspace
list_2 = list_2024 + list_2023 + list_2022 + list_2021 + list_2020 + list_2019 + list_2018 + list_2017 + list_2016 + list_2015 + list_2014 + list_2013 + list_2012 + list_2011
