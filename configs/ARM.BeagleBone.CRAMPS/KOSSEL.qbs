import qbs

MachinekitApplication {
    name: "KOSSEL"
    halFiles: ["KOSSEL.hal"]
    configFiles: ["KOSSEL.ini"]
    // bbioFiles: ["cramps2_cape3.bbio"]
    otherFiles: ["tool.tbl", "subroutines"]
    pythonFiles: ["python"]
    //compFiles: ["thermistor_check.comp"]
    linuxcncIni: "KOSSEL.ini"
    //display: "thinkpad.local:0.0"
}
