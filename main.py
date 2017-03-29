
import numpy as np
import matplotlib.pyplot as mp

class DEMFile:
    #stores DEM file and metadata

    def __init__(self, fname):
        #reads in DEM from file assuming .asc format
        #TODO ascii format check
        with open(fname, "r") as f:
            data = f.readlines()
        self.width = int(data[0].split()[1])
        self.height = int(data[1].split()[1])
        self.xllcorner = float(data[2].split()[1])
        self.yllcorner = float(data[3].split()[1])
        self.cellsize = float(data[4].split()[1])
        self.missing_data = int(data[5].split()[1])
        self.data = []
        for l in data[6:]:
            #l = l.split(" ")
            l = [float(x) for x in l.split()]
            self.data.append(l)
            #l = [float(x) for x in l.split()]
        self.data = np.array(self.data)
        self.data[self.data == self.missing_data] = float('NaN')



def main():
    mora_west = DEMFile('q1826.asc')
    dem = mora_west.data
    mp.imshow(dem)
    mp.colorbar()
    mp.show()


if __name__ == "__main__":
    main()