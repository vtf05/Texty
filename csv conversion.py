


import os,gzip,shutil

# PROVIDE YOUR DOWNLOAD DIRECTORY HERE
datapath ='C:\\Users\\Avinash vishwakarma\\Desktop\\New folder\\'  

# LISTING ALL ARCHIVES IN THE DIRECTORY
files = os.listdir(datapath)
for file in files:
    if file.endswith('gz'):
        print('Extracting ',file)
        with gzip.open(datapath+file, 'rb') as f_in:
            with open(datapath+file.split('.')[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
print('Extraction Complete')

# OPTIONAL REMOVE THE ARCHIVES
for file in files:
    if file.endswith('gz'):
        print('Removing ',file)
        os.remove(datapath+file)
print ('All archives removed')



def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
      
        image = [ord(l.read(1))]
        
        for j in range(28*28):
            #print(f.read(1))
            image.append(ord(f.read(1)))
           

        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()
    
convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte","mnist_train.csv", 60000)

convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte","mnist_test.csv", 10000)

print("done")