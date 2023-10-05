from Services.SplitwiseService import SplitWiseService

def process_input(input) -> list:
    '''
    Reads Input
    '''
    input = [str(i) for i in input.split()]
    if len(input) == 1 and input[0] == 'SHOW':
        input[0] = "SHOWALL"
    return iter(input)

def parse_input(input) -> list:
    inputType = next(input)
    def getExpenseInput() -> None:

        def getSplits(totalamount, ratio):
            return [float(totalamount*r/100)for r in ratio]
        
        # Read All Inputs
        payer, amount, payee_num = str(next(input)), float(next(input)), int(next(input))
        payee = []
        for _ in range(payee_num):
            payee.append(next(input))
        payee_dict = {}
        expenseType = next(input)

        # Calculate Splits according to Split Type
        match expenseType:

            case "EQUAL":
                splits = [100.0/payee_num]*payee_num
                for p, amt in zip(payee, getSplits(amount, splits)):
                    payee_dict[p] = amt

            case "EXACT":
                splits = [float(next(input)) for _ in range(payee_num)]
                for p, amt in zip(payee, splits):
                    payee_dict[p] = amt
                
            case "PERCENT":
                splits = [float(next(input)) for _ in range(payee_num)]
                for p, amt in zip(payee, getSplits(amount, splits)):
                    payee_dict[p] = amt

            case _:
                print("Couldnt Parse !! ")
        return [inputType, payer, amount, payee_dict]
        
    def getShowInput() -> list:
        user = next(input)
        return [inputType, user]
    
    def getShowAllInput() -> list:
        return [inputType]

    match inputType:
        case "EXPENSE": return getExpenseInput() 
        case "SHOW": return getShowInput()
        case "SHOWALL" : return getShowAllInput()

def main():
    splitWiseService = SplitWiseService()

    inputs = [
        "SHOW", 
        "SHOW u1", 
        "EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL",
        "SHOW u4",
        "SHOW u1",
        "EXPENSE u1 1250 2 u2 u3 EXACT 370 880",
        "SHOW",
        "EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20",
        "SHOW u1",
        "SHOW"
        ]

    for input in inputs:
        processed_input = process_input(input)
        parsed_input = parse_input(processed_input)
        splitWiseService.service_request(parsed_input[0], parsed_input[1:])


if __name__ == "__main__":
    main()