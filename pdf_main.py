import os
import glob
import pandas as pd

from pdf import PDF

os.chdir("data")

county, state, num_farms, land_farms, avg_farms, farm_size_1_9, \
farm_size_10_49, farm_size_50_179, farm_size_180_499, farm_size_500_999, \
farm_size_1000_plus, cropland, pastureland, woodland, other, broilers, \
cattle, goats, hogs, horses, layers, pullets, sheep, turkeys, crop_sales, \
livestock_sales =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], \
[], [], [], [], [], [], [], [], [], [], [], []        


for file in glob.glob("*.pdf"):
    pdf = PDF(file)
    county.append(pdf.county)
    state.append(pdf.state)
    num_farms.append(pdf.number_of_farms)
    land_farms.append(pdf.land_in_farms)
    avg_farms.append(pdf.average_size_of_farms)
    farm_size_1_9.append(pdf.acres_1_9)
    farm_size_10_49.append(pdf.acres_10_49)
    farm_size_50_179.append(pdf.acres_50_179)
    farm_size_180_499.append(pdf.acres_180_499)
    farm_size_500_999.append(pdf.acres_500_999)
    farm_size_1000_plus.append(pdf.acres_1000_plus)
    cropland.append(pdf.cropland)
    pastureland.append(pdf.pastureland)
    woodland.append(pdf.woodland)
    other.append(pdf.other)
    broilers.append(pdf.broilers)
    cattle.append(pdf.cattle)
    goats.append(pdf.goats)
    hogs.append(pdf.hogs)
    horses.append(pdf.horses)
    layers.append(pdf.layers)
    pullets.append(pdf.pullets)
    sheep.append(pdf.sheep)
    turkeys.append(pdf.turkeys)
    crop_sales.append(pdf.crop_sales)
    livestock_sales.append(pdf.livestock_sales)

pdf_data = {"State": state, "County": county, "Number of Farms": num_farms, "Land in Farms": land_farms, \
"Average Size of Farms": avg_farms, "Farm Size 1-9 acres": farm_size_1_9, "Farm Size 10-49 acres": farm_size_10_49, \
"Farm Size 50-179 acres": farm_size_50_179, "Farm Size 180-499": farm_size_180_499, "Farm Size 500-999": farm_size_500_999, \
"Farm Size 1000+": farm_size_1000_plus, "Cropland": cropland, "Pastureland": pastureland, "Woodland": woodland, \
"Other": other, "Broilers and other meat-type chickens": broilers, "Cattle and calves": cattle, "Goats": goats, \
"Hogs and pigs": hogs, "Horses and ponies": horses, "Layers": layers, "Pullets": pullets, "Sheep and lambs": sheep, \
"Turkeys": turkeys }

df = pd.DataFrame(data = pdf_data)
df.to_csv("data.csv")