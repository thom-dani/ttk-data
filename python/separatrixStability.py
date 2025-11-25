#!/usr/bin/env python
import paraview

paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(
    DatabasePath="protonTunnelingPrism.cdb"
)

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE ModeId=16 and GeomID in (10, 0, 20)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKCinemaProductReader1)
calculator1.ResultArrayName = "opposite"
calculator1.Function = "-rho"

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = ["POINTS", "opposite"]

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(
    Input=tTKScalarFieldNormalizer1
)
tTKTopologicalSimplificationByPersistence1.InputArray = ["POINTS", "opposite"]
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 1e-05

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(
    Input=tTKTopologicalSimplificationByPersistence1
)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "opposite"]
tTKMorseSmaleComplex1.OffsetField = ["POINTS", "opposite"]
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 2.5e-05

# find source
tTKMorseSmaleComplex1_1 = FindSource("TTKMorseSmaleComplex1")

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1, 1))
threshold1.Scalars = ["CELLS", "SeparatrixType"]
threshold1.UpperThreshold = 0.9

# create a new 'TTK SeparatrixStability'
tTKSeparatrixStability1 = TTKSeparatrixStability(Input=threshold1)

# create a new 'Convert To Point Cloud'
convertToPointCloud1 = ConvertToPointCloud(Input=tTKSeparatrixStability1)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKSeparatrixStability1)

# create a new 'Extract Block'
extractBlock5 = ExtractBlock(Input=tTKMorseSmaleComplex1)
extractBlock5.Assembly = "Hierarchy"
extractBlock5.Selectors = ["/Root/Block0"]

# create a new 'Threshold'
threshold3 = Threshold(Input=extractBlock5)
threshold3.Scalars = ["POINTS", "CellDimension"]

# create a new 'Threshold'
threshold2 = Threshold(Input=convertToPointCloud1)
threshold2.Scalars = ["POINTS", "MatchingIdInBlock0"]
threshold2.ThresholdMethod = "Above Upper Threshold"

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(Input=threshold2)
tTKIdentifierRandomizer2.ScalarField = ["POINTS", "MatchingIdInBlock0"]

# create a new 'Extract Block'
extractBlock4 = ExtractBlock(Input=tTKIdentifierRandomizer2)
extractBlock4.Assembly = "Hierarchy"
extractBlock4.Selectors = ["/Root/Block1"]

# create a new 'Extract Block'
extractBlock7 = ExtractBlock(Input=tTKIdentifierRandomizer2)
extractBlock7.Assembly = "Hierarchy"
extractBlock7.Selectors = ["/Root/Block2"]

# create a new 'Extract Block'
extractBlock3 = ExtractBlock(Input=tTKIdentifierRandomizer2)
extractBlock3.Assembly = "Hierarchy"
extractBlock3.Selectors = ["/Root/Block0"]

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=extractSurface1)
tTKGeometrySmoother1.IterationNumber = 50
tTKGeometrySmoother1.InputMaskField = ["CELLS", "SeparatrixType"]

# create a new 'Tube'
tube1 = Tube(registrationName="Tube1", Input=tTKGeometrySmoother1)
tube1.Scalars = ["POINTS", "CellDimension"]
tube1.Vectors = ["POINTS", "1"]
tube1.Radius = 0.02

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(Input=tube1)
tTKIdentifierRandomizer1.ScalarField = ["CELLS", "SeparatrixMatchingIdInBlock0"]

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=tTKIdentifierRandomizer1)
extractBlock1.Assembly = "Hierarchy"
extractBlock1.Selectors = ["/Root/Block0"]

# create a new 'Extract Block'
extractBlock2 = ExtractBlock(Input=tTKIdentifierRandomizer1)
extractBlock2.Assembly = "Hierarchy"
extractBlock2.Selectors = ["/Root/Block1"]

# create a new 'Extract Block'
extractBlock6 = ExtractBlock(Input=tTKIdentifierRandomizer1)
extractBlock6.Assembly = "Hierarchy"
extractBlock6.Selectors = ["/Root/Block2"]

SaveData("protonTunnelingMode16Prism.vtm", tTKSeparatrixStability1)

