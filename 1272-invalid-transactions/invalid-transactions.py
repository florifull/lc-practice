class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name_to_transactions = collections.defaultdict(list)
        res = []
        
        # Group transactions by name (store original string + parsed data)
        for trans in transactions:
            data = trans.split(',')
            name, time, amount, city = data[0], int(data[1]), int(data[2]), data[3]
            name_to_transactions[name].append((trans, time, amount, city))
        
        # Check each transaction
        for name, trans_list in name_to_transactions.items():
            for trans, time, amount, city in trans_list:
                invalid = False
                if amount > 1000: invalid = True
                for other_trans, other_time, other_amount, other_city in trans_list:
                    diffTime = abs(time - other_time)
                    if trans != other_trans and diffTime <= 60 and city != other_city:
                        invalid = True
                        break
                if invalid:
                    res.append(trans)
        return res