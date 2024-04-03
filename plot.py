from PIL import Image
import matplotlib.pyplot as plt
import io

console_sales = {
    2020: (('Switch','XBox','PS4'),(1.549, 0, 0)),
    2021: (('Switch','XBox','PS4'),(1.544, 0.325, 0.653)),
    2022: (('Switch','XBox','PS4'),(1.328, 0.605, 0.708)),
    2023: (('Switch','XBox','PS4'),(1.140, 0.456, 1.257)),
}

fig = plt.figure(figsize=(6,5))

images = []

for year, data in console_sales.items():
    companies,sales = data
    plt.bar(console_sales[year][0], 
            console_sales[year][1],
            color=['red','green','blue'])
    plt.title(f'Console Sales in {year}')
    plt.ylabel('Sales (in million units)')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    
    image = Image.open(buffer)
    images.append(image)
    
images[0].save('console_sales.gif', 
               save_all=True, 
               append_images=images[1:], 
               loop=0,
               duration=1000)