if not exist "..\docs" mkdir ..\docs
if not exist "..\docs\_markup" mkdir ..\docs\_markup

XCOPY ".\_build\html" "..\docs"
XCOPY ".\_build\markdown" "..\docs\_markup"
XCOPY "*.md" "..\docs\_markup"