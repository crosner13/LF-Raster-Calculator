# Libraries
import os
import arcpy
from arcpy.sa import * # Might need the image analyst version instead

# Functions 
def getLadderFuelsRaster(PathToRasters, PathToOutLF):
    
    # Slice to grab ID prefixes
    justIDs = slice(-7)
    rasterIDs = [file[justIDs] for file in os.listdir(PathToRasters) if file.endswith("_normal_std.tif")]
    arcpy.AddMessage(f"Found {len(rasterIDs)} ID prefixes.")

    # Grab extension
    arcpy.CheckOutExtension("Spatial")

    # This loop makes sure all three variables in the raster equation are there and performs the calculation
    for id in rasterIDs:
        stdDev = os.path.join(PathToRasters, (str(id) + "std.tif"))
        cover1_8 = os.path.join(PathToRasters, (str(id) + "d00.tif"))
        cover4_8 = os.path.join(PathToRasters, (str(id) + "d01.tif"))
        if os.path.exists(stdDev) and os.path.exists(cover1_8) and os.path.exists(cover4_8):
            arcpy.AddMessage(f"Required input files found for ID prefix: {id}. Performing calculation.")
            
            lfRaster = RasterCalculator([cover1_8, stdDev, cover4_8], ["x", "y", "z"], 
                                        "20.41 + 0.873 * x -1.73 * y - 0.189 * z")
            lfRaster.save(os.path.join(PathToOutLF, str(id)+ "LF.tif"))
            arcpy.AddMessage(f"LF Raster created and saved for {id}.")
        else:
            arcpy.AddMessage(f"Skipping ID prefix: {id}. It is missing an input")

    arcpy.AddMessage("Done.")

if __name__ == '__main__':
    
    rst = arcpy.GetParameterAsText(0) # full path to folder containing all rasters
    outLF = arcpy.GetParameterAsText(1) # full path to folder containing output LF Rasters

    getLadderFuelsRaster(PathToRasters = rst, PathToOutLF = outLF)