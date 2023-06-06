
# Libraries
# import arcpy
import os

# Variables
# put file folder pathways as params here
# equation:
'''  20.41 + 0.873 *("*_d00.tif")-1.73*("*_std.tif")-0.189*("_d01.tif")  '''
# three input folders:
    # Normal_d00_tif = "C:\\Users\\coler\\Documents\\ISU\\WFH\\Ladder_Fuels_3\\Normalized_Rasters\\Normal_d00.tif"
    # Normal_d01_tif = "C:\\Users\\coler\\Documents\\ISU\\WFH\\Ladder_Fuels_3\\Normalized_Rasters\\Normal_d01.tif"
    # Normal_std_tif = "C:\\Users\\coler\\Documents\\ISU\\WFH\\Ladder_Fuels_3\\Normalized_Rasters\\Normal_std.tif"


# Functions 
def matchFiles(StandardDev, COV1_8, COV4_8):
    # Get list of matching .TIFs in each file folder 
    
    justIDs = slice(19)

    rasterIDs = [file[justIDs] for file in os.listdir(StandardDev) if file.startswith("ot_pt") and file.endswith("_normal_std.txt")]
    print(rasterIDs)

    for id in rasterIDs:
        stdDev = os.path.join(StandardDev, (str(id) + "std.txt"))
        cover1_8 = os.path.join(COV1_8, (str(id) + "d00.txt"))
        cover4_8 = os.path.join(COV4_8, (str(id) + "d01.txt"))
        if os.path.exists(stdDev) and os.path.exists(cover1_8) and os.path.exists(cover4_8):
            print(f"Input files found: {stdDev}, {cover1_8}, {cover4_8}")
            # Continue here
        else:
            print(f"An input is missing for ID prefix: {id}.")

def getLadderFuelsRaster():
    pass

if __name__ == '__main__':
    
    '''
    std = arcpy.GetParameterAsText(0) # full path to folder containing Standard Deviation Rasters
    d00 = arcpy.GetParameterAsText(1) # full path to folder containing COV1_8 Rasters
    d01 = arcpy.GetParameterAsText(2) # full path to folder containing COV4_8 Rasters
    '''
    std = r"C:\Users\coler\Documents\ISU\WFH\LF3_Testing\Normalized_Rasters\Normal_std.tif"
    d00 = r"C:\Users\coler\Documents\ISU\WFH\LF3_Testing\Normalized_Rasters\Normal_d00.tif"
    d01 = r"C:\Users\coler\Documents\ISU\WFH\LF3_Testing\Normalized_Rasters\Normal_d01.tif"


    matchFiles(StandardDev = std, COV1_8 = d00, COV4_8 = d01)

