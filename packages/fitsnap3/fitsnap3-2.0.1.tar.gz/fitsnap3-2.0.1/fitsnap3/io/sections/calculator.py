from .sections import Section
from ...parallel_tools import pt


class Calculator(Section):

    def __init__(self, name, config, args):
        super().__init__(name, config, args)
        allowedkeys = ['calculator','energy','force','stress']
        for value_name in config['CALCULATOR']:
            if value_name in allowedkeys: continue
            else:
                raise RuntimeError(">>> Found unmatched variable in CALCULATOR section of input: ", value_name)
                #pt.single_print(">>> Found unmatched variable in CALCULATOR section of input: ",value_name)

        self.calculator = self.get_value("CALCULATOR", "calculator", "LAMMPSSNAP")
        self.energy = self.get_value("CALCULATOR", "energy", "True", "bool")
        pt.add_2_fitsnap("energy", self.energy)
        self.force = self.get_value("CALCULATOR", "force", "True", "bool")
        pt.add_2_fitsnap("force", self.force)
        self.stress = self.get_value("CALCULATOR", "stress", "True", "bool")
        pt.add_2_fitsnap("stress", self.stress)
        self.delete()
