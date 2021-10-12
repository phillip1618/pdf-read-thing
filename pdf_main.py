import os
import glob
import pandas

from pdf import PDF

os.chdir("data")

county, state, num_farms, land_farms, avg_farms, farm_size_1_9, \
farm_size_10_49, farm_size_50_179, farm_size_180_499, farm_size_500_999, \
farm_size_1000_plus, cropland, pastureland, woodland, other, broilers, \
cattle, goats, hogs, horses, layers, pullets, sheep, turkeys, crop_sales, \
livestock_sales =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], \
[], [], [], [], [], [], [], [], [], [], [], []        


for file in glob.glob("*.pdf"):
    print(file)
    pdf = PDF(file)
    county.append(pdf.county)
    state.append(pdf.state)
    num_farms.append(pdf.number_of_farms)
    land_farms.append(pdf.land_in_farms)
    avg_farms.append(pdf.average_size_of_farms)
    
