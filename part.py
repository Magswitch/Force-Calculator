class Geometry(object):
    """Geometry of the part to be evaluated. Physical dimensions only. """
    def __init__(self, length, width, height):
        super(Geometry, self).__init__()
        self.length = length
        self.width = width
        self.height = height
        self.volume = length*width*height

class Material(object):
	"""Material properties of the part to be evaluated. Values pulled from verified DB"""
	def __init__(self, kind):
		super(Material, self).__init__()
		self.kind = kind

		#fetchMaterialdata(kind) once implemented - need to establish excel sheet with steel properties

		if kind == "Steel":
			self.density = 2
			self.mag_Effy = 4
			self.mod_Elas = 72

		else:
			print("  Warning! - The material with kind *%s* does not have any property data. Defaulting to 1018 Steel." %kind)
			self.density = 1
			self.mag_Effy = 2
			self.mod_Elas = 5

		