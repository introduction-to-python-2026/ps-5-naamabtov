def split_before_uppercases(formula):
    split_formula=[]
    start_sub=0
    if formula== "":
      return split_formula
    for i  in range(1,len(formula)):
      if formula[i].isupper():
        split_formula.append(formula[start_sub:i])
        start_sub=i
    split_formula.append(formula[start_sub:len(formula)])
    return split_formula


def split_at_digit(formula):
    digit_location = 1
    while digit_location <=len(formula)-1 :
        if formula[digit_location].isdigit() :
            break
        digit_location += 1
    if digit_location > len(formula)-1 :
        return (formula,1)
    return (formula[0:digit_location],int(formula[digit_location:len(formula)]))


def count_atoms_in_molecule(molecular_formula):
    count = {}
    split_formula=split_before_uppercases(molecular_formula)
    for element in split_formula:
        split_element=split_at_digit(element)
        count[split_element[0]]=split_element[1]
    return count


def parse_chemical_reaction(reaction_equation):

    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
