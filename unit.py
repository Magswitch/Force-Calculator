import fetchdata

class Unit(object):
    """Describes a magswitch unit. Declared by name to be searched in master excel sheet"""
    def __init__(self, name):
        super(Unit, self).__init__()
        self.name = name
        self.thicknesses = fetchdata.getUnitData(name, 'thicknesses')
        self.forces = fetchdata.getUnitData(name, 'forces')
