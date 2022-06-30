# This creates a new command "hbPlus" in ChimeraX when run. 
#  Measures hbonds between ligand and protein, outputs a report. 

from chimerax.core.commands import run

def hbPlus(session, structures):
    for structure in structures:
        hb_output = run(session, 
        f"hb ligand restrict protein reveal t interModel f saveFile {structure.name}_hbond_Report.txt")
    return hb_output

def register_command(session):
    from chimerax.core.commands import CmdDesc, register
    from chimerax.atomic import StructuresArg
    desc = CmdDesc(required=[('structures', StructuresArg)],
                   synopsis='Save images of structures in session')
    register('hbPlus', desc, hbPlus, logger=session.logger)

register_command(session)