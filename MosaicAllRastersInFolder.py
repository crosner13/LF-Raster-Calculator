# Libraries
import arcpy
import os

# Functions
def mosaicAllRastersInFolder(PathToLFRasters, MosaicRasterOutputPath):
    
    walk = arcpy.da.Walk(PathToLFRasters, datatype="RasterDataset")

    for dir_path, dir_names, file_names in walk:
        AllFiles = []
        for filename in file_names:
            AllFiles.append(os.path.join(dir_path, filename)) # add this one to the list
        if len(AllFiles) > 0 :  # make sure there is actually rasters in this folder
            arcpy.AddMessage(f"Found {len(AllFiles)} rasters. Starting Mosaic To New Raster...")
            arcpy.MosaicToNewRaster_management(AllFiles, MosaicRasterOutputPath, "OutputMosaic.tif","", "32_BIT_FLOAT","1","1")
            arcpy.AddMessage("Success.")
        else:
            arcpy.AddMessage("No rasters found. Ensure the file path inputs are correct.")

if __name__ == '__main__':

    lfRasters = arcpy.GetParameterAsText(0) # Full path to folder containing LF Rasters
    mosOutpath = arcpy.GetParameterAsText(1) # Path to where you want to put the Mosaic of the LF rasters

    mosaicAllRastersInFolder(PathToLFRasters=lfRasters, MosaicRasterOutputPath=mosOutpath)
