ASSETSDIR =
         "C:\\Users\\Bruno\\PycharmProjects\\mhack\\buffer\\";
FILENAME = "input.json";
jsonimport[] := Association[Import[StringJoin[ASSETSDIR, FILENAME]]]

IN = jsonimport[];

OutputGraphics =
 ListLinePlot[IN["bitcoinPrice"], PlotTheme -> "Simple"]

Export[ASSETSDIR <> IN["META_OUTPUT_FILENAME"], OutputGraphics];



